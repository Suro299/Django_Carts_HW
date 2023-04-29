from django.db import models

class Cart(models.Model):
    prodcut = models.ForeignKey("Products", on_delete = models.CASCADE)
    count = models.PositiveIntegerField("Product count", blank = True, default = 1)
    price = models.PositiveBigIntegerField("Product Price",  default = 0)
    def __str__(self) -> str:
        return self.prodcut.name


class Products(models.Model):
    name = models.CharField("Product name", max_length = 255)
    price = models.PositiveBigIntegerField("Product Price")
    img = models.ImageField("Product image")
    
    def __str__(self) -> str:
        return self.name