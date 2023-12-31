import pyodbc
from spire.xls import *
from spire.xls.common import *
import sqlite3

conn = sqlite3.connect("LibraryMS.db")
cursor = conn.cursor()

#Create a workbook
workbook = Workbook()
# workbook = Workbook("D:/Sikandar Singh/Python Programming/All Projects/Library Management System/Excel_Files/ProgrammingBooks.xls")
# workbook.Version = ExcelVersion.Version2016
#Get the first worksheet of the file
worksheet = workbook.Worksheets[0]

#Set the path to your Access database file
# db_file_path = r'C:/Users/Administrator/Documents/Employees.accdb'

#Establish a connection to the database
# conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + db_file_path + ';')

#Execute a query to retrieve data from a database table named 'Employees'
# cursor = conn.cursor()
# db_query = 'SELECT * FROM Employees'
# cursor.execute(db_query)
cursor.execute("select * from ProgrammingBooksDetails")

#Get the headers of the data
headers = [column[0] for column in cursor.description]

#Write the headers to specific cells of the worksheet
for col_num, header in enumerate(headers, 1):
    worksheet.Range[1, col_num].Text = header
    #Set font style for headers
    worksheet.Range[1, col_num].Style.Font.IsBold = True

#Write the remaining data to specific cells of the worksheet
for row_num, row in enumerate(cursor, 2):
    for col_num, cell_value in enumerate(row, 1):
        if type(cell_value) == int:
            worksheet.Range[row_num, col_num].NumberValue = cell_value
        else:
            worksheet.Range[row_num, col_num].Text = str(cell_value)

#Autofit column widths
worksheet.AllocatedRange.AutoFitColumns()

#Save the Excel file to a specific location
workbook.SaveToFile('D:/Sikandar Singh/Python Programming/All Projects/Library Management System/Excel_Files/DatabaseToExcel.xlsx')
workbook.Dispose()
conn.close()