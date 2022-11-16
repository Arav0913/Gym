import time
import random
import mysql.connector
import pwinput

mydb=mysql.connector.connect(host='localhost',user='root',database='CBSE',password='12345678')

def main():
    
    print("\t\t\t\t*************************")
    print("\t\t\t\tWELCOME TO VARGHIS AKHADA")
    print("\t\t\t\t*************************")
    print('''

     \t \t1. Sign up
     \t \t2. Login
     \t \t3. Owners Login
    ''')
    m = int(input("Please select the login type (1-3): "))
    
    if m == 1:
        signup()
    
    elif m == 2:
        login()
    
    elif m == 3:
        o_login()
    
    else:
        ('Invalid entry!!!')
        
        time.sleep(1)
        main()



def signup():
    
    global username
    
    cursor=mydb.cursor()
    
    username = input('Enter New Username: ')
    
    sql = "select * from login"
    sql2 = "select * from o_login"
    cursor.execute(sql)
    tp = cursor.fetchall()
    cursor.execute(sql2)
    tp2 = cursor.fetchall()
    
    for i in tp:
        for j in tp2:
            if j[0]==username:
                print('Username is in use try again')
                signup()
        
        if i[0] == username:
            print('Username is in use try again')
            signup()
    
    else:
        password = pwinput.pwinput('Enter a password: ')      
    
    sql17 = "insert into login values('{}','{}','Basic','NULL',NULL,'NULL',NULL)".format(username,password)
    cursor.execute(sql17)
    mydb.commit()
    
    signup_2()

def signup_2():
    
    su=int(input('''
    1. Do you want to try out for a discount?
    2. Continue to login
    :'''))
    
    if su == 1:
        discount()
    
    if su == 2:
        login()

def discount():

    cursor=mydb.cursor()
    
    r1 = random.randint(10,90)
    r = r1/100
    print('Your discount is:',r1,'%')
    
    sql = "update login set Discount_Percent = {} where Username = '{}'".format(r1,username)
    cursor.execute(sql)
    mydb.commit()
    
    print('Please login to continue:')
    
    time.sleep(1)
    login()



def login():

    global u
    global p
    
    u=input('Enter username: ')
    p=pwinput.pwinput('Password: ') 
    
    sql = "select * from login"
    cursor=mydb.cursor()
    cursor.execute(sql)
    tp = cursor.fetchall()
    
    for i in tp:
    
        if i[0]==u and i[1]==p:
            time.sleep(1)
            menu()
            break
    
    else:
        exit = int(input('''
    1. Do you want to try again?
    2. Do you want to exit?
    :'''))
        
        if exit == 1:
            login()
        
        elif exit == 2:
            main()

def menu():

    print('''
     \t \tMENU
     \t \t1. MY ACCOUNT
     \t \t2. MEMBERSHIP PLANS
     \t \t3. CHANGE MEMBERSHIP
     \t \t4. DELETE ACCOUNT
     \t \t5. EQUIPMENT INFORMATION
     \t \t6. TIMINGS
     \t \t7. CHANGE PASSWORD
     \t \t8. ABOUT US
     \t \t9. LOCATIONS
     \t \t10. REVIEW
     \t \t11. SIGN OUT

    :''')
    n = int(input("please select the menu item you want to continue with: "))
    
    if n == 1:
        My_Account()
    
    elif n == 2:
        gmp()
    
    elif n == 3:
        upgrade()
    
    elif n == 4:
        CM()
    
    elif n == 5:
        EI()
    
    elif n == 6:
        mytimings()
    
    elif n==7:
        Changepass()
    
    elif n == 8:
        aboutus()
    
    elif n == 9:
        locations()
    
    elif n == 10:
        review()

    elif n == 11:
        main()
    
    else:
        print("Please select a valid option (1-11): ")
        time.sleep(1)
        menu()

def My_Account():
    
    cursor=mydb.cursor()
    sqq="select * from login where username = '{}'".format(u)
    cursor.execute(sqq)
    d=cursor.fetchall()
    
    print('Your Username:',d[0][0])
    print('Your Password:',d[0][1])
    print('Your Plan:',d[0][2])
    print('Your Timings:',d[0][3])
    print('Your Payment Type:',d[0][5])
    print('Your',d[0][5],'amount is:',d[0][4])
    
    time.sleep(3)
    menu()

def gmp():

    print(''' 
     \t \tGym Membership plans:

     \tPLAN 1: Basic Plan - This plan provides users gym access only.
    
     \tPLAN 2: Advanced Plan - This plan provides users the ability to access all equipment with no restriction but only in gym hours also access to training plans.
    
     \tPLAN 3: Enthusiast Plan - This plan contains all the benefits of the Advanced plan but along with it the users get 24/7 gym access.

     \tEnter 4 to EXIT
    
    :''')
    
    cursor=mydb.cursor()
    
    gmpv=int(input('Enter the plan number you would like to continue with: ')) 

    if gmpv == 1:
        ba = "Basic"
        sql1 = "update login set plans = '{}' where username = '{}'".format(ba,u)
        cursor.execute(sql1)
        mydb.commit()
        
        print('Your new plan is set to Basic!!!')
        
        time.sleep(2)
        payment()

    elif gmpv == 2:
        ap = "Advanced"
        sql2 = "update login set plans = '{}' where username = '{}'".format(ap,u)
        cursor.execute(sql2)
        mydb.commit()
        
        print('Your new plan is set to Advanced!!!')
        
        time.sleep(2)
        payment()

    elif gmpv == 3:
        ep = "Enthusiast"
        sql3 = "update login set plans = '{}' where username = '{}'".format(ep,u)
        cursor.execute(sql3)
        mydb.commit()
        
        print('Your new plan is set to Enthusiast!!!')
        
        time.sleep(2)
        payment()

    elif gmpv == 4:
        menu()
    
    else:
        print('Entered value is invalid!')
        time.sleep(2)
        gmp()

def upgrade():

    cursor=mydb.cursor()
    
    sql4="select plans from login where username = '{}'".format(u)
    cursor.execute(sql4)
    f=cursor.fetchall()
    
    print('Your current plan is:',f[0][0])

    time.sleep(2)
    
    print(''' 
     \t \tGym Membership plans:

     \tPLAN 1: Basic Plan - This plan provides users gym access only.
    
     \tPLAN 2: Advanced Plan - This plan provides users the ability to access all equipment with no restriction but only in gym hours also access to training plans.
    
     \tPLAN 3: Enthusiast Plan - This plan contains all the benefits of the Advanced plan but along with it the users get 24/7 gym access.

     \tEnter 4 to EXIT
    
    : ''')
    
    cursor=mydb.cursor()
    
    upgrade=int(input('Enter the plan number you would like to modify to: '))  
    
    if upgrade == 1:
        ba = "Basic"
        sql5 = "update login set plans = '{}' where username = '{}'".format(ba,u)
        cursor.execute(sql5)
        mydb.commit()
        
        print('Your new plan is set to Basic!!!')
        
        time.sleep(2)
        payment()
    
    elif upgrade == 2:
        ap = "Advanced"
        sql6 = "update login set plans = '{}' where username = '{}'".format(ap,u)
        cursor.execute(sql6)
        mydb.commit()
        
        print('Your new plan is set to Advanced!!!')
        
        time.sleep(2)
        payment()
    
    elif upgrade == 3:
        ep = "Enthusiast"
        sql7 = "update login set plans = '{}' where username = '{}'".format(ep,u)
        cursor.execute(sql7)
        mydb.commit()
        
        print('Your new plan is set to Enthusiast!!!')
        
        time.sleep(2)
        payment()
    
    elif upgrade == 4:
        menu()
    
    else:
        print('Entered value is invalid!')
        
        time.sleep(2)
        upgrade()

def payment():

    cursor=mydb.cursor()
    sql__1 = "select plans from login where username = '{}'".format(u)
    cursor.execute(sql__1)
    plan=cursor.fetchall()
    sqk = "select Discount_Percent from login where username = '{}'".format(u)
    cursor.execute(sqk)
    r1= cursor.fetchall()
    
    r = r1[0][0]/100

    M = 'Monthly'
    Q = 'Quarterly'
    Y = 'Yearly'

    if plan[0][0] == 'Basic' or plan[0][0] == 'basic':

        print('\t \tPayment options are:')
        print('\t1. Monthly - Rs 999 per month; Amount after discount:',round(999-999*r))
        print('\t2. Quarterly - Rs 2899 per quarter; Amount after discount:',round(2899-2899*r))
        print('\t3. Yearly - Rs 9999 per year; Amount after discount:',round(9999-9999*r))

        pt = int(input(':'))

        if pt == 1:
            n9 = round(999-999*r)
            sql__2 = "update login set payment = {} where username = '{}'".format(n9,u)
            sql__3 = "update login set payment_type = '{}' where username = '{}'".format(M,u)
            cursor.execute(sql__2)
            cursor.execute(sql__3)
            mydb.commit()
            
            print('Payment amount and payment type are added to your account!!!')
            
            time.sleep(2)
            Timings(u)
        
        elif pt == 2:
            n8 = round(2899 - 2899*r)
            sql__4 = "update login set payment = {} where username = '{}'".format(n8,u)
            sql__5 = "update login set payment_type = '{}' where username = '{}'".format(Q,u)
            cursor.execute(sql__4)
            cursor.execute(sql__5)
            mydb.commit()
            
            print('Payment amount and payment type are added to your account!!!')
            
            time.sleep(2)
            Timings(u)
        
        elif pt == 3:
            n7 = round(9999 - 9999*r)
            sql__6 = "update login set payment = {} where username = '{}'".format(n7,u)
            sql__7 = "update login set payment_type = '{}' where username = '{}'".format(Y,u)
            cursor.execute(sql__6)
            cursor.execute(sql__7)
            mydb.commit()
            
            print('Payment amount and payment type are added to your account!!!')
            
            time.sleep(2)
            Timings(u)

    elif plan[0][0] == 'Advanced' or plan[0][0] == 'advanced':
        print('\t \tPayment options are:')
        print('\t1. Monthly - Rs 1499 per month; Amount after discount:',round(1499 - 1499*r))
        print('\t2. Quarterly - Rs 4299 per quarter; Amount after discount:',round(4299 - 4299*r))
        print('\t3. Yearly - Rs 14999 per year; Amount after discount:',round(14999 - 14999*r))
        pt = int(input(':'))

        if pt == 1:
            n6 = round(1499 - 1499*r)
            sql__8 = "update login set payment = {} where username = '{}'".format(n6,u)
            sql__9 = "update login set payment_type = '{}' where username = '{}'".format(M,u)
            cursor.execute(sql__8)
            cursor.execute(sql__9)
            mydb.commit()
            
            print('Payment amount and payment type are added to your account!!!')
            
            time.sleep(2)
            Timings(u)
        
        elif pt == 2:
            n5 = round(4299 - 4299*r)
            sql__10 = "update login set payment = {} where username = '{}'".format(n5,u)
            sql__11 = "update login set payment_type = '{}' where username = '{}'".format(Q,u)
            cursor.execute(sql__10)
            cursor.execute(sql__11)
            mydb.commit()
            
            print('Payment amount and payment type are added to your account!!!')
            
            time.sleep(2)
            Timings(u)
        
        elif pt == 3:
            n4=round(14999 - 14999*r)
            sql__12 = "update login set payment = {} where username = '{}'".format(n4,u)
            sql__13 = "update login set payment_type = '{}' where username = '{}'".format(Y,u)
            cursor.execute(sql__12)
            cursor.execute(sql__13)
            mydb.commit()
            
            print('Payment amount and payment type are added to your account!!!')
            
            time.sleep(2)
            Timings(u)

    elif plan[0][0] == 'Enthusiast' or plan[0][0] == 'enthusiast':
        print('\t\tPayment options are:')
        print('\t1. Monthly - Rs 1999 per month; Amount after discount:',round(1999 - 1999*r))
        print('\t2. Quarterly - Rs 5499 per quarter; Amount after discount:',round(5499 - 5499*r))
        print('\t3. Yearly - Rs 19999 per year; Amount after discount:',round(19999 - 19999*r))
        pt = int(input(':'))
        if pt == 1:
            n3=round(1999 - 1999*r)
            sql__14 = "update login set payment = {} where username = '{}'".format(n3,u)
            sql__15 = "update login set payment_type = '{}' where username = '{}'".format(M,u)
            cursor.execute(sql__14)
            cursor.execute(sql__15)
            mydb.commit()
            
            print('Payment amount and payment type are added to your account!!!')
            
            time.sleep(2)
            Timings(u)
        
        elif pt == 2:
            n1 = round(5499 - 5499*r)
            sql__16 = "update login set payment = {} where username = '{}'".format(n1,u)
            sql__17 = "update login set payment_type = '{}' where username = '{}'".format(Q,u)
            cursor.execute(sql__16)
            cursor.execute(sql__17)
            mydb.commit()
            
            print('Payment amount and payment type are added to your account!!!')
            
            time.sleep(2)
            Timings(u)
        
        elif pt == 3:
            n=round(19999 - 19999*r)
            sql__18 = "update login set payment = {} where username = '{}'".format(n,u)
            sql__19 = "update login set payment_type = '{}' where username = '{}'".format(Y,u)
            cursor.execute(sql__18)
            cursor.execute(sql__19)
            mydb.commit()
            
            print('Payment amount and payment type are added to your account!!!')
            
            time.sleep(2)
            Timings(u)

def CM():

    cm=input ('Are you certain you want to leave gym? (yes/no): ')
    
    if cm == 'yes':
        u1=input('Enter username:')
        p1=pwinput.pwinput('Password:')
        
        sql8 = "select * from login"
        cursor=mydb.cursor()
        cursor.execute(sql8)
        tp = cursor.fetchall()
        
        for i in tp:
            
            if i[0]==u1 and i[1]==p1 and u1 == u and p1 == p:
                sql9="delete from login where Username = '{}'".format(u)
                cursor.execute(sql9)
                mydb.commit()
                
                print('Your account has been deleted!!!')
                
                time.sleep(2)
                main()
        
        else:
            print('Incorrect Username or Password')
            
            time.sleep(2)
            CM()
    
    else:
        menu()

def EI():

    sql10 = "select * from EI"
    cursor=mydb.cursor()
    cursor.execute(sql10)
    tp = cursor.fetchall()
    
    for i in tp:
        print('\t',i)
    
    time.sleep(3)
    menu()

def Timings(u):
    
    sql_5 = "select plans from login where username = '{}'".format(u)
    cursor=mydb.cursor()
    cursor.execute(sql_5)
    t=cursor.fetchall()
    
    for i in t:

        if i[0] == 'Basic' or i[0] == 'basic':
            To1=int(input('''
             \t \tPlease chose your gym timings
             \t \tAvailable Timing options are:
             \t1. 6:00 am - 9:00 am
             \t2. 1:00 pm - 4:00 pm
             \t3. 7:00 pm - 9:00 pm  
            '''))
            
            if To1 == 1:
                t1 = '6:00 am - 9:00 am'
                sql_6 = "update login set Timings = '{}' where username = '{}'".format(t1,u)
                cursor.execute(sql_6)
                mydb.commit()
                
                print('Timings changed!!!')

                time.sleep(2)
                menu()
            
            elif To1 == 2:
                t2 = '1:00 pm - 4:00 pm'
                sql_7 = "update login set Timings = '{}' where username = '{}'".format(t2,u)
                cursor.execute(sql_7)
                mydb.commit()
                
                print('Timings changed!!!')
                
                time.sleep(2)
                menu()
            
            elif To1 == 3:
                t3 = '7:00 pm - 9:00 pm'
                sql_8 = "update login set Timings = '{}' where username = '{}'".format(t3,u)
                cursor.execute(sql_8)
                mydb.commit()
                
                print('Timings changed!!!')
                
                time.sleep(2)
                menu()
        
        elif i[0] == 'Advanced' or i[0] == 'advanced':
            To2 = int(input('''
             \t \tPlease chose your gym timings
             \t \tAvailable Timing options are:
             \t1. 6:00 am - 10:00 am
             \t2. 3:00 pm - 6:00 pm
             \t3: 7:00 pm - 10:00 pm
            '''))

            if To2 == 1:
                t4 = '6:00 am - 10:00 am'
                sql_9 = "update login set Timings = '{}' where username = '{}'".format(t4,u)
                cursor.execute(sql_9)
                mydb.commit()
                
                print('Timings changed!!!')
                
                time.sleep(2)
                menu()
            
            elif To2 == 2:
                t5 = '3:00 pm - 6:00 pm'
                sql_10 = "update login set Timings = '{}' where username = '{}'".format(t5,u)
                cursor.execute(sql_10)
                mydb.commit()
                
                print('Timings changed!!!')
                
                time.sleep(2)
                menu()

            elif To2 == 3:
                t6 = '7:00 pm - 10:00 pm'
                sql_11 = "update login set Timings = '{}' where username = '{}'".format(t6,u)
                cursor.execute(sql_11)
                mydb.commit()
                
                print('Timings changed!!!')
                
                time.sleep(2)
                menu()

        elif i[0] == 'Enthusiast' or i[0] == 'enthusiast':
            print('As a member of the Enthusiast plan you can access the gym whenever you want (24/7)')
            To3 = '24/7'
            sql_12 = "update login set Timings = '{}' where username = '{}'".format(To3,u)
            cursor.execute(sql_12)
            mydb.commit()
            
            time.sleep(2)
            menu()
        
        else:
            print('Entered value is invalid!!!')
            
            time.sleep(2)
            Timings(u)

def mytimings():

    cursor=mydb.cursor()
    sql = "select Timings from login where username = '{}'".format(u)
    cursor.execute(sql)
    k = cursor.fetchall()
    
    print('Your currents Timings are: ',k[0][0])
    
    time.sleep(2)

    t = int(input('''
    1. Do you want to change Timings?
    2. Do you want to exit?
    '''))
    
    if t == 1:
        Timings(u)
    
    else:
        menu()

def Changepass():
    
    passw= pwinput.pwinput('Enter Old Password: ')
    
    if passw == p:
        cursor=mydb.cursor()
        passnew=pwinput.pwinput('Enter new password:')
        sql13 = "update login set password = '{}' where username = '{}'".format(passnew,u)
        cursor.execute(sql13)
        mydb.commit()
        
        print('Password has been updated!!!')
        
        time.sleep(2)
        menu()
    
    else:
        print('Entered password is incorrect: ')

        a = int(input('''
        1. Do you wan't to try again?
        2. Do you wan't to exit?
        '''))

        if a == 1:
            Changepass()
        
        else:
            menu()

def aboutus():

    print('''
 \t \tWe are a gym club under the name 'Vargis Akhada', we are here to make a big change in the fitness regime of this country. We want
 \t \tto inspire the entire country to workout and improve on their fitness as being fit is never a harm and always a gain.
 \t \tCompany name: Vargis Akhada
 \t \tCEO: Arav
 \t \tManagement Incharge: Sahil
 \t \tContact: XXXXXXX91
 \t \tEmail: Vargisakhada@gmail.com''')
    
    time.sleep(2)
    menu()

def locations():

    sql11 = "select location from loc"
    cursor=mydb.cursor()
    cursor.execute(sql11)
    location=cursor.fetchall()
    
    print(''' \tOur locations are:
    ''',location[0])
    
    time.sleep(2)
    menu()

def review():

    print('At Varghis Akhada the opinion of the users matter to us. We would love if you would fill out the review form that follows, your responses will be anonymous:')

    Gr='Great'
    G='Good'
    B='Bad'
    D='Decent'

    exp=int(input('''
    How would you rate your experience at the Gym.

    1. Great
    2. Good
    3. Decent
    4. Bad
    
    :'''))

    if exp == 1:
        cursor=mydb.cursor()
        sql = "update review set Gym_Experience = '{}' where Username = '{}'".format(Gr,u)
        cursor.execute(sql)
        mydb.commit()

    elif exp == 2:
        cursor=mydb.cursor()
        sql = "update review set Gym_Experience = '{}' where Username = '{}'".format(G,u)
        cursor.execute(sql)
        mydb.commit()
        
    elif exp == 3:
        cursor=mydb.cursor()
        sql = "update review set Gym_Experience = '{}' where Username = '{}'".format(D,u)
        cursor.execute(sql)
        mydb.commit()
        
    elif exp == 4:
        cursor=mydb.cursor()
        sql = "update review set Gym_Experience = '{}' where Username = '{}'".format(B,u)
        cursor.execute(sql)
        mydb.commit()
        
    time.sleep(1)

    qua=int(input('''
    How would you rate the quality at the Gym.

    1. Great
    2. Good
    3. Decent
    4. Bad
    
    :'''))

    if qua == 1:
        cursor=mydb.cursor()
        sql = "update review set Quality = '{}' where Username = '{}'".format(Gr,u)
        cursor.execute(sql)
        mydb.commit()
        
    elif qua == 2:
        cursor=mydb.cursor()
        sql = "update review set Quality = '{}' where Username = '{}'".format(G,u)
        cursor.execute(sql)
        mydb.commit()

    elif qua == 3:
        cursor=mydb.cursor()
        sql = "update review set Quality = '{}' where Username = '{}'".format(D,u)
        cursor.execute(sql)
        mydb.commit()

    elif qua == 4:
        cursor=mydb.cursor()
        sql = "update review set Quality = '{}' where Username = '{}'".format(B,u)
        cursor.execute(sql)
        mydb.commit()

    time.sleep(1)

    equ=int(input('''
    How would you rate the Equipment at the Gym.

    1. Great
    2. Good
    3. Decent
    4. Bad
    
    :'''))

    time.sleep(1)

    if equ == 1:
        cursor=mydb.cursor()
        sql = "update review set Equipment = '{}' where Username = '{}'".format(Gr,u)
        cursor.execute(sql)
        mydb.commit()

    elif equ == 2:
        cursor=mydb.cursor()
        sql = "update review set Equipment = '{}' where Username = '{}'".format(G,u)
        cursor.execute(sql)
        mydb.commit()

    elif equ == 3:
        cursor=mydb.cursor()
        sql = "update review set Equipment = '{}' where Username = '{}'".format(D,u)
        cursor.execute(sql)
        mydb.commit()

    elif equ == 4:
        cursor=mydb.cursor()
        sql = "update review set Equipment = '{}' where Username = '{}'".format(B,u)
        cursor.execute(sql)
        mydb.commit()

    time.sleep(1)

    c=int(input('''
    How would you rate the Crowd at the Gym.

    1. Great
    2. Good
    3. Decent
    4. Bad
    
    :'''))

    if c == 1:
        cursor=mydb.cursor()
        sql = "update review set Crowd = '{}' where Username = '{}'".format(Gr,u)
        cursor.execute(sql)
        mydb.commit()

    elif c == 2:
        cursor=mydb.cursor()
        sql = "update review set Crowd = '{}' where Username = '{}'".format(G,u)
        cursor.execute(sql)
        mydb.commit()

    elif c == 3:
        cursor=mydb.cursor()
        sql = "update review set Crowd = '{}' where Username = '{}'".format(D,u)
        cursor.execute(sql)
        mydb.commit()

    elif c == 4:
        cursor=mydb.cursor()
        sql = "update review set Crowd = '{}' where Username = '{}'".format(B,u)
        cursor.execute(sql)
        mydb.commit()

    time.sleep(1)

    mus=int(input('''
    How would you rate the Music at the Gym.

    1. Great
    2. Good
    3. Decent
    4. Bad
    
    :'''))

    if mus == 1:
        cursor=mydb.cursor()
        sql = "update review set Music = '{}' where Username = '{}'".format(Gr,u)
        cursor.execute(sql)
        mydb.commit()

    elif mus == 2:
        cursor=mydb.cursor()
        sql = "update review set Music = '{}' where Username = '{}'".format(G,u)
        cursor.execute(sql)
        mydb.commit()

    elif mus == 3:
        cursor=mydb.cursor()
        sql = "update review set Music = '{}' where Username = '{}'".format(D,u)
        cursor.execute(sql)
        mydb.commit()

    elif mus == 4:
        cursor=mydb.cursor()
        sql = "update review set Music = '{}' where Username = '{}'".format(B,u)
        cursor.execute(sql)
        mydb.commit()

    time.sleep(1)

    feedback = int(input('''
    Would you like to give a feedback?
    1. yes
    2. no
    '''))

    if feedback == 1:
        f=input('Enter your feedback (300 word wordlimit): ')
        
        cursor=mydb.cursor()
        sql = "update review set feedback = '{}' where Username = '{}'".format(f,u)
        cursor.execute(sql)
        mydb.commit()
        
        time.sleep(1)
        menu()

    
    elif feedback == 2:
        
        print("We hope we didn't disappoint")
        
        time.sleep(1)
        menu()



def o_login():

    o=input('Enter username: ')
    op=pwinput.pwinput('Password: ')
    
    sql12 = "select * from o_login"
    cursor=mydb.cursor()
    cursor.execute(sql12)
    kj = cursor.fetchall()
    
    for i in kj:
        
        if i[0]==o and i[1]==op:
            modtable()
    
    else:
        exit = input('Do you want to exit (yes/no): ')
        
        if exit == 'yes':
            main()
        
        else:
            o_login()

def modtable(): 
    
    print('''
     \t \t1. VIEW USERS
     \t \t2. VIEW USER SPECIFICS
     \t \t3. VIEW FEEDBACK
     \t \t4. CREATE A USER ACCOUNT
     \t \t5. PLANS
     \t \t6. DISCOUNTS
     \t \t7. EARNINGS
     \t \t8. LOCATIONS
     \t \t9. EQUIPMENT INFORMATION
     \t \t10. CHANGE USERNAME
     \t \t11. CHANGE PASSWORD
     \t \t12. DELETE ACCOUNT
     \t \t13. ADD OWNER
     \t \t14. EXIT
    
    :''')
    
    mt = int(input('Select a menu option (1-13):'))
    
    if mt == 1:
        viewusers()
    
    elif mt == 2:
        viewuser_details()

    elif mt == 3:
        viewfeed()
    
    elif mt == 4:
        createaccount()

    elif mt == 5:
        planschange()

    elif mt == 6:
        o_discount()
    
    elif mt == 7:
        earnings()

    elif mt == 8:
        newloc()
    
    elif mt == 9:
        newEquip()

    elif mt == 10:
        userchange()
        
    elif mt == 11:
        Passchange()

    elif mt == 12:
        delaccount()
    
    elif mt == 13:
        addowner()

    elif mt == 14:
        main()

    else:
        print('Entered value is invalid. Retry!!')

        time.sleep(2)
        modtable()

def viewusers():
    
    cursor = mydb.cursor()
    sql = "select username from login"
    cursor.execute(sql)
    r = cursor.fetchall()
    
    print('Usernames for all gym members are:')
    for i in r:
        print(i[0])
    
    time.sleep(3)
    modtable()

def viewuser_details():
    
    usernamee = input('Enter New Username: ')
    
    cursor=mydb.cursor()
    sql = "select * from login"
    sql2 = "select * from o_login"
    cursor.execute(sql)
    tp = cursor.fetchall()
    cursor.execute(sql2)
    tp2 = cursor.fetchall()
    
    for i in tp:
        for j in tp2:
            if j[0]!=usernamee:
                print('Username does not exist')
                viewuser_details()
        
        if i[0] != usernamee:
            print('Username does not exist')
            viewuser_details()
    
    else:
    
        sqq="select * from login where username = '{}'".format(usernamee)
        cursor.execute(sqq)
        d=cursor.fetchall()
        
        print('Your Username:',d[0][0])
        print('Your Password:',d[0][1])
        print('Your Plan:',d[0][2])
        print('Your Timings:',d[0][3])
        print('Your Payment Type:',d[0][5])
        print('Your',d[0][5],'amount is:',d[0][4])
        
        time.sleep(3)
        modtable()

def viewfeed():

    cursor = mydb.cursor()
    sql = "select feedback from review"
    cursor.execute(sql)
    
    r = cursor.fetchall()
    
    for i in r:
        print(i[0])
    
    time.sleep(3)
    modtable()

def createaccount():

    B = 'Basic'
    A = 'Advanced'
    E = 'Enthusiast'

    cursor = mydb.cursor()
    user = input('Enter the username for new account: ')
    
    sql = "select * from login"
    cursor=mydb.cursor()
    cursor.execute(sql)
    tp = cursor.fetchall()
    
    for i in tp:
    
        if i[0]!=user:
            passw = pwinput.pwinput('Enter password for new account: ')
            
            time.sleep(2)
            
            plan = int(input('''
            Choose a plan for the new account:
            1. Basic
            2. Advanced
            3. Enthusiast
            :'''))
            
            if plan == 1:
                sql = "insert into login values('{}','{}','{}','Null',Null,'Null',Null)".format(user,passw,B)
                cursor.execute(sql)
                mydb.commit()
            
            elif plan == 2:
                sql = "insert into login values('{}','{}','{}','Null',Null,'Null',Null)".format(user,passw,A)
                cursor.execute(sql)
                mydb.commit()
            
            elif plan == 3:
                sql = "insert into login values('{}','{}','{}','Null',Null,'Null',Null)".format(user,passw,E)
                cursor.execute(sql)
                mydb.commit()

            time.sleep(1)

            dis = int(input('''
            1. Discount Spin
            2. Continue with no discount
            : '''))

            if dis == 1:
                
                r1 = random.randint(10,90)
                r = r1/100
                print('Discount is:',r1,'%')
                sql = "update login set Discount_Percent = {} where Username = '{}'".format(r1,user)
                cursor.execute(sql)
                mydb.commit()
            
            elif dis == 2:
                
                r1 = 0
                sql = "update login set Discount_Percent = {} where Username = '{}'".format(r1,user)
                cursor.execute(sql)
                mydb.commit()
                cursor=mydb.cursor()
            
            sql_1 = "select plans from login where username = '{}'".format(user)
            cursor.execute(sql_1)
            plan=cursor.fetchall()
            sqk = "select Discount_Percent from login where username = '{}'".format(user)
            cursor.execute(sqk)
            r1= cursor.fetchall()
            r = r1[0][0] /100
            
            M = 'Monthly'
            Q = 'Quarterly'
            Y = 'Yearly'

            time.sleep(2)

            if plan  == 'Basic' or plan  == 'basic':

                print('\t \tPayment options are:')
                print('\t1. Monthly - Rs 999 per month; Amount after discount:',999-999*r )
                print('\t2. Quarterly - Rs 2899 per quarter; Amount after discount:',2899-2899*r )
                print('\t3. Yearly - Rs 9999 per year; Amount after discount:',9999-9999*r )

                pt = int(input(':'))

                if pt == 1:
                    n9 = 999-999*r 
                    
                    sql__2 = "update login set payment = {} where username = '{}'".format(n9,user)
                    sql__3 = "update login set payment_type = '{}' where username = '{}'".format(M,user)
                    cursor.execute(sql__2)
                    cursor.execute(sql__3)
                    mydb.commit()
                    
                    print('Payment amount and payment type are added to your account!!!')
                    
                    time.sleep(2)
                    Timings(user)
                
                elif pt == 2:
                    n8 = 2899 - 2899*r 
                    
                    sql__4 = "update login set payment = {} where username = '{}'".format(n8,user)
                    sql__5 = "update login set payment_type = '{}' where username = '{}'".format(Q,user)
                    cursor.execute(sql__4)
                    cursor.execute(sql__5)
                    mydb.commit()
                    
                    print('Payment amount and payment type are added to your account!!!')
                    
                    time.sleep(2)
                    Timings(user)
                
                elif pt == 3:
                    n7 = 9999 - 9999*r 
                    
                    sql__6 = "update login set payment = {} where username = '{}'".format(n7,user)
                    sql__7 = "update login set payment_type = '{}' where username = '{}'".format(Y,user)
                    cursor.execute(sql__6)
                    cursor.execute(sql__7)
                    mydb.commit()
                    
                    print('Payment amount and payment type are added to your account!!!')
                    
                    time.sleep(2)
                    Timings(user)

            elif plan  == 'Advanced' or plan  == 'advanced':
                print('\t \tPayment options are:')
                print('\t1. Monthly - Rs 1499 per month; Amount after discount:',1499*r )
                print('\t2. Quarterly - Rs 4299 per quarter; Amount after discount:',4299*r )
                print('\t3. Yearly - Rs 14999 per year; Amount after discount:',14999*r )
                pt = int(input(':'))

                if pt == 1:
                    
                    n6 = 1499 - 1499*r 
                    
                    sql__8 = "update login set payment = {} where username = '{}'".format(n6,user)
                    sql__9 = "update login set payment_type = '{}' where username = '{}'".format(M,user)
                    cursor.execute(sql__8)
                    cursor.execute(sql__9)
                    mydb.commit()
                    
                    print('Payment amount and payment type are added to your account!!!')
                    
                    time.sleep(2)
                    Timings(user)
                
                elif pt == 2:
                    n5 = 4299 - 4299*r 
                    
                    sql__10 = "update login set payment = {} where username = '{}'".format(n5,user)
                    sql__11 = "update login set payment_type = '{}' where username = '{}'".format(Q,user)
                    cursor.execute(sql__10)
                    cursor.execute(sql__11)
                    mydb.commit()
                    
                    print('Payment amount and payment type are added to your account!!!')
                    
                    time.sleep(2)
                    Timings(user)
                
                elif pt == 3:
                    n4=14999 - 14999*r 
                    
                    sql__12 = "update login set payment = {} where username = '{}'".format(n4,user)
                    sql__13 = "update login set payment_type = '{}' where username = '{}'".format(Y,user)
                    cursor.execute(sql__12)
                    cursor.execute(sql__13)
                    mydb.commit()
                    
                    print('Payment amount and payment type are added to your account!!!')
                    
                    time.sleep(2)
                    Timings(user)

            elif plan  == 'Enthusiast' or plan  == 'enthusiast':
                print('\t\tPayment options are:')
                print('\t1. Monthly - Rs 1999 per month; Amount after discount:',1999*r )
                print('\t2. Quarterly - Rs 5499 per quarter; Amount after discount:',5499*r )
                print('\t3. Yearly - Rs 19999 per year; Amount after discount:',19999*r )
                pt = int(input(':'))
                
                if pt == 1:
                    n3=1999 - 1999*r 
                    
                    sql__14 = "update login set payment = {} where username = '{}'".format(n3,user)
                    sql__15 = "update login set payment_type = '{}' where username = '{}'".format(M,user)
                    cursor.execute(sql__14)
                    cursor.execute(sql__15)
                    mydb.commit()
                    
                    print('Payment amount and payment type are added to your account!!!')
                    
                    time.sleep(2)
                    Timings(user)
                
                elif pt == 2:
                    n1 = 5499 - 5499*r 
                    
                    sql__16 = "update login set payment = {} where username = '{}'".format(n1,user)
                    sql__17 = "update login set payment_type = '{}' where username = '{}'".format(Q,user)
                    cursor.execute(sql__16)
                    cursor.execute(sql__17)
                    mydb.commit()
                    
                    print('Payment amount and payment type are added to your account!!!')
                    
                    time.sleep(2)
                    Timings(user)
                
                elif pt == 3:
                    
                    n=19999 - 19999*r 
                    
                    sql__18 = "update login set payment = {} where username = '{}'".format(n,user)
                    sql__19 = "update login set payment_type = '{}' where username = '{}'".format(Y,user)
                    cursor.execute(sql__18)
                    cursor.execute(sql__19)
                    mydb.commit()
                    
                    print('Payment amount and payment type are added to your account!!!')
                    
                    time.sleep(2)
                    Timings(user)
        else:
            y = int(input('''
            Entered account already exists!!!
            1. Try again
            2. Exit
            : '''))

            if y == 1:
                createaccount()
            
            else:
                modtable()

def planschange():

    cursor=mydb.cursor()
    namec=input('Enter username whose plan you want to change:')
    sql16 = "select plans from login where username = '{}'".format(namec)
    cursor.execute(sql16)
    cplan = cursor.fetchall()
    
    print('Current plan:',cplan[0][0])
    
    np=int(input('''
     \t \tChoose a plan to change to
     
     \t \tAvailable plans:
     
     \t1. Basic
     
     \t2. Advanced
     
     \t3. Enthusiast

    Enter 4 to Exit 
    :'''))
    
    time.sleep(1)

    if np == 1:
        basic='Basic'
        sql17="update login set plans = '{}' where username = '{}'".format(basic,namec)
        cursor.execute(sql17)
        mydb.commit()
        
        print('Plan has been updated to',basic,'!!!')
        
        time.sleep(2)
        modtable()
    
    elif np == 2:
        a ='advanced'
        sql18="update login set plans = '{}' where username = '{}'".format(a,namec)
        cursor.execute(sql18)
        mydb.commit()
        
        print('Plan has been updated to',a,'!!!')
        
        time.sleep(2)
        modtable()
    
    elif np == 3:
        e = 'Enthusiast'
        sql19="update login set plans = '{}' where username = '{}'".format(e,namec)
        cursor.execute(sql19)
        mydb.commit()
        
        print('Plan has been updated to',e,'!!!')
        
        time.sleep(2)
        modtable()
    
    elif np == 4:
        modtable()
    
    else:
        print('Invalid entry!')
        
        time.sleep(1)
        planschange()

def o_discount():

    user = input('Enter the name of the user whose Discount you want to change: ')
    sql = "select * from login"
    cursor=mydb.cursor()
    cursor.execute(sql)
    tp = cursor.fetchall()
    
    for i in tp:
        
        if i[0]==user:
            print('Current discount of',user,'is:',i[6])
            k = int(input('Enter new discount percentage:'))
            
            sql1 = "update login set Discount_Percent = {} where username = '{}'".format(k,user)
            cursor.execute(sql1)
            mydb.commit()
            
            print('Discount for',user,'has been changed to:',k)
            
            time.sleep(2)
            modtable()

    
    else:
        l=int(input('''
        The entered user doesn't exist
        1. Do you wan't to try again?
        2. Do you want to Exit?
        :'''))

        if l == 1:
            o_discount()
        
        else:
            modtable()

def earnings():

    cursor=mydb.cursor()
    sql = "select payment,payment_type from login"
    cursor.execute(sql)
    earn = cursor.fetchall()
    
    monthly=0
    quartly=0
    yearly=0
    
    for i in earn:
    
        if i[1] == 'Monthly':
            monthly += i[0]
    
        elif i[1] == 'Quarterly':
            quartly += i[0]
    
        elif i[1] == 'Yearly':
            yearly += i[0]
    
    profit = int(input('''
    \t\t1. Monthly Earning
    \t\t2. Quarterly Earning
    \t\t3. Yearly Earning
    '''))
    
    if profit == 1:
        print(' \t \tEarning per month:',monthly)
    
    elif profit == 2:
        print(' \t \tEarning per quarter:',quartly)
    
    elif profit == 3:
        print(' \t \tEarning per year:',yearly)
    
    else:
        print(' \t \tEarning per month:',monthly)
        print(' \t \tEarning per quarter:',quartly)
        print(' \t \tEarning per year:',yearly)
        
    time.sleep(5)
    modtable()

def newloc():

    cursor=mydb.cursor()
    nl=int(input('''
    1. Do you want to add more locations?
    2. Do you want to change the number of facilities at a location?
    '''))

    if nl == 1:
        loc1=input('Enter Location: ')
        qt = int(input('Enter quantity of gyms in that locality: '))
        
        sql15="insert into loc values(%s,%s)"
        list_l=[loc1,qt]
        tl=(list_l)
        cursor.execute(sql15,tl)
        mydb.commit()
        
        print('New location has been added')
        
        time.sleep(2)
        modtable()

    elif nl == 2:
        sql_1='select location from loc'
        cursor.execute(sql_1)
        pr=cursor.fetchall()
        
        for i in pr:
            print(i[0])
        
        cl=input('Please enter the city where the number of facilities has changed (please enter the name as it appears above):')
        nq=int(input('Please enter the new amount of facilities:'))
        
        sql_2="update loc set quantity = '{}' where location = '{}'".format(nq,cl)
        cursor.execute(sql_2)
        mydb.commit()
        
        print('Number of facilities changed in',cl,'to',nq)
        
        time.sleep(2)
        modtable()

def newEquip():

    cursor=mydb.cursor()
    nE=int(input('''
    1. Do you want to add new equipment?
    2. Do you want to modify the number of current equipment?
    '''))

    if nE == 1:
        Eq=input('Enter Equipment Name: ')
        qte = int(input('Enter quantity of Equipment: '))
        
        sql16="insert into EI values(%s,%s)"
        list_E=[Eq,qte]
        te=(list_E)
        cursor.execute(sql16,te)
        mydb.commit()
        
        print('New Equipment has been added!!!')
        
        time.sleep(2)
        modtable()

    elif nE == 2:
        sql_3='select * from EI'
        cursor.execute(sql_3)
        pr=cursor.fetchall()
        
        for i in pr:
            print(i[0],'-',i[1])
        
        cE=input('''Please enter the Equipment whose quantity you want to change
        (please enter the name as it appears above)
        ''')
        nqE1=int(input('Please enter the new amount of Equipment (how many more):'))
        nqE = nqE1 + i[1]
        
        sql_4="update EI set quantity = '{}' where E_name = '{}'".format(nqE,cE)
        cursor.execute(sql_4)
        mydb.commit()
        
        print('Number of Equipments changed of',cE,'to',nqE)
        
        time.sleep(2)
        modtable()

def userchange():
    
    cursor = mydb.cursor()
    user = input('Enter username you want to change: ')
    sql = "select username from login".format(user)
    cursor.execute(sql)
    r=cursor.fetchall()
    
    for i in r:
        
        if i[0]== user:
            usern = input('Enter new username: ')

            sql = "select * from login"
            sql2 = "select * from o_login"
            cursor.execute(sql)
            tp = cursor.fetchall()
            cursor.execute(sql2)
            tp2 = cursor.fetchall()
            
            for i in tp:
                for j in tp2:
                    if j[0]==usern:
                        print('Username is in use try again')
                
                if i[0] == usern:
                    print('Username is in use try again')
                     
            else:
                sql1 = "update login set username = '{}' where username = '{}'".format(usern,user)
                cursor.execute(sql1)
                mydb.commit()
                
                print('Username changed to:',usern,'from:',user)

                time.sleep(2)
                modtable()
        
    else:
        print("User Doesn't exist!!! Try again")
        userchange()

def Passchange():

    cursor=mydb.cursor()
    namep=input('Enter username whose password you want to change:')
    sql15 = "select password from login where username = '{}'".format(namep)
    cursor.execute(sql15)
    passc = cursor.fetchall()
    
    print('Current password is:',passc[0][0])
    passnew=pwinput.pwinput('Enter new password:')
    
    sql13 = "update login set password = '{}' where username = '{}'".format(passnew,namep)
    cursor.execute(sql13)
    mydb.commit()
    
    print('Password has been updated!!!')
    
    time.sleep(3)
    modtable()

def delaccount():

    user = input('Enter username whose account you want to delete: ')
    
    sql = "select * from login"
    cursor=mydb.cursor()
    cursor.execute(sql)
    tp = cursor.fetchall()
    
    for i in tp:
        
        if i[0]==user:
            d = int(input('''
            Are you sure you want to delete this account?
            1. Yes
            2. No
            '''))
            
            if d == 1:
                sql1 = "delete from login where username = '{}'".format(user)
                cursor.execute(sql1)
                mydb.commit()
                
                print(user,'has been virtually blocked!!!')
                
                time.sleep(1)
                modtable()
            
            else:
                modtable()
            break
    
    else:
        time.sleep(1)
        exit = int(input('''
    1. Do you want to try again?
    2. Do you want to exit?
    '''))
        
        if exit == 1:
            delaccount()
        
        elif exit == 2:
            modtable()

def addowner():
    
    cursor = mydb.cursor()
    owner = input('Enter the username of the new owner: ')
    sql = "select username from o_login"
    cursor.execute(sql)
    r = cursor.fetchall()

    for i in r:
        
        if i[0] != owner:
            passw = pwinput.pwinput('Please enter password: ')
            k = int(input('''
            Are you sure you want to add this user?
            1. Yes
            2. Terminate
            : '''))

            if k == 1:
                sql1 = "insert into o_login values('{}','{}')".format(owner,passw)
                cursor.execute(sql1)
                cursor.commit()
                print('New Owner',owner,'added!!!')
                
                time.sleep(1)

                y = int(input('''
                1. Do you want to login?
                2. Menu
                '''))

                if y == 1:
                    o_login()
                    break
                
                else:
                    modtable()
                    break
            
            if k == 2:
                modtable()
                break
        
        elif i[0] == owner:
            print('This Owner account exists!!! Try again')
            addowner()



main()