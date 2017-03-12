from django import forms


class ArtistForm(forms.Form):
    name = forms.CharField(label='Artist ', max_length=100)
