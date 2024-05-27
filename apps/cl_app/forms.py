from django import forms
from .models import Categoria

class CategoriaForm(forms.ModelForm):
    
    class Meta:
        model = Categoria
        fields = ('nombre','habilitada','margporc','valormag',)
        labels = {
            'nombre': 'Nombre de la Categoría',
            'habilitada': 'Categoría Activada/no Activada',
            'margproc': 'Margen/Porciento',
            'valormag': 'Valor del Margen Comercial CUP',       
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs= {
                    'class':'form-control',
                    'id':'nombre'
                }
            ),
            'habilitada': forms.CheckboxInput(
                attrs= {
                    'class':'form-control',
                    'id':'habilitada'
                }
            ),
            'margporc': forms.CheckboxInput(
                attrs= {
                    'class':'form-control',
                    'id':'margporc'
                }
            ),
            'valormag': forms.TextInput(
                attrs= {
                    'class':'form-control',
                    'id':'valormag'
                }
            )

        }
