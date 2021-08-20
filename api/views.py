from django.shortcuts import render, redirect
from .models import Project
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.
def home_view(request):
    return render(request, "home.html")

def about_view(request):
    projects = Project.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST["email"]
        message = request.POST["message"]
        send_mail(name, message, email, ["mauriceyangmy28@gmail.com"])
        return redirect("About")
    return render(request, "about.html", {"projects" : projects})

def contact_view(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]
        send_mail(name, message, email, ["mauriceyangmy28@gmail.com"])
        return redirect("About")
    return render(request, "contact.html")

def project_detail_view(request, id):
    project = Project.objects.get(id = id)
    return render(request, "project_detail.html", {"project" : project})
