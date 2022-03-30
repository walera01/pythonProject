from django.db import models


class Subs(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)
    text = models.TextField()
    img = models.ImageField()

    def __str__(self):
        return "Useremail__(%s) ___________name__(%s)" % (self.email, self.name)

