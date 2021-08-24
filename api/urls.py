from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name = "Home"),
    path("about", views.about_view, name="About"),
    path('contact', views.contact_view, name="Contact"),
    path('project/<int:id>', views.project_detail_view, name="Project Detail"),
    path('error', views.error_page, name="Error"),
    path("<str:random_string>", views.error_redirect, name = "Error Redirect")
]
