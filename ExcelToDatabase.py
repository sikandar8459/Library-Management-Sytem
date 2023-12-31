import xlrd
import random as rd
import sqlite3

conn = sqlite3.connect("LibraryMS.db")
cur = conn.cursor()

book = xlrd.open_workbook("D:/Sikandar Singh/Python Programming/All Projects/Library Management System/Excel_Files/ProgrammingBooksDetails.xls")
sheet = book.sheet_by_name("BookDetails")


for r in range(1, sheet.nrows):
    product_id = rd.randint(1111,9999)

    product_name = sheet.cell(r,1).value

    product_price = rd.randint(111,999)

    cur.execute("insert into ProgrammingBooksDetails values (?,?,?)", (product_id, product_name, product_price,))
    print("Data inserted successfully...")
    # values = (product_id, product_name, product_price)

    # cur.execute(query, values)

conn.commit()