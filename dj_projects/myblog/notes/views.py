from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def notesHome(request):
    return render(request, "notes/notesHome.html")
