from django.db import models
from datetime import datetime
class Category(models.Model):
    Name = models.CharField(max_length=100, blank=False)
    Created = models.DateField(default=datetime.now, blank=False)
    Updated = models.DateField(null=True, blank=True)
    Visible = models.BooleanField(default=False, blank=False)
    def __unicode__(self):
        return self.Name
class Product(models.Model):
    title = models.CharField(max_length=200, blank=False)
    Created = models.DateField(default=datetime.now, blank=False)
    Updated = models.DateField(null=True, blank=True)
    publish = models.BooleanField(default=False, blank=False)
    category = models.ForeignKey(Category  , on_delete=models.CASCADE)
    description = models.TextField(blank=True)