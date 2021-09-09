import psycopg2

#connect to the db 
con = psycopg2.connect(
            host = "localhost",
            database="test",
            user = "postgres",
            password = "5cf5bc4161e0414fa6e2e8ecd31b389e")

#cursor 
cur = con.cursor()

cur.execute("insert into employees (id, name) values (%s, %s)", (2, "vishnu") )

#execute query
cur.execute("select id, name from employees")

rows = cur.fetchall()

for r in rows:
    print (f"id {r[0]} name {r[1]}")

#commit the transcation 
con.commit()

#close the cursor
cur.close()

#close the connection
con.close()