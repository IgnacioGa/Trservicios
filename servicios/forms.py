from django import forms

class Consulta(forms.Form):
    nombre = forms.CharField(max_length=64,  required=True, label=False) 
    email = forms.EmailField(max_length=80,  required=True, label=False)
    msg = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}), required=True, label=False)

    def __init__(self, *args, **kwargs):
        super(Consulta, self).__init__(*args, **kwargs)
        self.fields['marca'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Nombre'
        }
        self.fields['email'].widget.attrs = {
            'class': 'form-control',
            'type': 'email',
            'placeholder': 'E-mail',
            'id' : 'exampleFormControlInput1'
        }
        self.fields['msg'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Escriba su consulta',
            'id' : 'exampleFormControlTextarea1'
        }
    