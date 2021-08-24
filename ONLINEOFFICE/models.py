from django.db import models


class registration(models.Model):

    FName = models.CharField(max_length=50, verbose_name='fullname', null=True)
    Address = models.CharField(max_length=50, verbose_name='Address',)
    ContactNo =models.DecimalField(max_digits=11, decimal_places=0, verbose_name='phone Number', default="")
    Username = models.CharField(max_length=20, verbose_name='username')
    Password = models.CharField(default="", max_length=15)   
    Email = models.EmailField(verbose_name='email')

    def __str__(self):
        return self.FName

class requesttable(models.Model):
    category = [
              ('Binyag', 'Binyag'),
              ('Kumpil', 'Kumpil'),
              ('Komunyon', 'Komunyon'),
              ('Kumpisal', 'Kumpisal'),
              ('Kasal', 'Kasal'),
              ('Blessing', 'Blessing'),
              ('Misa ng Patay', 'Misa ng Patay')
    ]
    statcat = [
            ('Accept', 'Accept'),
            ('Denied', 'Denied'),
            ('Pending', 'Pending')


    ]
    Name = models.CharField(max_length=50, verbose_name='fullname',)
    Purpose = models.CharField(max_length=15, choices=category, verbose_name='Purpose', default='')
    Date = models.DateField(default='')
    Details = models.CharField(max_length=50, verbose_name='Additional Details')
    Time = models.TimeField(default='')
    Status = models.TextField(max_length=20, choices=statcat, default="Pending", null=True )


    def __str__(self):
        return self.Name
# Create your models here.
