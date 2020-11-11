from django.db import models

# Create your models here.

class Order(models.Model):
    cname = models.CharField(max_length=50)
    nt = models.IntegerField(default='1')
    date = models.DateField()
    payment = models.BooleanField(default=False,null=True)
    tgive = models.BooleanField(default=False,null=True)
    trecv = models.BooleanField(default=False,null=True)

    def __str__(self):
        return self.cname

