from django.contrib import admin
from .models import LectureNote

# Register your models here.

@admin.register(LectureNote)
class LectureNotesAdmin(admin.ModelAdmin):
    list_display = ['code', 'pdf']
    list_filter = ['code']
    search_fields = ['code']
