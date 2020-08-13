from django.db import models
import datetime



class SingletonModel(models.Model):

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class PersonalInfo(SingletonModel):
    email = models.EmailField(default='har8unyan@gmail.com')
    avatar = models.ImageField(default='personal/default.jpg', upload_to='personal')
    photo = models.ImageField(upload_to='personal')
    signature = models.CharField(max_length=255)
    home_message = models.TextField()
    about_text = models.TextField()

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


__all__ = ['Job', 'Project', 'PersonalInfo']