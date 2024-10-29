from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QDialog, QLineEdit, QLabel


class AddTaskDialog(QDialog):
    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.db = db
        self.setWindowTitle("Add Task")

        self.title_input = QLineEdit()
        self.user_id_input = QLineEdit()
        self.project_id_input = QLineEdit()

        add_button = QPushButton("Add Task")
        add_button.clicked.connect(self.add_task)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Title"))
        layout.addWidget(self.title_input)
        layout.addWidget(QLabel("User ID"))
        layout.addWidget(self.user_id_input)
        layout.addWidget(QLabel("Project ID"))
        layout.addWidget(self.project_id_input)
        layout.addWidget(add_button)

        self.setLayout(layout)

    def add_task(self):
        title = self.title_input.text()
        user_id = int(self.user_id_input.text())
        project_id = int(self.project_id_input.text())
        self.db.create_task(title, 'Pending', user_id, project_id)
        self.accept()


class AddProjectDialog(QDialog):
    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.db = db
        self.setWindowTitle("Add Project")

        self.project_name_input = QLineEdit()

        add_button = QPushButton("Add Project")
        add_button.clicked.connect(self.add_project)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Project Name"))
        layout.addWidget(self.project_name_input)
        layout.addWidget(add_button)

        self.setLayout(layout)

    def add_project(self):
        project_name = self.project_name_input.text()
        if project_name:
            self.db.create_project(project_name)
            self.accept()


class ViewProjectsDialog(QDialog):
    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.db = db
        self.setWindowTitle("Projects")

        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Project ID", "Project Name"])

        self.add_project_button = QPushButton("Add Project")
        self.add_project_button.clicked.connect(self.open_add_project_dialog)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.add_project_button)
        self.setLayout(layout)

        self.load_projects()

    def load_projects(self):
        projects = self.db.get_projects()
        self.table.setRowCount(len(projects))
        for row, project in enumerate(projects):
            project_id, project_name = project
            self.table.setItem(row, 0, QTableWidgetItem(str(project_id)))
            self.table.setItem(row, 1, QTableWidgetItem(project_name))

    def open_add_project_dialog(self):
        dialog = AddProjectDialog(self.db, self)
        if dialog.exec():
            self.load_projects()


class AddUserDialog(QDialog):
    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.db = db
        self.setWindowTitle("Add User")

        self.username_input = QLineEdit()
        self.email_input = QLineEdit()

        add_button = QPushButton("Add User")
        add_button.clicked.connect(self.add_user)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Username"))
        layout.addWidget(self.username_input)
        layout.addWidget(QLabel("Email"))
        layout.addWidget(self.email_input)
        layout.addWidget(add_button)

        self.setLayout(layout)

    def add_user(self):
        username = self.username_input.text()
        email = self.email_input.text()
        if username and email:
            self.db.create_user(username, email)
            self.accept()


class ViewUsersDialog(QDialog):
    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.db = db
        self.setWindowTitle("Users")

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["User ID", "Username", "Email"])

        self.add_user_button = QPushButton("Add User")
        self.add_user_button.clicked.connect(self.open_add_user_dialog)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.add_user_button)
        self.setLayout(layout)

        self.load_users()

    def load_users(self):
        users = self.db.get_users()
        self.table.setRowCount(len(users))
        for row, user in enumerate(users):
            user_id, username, email = user
            self.table.setItem(row, 0, QTableWidgetItem(str(user_id)))
            self.table.setItem(row, 1, QTableWidgetItem(username))
            self.table.setItem(row, 2, QTableWidgetItem(email))

    def open_add_user_dialog(self):
        dialog = AddUserDialog(self.db, self)
        if dialog.exec():
            self.load_users()