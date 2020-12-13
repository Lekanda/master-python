from django import forms

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
        )
    )
    #### CONTENIDO #########
    content = forms.CharField(
        label="Contenido",
        max_length=250,
        required=True,
        widget=forms.Textarea
    )
    # Actualiza en widget de content
    content.widget.attrs.update({
        'placeholder':'Introduce Contenido del Articulo',
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