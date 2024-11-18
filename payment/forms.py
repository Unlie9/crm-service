from django import forms
from payment.models import Payment, Limit

class PaymentForm(forms.ModelForm):

    class Meta:
        model = Payment
        fields = ['name', 'first_name', 'last_name', 'balance', 'status', "limits"]

    
    def validate_limits(self):
        limits = self.cleaned_data.get("limits")
        balance = self.cleaned_data.get('balance')

        if not limits.exists():
            raise forms.ValidationError("At least one limit must be assigned.")

        # Валидация баланса относительно лимитов
        for limit in limits:
            if limit.name == "MIN_BALANCE_LIMIT" and balance < limit.value:
                self.add_error("balance", f"Balance cannot be less than {limit.value}.")
            if limit.name == "MAX_BALANCE_LIMIT" and balance > limit.value:
                self.add_error("balance", f"Balance cannot exceed {limit.value}.")

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
      self.validate_limits()

      return cleaned_data
    