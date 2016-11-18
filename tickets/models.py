""" models.py contains models relevant to the Ticket raised by a customer """
from __future__ import unicode_literals

from django.db import models
from customers.models import Customer
from employees.models import Employee

# Create your models here.
class Ticket(models.Model):
    """ model representing Ticket raised by a Customer """
    PRIORITY = (
    	   ('H', 'High'),
    	   ('M', 'Moderate'),
    	   ('L', 'Low')
    )

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=800)
    raised_by = models.ForeignKey(Customer)
    assigned_to = models.ForeignKey(Employee)
    priority = models.CharField(max_length=10, choices=PRIORITY, default='L')

    def __unicode__(self):
        return '{name}:{raised_by}:{assigned_to}'.format(name=self.name,
                                                         raised_by=self.raised_by__name,
                                                         assigned_to=self.assigned_to__name)
