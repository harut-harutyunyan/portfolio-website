from django.db import models
import datetime

class Project(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=255)
    image = models.ImageField(default='project_pics/default.jpg', upload_to='project_pics')
    link_to_code = models.CharField(blank=True, max_length=255)
    link = models.CharField(blank=True, max_length=255)
    link_desc = models.CharField(blank=True, max_length=100)
    skills = models.CharField(max_length=255)
    description = models.TextField()

    def skills_as_list(self):
        return self.skills.split(',')

    def __str__(self):
        return self.name

class Job(models.Model):
    role = models.CharField(max_length=36)
    company = models.CharField(max_length=36)
    start_date = models.DateField(blank=True, default=datetime.date.today)
    end_date = models.DateField(blank=True, null=True, default=None)
    thumb = models.ImageField(default='job_thumb/default.jpg', upload_to='job_thumb')
    description = models.TextField()

    def __str__(self):
        return self.role


__all__ = ['Job', 'Project']