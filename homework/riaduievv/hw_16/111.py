import csv
import mysql.connector as mysql
import os
import dotenv

dotenv.load_dotenv(override=True)
db = mysql.connect(
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSWD'),
    database=os.getenv('DB_DATABASE')
)
cursor = db.cursor(dictionary=True)

base_path = os.path.dirname(__file__)
home_path = os.path.dirname(os.path.dirname(base_path))
hw_16_path = os.path.join(home_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

with open(hw_16_path, newline='') as new_file:
    file_data = csv.DictReader(new_file)
    for row in file_data:
        if isinstance(row, dict):
            group_title = row.get('group_title')
            if group_title:
                query = """
                SELECT students.name, students.second_name, 
                `groups`.title, subjets.title, books.title, lessons.title, marks.value
                FROM students
                JOIN `groups` ON students.group_id = `groups`.id
                JOIN marks ON marks.student_id = students.id
                JOIN lessons ON lessons.id = marks.lesson_id
                JOIN subjets ON subjets.id = lessons.subject_id
                JOIN books ON books.taken_by_student_id = students.id
                WHERE `groups`.title = %s;
                """
                cursor.execute(query, (group_title,))
                result = cursor.fetchall()
                if not result:
                    print(f"Not in base {row}")

db.close()