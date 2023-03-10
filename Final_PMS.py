import mysql.connector as m

db=m.connect(host="localhost",user="root",password="root")
cursor=db.cursor()

cursor.execute("create database if not exists bank_data")
cursor.execute("use bank_data")
cursor.execute("create table if not exists account_data(Acc_no int primary key auto_increment,Fname varchar(30),Lname varchar(30),Balance float,Phone_Number int)")


def open_account():
    fname=input("Enter your first name : ")
    lname=input("Enter your last name : ")
    f_balance=float(input("Enter the opening balance : "))
    Phone_No=int(input("Enter your contact number : "))
    data1=(fname,lname,f_balance,Phone_No)
    query1=("insert into account_data(Fname ,Lname ,Balance ,Phone_Number) values(%s,%s,%s,%s)")
    cursor.execute(query1,data1)

    db.commit()
    query2=("select Acc_no from account_data where Phone_Number=%s")
    s=(Phone_No,)
    cursor.execute(query2,s)
    result = cursor.fetchone()
    #fetchone returns data in a tuple.
    for record in result:
        print("your account no:",record)

    print("Congratulation!! Your account is created successfully!")
    print("Press Enter for options")
    input()
    menu()

def deposit():
    amt=float(input("Enter the amount you want to deposit : "))
    acc=int(input("Enter the account number : "))
    data=(acc,)
    query=("select Balance from account_data where Acc_no=%s")
    cursor.execute(query,data)
    result=cursor.fetchone()

    total=result[0]+amt

    uquery=("update account_data set Balance=%s where Acc_no=%s")
    data=(total,acc)
    cursor.execute(uquery,data)
    db.commit()
    print("Transaction completed Successfully!!")
    print("Press Enter for options")
    input()
    menu()

def withdraw():
    amt=float(input("Enter the amount you want to withdraw : "))
    acc=int(input("Enter the account number : "))
    data=(acc,)
    query=("select Balance from account_data where Acc_no=%s")
    cursor.execute(query,data)
    result=cursor.fetchone()

    total=result[0]-amt

    if total<0:
        print("withdraw limit exceeded,current balance is :",result[0])
        menu()
    if total>0:
        uquery=("update account_data set Balance=%s where Acc_no=%s")
        data=(total,acc)
        cursor.execute(uquery,data)
        db.commit()
        print("Transaction completed Successfully!!")
        print("Press Enter for options")
        input()
        menu()

def show():
    acc=int(input("Enter the Account Number : "))
    query=("select Balance from account_data where Acc_no=%s")
    s=(acc,)
    cursor.execute(query,s)
    result = cursor.fetchone()
    print("Your balance is",result,"Rupees")
    print("Press Enter for options")
    input()
    menu()


print("Welcome")
print("Press Enter for more options")
input()

def menu():
        print("1.Open Account\n2.Deposit Money\n3.withdraw Money\n4.Show Balance\n0.Exit")
        n=int(input("Enter the Choice : "))
    
        if n==1:
            open_account()
        elif n==2:
            deposit()
        elif n==3:
            withdraw()
        elif n==4:
            show()
        elif n==0:
            print("Thank you")
        else:
            print("Enter valid option")
            menu()

menu()
