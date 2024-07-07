import sqlite3


def create_tables(database):
    sql_statement = "CREATE TABLE IF NOT EXISTS urls (url_id TEXT PRIMARY KEY, url text TEXT NOT NULL, visit_counter INT)"
    try:
        with sqlite3.connect(database) as conn:
            cursor = conn.cursor()
            cursor.execute(sql_statement)
            
            conn.commit()
    except sqlite3.Error as e:
        print(e)

if __name__ == '__main__':
    create_tables("urls.db")
