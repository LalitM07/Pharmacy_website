from django.shortcuts import render,HttpResponse ,redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView ,UpdateView,DeleteView
from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate,login,logout
from django.views import generic
from django.views.generic import View
from .forms import UserForm
from django.contrib import messages
from django.contrib import auth
from django.template import loader
from django.core.context_processors import csrf
from django.contrib.auth.models import User
import datetime
import MySQLdb

# Create your views here.
def Home(request):
	context={}
	return render(request,'home.html',context)
def signin(request):
 	return render(request, 'login.html') 
def mail(request):
	return render(request,'mail.html')
# def register(request):
# 	return render(request,'register.html')
# def prescription(request):
# 	return render(request,'medicinetable.html')
# def baby(request):
# 	return render(request,'medicinetable.html')
# def personal(request):
# 	return render(request,'medicinetable.html')
# def wellness(request):
# 	return render(request,'medicinetable.html')
# def health(request):
# 	return render(request,'medicinetable.html')
# def details(request):
#     return render(request,'productdetails.html')
# def cart(request):
# 	return render(request,'cart.html')


def start_session(request,uid):
	request.session["user_id"]=uid;
	return request

def check_userlogin(request):
	if request.session.has_key["user_id"]:
		return request.session["user_id"]
	else:
		return None
def close_session(request):
	if request.session.has_key["user_id"]:
		del request.session.has_key["user_id"]
		return True
	return False




class UserFormView(View):
	form_class = UserForm
	template_name = 'register.html'

	def get(self,request):
		form = self.form_class(None)
		return render(request,self.template_name,{'form':form})

	def post(self,request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit=False)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()
			user = authenticate(username=username,password=password)

			if user is not None:

				if user.is_active:
					#login(request,user)
					return redirect('/')
		return render(request,self.template_name,{'form':form})

def login_user(request):
	template = loader.get_template('login.html')

	if request.POST:
		username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            login(request, user)

            if request.user.is_superuser:
            	print("is_superuser")
                return redirect('/')
               
            return redirect('/')
        else:
            return render(request,'login.html')

def logout_user(request):
	#close_session(request)
	logout(request)
	return redirect('/')

def prescriptiontable(request):
	template = loader.get_template('medicinetable.html')
	db = MySQLdb.connect("localhost", "root", "root", "pharmacy")
	cursor = db.cursor()
	cursor.execute("select * from products where typeid = 1 ;")
	tablecontent1 = []

	class product_object:
		def __init__(self, pid, pname,price, quantity,details, manufdate,expdate):
			self.pid = pid
			self.pname = pname
			self.price=price
			self.quantity = quantity
			self.details = details
			self.manufdate = manufdate
			self.expdate=expdate

	for row in cursor:
		tablecontent1.append(product_object(row[0], row[1], row[2], row[3], row[4],row[5],row[6]))
	db.close()
	context={'products' : tablecontent1}
	return HttpResponse(template.render(context, request))

def babytable(request):
	template = loader.get_template('medicinetable.html')
	db = MySQLdb.connect("localhost", "root", "root", "pharmacy")
	cursor = db.cursor()
	cursor.execute("select * from products where typeid = 2 ;")
	tablecontent2 = []

	class product_object:
		def __init__(self, pid, pname,price, quantity,details, manufdate,expdate):
			self.pid = pid
			self.pname = pname
			self.price=price
			self.quantity = quantity
			self.details = details
			self.manufdate = manufdate
			self.expdate=expdate

	for row in cursor:
		tablecontent2.append(product_object(row[0], row[1], row[2], row[3], row[4],row[5],row[6]))
	db.close()
	context={'products' : tablecontent2}
	return HttpResponse(template.render(context, request))

def personaltable(request):
	template = loader.get_template('medicinetable.html')
	db = MySQLdb.connect("localhost", "root", "root", "pharmacy")
	cursor = db.cursor()
	cursor.execute("select * from products where typeid = 3 ;")
	tablecontent3 = []

	class product_object:
		def __init__(self, pid, pname,price, quantity,details, manufdate,expdate):
			self.pid = pid
			self.pname = pname
			self.price=price
			self.quantity = quantity
			self.details = details
			self.manufdate = manufdate
			self.expdate=expdate

	for row in cursor:
		tablecontent3.append(product_object(row[0], row[1], row[2], row[3], row[4],row[5],row[6]))
	db.close()
	context={'products' : tablecontent3}
	return HttpResponse(template.render(context, request))

def aidtable(request):
	template = loader.get_template('medicinetable.html')
	db = MySQLdb.connect("localhost", "root", "root", "pharmacy")
	cursor = db.cursor()
	cursor.execute("select * from products where typeid = 4 ;")
	tablecontent4 = []

	class product_object:
		def __init__(self, pid, pname,price, quantity,details, manufdate,expdate):
			self.pid = pid
			self.pname = pname
			self.price=price
			self.quantity = quantity
			self.details = details
			self.manufdate = manufdate
			self.expdate=expdate

	for row in cursor:
		tablecontent4.append(product_object(row[0], row[1], row[2], row[3], row[4],row[5],row[6]))
	db.close()
	context={'products' : tablecontent4}
	return HttpResponse(template.render(context, request))

def wellnesstable(request):
	template = loader.get_template('medicinetable.html')
	db = MySQLdb.connect("localhost", "root", "root", "pharmacy")
	cursor = db.cursor()
	cursor.execute("select * from products where typeid = 5 ;")
	tablecontent5 = []

	class product_object:
		def __init__(self, pid, pname,price, quantity,details, manufdate,expdate):
			self.pid = pid
			self.pname = pname
			self.price=price
			self.quantity = quantity
			self.details = details
			self.manufdate = manufdate
			self.expdate=expdate

	for row in cursor:
		tablecontent5.append(product_object(row[0], row[1], row[2], row[3], row[4],row[5],row[6]))
	db.close()
	context={'products' : tablecontent5}
	return HttpResponse(template.render(context, request))

def detailsfunction(request , pid):
	
	template = loader.get_template('productdetails.html')
	db = MySQLdb.connect("localhost", "root", "root", "pharmacy")
	cursor=db.cursor()
	cursor.execute("select * from products where pid = " + str(pid) + ";")
	
	detailscontent = []


	class details_object:
	        def __init__(self, pid,pname,price, quantity,typeid,details, manufdate,expdate):
	        	self.pid=pid
	        	self.pname = pname
	        	self.price=price
	        	self.quantity = quantity
	        	self.typeid=typeid
	        	self.details = details
	        	self.manufdate = manufdate
	        	self.expdate=expdate


	for row in cursor:
		detailscontent=details_object(row[0], row[1], row[2], row[3], row[4],row[5],row[6],row[7])


	db.close()
	context={'details' : detailscontent}
	return HttpResponse(template.render(context, request))

def addtocart(request):
	if request.method=='POST':

		pid=request.POST.get('pid')
		quantity=request.POST.get('quantity')
		
		#template = loader.get_template('cart.html')
		db = MySQLdb.connect("localhost", "root", "root", "pharmacy")
		cursor=db.cursor()
		 
		cursor.execute("insert into cart values(" + str(request.user.id) +","+ str(pid)+ "," + str(quantity) + ");"  )

		
		db.commit()
 		db.close()
 		return HttpResponse('Your item added to the cart ..!!')

def viewcart(request):
	template = loader.get_template('cart.html')
	db = MySQLdb.connect("localhost", "root", "root", "pharmacy")
	cursor=db.cursor()
	cursor.execute("select pid,quantity from cart where uid = " + str(request.user.id) + ";")
	entries = cursor.fetchall()

	class cartitems:
		def __init__(self,name,pid,quantity,price):
			self.name = name
			self.pid = pid
			self.quantity=quantity
			self.price = price

	details = []
	for item in entries:
		cursor.execute("select pname,price from products where pid = "+str(item[0])+";")
		pnameprice = cursor.fetchone()
		details.append(cartitems(pnameprice[0],item[0],item[1],item[1]*pnameprice[1]))

	db.close()

	context = {'details':details}
	return render(request,'cart.html',context)

def removecartitem(request,pid):
	id = request.user.id
	db = MySQLdb.connect("localhost", "root", "root", "pharmacy")
	cursor=db.cursor()
	cursor.execute("delete from cart where uid = "+ str(id) + " and pid = " + str(pid) +";")
	db.commit()
	db.close()
	return redirect('cart')

def checkout(request):
	template = loader.get_template('checkout.html')
	db = MySQLdb.connect("localhost", "root", "root", "pharmacy")
	cursor=db.cursor()
	cursor.execute("select pid,quantity from cart where uid = " + str(request.user.id) + ";")
	entries = cursor.fetchall()

	class cartitems:
		def __init__(self,name,pid,quantity,price):
			self.name = name
			self.pid = pid
			self.quantity=quantity
			self.price = price

	details = []
	total = no_of_items = 0
	for item in entries:
		cursor.execute("select pname,price from products where pid = "+str(item[0])+";")
		pnameprice = cursor.fetchone()
		no_of_items=no_of_items+1
		total=total + item[1]*pnameprice[1]
		details.append(cartitems(pnameprice[0],item[0],item[1],item[1]*pnameprice[1]))

	db.close()

	context = {'details':details,'no_of_items':no_of_items,'total':total}
	return render(request,'checkout.html',context)





#admin part

def admin_profile(request):
	return render(request,'admin_profile.html')

def customers(request):
    class user_details:
        def __init__(self,id,username,first_name,last_name,email,mobile,city):
            self.id = id
            self.username = username
            self.first_name = first_name
            self.last_name = last_name
            self.email=email
            self.mobile=mobile
            self.city = city
             

    db = MySQLdb.connect('localhost','root','root','pharmacy')
    cursor = db.cursor()
    cursor.execute("select auth_user.id,auth_user.username,auth_user.first_name,auth_user.last_name,auth_user.email,ordered.mobile,ordered.town from auth_user inner join ordered on auth_user.id = ordered.uid;")
    uservalues = cursor.fetchall()
    entries = []
    for item in uservalues:
        entries.append(user_details(item[0],item[1],item[2],item[3],item[4],item[5],item[6]))
    db.close()
    context={}
    context['details'] = entries
    return render(request,'customers.html',context)


def allorders(request):
    class order_display:
        def __init__(self,orderid,customername,productnames,orderdate,cost,deliverystatus,paymentstatus,paymentdetails):
            self.orderid = orderid
            self.customername = customername
            self.productnames = productnames
            self.orderdate = orderdate
            self.cost = cost
            self.deliverystatus = deliverystatus
            self.paymentstatus = paymentstatus
            self.paymentdetails = paymentdetails

    db = MySQLdb.connect('localhost','root','root','pharmacy')
    cursor = db.cursor()
    cursor.execute("select ordered.oid,ordered.name,orderhistory.order_date,orderhistory.price from ordered inner join orderhistory on ordered.oid = orderhistory.oid;")
    entries = cursor.fetchall()
    details = []
    context={}
    for item in entries:
        cursor.execute("select status,tid from payment where oid = "+str(item[0])+";")
        paymentstat = cursor.fetchone()
        cursor.execute("select status from delivery where oid = "+str(item[0])+";")
        deliverystatus = cursor.fetchone()
        cursor.execute("select orderhistory.quantity, products.pname from orderhistory inner join products on orderhistory.pid = products.pid  where orderhistory.oid = "+str(item[0])+";")
        productsget = cursor.fetchall()
        listofproducts = ""
        for element in productsget:
            listofproducts+= str(element[1])+": "+str(element[0])+",\n"
        details.append(order_display(item[0],item[1],listofproducts,item[2],item[3],deliverystatus[0],paymentstat[0],paymentstat[1]))
       
    db.close()
    context['details'] = details
    return render(request,'allorders.html',context)


def suppliers(request):
    class supplierpeople:
        def __init__(self, id, name, phone,address,email):
            self.id = id
            self.name = name
            self.phone=phone
            self.address = address
            self.email = email
            

    db = MySQLdb.connect('localhost', 'root', 'root', 'pharmacy')
    cursor = db.cursor()
    cursor.execute("select  supid,name,phone,address,email from supplier ;")
    entries = cursor.fetchall()
    details = []
    for item in entries:
        details.append(supplierpeople(item[0], item[1] ,item[2], item[3], item[4]))
    db.close()
    context={}
    context['details'] = details
    return render(request, 'suppliers.html', context)

def supply_details(request,suppid):
    class stockview:
        def __init__(self,prodid,name,price,quantity,dateofsupply):
            self.prodid =prodid
            self.name = name
            self.price = price
            self.quantity = quantity
            self.dateofsupply = dateofsupply
           

    db = MySQLdb.connect('localhost','root','root','pharmacy')
    cursor = db.cursor()
    cursor.execute("select suppliedby.pid,products.pname,suppliedby.price,suppliedby.quantity,suppliedby.supdate from suppliedby inner join products on suppliedby.pid = products.pid where suppliedby.supid = "+str(suppid)+";")
    entries = cursor.fetchall()
    details = []
    for item in entries:
        details.append(stockview(item[0],(item[1]), (item[2]),item[3],item[4]))
    db.close()
    context={}
    context['details'] = details 
    return render(request,'supply_details.html',context)

def view_customer_orders(request,uid):
	class orderdisplay:
		def __init__(self,order_id, order_date, total_cost, payment_status, delivery_status):
			self.order_id = order_id
			self.order_date = order_date
			self.total_cost = total_cost
			self.payment_status = payment_status
			self.delivery_status = delivery_status

	db = MySQLdb.connect('localhost','root','root','pharmacy')
	cursor = db.cursor()
	cursor.execute("select oid from ordered where uid = "+str(uid)+";")
	oid = cursor.fetchall()
	details = []
	for item in oid:	 
		cursor.execute("select price , order_date  from orderhistory where oid = "+str(item[0])+";")
		datecost = cursor.fetchone()
		cursor.execute("select status from payment where oid = "+str(item[0])+";")
		paymentstat = cursor.fetchone()
		cursor.execute("select status from delivery where oid = "+str(item[0])+";")
		deliverystatus = cursor.fetchone()
		details.append(orderdisplay(item[0],datecost[1],datecost[0],paymentstat[0],deliverystatus[0]))
		print(item[0],datecost[1],datecost[0],paymentstat[0],deliverystatus[0])
	db.close()
	context = {}
	context['details'] = details 
	return render(request,'view_customer_orders.html',context)

def employees(request):
    class adminemployee:
        def __init__(self,id,name,sex,phone,address,dateofjoin,salary):
            self.id = id
            self.name = name
            self.sex = sex
            self.phone = phone
            self.address = address
            self.dateofjoin = dateofjoin
            self.salary = salary
    
    db = MySQLdb.connect('localhost', 'root', 'root', 'pharmacy')
    cursor = db.cursor()
    cursor.execute("select * from shipper ;")
    entries = cursor.fetchall()
    details = []
    for item in entries:
        details.append(adminemployee(item[0],item[1],item[6],item[2],item[3],item[4],item[5]))
    context = {}
    context['details'] = details
    db.close()
    return render(request,'employees.html',context)

def add_employee(request):
    return render(request,'add_employee.html')

def insertemployee(request):
    name = request.POST.get('name')
    address = request.POST.get('address')
    phone = request.POST.get('phone')
    sex = request.POST.get('sex')
    salary = request.POST.get('salary')
    dateofjoin = request.POST.get('date')
    
    db = MySQLdb.connect('localhost', 'root', 'root', 'pharmacy')
    cursor = db.cursor()
    print(dateofjoin)
    cursor.execute("insert into shipper (name,phone,address,join_date,salary,sex) values ('" + str(name) +"',"+str(phone) +",'"+ str(address)+"','"+str(dateofjoin)+"',"+str(salary)+",'"+str(sex) +"');" )
  
    db.commit()
    db.close()
    return redirect('employees')


def remove_employee(request,emplid):
    db = MySQLdb.connect('localhost', 'root', 'root', 'pharmacy')
    cursor = db.cursor()
    cursor.execute("delete from shipper where sid = "+str(emplid)+";")
    db.commit()
    db.close()
    return redirect('employees')
def stock_products(request):
    class product_display:
        def __init__(self,id,name,price,quantity,description):
            self.id = id
            self.name = name
            self.quantity = quantity
            self.description = description
            self.price = price

    db = MySQLdb.connect('localhost','root','root','pharmacy')
    cursor = db.cursor()
    cursor.execute("select pid ,pname,price,quantity,details from products;")
    entries = cursor.fetchall()
    details = []
    for item in entries:
        details.append(product_display(item[0],item[1],item[2],item[3],item[4]))
    db.close()
    context = {}
    context['details'] = details
    return render(request,'stock_products.html',context)

def contactus(request):
    name = request.POST.get('fullname')
    email = request.POST.get('email')
    subject = request.POST.get('sub')
    message = request.POST.get('message')

    db = MySQLdb.connect('localhost','root','root','pharmacy')
    cursor = db.cursor()
    cursor.execute("insert into contactus (fullname,email,sub,message) values ('"+str(name)+"','"+str(email)+"','"+str(subject)+"','"+str(message)+"');")
    db.commit()
    db.close()
    return redirect('home')


def viewfeedback(request):
    class feedbacks:
        def __init__(self,name,email,subject,message):
            self.name = name
            self.email = email
            self.subject = subject
            self.message = message

    db = MySQLdb.connect('localhost', 'root', 'root', 'pharmacy')
    cursor = db.cursor()
    cursor.execute("select * from contactus;")
    entries = cursor.fetchall()
    details=[]
    for item in entries:
        details.append(feedbacks(item[0],item[1],item[2],item[3]))
    context = {}
    context['details'] = details 
    db.close()
    return render(request,'viewfeedback.html',context)



def addstock(request):
    class supplierform:
        def __init__(self, id, name):
            self.id = id
            self.name = name

    class productform:
        def __init__(self, id, name):
            self.id = id
            self.name = name

    db = MySQLdb.connect('localhost', 'root', 'root', 'pharmacy')
    cursor = db.cursor()
    cursor.execute("select supid,name from supplier;")
    suppliers = cursor.fetchall()
    cursor.execute("select pid,pname from products;")
    products = cursor.fetchall()
    supplier = []
    product = []
    for item in suppliers:
        supplier.append(supplierform(item[0],item[1]))
    for item in products:
        product.append(productform(item[0],item[1]))
    context = {}
    context = {
        'product':product,
        'suppliers':supplier,
    }
    db.close()
    return render(request, 'addstock.html', context)

def add_products_to_stock(request):
    supplierid = request.POST.get('supplier')
    productoption = request.POST.get('optradio')
    quantity = request.POST.get('quantity')
    price = request.POST.get('price')
     

    db = MySQLdb.connect('localhost', 'root', 'root', 'pharmacy')
    cursor = db.cursor()

    if productoption == "old":
        productchosen = request.POST.get('product')
        print(supplierid)
        print(productoption)
        print(quantity)
        print(comments)
        print(productchosen)
        cursor.execute("insert into suppliedby values ("+str(supplierid)+","+ str(productchosen) +","+str(quantity)+","+str(price)+","+CURDATE()+");")
        cursor.execute("update products set quantity = quantity + "+str(quantity)+" where pid = "+str(productchosen)+";")
    elif productoption == "new":
        print(supplierid)
        name = request.POST.get('name')
        typeid = request.POST.get('typeid')
        manufdate = request.POST.get('manufdate')
        expdate = request.POST.get('expdate')
        description = request.POST.get('description')
        cursor.execute("insert into products (pname,price,quantity,typeid,details,manufdate,expdate) values ('"+str(name)+"',"+str(price)+","+str(quantity)+","+str(typeid)+",'"+str(description)+"','"+str(manufdate)+"','"+str(expdate)+"');")
        cursor.execute("select LAST_INSERT_ID();")
       # id = cursor.fetchone()
        #id = int(id[0])
       # cursor.execute("insert into suppliedby values (" + str(id)+","+str(supplierid)+","+str(quantity)+",CURDATE(),'"+str(comments) +"');")
    db.commit()
    db.close()
    return redirect('stock_products')