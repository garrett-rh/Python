#!/usr/bin/python3

import sqlite3

class Database:

    DATABASE_LOCATION = '/home/garrett/.agenda/agenda.db'

    def __init__(self, conn, c):
        self.conn = sqlite3.connect(DATABASE_LOCATION)
        self.c = conn.cursor()
        self.query = query

    def create_table(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS agenda(
                ID integer,
                date text,
                class text,
                assignment text,
                status text
                )"""
                )
        Database.commit()
#Takes query from previous response & then fetches and returns all
    def query(self, query):
        self.c.execute(query)
        query_in_list = self.c.fetchall()
        return query_in_list

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.commit()
        self.conn.close()

class View(Database):

    def __init__(self, conn, c, data_list): 
        super().__init__(conn, c)
        self.data_list = self.c.execute('SELECT * FROM AGENDA')

#Works with query to get data then sort it
    def by_date(self, query_in_list):
        query_in_list.sort(key = lambda query_in_list: query_in_list[1])
        for i in query_in_list:
            print(f"{i[4]:15} {i[1]} {i[2]:10} {i[3]}")

    def by_course(self, query_in_list):
        pass
    def by_status(self, query_in_list):
        pass
def menu():
    choice = input("""choose one of the following options:
    1) view by date.
    2) view by course.
    3) view by status.
    4) edit the agenda.
    5) manage the agenda.
    99) quit.
    -->""")
    
    choice_list = [1, 2, 3, 4, 5, 99]
    if choice.isdigit() != true or choice not in choice_list:
        print("not a proper input. please try again.")
        menu()

#if __name__ == "__main__":
#    main()
