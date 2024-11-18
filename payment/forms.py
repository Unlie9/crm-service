from django import forms
from payment.models import Payment, Limit

class PaymentForm(forms.ModelForm):

    class Meta:
        model = Payment
        fields = ['name', 'first_name', 'last_name', 'balance', 'status']
        # exclude = ["limits", "site", "invoice"]

    
    def validate_name(self):
        name = self.cleaned_data.get("name")

        if len(name) < 4:
            self.add_error("name", "name of payment must be longer than 4 chars")


    def validate_initials(self):
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")

        if len(first_name) < 4:
            self.add_error("first_name", "first name must be longer than 4 chars")

        if len(last_name) < 4:
            self.add_error("last_name", "last name must be longer than 4 chars")

    def validate_balance(self):
        balance = self.cleaned_data.get("balance")

        if balance > 200000:
            self.add_error("balance", "balance can not be more than 200000")

    def clean(self):
      cleaned_data = super().clean()
      self.validate_name()
      self.validate_initials()
      self.validate_balance()

      return cleaned_data
    