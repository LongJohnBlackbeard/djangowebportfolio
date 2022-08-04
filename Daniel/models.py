from django.db import models

# Home Section


class Home(models.Model):
    name = models.CharField(max_length=20)
    greeting_1 = models.CharField(max_length=20)
    greeting_2 = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='picture/')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# About Section

class About(models.Model):
    heading = models.CharField(max_length=150)
    career = models.CharField(max_length=30)
    description = models.TextField(blank=False)
    profile_image = models.ImageField(upload_to='profile/')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.career


class Profile(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    social_name = models.CharField(max_length=20)
    link = models.URLField(max_length=200)


# Skills Section

class Category(models.Model):
    name = models.CharField(max_length=30)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name


class Skills(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=30)
    skill_link = models.URLField(max_length=100)


# Portfolio Section

class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f'Portfolio {self.id}'


# Contact Section
class Contact(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email
