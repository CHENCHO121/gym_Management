from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from .models import Equipment,Enquiry,Plan,Member,ContactUs
from django.contrib import messages

def home(request):
    if not request.user.is_staff:
        return redirect('login')
    enq=Enquiry.objects.count()
    equip=Equipment.objects.count()
    plan=Plan.objects.count()
    mem=Member.objects.count()
    query=ContactUs.objects.count()
    context={
        'enq':enq,
        'equip':equip,
        'plan':plan,
        'mem':mem,
        'query':query
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def contact(request):
    error=""
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        try:
            con = ContactUs(name=name, email=email, phone=phone, msg=message)
            con.save()
            error="no"
        except:
            error="yes"
    d={'error':error}

    return render(request,'contact.html',d)



def view_contact(request):
    if not request.user.is_staff:
        return redirect('/login')
    query=ContactUs.objects.all()
    return render(request,'view_query.html',{'query':query})

def delete_query(request,id):
    query=ContactUs.objects.get(id=id)
    query.delete()
    return redirect('/view_contact')

def Login(request):
    error=""
    if request.method=="POST":
        uname=request.POST['uname']
        pwd=request.POST['password']
        user=authenticate(username=uname,password=pwd)
        try:
             if user.is_staff:
                 login(request,user)
                 error="no"
             else:
                 error="yes"
        except:
             error="yes"
    d={'error':error}
    return render(request,'login.html',d)

def logout_admin(request):
    logout(request)
    return redirect('/')

def add_enquiry(request):
    error=""
    if not request.user.is_staff:
        return redirect('/login')
    if request.method=="POST":
        name=request.POST['name']
        contact=request.POST['contact']
        email=request.POST['email']
        age=request.POST['age']
        gender=request.POST['gender']
        try:
            Enquiry.objects.create(name=name,contact=contact,email=email,age=age,gender=gender)
            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'add_enquiry.html',d)


def view_enquiry(request):
    if not request.user.is_staff:
        return redirect('/login')
    enq=Enquiry.objects.all()
    return render(request,'view_enquiry.html',{'enq':enq})

def delete_enquiry(request,id):
    enquiry=Enquiry.objects.get(id=id)
    enquiry.delete()
    return redirect('/view_enquiry')






def add_equipment(request):
    error=""
    if not request.user.is_staff:
        return redirect('/login')
    if request.method=="POST":
        name=request.POST['name']
        price=request.POST['price']
        unit=request.POST['unit']
        date=request.POST['date']
        description=request.POST['description']
        try:
            Equipment.objects.create(name=name,price=price,unit=unit,date=date,description=description)
            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'add_equipment.html',d)


def view_equipment(request):
    if not request.user.is_staff:
        return redirect('/login')
    equip=Equipment.objects.all()
    return render(request,'view_equipment.html',{'equip':equip})

def delete_equipment(request,id):
    equipment=Equipment.objects.get(id=id)
    equipment.delete()
    return redirect('/view_equipment')


def add_plan(request):
    error=""
    if not request.user.is_staff:
        return redirect('/login')
    if request.method=="POST":
        name=request.POST['name']
        amount=request.POST['amount']
        duration=request.POST['duration']

        try:
            Plan.objects.create(name=name,amount=amount,duration=duration)
            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'add_plan.html',d)


def view_plan(request):
    if not request.user.is_staff:
        return redirect('/login')
    plan=Plan.objects.all()
    return render(request,'view_plan.html',{'plan':plan})

def delete_plan(request,id):
    plan=Plan.objects.get(id=id)
    plan.delete()
    return redirect('/view_plan')




def add_member(request):
    error=""
    if not request.user.is_staff:
        return redirect('/login')
    plan1=Plan.objects.all()
    if request.method=="POST":
        name=request.POST['name']
        contact=request.POST['contact']
        email=request.POST['email']
        age=request.POST['age']
        gender=request.POST['gender']
        p=request.POST['plan']
        joindate=request.POST['joindate']
        expireddate=request.POST['expireddate']
        initialamount=request.POST['initialamount']
        plan=Plan.objects.filter(name=p).first()
        try:
            Member.objects.create(name=name,contact=contact,email=email,age=age,gender=gender,plan=plan,join_date=joindate,expired_date=expireddate,initial_amount=initialamount)
            error="no"
        except:
            error="yes"
    d={'plan':plan1,'error':error}
    return render(request,'add_member.html',d)


def view_member(request):
    if not request.user.is_staff:
        return redirect('/login')
    member=Member.objects.all()
    return render(request,'view_member.html',{'member':member})

def delete_member(request,id):
    member=Member.objects.get(id=id)
    member.delete()
    return redirect('/view_member')


def hero_section(request):
    return render(request,'hero_section.html')


