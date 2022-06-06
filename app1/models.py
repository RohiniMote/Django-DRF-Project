from django.db import models

# Create your models here.
class Laptop(models.Model):
    id=models.IntegerField(primary_key=True)
    brand_name=models.CharField(max_length=100)
    model_name=models.CharField(max_length=100)
    price=models.FloatField()
    ram=models.CharField(max_length=40)
    rom=models.CharField(max_length=40)
    SSD=models.CharField(max_length=40)
    HDD=models.CharField(max_length=40)
    weight=models.CharField(max_length=40)
    year=models.DateTimeField()

    def __str__(self):
        return f"{self.id},{self.brand_name},{self.model_name},{self.price},{self.ram},{self.rom},{self.SSD},{self.HDD},{self.weight},{self.year}"


