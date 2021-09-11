from django.shortcuts import render, HttpResponse, redirect
from .models import Contact
from blog.models import Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError

# Create your views here.
def home(request):
    allPosts = Post.objects.all()
    context = { 'allPosts' : allPosts}
    return render(request, 'home/home.html', context)

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        contact = Contact(name=name, email=email, phone=phone, message=message)
        
        if len(name)<2 or len(email)<2 or len(phone)<2 or len(message)<2:
            messages.error(request,  'Please fill the form correctly.')
        else:
            contact.save()
            messages.success(request, 'Your Form has been submited successfully.')    


    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')

def search(request):
    query = request.GET['query']
    if len(query)>75:
        allPosts = []
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)
    context = {'allPosts' : allPosts, 'query' : query}    
    return render(request, 'home/search.html', context)


def signUp_user(request):
    if request.method != 'POST':
            return  HttpResponse('404 - Page Not Found')

    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmPassword']

        # checks error and validations
        if len(username) > 10 :
            messages.error(request, "Username must be under 10 characters")
            return redirect('home')
       
        if not username.isalnum() :
            messages.error(request, "Username should contain alphanumeric characters (abc123)")
            return redirect('home')

        if password != confirmpassword:
            messages.error(request, "Password do not match, Please enter correct Password")
            return  redirect("home") 
                

        # creating useraccount
        myuser = User.objects.create_user(username,email,password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your WebDevCode account has been successfully created")
        return redirect('home')
    else:
        messages.error(request, "Your WebDevCode account has been not successfully created")
        return redirect('home')

def login_user(request):
    if request.method == "POST":
        loginUsername = request.POST['loginUsername']
        loginPassword = request.POST['loginPassword']
        user = authenticate(request, username = loginUsername , password = loginPassword)

    if user is not None:
        login(request,user)
        messages.success(request, 'Successfully Logged In')
        return redirect('home')
    else:
        messages.error(request, 'Invalid credentials')
        return redirect('home')

    return HttpResponse('404 - Page Not Found')    

def logout_user(request):
    logout(request)
    messages.success(request, 'Successfully Logged Out')   
    return redirect('home')

        
