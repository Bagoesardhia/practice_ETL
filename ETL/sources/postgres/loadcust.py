from connection import connection, conn

def main():
    if connection() == 0:
        load()
    else:
        err_handler()

def load():
    try:
        cursor = conn.cursor()
        queries = "select * from cust.master_customers where card_type = 'GOLD'"
        cursor.execute(queries)
        data = cursor.fetchone()
        return data
    except Exception as error:
        print('Error load data customer',error)

def err_handler():
    print('Error get data')

print(load())

main()