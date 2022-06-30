from django.db import models
from user.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Kategoriyalar'

    def __str__(self):
        return self.category_name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Mahsulot nomi',max_length=100)
    brand = models.CharField(verbose_name='Brend',max_length=80, blank=True)
    description = models.TextField(verbose_name='Tavsif')
    model = models.CharField(verbose_name='Mahsulot modeli',max_length=20)
    cost = models.PositiveIntegerField(verbose_name='Narx',default=100)
    photo = models.ImageField(verbose_name='Mahsulot rasmi',upload_to='product-photos/', blank=True)
    views = models.IntegerField(default=0)
    like = models.PositiveIntegerField(default=0)
    product_count = models.PositiveIntegerField(verbose_name='Mahsulot soni', default=10)

    class Meta:
        verbose_name_plural = 'Mahsulotlar'

    def __str__(self):
        return f"{self.category.category_name} | {self.brand} | {self.name}"

class Box(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Savatcha'

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.product.name}'