from socket import fromshare
from django import forms
from django.core.validators import MinValueValidator



class DishForm(forms.Form):
    name = forms.CharField(label='Название блюда: ', max_length=300)
    type = forms.ChoiceField(label='Тип блюда', choices=['напиток', 'второе блюдо', 'суп', 'запеканка', 'салат'])
    count = forms.FloatField(label='Количество: ',validators=[MinValueValidator(0,0)])

       

