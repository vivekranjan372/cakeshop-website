from cakeshop.models import Registration
class RegistrationForum(forms.ModelForm):
    class Meta:
        model=Registration
        fields="__all__"

class SellCakeForum(forms.ModelForm):
    class Meta:
        model=SellCake()
        fields="__all__"