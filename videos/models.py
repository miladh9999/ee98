from django.db import models


class Professor(models.Model):
    name = models.CharField(max_length=60)
    course_name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='videos/images', blank=True)

    def __str__(self):
        return self.name


class Video(models.Model):
    session = models.IntegerField()
    link = models.URLField(max_length=500)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='videos')
    topic = models.CharField(max_length=150, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.professor.course_name