from django.contrib.auth.models import User
from django.db import models

class Suv(models.Model):
    brend = models.CharField(max_length=500)
    narx = models.FloatField()
    litr = models.FloatField()
    batafsil = models.TextField()

    def __str__(self):
        return f"{self.brend}({self.litr})"
class Mijoz(models.Model):
    ism = models.CharField(max_length=150)
    tel = models.PositiveIntegerField()
    manzil = models.CharField(max_length=500)
    qarz = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.ism}"

class Admin(models.Model):
    ism = models.CharField(max_length=150)
    yosh = models.PositiveIntegerField()
    ish_vaqti = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.ism}"

class Haydovchi(models.Model):
    ism = models.CharField(max_length=150)
    tel = models.PositiveIntegerField()
    kiritilgan_sana = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.ism}"

class Buyurtma(models.Model):
    suv = models.ForeignKey(Suv, on_delete=models.CASCADE)
    sana = models.DateTimeField(auto_now_add=True)
    miqdor = models.PositiveIntegerField()
    umumiy_narx = models.FloatField()
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    haydovchi = models.ForeignKey(Haydovchi, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.suv}({self.sana})"