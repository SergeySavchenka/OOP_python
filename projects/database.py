import pymysql


class Database:
    def __init__(self):
        self.conn = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="task_management"
        )
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def create_user(self, username, email):
        self.cursor.execute("INSERT INTO Users (username, email) VALUES (%s, %s)", (username, email))
        self.conn.commit()

    def create_project(self, project_name):
        self.cursor.execute("INSERT INTO Projects (project_name) VALUES (%s)", (project_name,))
        self.conn.commit()

    def create_task(self, title, status, user_id, project_id):
        self.cursor.execute(
            "INSERT INTO Tasks (title, status, user_id, project_id) VALUES (%s, %s, %s, %s)",
            (title, status, user_id, project_id)
        )
        self.conn.commit()

    def get_tasks(self):
        self.cursor.execute("SELECT task_id, title, status, user_id FROM Tasks")
        tasks = self.cursor.fetchall()
        return tasks

    def get_projects(self):
        self.cursor.execute("SELECT project_id, project_name FROM Projects")
        projects = self.cursor.fetchall()
        return projects

    def get_users(self):
        self.cursor.execute("SELECT user_id, username, email FROM Users")
        users = self.cursor.fetchall()
        return users
