import psycopg2

conn = psycopg2.connect(
            database='dev', 
            user='dev', 
            password='dev123', 
            host='209.97.172.45', 
            port='5511'
        )

def connection():
    try:
        conn
        return 0
    except:
        return 1

if connection() == 0:
    print("Connection established", connection())
    connection()
else:
    print("Error connecting to database", connection())


