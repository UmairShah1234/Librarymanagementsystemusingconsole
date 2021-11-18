import mysql.connector
import time
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="umairshah@1234",
    database="librarymanagementsystem"
)
mycursor=mydb.cursor()

# members class
class Members:
    def register(self):
        mycursor.execute("SELECT * FROM members")
        myresult = mycursor.fetchall()
        first_name=input("Enter your first name : ")
        last_name=input("Enter your last name : ")
        phone_number=input("Enter your number : ")
        email=input("Enter your email : ")
        p=0
        for x in myresult:
            if x[1]==first_name and x[2]==last_name and x[3]==phone_number and x[4]==email:
                p=1
        if p==1:
            print("Already registered...")
        else:
            sql="INSERT INTO members (first_name,last_name,phone_number,email) VALUES (%s,%s,%s,%s)"
            val=(first_name,last_name,phone_number,email)
            mycursor.execute(sql,val)
            mydb.commit()
    def show_members(self):
        while True:
            print("1. show everthing\n"
                  "2. show  name only\n"
                  "3. show first name  with phone number \n"
                  "4. show first name  with phone number and email id\n"
                  "5. show first name with email")
            user_choice = int(input("Enter your choice : "))
            if user_choice == 1:
                mycursor.execute("SELECT * FROM members")
                myresult = mycursor.fetchall()
                for x in myresult:
                    print(x)
            elif user_choice == 2:
                mycursor.execute("SELECT first_name,last_name FROM members")
                myresult=mycursor.fetchall()
                for x in myresult:
                    print(x)
                print()
            elif user_choice == 3:
                mycursor.execute("SELECT first_name,phone_number,email FROM members")
                myresult = mycursor.fetchall()
                for x in myresult:
                    print(x)
                print()
            elif user_choice == 4:
                mycursor.execute("SELECT first_name,email FROM members")
                myresult = mycursor.fetchall()
                for x in myresult:
                    print(x)
                print()
            else:
                break
    def remove_member(self):
        first_name=input("Enter the first name to delete : ")
        id=int(input("enter the id : "))
        sql="DELETE FROM TABLE WHERE id=%s,first_name=%s"
        val=(id,first_name)
        mycursor.execute(sql,val)
        mydb.commit()

# books class
class Books(Members):
    def showbooks(self):
        mycursor.execute("SELECT * FROM books")
        myresult=mycursor.fetchall()
        while True:
            print("1. show everthing\n"
                "2. show book name only\n"
                "3. show book with author\n")
            user_choice=int(input("Enter your choice : "))
            if user_choice==1:
                for x in myresult:
                    print(x)
            elif user_choice==2:
                for i,x in enumerate(myresult):
                    print(i,x[1])
                print()
            elif user_choice==3:
                for i,x in enumerate(myresult):
                    print(f"{i}.Book={x[1]} : Author={x[2]}")
                print()
            else:
                break
    def add_books(self):
        mycursor.execute("SELECT * FROM books")
        myresult = mycursor.fetchall()
        book_name=input("Enter the book name : ")
        author_name=input("Author name : ")
        p=0
        for x in myresult:
            if book_name==x[1] and author_name==x[2]:
                p=1
        if p==1:
            print("Already present...")
        else:
            print("adding book..")
            sql = "INSERT INTO books (book_name,author_name) VALUES (%s,%s)"
            val = (book_name, author_name)
            mycursor.execute(sql, val)
            mydb.commit()
            print("added...")
    def issue_book(self):
        user_choice=input("Enter book name : ")
        p=0
        mycursor.execute("SELECT book_id,book_name,issue FROM books")
        myresult=mycursor.fetchall()
        print(myresult)
        for x in myresult:
            if user_choice==x[1] and x[2] == None:
                p=1
                bkid=x[0]

                try:
                    val=('issue',bkid)
                    mycursor.execute("UPDATE books SET issue=%s WHERE book_id= %s ",val)
                    mydb.commit()
                except Exception as e:
                    print(e)
                break
        else:
            print("Not found or issued to someone...")
        if p==1:
            member_name = input("Enter your first name : ")
            try:
                val=(member_name,)
                mycursor.execute("SELECT member_id FROM members WHERE first_name = %s",val)
                r=mycursor.fetchall()
                print(r)
                for x in r:
                    mem_id = x[0]
                    print(mem_id)
                mycursor.execute("INSERT INTO issuebook  (book_id,member_id) VALUES (%s,%s)",(bkid,mem_id))
                mydb.commit()
                print("issued.................")
            except Exception as e:
                print(e)






# Library class
class Library(Books,Members):
    def func(self):
        print("Welcome")
        while True:
            print("1. show books")
            print("2. issue book")
            print("3. add books")
            print("4. show members")
            print("5. register members")
            print("6. remove members")
            user_input=int(input("Enter your choice : "))
            if user_input==1:
                print("showing books..")
                time.sleep(0.8)
                self.showbooks()
            elif user_input==2:
                self.issue_book()
                print("issuing book..")
                time.sleep(0.8)
            elif user_input==3:
                self.add_books()

                time.sleep(0.8)
            elif user_input==4:
                print("showing members..")
                time.sleep(0.8)
                self.show_members()
            elif user_input==5:
                print("registering members..")
                time.sleep(0.8)
                self.register()
            elif user_input==6:
                print("removing members..")
                time.sleep(0.8)
            else:
                print("Try again...")
                break

if __name__=="__main__":
    l=Library()
    l.func()



