from django.shortcuts import render, redirect
from django.contrib import messages
from home.models import Signup
from home.models import Feedback
from home.models import Contactus
from datetime import datetime
from home.forms import feedbackform
from home.forms import contactform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')

def signups(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # Check for Input Error 
        if len(username) > 10:
            messages.error(request, 'Username is under 10 characters')
            return redirect('/')

        if not username.isalnum():
            messages.error(request, 'Username only contain letters and numbers')
            return redirect('/')

        if pass1 != pass2:
            messages.error(request, 'Password do not match..!Please try again')
            return redirect('/')
        # Create the user 
        myuser = User.objects.create_user(username,email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, 'Your message has been sent.')
        return redirect('/')
    else:
        return HttpResponse('404 - Not Found')

def signin(request):
    if request.method == 'POST':
        signinusername = request.POST['signinusername']
        signinpass1 = request.POST['signinpass1']

    user = authenticate(username=signinusername, password=signinpass1)

    if user is not None:
        login(request, user)
        messages.success(request, 'Successfully Signin.')
        return redirect('/')

    else:
        messages.error(request, 'Invalide input..!Please try again')
        return redirect('/')

    return HttpResponse('404 - Not Found')

def signout(request):
    logout(request)
    messages.success(request, 'Successfully Signout.')
    return redirect('/')

    return HttpResponse('404 - Not Found')

def contact(request):
    all_data_contact = Contactus.objects.all()
    if request.method == "POST":
        contactemail = request.POST.get('contactemail')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        data1 = Contactus(contactemail=contactemail, fname=fname, lname=lname, date_add1= datetime.today())
        data1.save()
        return render(request, 'contact.html', {'Messagess':all_data_contact})
    return render(request, 'contact.html', {'Messagess':all_data_contact})


def feedback(request):
    all_data = Feedback.objects.all()
    # print(all_data)
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        feedbackemail = request.POST.get('feedbackemail')
        subject = request.POST.get('subject')
        feedback= request.POST.get('feedback')
        data = Feedback(first_name=first_name, last_name=last_name, feedbackemail=feedbackemail, subject=subject, feedback=feedback, date_add= datetime.today())
        data.save()
        messages.success(request, 'Your message has been sent.')
        return render(request, 'feedback.html', {'Messages':all_data})
    return render(request, 'feedback.html', {'Messages':all_data})

def delete(request, id):
    userdata = Feedback.objects.get(id=id)
    userdata.delete()
    return redirect('/feedback')

def update(request, id):
    userdata = Feedback.objects.get(id=id)
    return render(request, 'feedback2.html', {'Feedback':userdata})

def edit(request, id):
    result = Feedback.objects.get(id=id)
    form = feedbackform(request.POST, instance=result)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your Feedback is updated.')
        return render(request, 'feedback2.html', {'Feedback':result})
    return redirect('/feedback')

def deletecontact(request, id):
    userdata1 = Contactus.objects.get(id=id)
    userdata1.delete()
    return redirect('/contact')

def updatecontact(request, id):
    userdata1 = Contactus.objects.get(id=id)
    return render(request, 'contact2.html', {'Contactus':userdata1})

def editcontact(request, id):
    result1 = Contactus.objects.get(id=id)
    form1 = contactform(request.POST, instance=result1)
    if form1.is_valid():
        form1.save()
        messages.success(request, 'Your Contact is updated.')
        return render(request, 'contact2.html', {'Contactus':result1})
    return redirect('/contact')