from django import forms

class TicketForm(forms.form):
    confirmation_number = forms.IntegerField(label='Confirmation Number')

