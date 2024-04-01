import os
from datetime import datetime, timedelta

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
hw13_data_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')

with open(hw13_data_path) as data_file:
    lines = data_file.readlines()

for line in lines:
    date_str = line.split(' - ')[0][3:]

    if date_str == '2023-11-27 20:34:13.212967':
        given_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
        one_week_later = given_date + timedelta(weeks=1)
        print(one_week_later.strftime("%Y-%m-%d %H:%M:%S.%f"))

    elif date_str == '2023-07-15 18:25:10.121473':
        given_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
        print(given_date.strftime("%A"))

    elif date_str == '2023-06-12 15:23:45.312167':
        given_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
        today = datetime.now()
        days_ago = (today - given_date).days
        print(days_ago)
