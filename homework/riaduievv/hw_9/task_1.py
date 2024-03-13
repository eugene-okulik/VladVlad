from datetime import datetime

date = "Jan 15, 2023 - 12:05:33"
python_date = datetime.strptime(date, "%b %d, %Y - %H:%M:%S")
full_month = python_date.strftime("%B")
print(full_month)
new_format = python_date.strftime("%d.%m.%Y, %H:%M")
print(new_format)
