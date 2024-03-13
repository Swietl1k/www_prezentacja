from django.db import models

class Siteuser(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    join_date = models.DateField(null=True)
    slug = models.SlugField(default="", null=False)

    def __str__(self): #poprawia widoczność zmiennych w panelu admina
        return f"{self.firstname} {self.lastname}"

