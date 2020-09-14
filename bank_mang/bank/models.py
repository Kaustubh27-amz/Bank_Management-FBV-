from django.db import models

# Create your models here.
class Account(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    age=models.CharField(max_length=2)
    adhaar_no=models.CharField(max_length=16)
    mobile_no=models.CharField(max_length=20)
    balance=models.IntegerField()

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('account_list',kwargs={'pk':self.pk})
