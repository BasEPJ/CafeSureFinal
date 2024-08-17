from django import forms
from .models import Cliente
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError



class ClienteForm(forms.ModelForm):
    confirmar_contrasenia = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Cliente
        fields = ['nombre_cliente', 'correo', 'contrasenia', 'puntos']
        widgets = {
            'contrasenia': forms.PasswordInput(),
        }

    def clean_correo(self):
        correo = self.cleaned_data.get('correo')
        EmailValidator()(correo)  # Validar que el correo tenga formato de correo electrónico

        if Cliente.objects.filter(correo=correo).exists():
            raise ValidationError('Este correo ya está registrado.')
        
        return correo

    def clean(self):
        cleaned_data = super().clean()
        contrasenia = cleaned_data.get("contrasenia")
        confirmar_contrasenia = cleaned_data.get("confirmar_contrasenia")

        if contrasenia and confirmar_contrasenia and contrasenia != confirmar_contrasenia:
            self.add_error('confirmar_contrasenia', 'Las contraseñas no coinciden.')

        return cleaned_data
    
class ModificarClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre_cliente', 'puntos']
    

