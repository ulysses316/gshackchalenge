from django import forms

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
BIRTH_MONTH_CHOICES = ['monday', 'tuesday', 'wendsday','thursday','friday','saturday','sunday']
BIRTH_DAY_CHOICES = ['1', '2', '3','4','5','6','7','8','9','10'
                     '11', '12', '13','14','15','16','17','18','19','20'
                     '21', '22', '23','24','25','26','27','28','29','30','31']


class PerfilForm(forms.Form):
    first_name = forms.CharField(label='Nombres', max_length = 30)
    last_name = forms.CharField(label='Apellidos', max_length = 30)
    birth_date = forms.DateField(initial=datetime.date.today)