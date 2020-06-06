from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_name = models.CharField(max_length=50)
    customer_code = models.IntegerField(unique=True)
    address = models.TextField()
    account_bal = models.FloatField(default=0.0)
    bill = models.FloatField(default=0.0)
    advance =models.FloatField(default=0.0)

    def __str__(self):
        return self.customer_name
