from django import forms


class PeopleF(forms.Form):
    lastname = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control text-uppercase'}), max_length=50, label='Apellido *', required=True)
    firstname = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control text-uppercase'}), max_length=50, label='Nombres *', required=True)
    identity = forms.IntegerField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), label='Documento *', required=True)
    datebirth = forms.DateTimeField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), label='Fecha Nacimiento *', required=True)


class PeoplePhone(forms.Form):
    id_people = forms.IntegerField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), label='Familiar *', required=True)
    phonenumber = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}),
         label='Teléfono *', required=True)


class PeopleAddress(forms.Form):
    id_people = forms.IntegerField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), label='Familiar *', required=True)
    address = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control text-uppercase'}), max_length=100, label='Domicilio *', required=True)
    type = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control text-uppercase'}), max_length=25, label='Tipo *', required=True)



