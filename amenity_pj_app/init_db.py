import sqlite3

connection = sqlite3.connect('db/database.db')

with open('db/schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content, publisher) VALUES (?, ?, ?)",
            ('Open Source Tools', 'All the Tools provided here are open source. Code can be found at Github.', 'Admin')
            )

cur.execute("INSERT INTO posts (title, content, publisher) VALUES (?, ?, ?)",
            ('Asn1Play', 'I am using this tool from couple of years & it helps me boost my Productivity', 'Pratik')
            )

cur.execute("INSERT INTO posts (title, content, publisher) VALUES (?, ?, ?)",
            ('TlvPlay', 'Great Tool, able to parse any TLV for known as well as unknown Tools', 'Pj')
            )

cur.execute("INSERT INTO posts (title, content, publisher) VALUES (?, ?, ?)",
            ('QrPlay', 'Wow !!!, Variety of Qr versions are supporrted under one roof', 'Amrit')
            )

connection.commit()
connection.close()
