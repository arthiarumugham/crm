from __future__ import unicode_literals

from django.db import models
from department.models import Department

# Create your models here.
class Employee(models.Model):
    """ Model representating Employees in an organisation """
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    official_email = models.CharField(max_length=200)
    department = models.ForeignKey(Department)

    def __unicode__(self):
		return'{first_name}:{last_name}'.format(first_name=self.first_name, last_name=self.last_name)
