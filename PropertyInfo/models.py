from django.db import models
import uuid
from django.contrib.auth.models import User


class Property(models.Model):
    uid = models.UUIDField(default=uuid.uuid4(),
                           editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    property_name = models.CharField(max_length=30)
    property_description = models.TextField()


    class Meta:
        verbose_name_plural = 'Properties'

    def __str__(self):
        return self.property_name


class ActivityType(models.Model):
    type = models.CharField(max_length=30)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    def __str__(self):
        return self.type

class Activities(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    activity_type = models.ForeignKey(ActivityType, on_delete=models.CASCADE)

    location = models.CharField(max_length=30)
    url = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Activities'

