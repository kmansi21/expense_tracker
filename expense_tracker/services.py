import pymysql
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file

  
class TrackerServices:
    # ======================================= adding new user registration form =======================================
    def addnewuser(self,uid,ps,nm,mob,age,gen,occ,ct):
        try:
            con = pymysql.connect(
            host=os.getenv('DB_HOST'),
            port=int(os.getenv('DB_PORT')),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
            curs=con.cursor()
            curs.execute(f"insert into users values('{uid}','{ps}','{nm}','{mob}','{age}','{gen}','{occ}','{ct}')")
            con.commit()
            msg='success'
            con.close()
        except:
            msg='failed'
        return msg
 # ======================================= checking new user login form =======================================
  
    def checkuser(self, uid, ps):
        try:
            con = pymysql.connect(
            host=os.getenv('DB_HOST'),
            port=int(os.getenv('DB_PORT')),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
            )
            curs=con.cursor()
            curs.execute(f"select * from users where userid='{uid}' and password='{ps}'")
            data=curs.fetchone()
            if data:
                msg='success'
                username = data[2]
            else:
                msg = 'failed'
                username = None
                con.close()
        except:
            msg = 'failed'
            username = None
        return msg, username
# ======================================= adding new expense add_expense form =======================================

    def addnewexpense(self,uid,dt,cat,des,amt,mode):
        try:
            con = pymysql.connect(
            host=os.getenv('DB_HOST'),
            port=int(os.getenv('DB_PORT')),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
            )
            curs=con.cursor()
            curs.execute(f"insert into expenses(userid,expense_date,category,description,amount,paymentmode) values('{uid}','{dt}','{cat}','{des}',{amt},'{mode}')")
            con.commit()
            msg='Expense entry recorded successfully'
            con.close()
        except:
            msg='Expense entry failed'

        return msg
# ======================================= getting expense for showing all expense data modify_expense =======================================
   
    def generatemodify(self,uid):
        con = pymysql.connect(
        host=os.getenv('DB_HOST'),
        port=int(os.getenv('DB_PORT')),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
        )        
        curs=con.cursor()
        curs.execute(f"select * from expenses where userid='{uid}'")
        data=curs.fetchall()
        con.close()
        return data       
# ======================================= getting expense by id for edit_expense =======================================
    
    def get_expense_by_id(self,eid):
        con = pymysql.connect(
        host=os.getenv('DB_HOST'),
        port=int(os.getenv('DB_PORT')),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
        )
        curs = con.cursor()
        curs.execute(f"SELECT * FROM expenses WHERE expenseid={eid}")
        data = curs.fetchone()
        con.close()
        return data    
    
# ======================================= updating expense updateExpense =======================================
    def update_expense(self, uid, eid, dt, cat, des, amt, mode):
        try:
            con = pymysql.connect(
            host=os.getenv('DB_HOST'),
            port=int(os.getenv('DB_PORT')),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
            )
            curs = con.cursor()
            cnt = curs.execute(f"UPDATE expenses SET expense_date='{dt}', category='{cat}', description='{des}', amount={amt}, paymentmode='{mode}' WHERE userid='{uid}' AND expenseid={eid}" )
            con.commit()
            if cnt == 1:
                 msg = "Expense updated successfully"
            else:
                msg = "Expense not found or not updated"
                con.close()
        except Exception as e:
             msg = f"Update failed: {str(e)}"
        return msg




# ======================================= deleting expense deleteExpense =======================================
    
    def deleteexpense(self,uid,eid):
        con = pymysql.connect(
        host=os.getenv('DB_HOST'),
        port=int(os.getenv('DB_PORT')),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
        )
        curs=con.cursor()
        cnt=curs.execute(f"delete from expenses where userid='{uid}' and expenseid={eid}")
        con.commit()
        if cnt==1:
            msg="Expense entry deleted"
        else:
            msg="Not Found for the user"
        con.close()
        return msg
    
 # ======================================= Showing expense data report =======================================
    
    def generatereport(self,uid):
        con = pymysql.connect(
        host=os.getenv('DB_HOST'),
        port=int(os.getenv('DB_PORT')),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
        )
        curs=con.cursor()
        curs.execute(f"select * from expenses where userid='{uid}'")
        data=curs.fetchall()
        con.close()
        return data 
    
# ======================================= searching Expense Data SearchExpense =======================================

    def searchexpondate(self,uid,sdt):
        con = pymysql.connect(
        host=os.getenv('DB_HOST'),
        port=int(os.getenv('DB_PORT')),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
        )
        curs=con.cursor()
        curs.execute(f"select * from expenses where userid='{uid}' and expense_date='{sdt}'")
        data=curs.fetchall()
        con.close()
        return data    
        
 # ======================================= changing user Password change_password =======================================
 
 
    def changeuserpassword(self,uid,opass,npass1,npass2):
        if npass1==npass2:
            con = pymysql.connect(
            host=os.getenv('DB_HOST'),
            port=int(os.getenv('DB_PORT')),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
            )
            curs=con.cursor()
            cnt=curs.execute(f"update users set password='{npass1}' where userid='{uid}' and password='{opass}'")
            con.commit()
            if cnt>0:
                status="Password changed successfully"
            else:
                status="Current password incorrect"
            con.close()
        else:
            status="New passwords mismatched"
        return status
# ======================================= Profile data  =========================================================
            
    def get_user_profile(self, uid):
        try:
            con = pymysql.connect(
            host=os.getenv('DB_HOST'),
            port=int(os.getenv('DB_PORT')),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
            )
            curs = con.cursor()
            curs.execute(f"SELECT userid, username, mobile, age, gender, occupation, city FROM users WHERE userid='{uid}'")
            data = curs.fetchone()
            con.close()
            if data:
            
                return {
                'userid': data[0],
                'username': data[1],
                'mobile': data[2],
                'age': data[3],
                'gender': data[4],
                'occupation': data[5],
                'city': data[6]
                 }
            else:
             return None
        except:
            return None