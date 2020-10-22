from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Cycle(models.Model):
    model_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    cycle_img_main = models.ImageField(upload_to='cycles/images', default='')
    cycle_img_sub1 = models.ImageField(upload_to='cycles/images', default='')
    cycle_img_sub2 = models.ImageField(upload_to='cycles/images', default='')
    cycle_img_sub3 = models.ImageField(upload_to='cycles/images', default='')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.model_name


class Description(models.Model):
    cycle_id = models.ForeignKey('Cycle', on_delete=models.CASCADE)
    cycle_type = models.CharField(max_length=40)
    frame_material = models.CharField(max_length=40)
    frame_size = models.CharField(max_length=40)
    suspension = models.CharField(max_length=40)
    brake_type = models.CharField(max_length=40)
    number_of_speeds = models.CharField(max_length=40)
    wheel_size = models.CharField(max_length=40)

    def __str__(self):
        return self.cycle_type


class Price(models.Model):
    cycle_id = models.ForeignKey('Cycle', on_delete=models.CASCADE)
    daily_rental = models.IntegerField()
    weekly_rental = models.IntegerField()
    monthly_rental = models.IntegerField()




