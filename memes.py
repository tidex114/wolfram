import sqlite3, time
import sqlite3
import time
from datetime import datetime

conn = sqlite3.connect('database.sqlite')
c = conn.cursor()

c.execute("INSERT INTO memes (url, comment, time) VALUES (?, ?, ?)",
          ("https://img.rosbalt.ru/photobank/8/f/e/d/RZKLg4YQ-580.jpg",
           "Когда Вильнюсов дает неправильный прогноз",
           time.time()))

c.execute("SELECT * FROM memes")
result = c.fetchall()

for line in result:
    print("id", line[0])
    print("url", line[1])
    print("comment", line[2])
    print("time", datetime.fromtimestamp(line[3]).strftime("%m/%d/%Y, %H:%M:%S"))

conn.commit()
conn.close()
