from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('course/<code>', views.pdf_page, name='pdf'),
    path('<code>', views.course_page, name='pdfs'),
]
