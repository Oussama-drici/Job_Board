from asyncio.windows_events import NULL
from distutils.command.upload import upload
from doctest import DONT_ACCEPT_TRUE_FOR_1
from email.policy import default
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
JOB_TYPE = (
    ('Full time', 'Full time'),
    ('Part time', 'Part time'),
)


def upload_img(instance, filename):
    img_name, extension = filename.split(".")
    return "jobs/%s.%s" % (instance.id, extension)
# Create your models here.


class job(models.Model):
    owner = models.ForeignKey(
        User, related_name='job_owner', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    # location
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_img)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class category(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class apply(models.Model):
    job = models.ForeignKey(
        'job', related_name='apply_job', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='jobs/', default='jobs/7.webp')

    def __str__(self) -> str:
        return self.name
