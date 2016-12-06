""" forms.py lists all the forms used in Tickets app """
from django import forms
from customers.models import Customer
from employees.models import Employee
from .models import Ticket

class TicketCreateForm(forms.ModelForm):
    """ Ticket Create Form lists fields used for Ticket Creation """
    class Meta:
        model = Ticket
        fields = ("name", "description", "priority", "raised_by", "assigned_to")

    PRIORITY = (
    	   ('H', 'High'),
    	   ('M', 'Moderate'),
    	   ('L', 'Low')
    )

    name = forms.CharField(widget=forms.TextInput())
    description = forms.CharField(widget=forms.TextInput())
    priority = forms.ChoiceField(choices=PRIORITY)
    raised_by = forms.ModelChoiceField(queryset=Customer.objects.all())
    assigned_to = forms.ModelChoiceField(queryset=Employee.objects.all())
