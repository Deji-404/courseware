from django.shortcuts import render, get_object_or_404
from .models import LectureNote

# Create your views here.


def home_page(request):

    return render(request, 'index1.html')


def pdf_page(request, code):

    note = get_object_or_404(LectureNote, code=code)

    return render(request, 'pdfpage.html', {'note': note})


def course_page(request, code):

    notes = LectureNote.objects.filter(code=code)

    return render(request, 'coursepage.html', {'notes': notes})