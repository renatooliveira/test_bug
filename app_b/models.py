from django.db import models

from app_a.models import Model_A


class Model_B(models.Model):
    field_a = models.ForeignKey('app_a.Model_A')
