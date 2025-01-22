from django import forms


class OrderForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    delivery_address = forms.CharField(required=True)
