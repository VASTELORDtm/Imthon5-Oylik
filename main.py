# 3-masala
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
# import mysql.connector
# from mysql.connector import Error
#
# class UserInfoApp(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#         self.connection = self.create_connection()
#
#     def initUI(self):
#         self.setWindowTitle('User Information')
#         layout = QVBoxLayout()
#
#         self.name_input = QLineEdit(self)
#         self.name_input.setPlaceholderText('Enter Name')
#         layout.addWidget(QLabel('Name:'))
#         layout.addWidget(self.name_input)
#
#         self.description_input = QLineEdit(self)
#         self.description_input.setPlaceholderText('Enter Description')
#         layout.addWidget(QLabel('Description:'))
#         layout.addWidget(self.description_input)
#
#         self.expiration_input = QLineEdit(self)
#         self.expiration_input.setPlaceholderText('Enter Expiration Date (YYYY-MM-DD)')
#         layout.addWidget(QLabel('Expiration Date:'))
#         layout.addWidget(self.expiration_input)
#
#         self.assigned_person_input = QLineEdit(self)
#         self.assigned_person_input.setPlaceholderText('Enter Assigned Person')
#         layout.addWidget(QLabel('Assigned Person:'))
#         layout.addWidget(self.assigned_person_input)
#
#         self.submit_button = QPushButton('Submit', self)
#         self.submit_button.clicked.connect(self.submit_data)
#         layout.addWidget(self.submit_button)
#
#         self.setLayout(layout)
#         self.setWindowTitle('Add Task')
#         self.show()
#
#     def create_connection(self):
#         try:
#             connection = mysql.connector.connect(
#                 host='localhost',
#                 database='foydalanuvchi',
#                 user='root',
#                 password='998810120VastelordTM'
#             )
#             return connection
#         except Error as e:
#             print(f"Error: {e}")
#             return None
#
#     def insert_data(self, name, description, expiration_date, assigned_person):
#         cursor = self.connection.cursor()
#         query = "INSERT INTO users (name, description, expiration_date, assigned_person) VALUES (%s, %s, %s, %s)"
#         cursor.execute(query, (name, description, expiration_date, assigned_person))
#         self.connection.commit()
#         cursor.close()
#
#     def submit_data(self):
#         name = self.name_input.text()
#         description = self.description_input.text()
#         expiration_date = self.expiration_input.text()
#         assigned_person = self.assigned_person_input.text()
#
#         if name and description and expiration_date and assigned_person:
#             try:
#                 self.insert_data(name, description, expiration_date, assigned_person)
#                 QMessageBox.information(self, 'Success', 'Data saved successfully!')
#             except Error as e:
#                 QMessageBox.warning(self, 'Error', f'Failed to save data: {e}')
#         else:
#             QMessageBox.warning(self, 'Input Error', 'Please fill all fields.')
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = UserInfoApp()
#     ex.show()
#     sys.exit(app.exec())
# 2-masala
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
# import mysql.connector
# from mysql.connector import Error
# import re
# from datetime import datetime
#
# class UserInfoApp(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#         self.connection = self.create_connection()
#
#     def initUI(self):
#         self.setWindowTitle('User Information')
#         layout = QVBoxLayout()
#
#         self.name_input = QLineEdit(self)
#         self.name_input.setPlaceholderText('Enter Task Name')
#         layout.addWidget(QLabel('Task Name:'))
#         layout.addWidget(self.name_input)
#
#         self.description_input = QLineEdit(self)
#         self.description_input.setPlaceholderText('Enter Description (max 255 chars)')
#         layout.addWidget(QLabel('Description:'))
#         layout.addWidget(self.description_input)
#
#         self.deadline_input = QLineEdit(self)
#         self.deadline_input.setPlaceholderText('Enter Deadline (YYYY-MM-DD)')
#         layout.addWidget(QLabel('Deadline:'))
#         layout.addWidget(self.deadline_input)
#
#         self.time_input = QLineEdit(self)
#         self.time_input.setPlaceholderText('Enter Time (HH:MM)')
#         layout.addWidget(QLabel('Time:'))
#         layout.addWidget(self.time_input)
#
#         self.assigned_person_input = QLineEdit(self)
#         self.assigned_person_input.setPlaceholderText('Enter Assigned Person')
#         layout.addWidget(QLabel('Assigned To:'))
#         layout.addWidget(self.assigned_person_input)
#
#         self.submit_button = QPushButton('Submit', self)
#         self.submit_button.clicked.connect(self.submit_data)
#         layout.addWidget(self.submit_button)
#
#         self.setLayout(layout)
#         self.setWindowTitle('Add Task')
#         self.show()
#
#     def create_connection(self):
#         try:
#             connection = mysql.connector.connect(
#                 host='localhost',
#                 database='tasks',
#                 user='root',
#                 password='998810120VastelordTM'
#             )
#             return connection
#         except Error as e:
#             print(f"Error: {e}")
#             return None
#
#     def insert_data(self, name, description, deadline, time, assigned_person):
#         cursor = self.connection.cursor()
#         query = "INSERT INTO users (name, description, expiration_date, assigned_person) VALUES (%s, %s, %s, %s)"
#         cursor.execute(query, (name, description, deadline, assigned_person))
#         self.connection.commit()
#         cursor.close()
#
#     def validate_inputs(self):
#         name = self.name_input.text()
#         description = self.description_input.text()
#         deadline = self.deadline_input.text()
#         time = self.time_input.text()
#         assigned_person = self.assigned_person_input.text()
#
#         if not name:
#             return "Task name cannot be empty."
#         if not description or len(description) > 255:
#             return "Description cannot be empty and must not exceed 255 characters."
#         if not self.validate_date(deadline):
#             return "Invalid deadline format. Use YYYY-MM-DD."
#         if not self.validate_time(time):
#             return "Invalid time format. Use HH:MM."
#         if not assigned_person:
#             return "Assigned person cannot be empty."
#
#         return None
#
#     def validate_date(self, date_text):
#         try:
#             datetime.strptime(date_text, '%Y-%m-%d')
#             return True
#         except ValueError:
#             return False
#
#     def validate_time(self, time_text):
#         return bool(re.match(r'^\d{2}:\d{2}$', time_text))
#
#     def submit_data(self):
#         validation_error = self.validate_inputs()
#         if validation_error:
#             QMessageBox.warning(self, 'Input Error', validation_error)
#             return
#
#         name = self.name_input.text()
#         description = self.description_input.text()
#         deadline = self.deadline_input.text()
#         time = self.time_input.text()
#         assigned_person = self.assigned_person_input.text()
#
#         try:
#             self.insert_data(name, description, deadline, time, assigned_person)
#             QMessageBox.information(self, 'Success', 'Data saved successfully!')
#         except Error as e:
#             QMessageBox.warning(self, 'Error', f'Failed to save data: {e}')
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = UserInfoApp()
#     ex.show()
#     sys.exit(app.exec_())
#    1-masala
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
# import re
# from datetime import datetime
#
# class UserInfoApp(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle('User Information')
#         layout = QVBoxLayout()
#
#         self.name_input = QLineEdit(self)
#         self.name_input.setPlaceholderText('Enter Task Name')
#         layout.addWidget(QLabel('Task Name:'))
#         layout.addWidget(self.name_input)
#
#         self.description_input = QLineEdit(self)
#         self.description_input.setPlaceholderText('Enter Description (max 255 chars)')
#         layout.addWidget(QLabel('Description:'))
#         layout.addWidget(self.description_input)
#
#         self.deadline_input = QLineEdit(self)
#         self.deadline_input.setPlaceholderText('Enter Deadline (YYYY-MM-DD)')
#         layout.addWidget(QLabel('Deadline:'))
#         layout.addWidget(self.deadline_input)
#
#         self.time_input = QLineEdit(self)
#         self.time_input.setPlaceholderText('Enter Time (HH:MM)')
#         layout.addWidget(QLabel('Time:'))
#         layout.addWidget(self.time_input)
#
#         self.assigned_person_input = QLineEdit(self)
#         self.assigned_person_input.setPlaceholderText('Enter Assigned Person')
#         layout.addWidget(QLabel('Assigned To:'))
#         layout.addWidget(self.assigned_person_input)
#
#         self.submit_button = QPushButton('Submit', self)
#         self.submit_button.clicked.connect(self.submit_data)
#         layout.addWidget(self.submit_button)
#
#         self.setLayout(layout)
#         self.setWindowTitle('Add Task')
#         self.show()
#
#     def validate_inputs(self):
#         name = self.name_input.text()
#         description = self.description_input.text()
#         deadline = self.deadline_input.text()
#         time = self.time_input.text()
#         assigned_person = self.assigned_person_input.text()
#
#         if not name:
#             return "Task name cannot be empty."
#         if not description or len(description) > 255:
#             return "Description cannot be empty and must not exceed 255 characters."
#         if not self.validate_date(deadline):
#             return "Invalid deadline format. Use YYYY-MM-DD."
#         if not self.validate_time(time):
#             return "Invalid time format. Use HH:MM."
#         if not assigned_person:
#             return "Assigned person cannot be empty."
#
#         return None
#
#     def validate_date(self, date_text):
#         try:
#             datetime.strptime(date_text, '%Y-%m-%d')
#             return True
#         except ValueError:
#             return False
#
#     def validate_time(self, time_text):
#         return bool(re.match(r'^\d{2}:\d{2}$', time_text))
#
#     def submit_data(self):
#         validation_error = self.validate_inputs()
#         if validation_error:
#             QMessageBox.warning(self, 'Input Error', validation_error)
#             return
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = UserInfoApp()
#     ex.show()
#     sys.exit(app.exec_())

# kichik masala 1
# def missingNumber(nums: list[int]) -> int:
#     n = len(nums)
#     expected_sum = n * (n + 1) // 2
#     actual_sum = sum(nums)
#     return expected_sum - actual_sum
#
# nums = [3,0,1]
# print(missingNumber(nums))
# kichik masala 2
# def missingNumber(nums: list[int]) -> int:
#     n = len(nums)
#     expected_sum = n * (n + 1) // 2
#     actual_sum = sum(nums)
#     return expected_sum - actual_sum
#
# nums = [9,6,4,2,3,5,7,0,1]
# print(missingNumber(nums))
# kichik masala 3
# def missingNumber(nums: list[int]) -> int:
#     n = len(nums)
#     expected_sum = n * (n + 1) // 2
#     actual_sum = sum(nums)
#     return expected_sum - actual_sum
#
# nums = [0,1]
# print(missingNumber(nums))
# kichik masala 3
# import re
#
#
# def isValid(word: str) -> bool:
#     if len(word) < 3:
#         return False
#
#     if not re.match("^[a-zA-Z0-9]*$", word):
#         return False
#
#     vowels = "aeiouAEIOU"
#     vowel_found = False
#     consonant_found = False
#
#     for char in word:
#         if char in vowels:
#             vowel_found = True
#         elif char.isalpha():
#             consonant_found = True
#
#     return vowel_found and consonant_found
#
#
# word ="234Adas"
# print(isValid(word))
# import re
#
# kichik masala 4
# def isValid(word: str) -> bool:
#     if len(word) < 3:
#         return False
#
#     if not re.match("^[a-zA-Z0-9]*$", word):
#         return False
#
#     vowels = "aeiouAEIOU"
#     vowel_found = False
#     consonant_found = False
#
#     for char in word:
#         if char in vowels:
#             vowel_found = True
#         elif char.isalpha():
#             consonant_found = True
#
#     return vowel_found and consonant_found
#
# word = "b3"
# print(isValid(word))
# import re
#
# kichik masala 5
# def isValid(word: str) -> bool:
#     if len(word) < 3:
#         return False
#
#     if not re.match("^[a-zA-Z0-9]*$", word):
#         return False
#
#     vowels = "aeiouAEIOU"
#     vowel_found = False
#     consonant_found = False
#
#     for char in word:
#         if char in vowels:
#             vowel_found = True
#         elif char.isalpha():
#             consonant_found = True
#
#     return vowel_found and consonant_found
#
# word = "a3$e"
# print(isValid(word))



