import sqlite3

# 连接到SQLite数据库（如果数据库不存在，将会创建一个）
conn = sqlite3.connect('test.db')

# 创建一个Cursor对象
cursor = conn.cursor()

# 创建一个表
cursor.execute('''
    CREATE TABLE employee (  
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        position TEXT NOT NULL
    );
''')

# 插入一些数据
cursor.execute("INSERT INTO employee (name, position) VALUES ('John Doe', 'Software Engineer')")
cursor.execute("INSERT INTO employee (name, position) VALUES ('Jane Smith', 'Data Scientist')")

# 提交事务
conn.commit()

# 查询数据
cursor.execute('SELECT * FROM employee')
rows = cursor.fetchall()

for row in rows:
    print(row)

# 关闭连接
conn.close()
