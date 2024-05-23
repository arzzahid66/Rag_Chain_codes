import psycopg2
from psycopg2 import sql, DatabaseError

def delete_bot_id(bot_id):
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
        
        # Deleting rows with the specified bot_id
        delete_query = sql.SQL("DELETE FROM chatbot_chat_history WHERE bot_id = %s")
        cursor.execute(delete_query, (bot_id,))
        conn.commit()
        
        # Check the number of deleted rows
        deleted_rows = cursor.rowcount
        result = f"Deleted {deleted_rows} rows with bot_id {bot_id}"
    except (DatabaseError, Exception) as error:
        result = f"Error occurred: {error}"
        
    cursor.close()
    conn.close()
    print('Database connection closed.')
    
    return result

# Example usage
print(delete_bot_id(3))
