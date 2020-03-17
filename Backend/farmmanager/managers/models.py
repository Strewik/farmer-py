from django.db import models 


class Income(models.Model):
    date =models.DateTimeField(auto_now_add=True)
    customer = models.CharField(max_length=100)
    phone = models.IntegerField(max_length=10)
    product = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)
    unitprice = models.IntegerField()
    quantity = models.IntegerField()
    subtotal = models.IntegerField()
    tax = models.IntegerField(blank=True)
    descript = models.CharField(max_length=500, blank=True)
    total = models.IntegerField()
    invnumber = models.IntegerField(blank=True)
    amountpaid = models.IntegerField()
    paymode = models.CharField(max_length=50)
    receiptnum = models.IntegerField(blank=True)
    balancedue = models.IntegerField(blank=True)
    balduedate = models.DateTimeField(blank=True)