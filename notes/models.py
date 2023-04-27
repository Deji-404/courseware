from django.db import models

# Create your models here.


class LectureNote(models.Model):
    code = models.CharField(max_length=10)
    pdf = models.FileField(upload_to='lecture_notes')


    def __str__(self) -> str:
        return f"{self.code}"