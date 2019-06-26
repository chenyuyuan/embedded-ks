import time
import sqlite3

def main():
    conn = sqlite3.connect('dev.db')
    curs = conn.cursor()

    curs.execute("INSERT INTO temps(temperature) VALUES((?))",(1,))
    conn.commit()

    conn.close()



if __name__ == '__main__':
    main()
