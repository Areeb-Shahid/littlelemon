from django.db import models

# Create your models here.

class DrinksCategory(models.Model):
    category_name = models.CharField(max_length=200)


class Drinks(models.Model):
    drink_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category_id = models.ForeignKey(DrinksCategory, on_delete=models.PROTECT, default=None)


class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now=True)
    comments = models.CharField(max_length=1000)


class Employees(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    shift = models.IntegerField()

    def __str__(self) -> str:
        return self.first_name

class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField(default='Default description')
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)

    def __str__(self) -> str:
        return self.name