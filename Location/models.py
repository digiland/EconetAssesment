from django.db import models

# Create your models here.


class Area(models.Model):
    name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Street(models.Model):
    street_name = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    area = models.ForeignKey(
        Area, on_delete=models.CASCADE, related_name='area')

    def __str__(self):
        return self.street_name
