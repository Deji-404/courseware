from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('course/<code>', views.pdf_page, name='pdf'),
    path('courses/<code>', views.course_page, name='pdfs'),
    path('ads.txt', views.ads_view, name='ads'),
]
