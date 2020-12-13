from django import forms

class FormArticle(forms.Form):
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
        )
    )
    content = forms.CharField(
        label="Contenido",
        max_length=250,
        required=True,
        widget=forms.Textarea(
            attrs={
                'placeholder':'Introduce Contenido del Articulo',
                'class':'contenido_form_article'
            }
        )
    )
    






    public_options=[
        (1, 'Si'),
        (0, 'No')
    ]
    public=forms.TypedChoiceField(
        label="Publicado?",
        choices = public_options
    )