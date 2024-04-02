import mysql.connector as mysql

db = mysql.connect(
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    database='st-onl'
)

cursor = db.cursor(dictionary=True)
cursor.execute('SELECT * FROM marks  WHERE student_id = 863')
print(cursor.fetchall())

cursor = db.cursor(dictionary=True)
cursor.execute('SELECT * FROM books WHERE taken_by_student_id = 863')
print(cursor.fetchall())

cursor = db.cursor(dictionary=True)
cursor.execute('''
    SELECT students.name, students.second_name, `groups`.title, subjets.title, books.title, lessons.title, marks.value
    FROM students
    JOIN `groups` ON students.group_id = `groups`.id
    JOIN marks ON marks.student_id = students.id
    JOIN lessons ON lessons.id = marks.lesson_id
    JOIN subjets ON subjets.id = lessons.subject_id
    JOIN books ON books.taken_by_student_id = students.id
    WHERE students.id = 863
''')
print(cursor.fetchall())

db.close()
