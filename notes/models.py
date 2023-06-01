from django.db import models

# Create your models here.


class LectureNote(models.Model):
    code = models.CharField(max_length=10)
    pdf = models.FileField(upload_to='lecture_notes')
    name = models.CharField(max_length=100, blank=True, null=True)
    author = models.CharField(max_length=50, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.code}"
    

    class Meta:
        ordering = ['-created_on']