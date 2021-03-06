from django.shortcuts import render, redirect
from .models import Project
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from .forms import AddProjectForm

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
        send_mail(subject=str(name) + ", from : " + str(email), message=str(email) + " sent you :  " + str(message), from_email=email, recipient_list=["mauriceyangmy28@gmail.com"])
        return redirect("About")
    return render(request, "contact.html")

def project_detail_view(request, id):
    try:
        project = Project.objects.get(id = id)
        return render(request, "project_detail.html", {"project" : project})
    except ObjectDoesNotExist:
        return redirect("Error")

def add_project_view(request):
    if request.method == "POST":
        form = AddProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            desc = form.cleaned_data["desc"]
            image = form.cleaned_data["image"]
            link = form.cleaned_data["link"]
            project = Project.objects.create(name, desc,image,link)
            project.save()
            return redirect("About")
    else:
        form = AddProjectForm
    return render(request, "add_project.html", {"form" : form})

def error_page(request, *args):
    return render(request, "error404.html")

def error_redirect(request, random_string):
    return redirect("Error")
