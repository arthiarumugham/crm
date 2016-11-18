""".models.py contains the models relevant to the Department app """
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Department(models.Model):
    """ Model representating Departments in the organisation """
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return'{name}'.format(name=self.name)
        