import os
from django.db import models
from .choices_electronics import *
from django.core.exceptions import ValidationError


class HomeModel(models.Model):
    home_id = models.IntegerField(unique=True)
    home_owner = models.CharField(max_length=50)
    home_address = models.CharField(max_length=50)
    home_electronic = models.FloatField(default=0)
    phone_number = models.IntegerField()
    connected_telegram = models.IntegerField(null=True, default=0)
    date_joined = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    password = models.CharField(max_length=16)

    def __str__(self):
        return str(self.home_owner)


class ElectronicItem(models.Model):
    item = models.CharField(choices=ELECTRONIC_CHOICES, max_length=50)
    related_home = models.ForeignKey(HomeModel, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.item)


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.mp4', '.png', '.jpg', '.jpeg', '.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError(f'Unsupported file extension: {ext}. Allowed extensions are {valid_extensions}')


class ReportModel(models.Model):
    home = models.ForeignKey(HomeModel, on_delete=models.CASCADE)
    report_type = models.CharField(choices=REPORT_CHOICES, max_length=50)
    report_description = models.CharField(max_length=100)
    report_file = models.FileField(upload_to='uploads/', validators=[validate_file_extension])

    def __str__(self):
        return str(self.report_description)


