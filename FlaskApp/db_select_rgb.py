import time
import sqlite3

def main():
    conn = sqlite3.connect('rgb.db')
    curs = conn.cursor()

    for row in curs.execute("SELECT * FROM temps ORDER BY id DESC"):
        print(row)
    conn.commit()

    conn.close()



if __name__ == '__main__':
    main()
