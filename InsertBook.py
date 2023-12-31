from tkinter import *
from tkinter import ttk
import tkinter.messagebox as msg
import random as rd
from datetime import *
import sqlite3

conn = sqlite3.connect("LibraryMS.db")
cur = conn.cursor()

class AddBookClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System | Developed by Sikandar Singh")
        self.root.geometry("1200x600+30+0")
        self.root.resizable(0, 0)
        self.root.grab_set()
        
        self.main_label = Label(self.root, bd = 6, relief = RAISED, text = "Kaali Groups | Library Management System", fg = "white", bg = "darkblue", font = ("Bookman Old Style", 20, "bold"))
        self.main_label.pack(fill = X)

        self.main_heading = Label(self.root, text = "ADD BOOKS DETAILS", fg = "darkblue", font = ("Bookman Old Style", 20, "bold"))
        self.main_heading.pack(fill = X, pady = 20)
    
        self.FrameOne = LabelFrame(self.root, bg = "white", bd = 8, relief = SUNKEN)
        self.FrameOne.pack(padx = 40, pady = 30)
        
        Label(self.FrameOne, text = "Date", font = ("Bookman Old Style", 12), bg = "white", fg = "darkblue").grid(row = 0, column = 0, sticky = "w", padx = 20, pady = 10)
        Label(self.FrameOne, text = "Time", font = ("Bookman Old Style", 12), bg = "white", fg = "darkblue").grid(row = 1, column = 0, sticky = "w", padx = 20, pady = 10)
        Label(self.FrameOne, text = "Book ID", font = ("Bookman Old Style", 12), bg = "white", fg = "darkblue").grid(row = 2, column = 0, sticky = "w", padx = 20, pady = 10)
        Label(self.FrameOne, text = "Book Name", font = ("Bookman Old Style", 12), bg = "white", fg = "darkblue").grid(row = 3, column = 0, sticky = "w", padx = 20, pady = 10)
        Label(self.FrameOne, text = "Author Name", font = ("Bookman Old Style", 12), bg = "white", fg = "darkblue").grid(row = 4, column = 0, sticky = "w", padx = 20, pady = 10)
        Label(self.FrameOne, text = "Price", font = ("Bookman Old Style", 12), bg = "white", fg = "darkblue").grid(row = 5, column = 0, sticky = "w", padx = 20, pady = 10)
        
        self.date = StringVar()
        self.time = StringVar()
        self.book_id = StringVar()
        self.book_name = StringVar()
        self.author_name = StringVar()
        self.price = StringVar()
        
        Entry(self.FrameOne, bd = 5, relief = SUNKEN, textvariable = self.date, state = "readonly", font = ("Bookman Old Style", 12), bg = "lightgreen").grid(row = 0, column = 1, sticky = "w", padx = 20, pady = 10)
        Entry(self.FrameOne, bd = 5, relief = SUNKEN, textvariable = self.time, state = "readonly", font = ("Bookman Old Style", 12), bg = "lightgreen").grid(row = 1, column = 1, sticky = "w", padx = 20, pady = 10)
        Entry(self.FrameOne, bd = 5, relief = SUNKEN, textvariable = self.book_id, state = "readonly", font = ("Bookman Old Style", 12), bg = "lightgreen").grid(row = 2, column = 1, sticky = "w", padx = 20, pady = 10)
        Entry(self.FrameOne, bd = 5, relief = SUNKEN, textvariable = self.book_name, font = ("Bookman Old Style", 12), bg = "lightgreen").grid(row = 3, column = 1, sticky = "w", padx = 20, pady = 10)
        Entry(self.FrameOne, bd = 5, relief = SUNKEN, textvariable = self.author_name, font = ("Bookman Old Style", 12), bg = "lightgreen").grid(row = 4, column = 1, sticky = "w", padx = 20, pady = 10)
        Entry(self.FrameOne, bd = 5, relief = SUNKEN, textvariable = self.price, font = ("Bookman Old Style", 12), bg = "lightgreen").grid(row = 5, column = 1, sticky = "w", padx = 20, pady = 10)

        self.book_id.set(rd.randint(111111, 999999))
        self.c_dt = datetime.now()
        self.date.set(f"{self.c_dt.day}-{self.c_dt.month}-{self.c_dt.year}")
        self.time.set(f"{self.c_dt.hour} : {self.c_dt.minute} : {self.c_dt.second}")

        Button(self.FrameOne, bd = 4, relief = RAISED, cursor = "hand2", text = "Add Book", command = self.AddBookDetails, font = ("Bookman Old Style", 12, "bold"), fg = "white", bg = "green").grid(row = 6, column = 0, sticky = "w", padx = 20, pady = 10)
        Button(self.FrameOne, bd = 4, relief = RAISED, cursor = "hand2", text = "Exit", command = self.ExitApplication, font = ("Bookman Old Style", 12, "bold"), fg = "white", bg = "red").grid(row = 6, column = 1, sticky = "w", padx = 20, pady = 10)

    def AddBookDetails(self):
        try:
            if self.date.get() == "" or self.time.get() == "" or self.book_id.get() == "" or self.book_name.get() == "" or self.author_name.get() == "" or self.price.get() == "":
                msg.showerror("Error", "All fields are required", parent = self.root)
            else:
                cur.execute("select book_id from ProgrammingBooksDetails where book_id = ?", (self.book_id.get(),))
                result = cur.fetchall()
                if len(result) == 0:
                    cur.execute("insert into ProgrammingBooksDetails values (?,?,?,?,?,?)", (
                        self.date.get(),
                        self.time.get(),
                        self.book_id.get(),
                        self.book_name.get(),
                        self.author_name.get(),
                        self.price.get(),
                    ))
                    conn.commit()
                    msg.showinfo("Success", "Book has been added successfully...", parent = self.root)
                    self.ClearData()
                else:
                    msg.showerror("Error", f"{self.book_id.get()} is already Exists\nTry different..", parent = self.root)
        except Exception as ex:
            msg.showerror("Error", f"Error due to {ex}", parent = self.root)
            
    def ClearData(self):
        self.book_id.set(rd.randint(111111, 999999))
        self.c_dt = datetime.now()
        self.date.set(f"{self.c_dt.day}-{self.c_dt.month}-{self.c_dt.year}")
        self.time.set(f"{self.c_dt.hour} : {self.c_dt.minute} : {self.c_dt.second}")
        self.book_name.set("")
        self.author_name.set("")
        self.price.set("")
    
    def ExitApplication(self):
        close = msg.askyesno("Exit Application","Do you really want to exit ??", parent = self.root)
        if close == True:
            self.root.destroy()
    
if __name__ == "__main__":
    root = Tk()
    obj = AddBookClass(root)
    root.mainloop()