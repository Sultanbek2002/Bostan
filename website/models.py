from django.db import models

# Create your models here.
class Categoria(models.Model):
    categoria=models.CharField(verbose_name='категория',max_length=100, default=None)
    
class Product(models.Model):
    cat_id=models.ForeignKey(Categoria,on_delete=models.CASCADE,default=None)
    name_product=models.CharField(verbose_name='Продуктанын аты' ,max_length=100)
    characteris = models.JSONField(default=dict, blank=True, null=True, verbose_name='Характеристики')
    def add_characteristic(self, name, value):
        if not self.characteristics:
            self.characteristics = {}
        self.characteristics[name] = value
        self.save()

# class ProductCharacteristic(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='characteristics')
#     characteristic_name = models.CharField(verbose_name='Название характеристики', max_length=255,default=None)