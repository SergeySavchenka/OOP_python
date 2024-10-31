from PyQt6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QApplication, QWidget, QHeaderView
from PyQt6.QtWidgets import QVBoxLayout
from dialogs import AddTaskDialog, ViewProjectsDialog, ViewUsersDialog
from database import Database
import sys


class MainWindow(QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.setWindowTitle("Менеджер заданий")
        self.resize(600, 400)

        self.table = QTableWidget()
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.verticalHeader().setVisible(False)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID задания", "Название", "Статус", "ID работника"])

        self.add_task_button = QPushButton("Добавить задание")
        self.add_task_button.clicked.connect(self.open_add_task_dialog)

        self.view_projects_button = QPushButton("Проекты")
        self.view_projects_button.clicked.connect(self.open_view_projects_dialog)

        self.view_users_button = QPushButton("Работники")
        self.view_users_button.clicked.connect(self.open_view_users_dialog)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.add_task_button)
        layout.addWidget(self.view_projects_button)
        layout.addWidget(self.view_users_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.load_tasks()

    def open_add_task_dialog(self):
        dialog = AddTaskDialog(self.db, self)
        if dialog.exec():
            self.load_tasks()

    def open_view_projects_dialog(self):
        dialog = ViewProjectsDialog(self.db, self)
        dialog.exec()

    def open_view_users_dialog(self):
        dialog = ViewUsersDialog(self.db, self)
        dialog.exec()

    def load_tasks(self):
        tasks = self.db.get_tasks()
        self.table.setRowCount(len(tasks))
        for row, task in enumerate(tasks):
            task_id, title, status, user_id = task
            self.table.setItem(row, 0, QTableWidgetItem(str(task_id)))
            self.table.setItem(row, 1, QTableWidgetItem(title))
            self.table.setItem(row, 2, QTableWidgetItem(status))
            self.table.setItem(row, 3, QTableWidgetItem(str(user_id)))

    def closeEvent(self, event):
        self.db.close()
        event.accept()


app = QApplication(sys.argv)
db = Database()
window = MainWindow(db)
window.show()
sys.exit(app.exec())
