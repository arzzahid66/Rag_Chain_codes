import psycopg2


def fetch_data_by_bot_id(bot_id):
    try:
        # Connecting to the PostgreSQL server
        conn = psycopg2.connect(
            host="localhost",
            database="con_ret_chat_history",
            user="postgres",
            password="pass"
        )
        print('Connected to the PostgreSQL server.')
        
        cursor = conn.cursor()
        cursor.execute("SELECT question, answer FROM chatbot_chat_history WHERE bot_id = %s", (bot_id,))
        rows = cursor.fetchall()
        return rows
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        return []
    






















# def connect():
#     try:
#         # Connecting to the PostgreSQL server
#         conn = psycopg2.connect(
#             host="localhost",
#             database="con_ret_chat_history",
#             user="postgres",
#             password="7866"
#         )
#         print('Connected to the PostgreSQL server.')
#         return conn
#     except (psycopg2.DatabaseError, Exception) as error:
#         print(error)

# conn = connect()


# def fetch_data(conn, bot_id):
#     try:
#         cursor = conn.cursor()
#         cursor.execute("SELECT question, answer FROM chatbot_chat_history WHERE bot_id = %s", (bot_id,))
#         rows = cursor.fetchall()
#         return rows
#     except (psycopg2.DatabaseError, Exception) as error:
#         print(error)


# bot_id = input("enter ..")
# result = fetch_data(bot_id,conn)
# print(result)



# if __name__ == "__main__":
#     bot_id = input("Enter Bot ID: ")
#     # Connect to the database

# def get_final(bot_id):
#     data = fetch_data(conn,bot_id)
#     print("Fetched data:")
#     for row in data:
#         print(row)
# conn.close()


    

