from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone


class Color(models.Model):
    name = models.CharField(max_length=16)
    hex = models.CharField(max_length=16)
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=16)
    def __str__(self):
        return self.name


class Times(models.Model):
    time_type = models.CharField(max_length = 30)
    timeslot= models.TimeField(blank = True)
    time_check= models.BooleanField(default = True)

    def __str__(self):
        return self.time_type




class Car(models.Model):
    TRANSMISSION_CHOICES = (
        ('Auto', 'Auto'),
        ('Manual', 'Manual')
    )
    SEATS_CHOICES = (
        ('2', '2'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        )
    FUEL_CHECK = (
        ('Petrol', 'PETROL'),
        ('Diesel', 'Diesel'),
        ('Gas', 'Gas'),
    )
    reg_no = models.CharField(max_length=16, unique=True)
    model_year = models.DateField()
    car_name =models.CharField(max_length=40)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    times_for = models.ForeignKey(Times,on_delete=models.CASCADE)
    car_image = models.ImageField(upload_to='cars', blank = True)
    description = models.CharField(max_length=200)
    is_available_car = models.BooleanField(default = False)
    car_price = models.IntegerField(blank = False)
    power_hp = models.CharField(max_length= 20 , blank = True)
    transmission = models.CharField(max_length = 10 , choices = TRANSMISSION_CHOICES)
    seats = models.CharField(max_length=10, choices = SEATS_CHOICES)
    air_bags = models.CharField (max_length = 10 , choices = SEATS_CHOICES)
    car_image_internal = models.ImageField(upload_to='cars', blank = True)
    car_image_internal2 = models.ImageField(upload_to='cars', blank = True)
    fuel_type = models.CharField(max_length= 20 , choices = FUEL_CHECK)

    def __str__(self):
        return self.car_name

    def get_absolute_url(self):
        return reverse("buggy_app:details",kwargs={'pk':self.pk})



class Customer(models.Model):
    first_name = models.CharField(max_length=64,null= False)
    last_name = models.CharField(max_length=64)
    customer_age = models.IntegerField(blank=True, null=True)
    last_name = models.CharField(blank=True, max_length=100)
    license_year = models.IntegerField(blank=False, null=False)
    tlc_number = models.IntegerField(blank=False ,null=False)
    contact_num =models.IntegerField(blank=False, null=False)
    contact_email = models.EmailField(blank =False)


    def __str__(self):
        return self.first_name


class Booking(models.Model):
    booking_name = models.CharField(max_length=240,null= False)
    customer_name = models.ForeignKey(Customer ,on_delete=models.CASCADE,related_name='book_customers' )
    book_car = models.ForeignKey(Car, on_delete=models.CASCADE ,related_name='book_car')
    booking_start_date = models.DateTimeField(auto_now_add=True ,blank=True)
    booking_end_date = models.DateTimeField(blank = True , null = True)
    rental_price = models.IntegerField(blank=False, null=False)
    is_approved = models.BooleanField(default=False)
    def __str__(self):
        return self.booking_name

    def get_absolute_url(self):
        return reverse("buggy_app:detail",kwargs={'pk':self.pk})
