# Importa la libreria de formularios
from django import forms
# Importa la libreria de validacion
from django.core import validators

class FormArticle(forms.Form):
    #### TITULO #########
    title = forms.CharField(
        # required=False => Nos desconecta el campo 'title'. True=conectado
        # max_length => Max numero de caracteres. "No deja meter mas"
        label="Titulo",
        max_length=40,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Introduce Titulo del Articulo',
                'class':'titulo_form_article'
            }
        ),
        validators=[
            validators.MinLengthValidator(4, 'Pon un titulo mas descriptivo!'),
            validators.RegexValidator('^[A-Za-z0-9 .ñ-]*$','No se permiten simbolos', 'invalid_title')
        ]
    )
    #### CONTENIDO #########
    content = forms.CharField(
        label="Contenido",
        required=True,
        widget=forms.Textarea,
        validators = [
            validators.MaxLengthValidator(700, 'Texto de articulo demasiado largo solo 700 caracteres')
        ]
    )
    # Actualiza en widget de content
    content.widget.attrs.update({
        'placeholder':'Introduce Contenido del articulo',
        'class':'contenido_form_article',
        'id':'contenido_form'
    })
    #### ¿Publicado? (SELECT) #########
    public_options=[
        (1, 'Si'),
        (0, 'No')
    ]
    public=forms.TypedChoiceField(
        label="Publicado?",
        choices = public_options
    )