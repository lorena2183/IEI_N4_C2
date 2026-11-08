from django import forms
from .models import EntradaDiario


class EntradaDiarioForm(forms.ModelForm):
    class Meta:
        model = EntradaDiario
     
        fields = ['categoria', 'etiquetas', 'titulo', 'contenido',
                  'fecha', 'hora', 'estado_animo', 'nivel_importancia']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
            'contenido': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
      
        for campo in self.fields.values():
            campo.widget.attrs['class'] = 'form-control'
