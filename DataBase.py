import sqlite3

conn = sqlite3.connect("LibraryMS.db")
cur = conn.cursor()

def CreateTable():
    cur.execute("create table if not exists IssueTable (date text,time text,student_id text,name text,roll_no text,branch text,contact text,email text,book_id text,book_name text,author_name text,issue_date text,return_date text,fine text)")
    cur.execute("create table if not exists ProgrammingBooksDetails ( date text, time text, book_id text, book_name  text, author_name text , price text )")
    conn.commit()
    print("Table Created Successfully...")
    
# CreateTable()

def ShowData():
    cur.execute("select * from IssueTable")
    result = cur.fetchall()
    for row in result:
        print(row)
        
# ShowData()

def DeleteData():
    cur.execute("delete from IssueTable")
    cur.execute("delete from ProgrammingBooksDetails")
    print("Data has been deleted from table.")
    conn.commit()
    
DeleteData()