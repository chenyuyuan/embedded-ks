import time
import sqlite3

def main():
    conn = sqlite3.connect('dev.db')
    curs = conn.cursor()

    for row in curs.execute("SELECT * FROM temps ORDER BY time DESC"):
        print(row)
    conn.commit()

    conn.close()



if __name__ == '__main__':
    main()
