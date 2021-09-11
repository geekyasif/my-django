from django.shortcuts import render, HttpResponse

# Create your views here.
def notesHome(request):
    return render(request,"notesHome.html")

