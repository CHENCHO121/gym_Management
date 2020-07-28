from django.db import models

class Enquiry(models.Model):
    name=models.CharField(max_length=100)
    contact=models.CharField(max_length=10)
    email=models.EmailField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Equipment(models.Model):
    name=models.CharField(max_length=100)
    price=models.FloatField()
    unit=models.IntegerField()
    date = models.CharField(max_length=40)
    description=models.TextField(max_length=500)


    def __str__(self):
        return self.name


class Plan(models.Model):
    name=models.CharField(max_length=50)
    amount=models.FloatField()
    duration=models.CharField(max_length=10)
    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    plan=models.CharField(max_length=50)
    join_date=models.CharField(max_length=40)
    expired_date=models.CharField(max_length=40)
    initial_amount=models.FloatField()
    def __str__(self):
        return self.name

class ContactUs(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=8)
    msg=models.TextField(max_length=500)
    def __str__(self):
        return self.name

