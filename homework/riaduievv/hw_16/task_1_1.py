import csv
import mysql.connector as mysql
import os
import dotenv

dotenv.load_dotenv(override=True)
db = mysql.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    user=os.getenv("DB_USER"),
    passwd=os.getenv("DB_PASSWD"),
    database=os.getenv("DB_DATABASE"),
)
cursor = db.cursor(dictionary=True)

base_path = os.path.dirname(__file__)
home_path = os.path.dirname(os.path.dirname(base_path))
hw_16_path = os.path.join(
    home_path, "eugene_okulik", "Lesson_16", "hw_data", "data.csv"
)

with open(hw_16_path, newline="") as new_file:
    file_data = csv.DictReader(new_file)
    for row in file_data:
        if isinstance(row, dict):
            name = row.get("name")
            second_name = row.get("second_name")
            group_title = row.get("group_title")
            book_title = row.get("book_title")
            subject_title = row.get("subject_title")
            lesson_title = row.get("lesson_title")
            mark_value = row.get("mark_value")
            if all(
                [name, second_name, group_title, book_title, subject_title, mark_value]
            ):
                query = """
                SELECT students.name, students.second_name,
                `groups`.title, subjets.title, books.title, lessons.title, marks.value
                FROM students
                JOIN `groups` ON students.group_id = `groups`.id
                JOIN marks ON marks.student_id = students.id
                JOIN lessons ON lessons.id = marks.lesson_id
                JOIN subjets ON subjets.id = lessons.subject_id
                JOIN books ON books.taken_by_student_id = students.id
                WHERE students.name = %s
                AND students.second_name = %s
                AND `groups`.title = %s
                AND books.title = %s
                AND subjets.title = %s
                AND lessons.title = %s
                AND marks.value = %s;
                """
                cursor.execute(
                    query,
                    (
                        name,
                        second_name,
                        group_title,
                        book_title,
                        subject_title,
                        lesson_title,
                        mark_value,
                    ),
                )
                result = cursor.fetchall()
                if not result:
                    print(row)


db.close()
