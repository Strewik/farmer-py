from django.db import models 


class Income(models.Model):
    date =models.DateTimeField(auto_now_add=True)
    customer = models.CharField(max_length=100)
    phone = models.IntegerField(max_length=10)
    product = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)
    unitprice = models.IntegerField(max_length=20)
    quantity = models.IntegerField(max_length=20)
    subtotal = models.IntegerField(max_length=20)
    tax = models.IntegerField(max_length=20, blank=True)
    descript = models.CharField(max_length=500, blank=True)
    total = models.IntegerField(max_length=20)
    invnumber = models.IntegerField(max_length=20, blank=True)
    amountpaid = models.IntegerField(max_length=20)
    paymode = models.CharField(max_length=50)
    receiptnum = models.IntegerField(max_length=20, blank=True)
    balduedate = models.DateTimeField(blank=True)