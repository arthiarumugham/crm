"""models.py containing all the models relevant to the customer's app """
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Customer(models.Model):
    """ Model representing the customers of organisation """
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email_id = models.CharField(max_length=200)
    phone_number = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return '{first_name}:{last_name}'.format(first_name=self.first_name,
                                                 last_name=self.last_name)
