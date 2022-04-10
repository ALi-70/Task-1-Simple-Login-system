from django.shortcuts import render,redirect


from .models import doc_table 
from .models import pat_table

from django.contrib import messages

# Create your views here.
def home(request):
	return render (request,'home.html')

def doc_sec(request):
	return render(request,'doctor_section.html')

def pat_sec(request):
	return render(request,'patient_section.html')


def doctor_signup(request):

	if(request.method=="POST"):
		fn=request.POST.get('FirstName','')
		ln=request.POST.get('LastName','')

		pic=request.FILES['ProfilePic']

		un=request.POST.get('UserName','')  # .get() is fetching data from textbox
		eml=request.POST.get('Email','')
		pwd=request.POST.get('Password','')
		confirm_pwd=request.POST.get('ConfirmPassword','')
		add=request.POST.get('Address','')

		if pwd !=confirm_pwd:
			messages.warning(request,"Password does not match")


		else:
			rec=doc_table(firstname=fn,lastname=ln,image=pic,username=un,email=eml,password=pwd,confirm_password=confirm_pwd,address=add)
			rec.save()
			return redirect('dsin')   #redirect to sigin page
	return render(request,'doc_signup.html')



def doctor_signin(request):
	if request.method == "POST":
		un=request.POST['UserName']
		pwd=request.POST['Password']
		try:
			d1=doc_table.objects.get(username=un,password=pwd)
		except doc_table.DoesNotExist:
			return render(request,'doc_signin.html')
		else:
			request.session['uid'] = d1.id
			return redirect("dpro")
	else:
		return render(request,'doc_signin.html')





def doctor_profile(request):
	if(request.session.get('uid')):
		uid=request.session['uid']
		UID=doc_table.objects.get(id=uid)
		return render(request,'doc_profile.html',{"uid":UID})
	else:
		return render(request,'doc_signin.html')
	
	



# PATIENT FUNCTIONS

# Patient Signup
def patient_signup(request):

	if(request.method=="POST"):
		fn=request.POST.get('FirstName','')
		ln=request.POST.get('LastName','')

		pic=request.FILES['ProfilePic']

		un=request.POST.get('UserName','')  # .get() is fetching data from textbox
		eml=request.POST.get('Email','')
		pwd=request.POST.get('Password','')
		confirm_pwd=request.POST.get('ConfirmPassword','')
		add=request.POST.get('Address','')

		if pwd !=confirm_pwd:
			messages.warning(request,"Password does not match")


		else:
			rec=pat_table(firstname=fn,lastname=ln,image=pic,username=un,email=eml,password=pwd,confirm_password=confirm_pwd,address=add)
			rec.save()
			return redirect('psin')   #redirect to sigin page
	return render(request,'pat_signup.html')


# Patient Signin
def patient_signin(request):
	if request.method == "POST":
		un=request.POST['UserName']
		pwd=request.POST['Password']
		try:
			d1=pat_table.objects.get(username=un,password=pwd)
		except pat_table.DoesNotExist:
			return render(request,'pat_signin.html')
		else:
			request.session['uid'] = d1.id
			return redirect("ppro")
	else:
		return render(request,'pat_signin.html')



# Patient Profile
def patient_profile(request):
	if(request.session.get('uid')):
		uid=request.session['uid']
		UID=pat_table.objects.get(id=uid)
		return render(request,'pat_profile.html',{"uid":UID})
	else:
		return render(request,'pat_signin.html')



# Logout Function
from django.contrib.auth import logout as logouts
def logout1(request):
	logouts(request)
	try:
		del request.session['uid']    
	except KeyError:        
		pass
	return redirect('hm')
