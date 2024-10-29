import sys
import pymysql
from PyQt6.QtWidgets import QApplication, QMainWindow, QTreeView, QAbstractItemView, QVBoxLayout, QWidget
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtCore import Qt


class DB:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
        )
        self.cursor = self.conn.cursor()

    def execute_proc(self):
        self.cursor.execute("CALL GetComponentHierarchy()")
        return self.cursor.fetchall()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()


class ComponentTreeView(QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.db = db

        self.setWindowTitle("TreeView")
        self.setGeometry(200, 200, 600, 500)

        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)

        self.treeView = QTreeView(self)
        self.treeView.setUniformRowHeights(True)
        self.treeView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.treeView.setAlternatingRowColors(True)
        self.treeView.setHeaderHidden(False)
        self.treeView.header().setStretchLastSection(False)
        self.treeView.header().setDefaultAlignment(Qt.AlignmentFlag.AlignCenter)

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Компонент', 'Количество'])
        self.treeView.setModel(self.model)

        layout.addWidget(self.treeView)

        self.populate_tree()

    def populate_tree(self):
        self.model.removeRows(0, self.model.rowCount())
        rows = self.db.execute_proc()
        component_items = {}

        for parent_id, parent_name, child_id, child_name, amount in rows:
            if parent_id not in component_items:
                parent_item = QStandardItem(parent_name)
                parent_item.setEditable(False)
                component_items[parent_id] = parent_item
                self.model.appendRow(parent_item)
            else:
                parent_item = component_items[parent_id]

            if child_id is not None:
                child_item = QStandardItem(child_name)
                amount_item = QStandardItem(str(amount))
                child_item.setEditable(False)
                amount_item.setEditable(False)

                parent_item.appendRow([child_item, amount_item])
                component_items[child_id] = child_item

    def closeEvent(self, event):
        self.db.close()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    db = DB(
        host='localhost',
        user='root',
        password='',
        database='tree'
    )
    db.connect()
    window = ComponentTreeView(db)
    window.show()
    sys.exit(app.exec())
