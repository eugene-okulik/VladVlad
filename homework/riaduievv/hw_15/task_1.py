import mysql.connector as mysql

db = mysql.connect(
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    database='st-onl'
)

cursor = db.cursor()

group_data = ('Group#30', 'oct 2023', 'feb 2023')
cursor.execute('INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)', group_data)
group_id = cursor.lastrowid

cursor.execute("INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)",
               ('Bob', 'Smith', group_id))
student_id = cursor.lastrowid

insert_query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
books_data = [
    ('book_001', student_id),
    ('book_002', student_id),
    ('book_003', student_id)
]
cursor.executemany(insert_query, books_data)
books_id = [cursor.lastrowid, cursor.lastrowid + 1, cursor.lastrowid + 2]

insert_query = "INSERT INTO subjets (title) VALUES (%s)"
subjets_data = [('subject_001',), ('subject_002',)]
cursor.executemany(insert_query, subjets_data)
subjets_id = [cursor.lastrowid, cursor.lastrowid + 1]

insert_query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"

lessons_data = [
    ('lesson1', subjets_id[0]),
    ('lesson2', subjets_id[1]),
    ('lesson1', subjets_id[0]),
    ('lesson2', subjets_id[1])
]
cursor.executemany(insert_query, lessons_data)
lessons_id = [cursor.lastrowid, cursor.lastrowid + 1, cursor.lastrowid + 2, cursor.lastrowid + 3]

insert_query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
marks_data = [
    ('perfect', lessons_id[0], student_id),
    ('good', lessons_id[1], student_id),
    ('bad', lessons_id[2], student_id),
    ('perfect', lessons_id[3], student_id)
]
cursor.executemany(insert_query, marks_data)
marks_id = [cursor.lastrowid, cursor.lastrowid + 1, cursor.lastrowid + 2, cursor.lastrowid + 3]

select_query = """
    SELECT *
    FROM marks
    WHERE student_id = %s;
"""
cursor.execute(select_query, (student_id,))
marks = cursor.fetchall()
print(marks)

select_query = """
    SELECT *
    FROM books
    WHERE taken_by_student_id = %s;
"""
cursor.execute(select_query, (student_id,))
books = cursor.fetchall()
print(books)

select_query = """
    SELECT students.name, students.second_name, `groups`.title, subjets.title, books.title, lessons.title, marks.value
    FROM students
    JOIN `groups` ON students.group_id = `groups`.id
    JOIN marks ON marks.student_id = students.id
    JOIN lessons ON lessons.id = marks.lesson_id
    JOIN subjets ON subjets.id = lessons.subject_id
    JOIN books ON books.taken_by_student_id = students.id
    WHERE students.id = %s;
"""
cursor.execute(select_query, (student_id,))
student_info = cursor.fetchall()
print(student_info)

db.commit()
db.close()
