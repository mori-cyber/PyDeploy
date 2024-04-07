import sqlite3
connection =sqlite3.connect("fastapi.classwork.db")
my_cursor =connection.cursor()

#READ
#راه اول برای خواندن یک تیبل از دیتابیس
# for data in my_cursor.execute("SELECT * FROM student"):
#     print(data) 
#راه اول برای خواندن اطلاعات یک سطر از دیتا بیس بر اساس یک موجودیت
# for data in my_cursor.execute("SELECT * FROM student where family='biranvand'"):
#     print(data) 
#راه دوم برای خواندن یک سطر و یا کل سطر های دیتابیس
#fetchall for all over
#fetchone for one
# result = my_cursor.execute("SELECT * FROM student where family='biranvand'")
# biranvand =result.fetchall()
# print(biranvand)
# # به صورت زیر هم میتونیم چاپ کنیم
# for data in biranvand:
#     print(data)
#INSERT
# my_cursor.execute("INSERT INTO student(id,name,family,age) VALUES(3,'reza','kord',34)")
# connection.commit() #برای ذخیره کردن دیتا های جدید در دیتابیس
# for data in my_cursor.execute("SELECT * FROM student"):
#     print(data)
#UPDATE
# my_cursor.execute("UPDATE student SET name='gholi',family='darvishi' WHERE id=3")
# connection.commit()
# for data in my_cursor.execute("SELECT * FROM student"):
#     print(data)

# DELETE
# my_cursor.execute("DELETE FROM student WHERE id=3")
# connection.commit()
# for data in my_cursor.execute("SELECT * FROM student"):
#     print(data)

# Open the image file
with open('image.jpg', 'rb') as file:
    image_data = file.read()
# Insert image data into the database
result=my_cursor.execute("INSERT INTO Images (data) VALUES (?)", (sqlite3.Binary(image_data),))
connection.commit()
# Close resources
my_cursor.close()
connection.close()



