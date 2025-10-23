from django.shortcuts import render,redirect
from django.views.decorators.cache import never_cache
from .services import TrackerServices

# ========================================================= show home page ===================================================
def home(request):
    return render(request,"index.html")
# ========================================================= registration page ===================================================

def registerform(request):
    return render(request, "Registration.html")


# ========================================================= adding user by registration form ===================================================

def adduser(request) :
    if request.method == "POST":
        uid=request.POST.get("userid")
        ps=request.POST. get ("password")
        nm=request. POST. get("username")
        mob=request.POST.get("mobile")
        age=int(request.POST.get("age"))
        gen=request. POST.get("gender")
        occ=request. POST. get ("occupation")
        ct=request.POST.get("city")
        obj=TrackerServices()
        msg=obj.addnewuser(uid,ps,nm,mob,age,gen,occ,ct)
    return render(request,"registration_success.html",{'status': msg,'name':nm})

# ========================================================= user login  ===================================================

def login(request):
    if request.method == "POST":
        uid = request.POST.get("userid")
        ps = request.POST.get("password")
        obj = TrackerServices()
        status, username = obj.checkuser(uid, ps)

        if status == 'success':
            request.session['authenticated'] = True
            request.session['user'] = uid
            request.session['username'] = username
            return redirect('/dashboard/')
        else:
            request.session['authenticated'] = False
            return render(request, "index.html", {'error': 'Invalid User ID or Password'})
    else:
        # Handle GET request by showing login form
        return render(request, "index.html")


@never_cache

# ========================================================= after login dashboard page ===================================================

def dashboard(request):
    if not request.session.get('authenticated'):
        return redirect('/')
    username = request.session.get('username', '')
    return render(request, "dashboard.html", {'name': username})
# =========================================================  add_expense form  ===================================================

def newexpense(request):
    if not request.session.get('authenticated'):
        return redirect('/')
    username = request.session.get('username', '')
    return render(request, "add_expense.html", {'name': username})

# =========================================================  after add_expense form submitting  ===================================================

def addexpense(request):
    msg=''
    if request.method=="POST":
        uid=request.session.get("user")
        dt=request.POST.get("expense_date")
        cat=request.POST.get("category")
        des=request.POST.get("description")
        amt=float(request.POST.get("amount"))
        mode=request.POST.get("paymentmode")
        obj=TrackerServices()
        msg=obj.addnewexpense(uid,dt,cat,des,amt,mode)
    
    return render(request,"ExpenseStatus.html",{'status':msg})

# ========================================================= modify_expense page   ===================================================
def modify(request):
    if not request.session.get('authenticated'):
        return redirect('/')
    username = request.session.get('username', '')
    uid=request.session.get('user')
    obj=TrackerServices()
    data=obj.generatemodify(uid)
    return render(request,"modify_expense.html",{"expdata":data,'name':username})

# ========================================================= edit_expense page   ===================================================

def edit_expense(request):
    if not request.session.get('authenticated'):
        return redirect('/')
    expense_id = request.GET.get('id')  # get from query string
    if not expense_id:
        return redirect('/modify/')
    obj = TrackerServices()
    expense = obj.get_expense_by_id(expense_id)
    username = request.session.get('username', 'User')
    
    return render(request, "edit_expense.html", {"expense": expense, "name": username})
# ========================================================= update expense after edit_expense form ===================================================
def modifystatus(request):
    if not request.session.get('authenticated'):
        return redirect('/')
    
    msg = ''
    if request.method == "POST":
        uid = request.session.get('user')
        eid = request.POST.get("expenseid")
        dt = request.POST.get("expense_date")
        cat = request.POST.get("category")
        des = request.POST.get("description")
        amt = float(request.POST.get("amount"))
        mode = request.POST.get("paymentmode")

        obj = TrackerServices()
        msg = obj.update_expense(uid, eid, dt, cat, des, amt, mode)

    return render(request, "modifyStatus.html", {"status": msg})



# =========================================================  deleteExpense form  ===================================================

def delete(request):
    if not request.session.get('authenticated'):
        return redirect('/')
    username = request.session.get('username', '')
    uid = request.session.get('user')
    obj = TrackerServices()
    data = obj.generatereport(uid)
    return render(request, "DeleteExpense.html", { "name": username,"expdata": data})

# =========================================================  after deleteExpense  ===================================================

def deleteexpense(request):
    if not request.session.get('authenticated'):
        return redirect('/')
    uid = request.session.get('user')
    obj = TrackerServices()
    if request.method == "POST":
        eid = request.POST.get("expenseid")
        msg = obj.deleteexpense(uid, eid)
    else:
        msg = "Invalid request."
    return render(request, "DeleteStatus.html", {"status": msg})

# =========================================================  for showing report data ===================================================

def showreport(request):
    if not request.session.get('authenticated'):
        return redirect('/')
    username = request.session.get('username', '')
    uid=request.session.get('user')
    obj=TrackerServices()
    data=obj.generatereport(uid)
    return render(request,"report.html",{"expdata":data,'name':username})

# =========================================================  for search expense    ===================================================

def search(request):
    if not request.session.get('authenticated'):
        return redirect('/')
    username = request.session.get('username', '')
    return render(request,"SearchExpenses.html",{'name':username}) 
# =========================================================  for showing  search expense data   ===================================================

def searchexp(request):
    if request.method=="POST":
        uid=request.session.get('user')
        sdt=request.POST.get("expense_date")
        obj=TrackerServices()
        data=obj.searchexpondate(uid,sdt)
    
    return render(request,"SearchResult.html",{"expdt":sdt,"expdata":data})

# =========================================================  change_password form  ===================================================

def change(request):
    if not request.session.get('authenticated'):
        return redirect('/')
    username = request.session.get('username', '')
    return render(request,"change_password.html",{'name':username})

# =========================================================  for changing password   ===================================================

def changepass(request):
    if request.method=="POST":
        uid=request.session.get('user')
        opass=request.POST.get("old_password")
        npass1=request.POST.get("new_password")
        npass2=request.POST.get("confirm_password")
        obj=TrackerServices()
        status=obj.changeuserpassword(uid,opass,npass1,npass2)

    return render(request,"ChangePass_Status.html",{"status":status})

# =========================================================  showing profile page   ===================================================

def profile(request):
    if not request.session.get('authenticated'):
        return redirect('/')  

    userid = request.session.get('user')  
    obj = TrackerServices()
    user_data = obj.get_user_profile(userid)  

    return render(request, "profile.html", {'user': user_data})

# =========================================================  logout page ===================================================

def logout(request):
    request.session.flush()
    return redirect('/')