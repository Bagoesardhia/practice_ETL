from connection import connection, conn

def main():
    if connection() == 0:
        load()
    else:
        err_handler()
    def load():
        try:
            cursor = conn.cursor()
            cursor.execute('select * from cust.master_customers')
            data = cursor.fetchall()
            print(data)
        except Exception as error:
            print('Error load data customer',error)

main()