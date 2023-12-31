from tkinter import *
from tkinter import ttk
from datetime import *
import tkinter.messagebox as msg
import random as rd
import sqlite3
import os

conn = sqlite3.connect("LibraryMS.db")
cur = conn.cursor()

class LibraryClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System | Developed by Sikandar Singh")
        self.root.geometry("1200x600+30+0")
        self.root.resizable(0, 0)
        self.root.grab_set()
        
        self.main_label = Label(self.root, text = "Kaali Groups | Library Management System", fg = "white", bg = "darkblue", font = ("Bookman Old Style", 20, "bold"))
        self.main_label.place(x = 0, y = 0, relwidth = 1, height = 40)
    
        self.FrameOne = LabelFrame(self.root, bg = "white", bd = 2, relief = GROOVE)
        self.FrameOne.place(x = 10, y = 50, width = 400, height = 250)
        
        Label(self.FrameOne, text = "ID", font = ("Bookman Old Style", 12), bg = "white", fg = "darkblue").place(x = 10, y = 10)
        Label(self.FrameOne, text = "Name", font = ("Bookman Old Style", 12), bg = "white", fg = "darkblue").place(x = 10, y = 50)
        Label(self.FrameOne, text = "Roll No", font = ("Bookman Old Style", 12), bg = "white", fg = "darkblue").place(x = 10, y = 90)
        Label(self.FrameOne, text = "Branch", font = ("Bookman Old Style", 12), bg = "white", fg = "darkblue").place(x = 10, y = 130)
        Label(self.FrameOne, text = "Contact", font = ("Bookman Old Style", 12), bg = "white", fg = "darkblue").place(x = 10, y = 170)
        Label(self.FrameOne, text = "Email", font = ("Bookman Old Style", 12), bg = "white", fg = "darkblue").place(x = 10, y = 210)

        self.c_dt = datetime.now()
        self.date = f"{self.c_dt.day}-{self.c_dt.month}-{self.c_dt.year}"
        self.time = f"{self.c_dt.hour} : {self.c_dt.minute} : {self.c_dt.second}"

        self.student_id = StringVar()
        self.name = StringVar()
        self.roll_no = StringVar()
        self.branch = StringVar()
        self.contact = StringVar()
        self.email = StringVar()
        
        Entry(self.FrameOne, state = "readonly", fg = "red", textvariable = self.student_id, font = ("Bookman Old Style", 12), bg = "lightgreen").place(x = 100,  y = 10, width = 270)
        self.student_id.set(rd.randint(11111, 99999))
        
        Entry(self.FrameOne, textvariable = self.name, font = ("Bookman Old Style", 12), bg = "lightgreen").place(x = 100,  y = 50, width = 270)
        Entry(self.FrameOne, textvariable = self.roll_no, font = ("Bookman Old Style", 12), bg = "lightgreen").place(x = 100,  y = 90, width = 270)
        Entry(self.FrameOne, textvariable = self.branch, font = ("Bookman Old Style", 12), bg = "lightgreen").place(x = 100,  y = 130, width = 270)
        Entry(self.FrameOne, textvariable = self.contact, font = ("Bookman Old Style", 12), bg = "lightgreen").place(x = 100,  y = 170, width = 270)
        Entry(self.FrameOne, textvariable = self.email, font = ("Bookman Old Style", 12), bg = "lightgreen").place(x = 100,  y = 210, width = 270)

        self.FrameTwo = LabelFrame(self.root, bg = "white", bd = 2, relief = GROOVE)
        self.FrameTwo.place(x = 420, y = 50, width = 250, height = 250)
        
        self.book_id = StringVar()
        self.book_name = StringVar()
        self.author_name = StringVar()
        self.issue_date = StringVar()
        self.return_date = StringVar()
        self.fine = StringVar()

        Entry(self.FrameTwo, fg = "grey", state = "readonly", textvariable = self.book_id, font = ("Bookman Old Style", 12), bg = "lightgreen").place(x = 10,  y = 10, width = 220)
        Entry(self.FrameTwo, fg = "grey", state = "readonly", textvariable = self.book_name, font = ("Bookman Old Style", 12), bg = "lightgreen").place(x = 10,  y = 50, width = 220)
        Entry(self.FrameTwo, fg = "grey", state = "readonly", textvariable = self.author_name, font = ("Bookman Old Style", 12), bg = "lightgreen").place(x = 10,  y = 90, width = 220)
        Entry(self.FrameTwo, fg = "grey", state = "readonly", textvariable = self.issue_date, font = ("Bookman Old Style", 12), bg = "lightgreen").place(x = 10,  y = 130, width = 220)
        Entry(self.FrameTwo, fg = "grey", state = "readonly", textvariable = self.return_date, font = ("Bookman Old Style", 12), bg = "lightgreen").place(x = 10,  y = 170, width = 220)
        Entry(self.FrameTwo, fg = "grey", state = "readonly", textvariable = self.fine, font = ("Bookman Old Style", 12), bg = "lightgreen").place(x = 10,  y = 210, width = 220)

        self.book_id.set("Book ID")
        self.book_name.set("Book Name")
        self.author_name.set("Author Name")
        self.issue_date.set("Issue Date")
        self.return_date.set("Return Date")
        self.fine.set("Fine per Day")
    
        self.FrameThree = LabelFrame(self.root, bg = "white", bd = 2, relief = GROOVE)
        self.FrameThree.place(x = 680, y = 50, width = 200, height = 250)
        
        self.scroll_y = Scrollbar(self.FrameThree, orient = VERTICAL)
        self.ListBox = Listbox(self.FrameThree, font = ("Bookman Old Style", 10), cursor = "hand2", yscrollcommand = self.scroll_y.set)
        self.scroll_y.pack(fill = Y, side = RIGHT)
        self.ListBox.pack(fill = BOTH, expand = 1)
        self.scroll_y.config(command = self.ListBox.yview)
        self.ListBox.bind('<<ListboxSelect>>', self.ListboxFetchData)
        self.ListBoxData()
        
        self.FrameFour = LabelFrame(self.root, bg = "white", bd = 2, relief = GROOVE)
        self.FrameFour.place(x = 890, y = 50, width = 300, height = 250)
        
        self.SearchFrame = LabelFrame(self.FrameFour, bg = "white")
        self.SearchFrame.pack(fill = X)
        
        self.VarSearchData = StringVar()
        Label(self.SearchFrame, text = "Student ID", font = ("times new roman", 10, "bold"), fg = "darkblue", bg = "white").grid(row = 0, column = 0, sticky = "w", padx = 10, pady = 6)
        Entry(self.SearchFrame, textvariable = self.VarSearchData, font = ("times new roman", 10), fg = "darkblue", bd = 2, relief = SUNKEN, bg = "lightgreen").grid(row = 0, column = 1, sticky = "w", padx = 10, pady = 6)
        Button(self.SearchFrame, cursor = "hand2", text = "Search", command = self.SearchStudentID, font = ("times new roman", 9), fg = "white", bg = "darkblue").grid(row = 0, column = 2, sticky = "w", padx = 10, pady = 6)
        
        self.ReceiptText = Text(self.FrameFour, font = ("Bookman Old Style", 10), wrap = WORD, bd = 2, relief = SUNKEN)
        self.ReceiptText.pack(fill = BOTH, expand = 1)
        self.ReceiptFormat()
    
        self.FrameFive = LabelFrame(self.root, bg = "white", bd = 2, relief = GROOVE)
        self.FrameFive.place(x = 10, y = 310, width = 1180, height = 50)
        
        Button(self.FrameFive, cursor = "hand2", text = "Save", command = self.SaveData, font = ("Bookman Old Style", 14, "bold"), fg = "white", bg = "green").place(x = 10, y = 7, width = 180, height = 30)
        Button(self.FrameFive, cursor = "hand2", text = "Update", command = self.UpdateData, font = ("Bookman Old Style", 14, "bold"), fg = "white", bg = "blue").place(x = 200, y = 7, width = 180, height = 30)
        Button(self.FrameFive, cursor = "hand2", text = "Delete", command = self.DeleteData, font = ("Bookman Old Style", 14, "bold"), fg = "white", bg = "red").place(x = 390, y = 7, width = 180, height = 30)
        Button(self.FrameFive, cursor = "hand2", text = "Generate Receipt", command = self.GenerateReceipt, font = ("Bookman Old Style", 14, "bold"), fg = "black", bg = "skyblue").place(x = 580, y = 7, width = 200, height = 30)
        Button(self.FrameFive, cursor = "hand2", text = "Print", command = self.PrintReceipt, state = "disabled", font = ("Bookman Old Style", 14, "bold"), fg = "white", bg = "darkred").place(x = 790, y = 7, width = 120, height = 30)
        Button(self.FrameFive, cursor = "hand2", text = "Clear", command = self.ClearFieldData, font = ("Bookman Old Style", 14, "bold"), fg = "white", bg = "darkblue").place(x = 920, y = 7, width = 120, height = 30)
        Button(self.FrameFive, cursor = "hand2", text = "Exit", command = self.ExitApplication, font = ("Bookman Old Style", 14, "bold"), fg = "black", bg = "grey").place(x = 1050, y = 7, width = 115, height = 30)
        
        self.FrameSix = LabelFrame(self.root, bg = "white", bd = 2, relief = GROOVE)
        self.FrameSix.place(x = 10, y = 370, width = 1180, height = 220)
        
        self.xscroll = Scrollbar(self.FrameSix, orient = HORIZONTAL)
        self.yscroll = Scrollbar(self.FrameSix, orient = VERTICAL)
        
        self.DataTable = ttk.Treeview(self.FrameSix, columns = ("date","time","student_id","name","roll_no","branch","contact","email","book_id","book_name","author_name","issue_date","return_date","fine"), xscrollcommand = self.xscroll.set, yscrollcommand = self.yscroll.set)
        self.xscroll.pack(fill = X, side = BOTTOM)
        self.yscroll.pack(fill = Y, side = RIGHT)
        self.DataTable.pack(fill = BOTH, expand = 1)
        self.xscroll.config(command = self.DataTable.xview)
        self.yscroll.config(command = self.DataTable.yview)
        
        self.DataTable.bind("<ButtonRelease-1>", self.GetTreeviewData)
        
        self.DataTable.heading("date", text = "Date")
        self.DataTable.heading("time", text = "Time")
        self.DataTable.heading("student_id", text = "Student ID")
        self.DataTable.heading("name", text = "Student Name")
        self.DataTable.heading("roll_no", text = "Roll No")
        self.DataTable.heading("branch", text = "Branch")
        self.DataTable.heading("contact", text = "Contact No")
        self.DataTable.heading("email", text = "Email")
        self.DataTable.heading("book_id", text = "Book ID")
        self.DataTable.heading("book_name", text = "Book Name")
        self.DataTable.heading("author_name", text = "Author Name")
        self.DataTable.heading("issue_date", text = "Issue Date")
        self.DataTable.heading("return_date", text = "Return Date")
        self.DataTable.heading("fine", text = "Fine")
        
        self.DataTable["show"] = "headings"
        self.FetchDatabaseData()
        
    def SearchStudentID(self):
        try:
            if self.VarSearchData.get() == "":
                msg.showerror("Error", "All fields are required..", parent = self.root)
            else:
                cur.execute("select student_id from IssueTable where student_id = ?", (self.VarSearchData.get(),))
                result = cur.fetchall()
                if len(result) == 1:
                    self.FetchFile(self.VarSearchData.get())
                    self.FetchDatabase(self.VarSearchData.get())
                else:
                    msg.showerror("Error", f"{self.VarSearchData.get()} does not exist.", parent = self.root)
        except Exception as ex:
            msg.showerror("Error", f"Error due to {ex}", parent = self.root)
            print(ex)
    
    def FetchDatabase(self, search_id_data):
        SearchVariable = search_id_data
        cur.execute("select * from IssueTable where student_id = ?", (SearchVariable,))
        rows = cur.fetchall()
        self.DataTable.delete(*self.DataTable.get_children())
        for row in rows:
            self.DataTable.insert("", END, values = row)
    
    def FetchFile(self, search_id):
        SearchVariable = search_id
        with open(f"Receipts/{SearchVariable}.txt", "r") as fetchfile:
            FileData = fetchfile.read()
            self.ReceiptText.delete("1.0", END)
            self.ReceiptText.insert(END, FileData)
        
    def ListboxFetchData(self, event):
        self.value = self.ListBox.get(self.ListBox.curselection())
        cur.execute("select * from ProgrammingBooksDetails where book_name = ?", (self.value,))
        result = cur.fetchall()
        for data in result:
            dt = data[0]
            tm = data[1]
            Id = data[2]
            bt = data[3]
            ba = data[4]
            pr = data[5]

        self.book_id.set(Id)
        self.book_name.set(bt)
        self.author_name.set(ba)
        
        self.iDate = date.today()
        self.rDate = self.iDate + timedelta(days = 15)
        self.issue_date.set(self.iDate)
        self.return_date.set(self.rDate)
        self.fine.set("Rs.30 / Day")
               
    def ListBoxData(self):
        cur.execute("select book_name from ProgrammingBooksDetails")
        result = cur.fetchall()
        for name in result:
            self.ListBox.insert(END, name[0])
    
    def SaveData(self):
        try:
            if self.student_id.get() == "" or self.name.get() == "" or self.roll_no.get() == "" or self.branch.get() == "" or self.contact.get() == "" or self.email.get() == "" or self.book_id.get() == "Book ID" or self.book_name.get() == "Book Name" or self.author_name.get() == "Author Name" or self.issue_date.get() == "Issue Date" or self.return_date.get() == "Return Date" or self.fine.get() == "Fine per Day":
                msg.showerror("Error","All fields are required..", parent = self.root)
            else:
                cur.execute("select student_id from IssueTable where student_id = ?", (self.student_id.get(),))
                result = cur.fetchall()
                if len(result) == 1:
                    msg.showerror("Error", f"{self.student_id.get()} is already exists..", parent = self.root)
                else:
                    cur.execute("insert into IssueTable values (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (
                            self.date,
                            self.time,
                            self.student_id.get(),
                            self.name.get(),
                            self.roll_no.get(),
                            self.branch.get(),
                            self.contact.get(),
                            self.email.get(),
                            self.book_id.get(),
                            self.book_name.get(),
                            self.author_name.get(),
                            self.issue_date.get(),
                            self.return_date.get(),
                            self.fine.get(),
                        ))
                    conn.commit()
                    msg.showinfo("Success", "Book has been issued to student successfully...", parent = self.root)
                    self.ClearFieldData()
                    self.FetchDatabaseData()
        except Exception as ex:
            msg.showerror("Error", f"Error due to {ex}", parent = self.root)
    
    def DeleteData(self):
        try:
            if self.name.get() == "":
                msg.showerror("Error", "Student ID & Name is Must..", parent = self.root)
            else:
                delete = msg.askyesno("Delete", "Do you really want to delete ??", parent = self.root)
                if delete == 1:
                    cur.execute("delete from IssueTable where student_id = ?", (self.student_id.get(),))
                    conn.commit()
                    msg.showinfo("Success","Data has been deleted successfully", parent = self.root)
                    self.ClearFieldData()
                    self.FetchDatabaseData()
                else:
                    pass
        except Exception as ex:
            msg.showerror("Error", f"Error due to {ex}", parent = self.root)
    
    def UpdateData(self):
        try:
            if self.name.get() == "":
                msg.showerror("Error", "Student ID & Name is Must..", parent = self.root)
            else:
                update = msg.askyesno("Update", "Do you really want to update ??", parent = self.root)
                if update == 1:
                    cur.execute("update IssueTable set name=?,roll_no=?,branch=?,contact=?,email=?,book_id=?,book_name=?,author_name=?,issue_date=?,return_date=?,fine=? where student_id = ?", (
                        self.name.get(),
                        self.roll_no.get(),
                        self.branch.get(),
                        self.contact.get(),
                        self.email.get(),
                        self.book_id.get(),
                        self.book_name.get(),
                        self.author_name.get(),
                        self.issue_date.get(),
                        self.return_date.get(),
                        self.fine.get(),
                        self.student_id.get(),))
                    conn.commit()
                    msg.showinfo("Success","Data has been updated successfully", parent = self.root)
                    self.ClearFieldData()
                    self.FetchDatabaseData()
                else:
                    pass
        except Exception as ex:
            msg.showerror("Error", f"Error due to {ex}", parent = self.root)
    
    def SaveReceipt(self):
        PrintData = self.ReceiptText.get("1.0", END)
        with open(f"Receipts/{self.student_id.get()}.txt", "w") as filename:
            filename.write(PrintData)
            filename.close()
            
        # os.startfile("", "print")
        
    def PrintReceipt(self):
        with open(f"Receipts/{self.student_id.get()}.txt", "r") as filename:
            receipt = filename.read()
            filename.close()
            
        os.startfile(receipt, "print")
        
        
    def ClearFieldData(self):
        self.student_id.set(rd.randint(11111, 99999))
        self.name.set("")
        self.roll_no.set("")
        self.branch.set("")
        self.contact.set("")
        self.email.set("")
        self.book_id.set("Book ID")
        self.book_name.set("Book Name")
        self.author_name.set("Author Name")
        self.issue_date.set("Issue Date")
        self.return_date.set("Return Date")
        self.fine.set("Fine per Day")
        self.VarSearchData.set("")
        
        self.ReceiptFormat()
        self.FetchDatabaseData()
        
    def ExitApplication(self):
        exit = msg.askyesno("Exit Application", "Do you really want to exit application ??", parent = self.root)
        if exit == 1:
            self.root.destroy()
        else:
            pass
        
    def GetTreeviewData(self, event):
        r = self.DataTable.focus()
        content = self.DataTable.item(r)
        row = content["values"]
        self.student_id.set(row[2])
        self.name.set(row[3])
        self.roll_no.set(row[4])
        self.branch.set(row[5])
        self.contact.set(row[6])
        self.email.set(row[7])
        self.book_id.set(row[8])
        self.book_name.set(row[9])
        self.author_name.set(row[10])
        self.issue_date.set(row[11])
        self.return_date.set(row[12])
        self.fine.set(row[13])

    def FetchDatabaseData(self):
        cur.execute("select * from IssueTable")
        result = cur.fetchall()
        self.DataTable.delete(*self.DataTable.get_children())
        for row in result:
            self.DataTable.insert("", END, values = row)

    def ReceiptFormat(self):
        self.ReceiptText.delete("1.0", END)
        self.ReceiptText.insert(END, "====================================")
        self.ReceiptText.insert(END, "\n\t ** Kaali Groups | Library **")
        self.ReceiptText.insert(END, "\n====================================")
        self.ReceiptText.insert(END, "\n\t   ** Student's Details **")
        self.ReceiptText.insert(END, "\nStudent ID :-")
        self.ReceiptText.insert(END, "\nStudent Name :-")
        self.ReceiptText.insert(END, "\nRoll No :-")
        self.ReceiptText.insert(END, "\nBranch :-")
        self.ReceiptText.insert(END, "\nContact :-")
        self.ReceiptText.insert(END, "\nEmail :- ")
        self.ReceiptText.insert(END, "\n====================================")
        self.ReceiptText.insert(END, "\n            ** Issue Book Details **")
        self.ReceiptText.insert(END, "\nBook ID :-")
        self.ReceiptText.insert(END, "\nBook Name :-")
        self.ReceiptText.insert(END, "\nAuthor Name :-")
        self.ReceiptText.insert(END, "\n")
        self.ReceiptText.insert(END, "\nIssue Date :-")
        self.ReceiptText.insert(END, "\nReturn Date :-")
        self.ReceiptText.insert(END, "\n")

        self.ReceiptText.insert(END, "\nFine :-")
        self.ReceiptText.insert(END, "\n** Note")
        self.ReceiptText.insert(END, "\nIf you don't return book on return date you will be by fine .i.e Rs. 30 for per Day.")
        self.ReceiptText.insert(END, "\n")

        self.ReceiptText.insert(END, "\n=============Thank You==============")
        self.ReceiptText.insert(END, "\nBy Kaali Groups of Library Management System")

    def GenerateReceipt(self):
        self.ReceiptText.delete("1.0", END)
        self.ReceiptText.insert(END, "====================================")
        self.ReceiptText.insert(END, "\n\t ** Kaali Groups | Library **")
        self.ReceiptText.insert(END, "\n====================================")
        self.ReceiptText.insert(END, "\n\t   ** Student's Details **")
        self.ReceiptText.insert(END, f"\nStudent ID :- {self.student_id.get()}")
        self.ReceiptText.insert(END, f"\nStudent Name :- {self.name.get()}")
        self.ReceiptText.insert(END, f"\nRoll No :- {self.roll_no.get()}")
        self.ReceiptText.insert(END, f"\nBranch :- {self.branch.get()}")
        self.ReceiptText.insert(END, f"\nContact :- {self.contact.get()}")
        self.ReceiptText.insert(END, f"\nEmail :- {self.email.get()}")
        self.ReceiptText.insert(END, "\n====================================")
        self.ReceiptText.insert(END, "\n            ** Issue Book Details **")
        self.ReceiptText.insert(END, f"\nBook ID :- {self.book_id.get()}")
        self.ReceiptText.insert(END, f"\nBook Name :- {self.book_name.get()}")
        self.ReceiptText.insert(END, f"\nAuthor Name :- {self.author_name.get()}")
        self.ReceiptText.insert(END, "\n")
        self.ReceiptText.insert(END, f"\nIssue Date :- {self.issue_date.get()}")
        self.ReceiptText.insert(END, f"\nReturn Date :- {self.return_date.get()}")
        self.ReceiptText.insert(END, "\n")

        self.ReceiptText.insert(END, f"\nFine :- {self.fine.get()}")
        self.ReceiptText.insert(END, "\n** Note")
        self.ReceiptText.insert(END, "\nIf you don't return book on return date you will be by fine .i.e Rs. 30 for per Day.")
        self.ReceiptText.insert(END, "\n")

        self.ReceiptText.insert(END, "\n=============Thank You==============")
        self.ReceiptText.insert(END, "\nBy Kaali Groups of Library Management System")
        
        self.SaveReceipt()

if __name__ == "__main__":
    root = Tk()
    obj = LibraryClass(root)
    root.mainloop()