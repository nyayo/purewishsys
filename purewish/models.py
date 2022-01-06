from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


class Posts(models.Model):
    title = models.CharField(max_length=200)
    post = models.TextField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Donor(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, blank=True)
    second_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    organisation = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=20)
    phone = models.IntegerField()
    image = models.ImageField(default='default.png', upload_to='profile/')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.organisation

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Messages(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_msg')
    message = models.TextField()
    room = models.CharField(max_length=150, default='purewish')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message[0:50]

    class Meta:
        ordering = ('created',)


class Stuff(models.Model):
    stuff = models.ForeignKey(
        User, related_name='stuff', on_delete=models.CASCADE)
    phone = models.IntegerField()
    image = models.ImageField(default='default.png', upload_to='profile/')
    role = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.stuff

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Volunteer(models.Model):
    volunteer = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200, blank=True)
    second_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    phone = models.IntegerField()
    image = models.ImageField(default='default.png', upload_to='profile/')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.volunteer

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Gallery(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='gallery/')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 160 or img.width > 160:
            output_size = (180, 180)
            img.thumbnail(output_size)
            img.save(self.image.path)


class MailManager(models.Model):
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=500)
    receiver = models.EmailField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class ProjectManager(models.Model):
    project = models.CharField(max_length=100)
    description = models.TextField(max_length=280)
    sponsors = models.CharField(max_length=100, blank=True)
    image = models.FileField(blank=True)
    project_manager = models.CharField(max_length=100)
    theme = models.CharField(max_length=100, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    role = models.CharField(
        max_length=200, default=None, blank=True, null=True)
    phone = models.CharField(max_length=256, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=(
        ('m', ('Male')), ('f', ('Female'))), blank=True, null=True)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (180, 180)
            img.thumbnail(output_size)
            img.save(self.image.path)
