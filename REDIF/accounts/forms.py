from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from RedifApp.models import Usuario

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ["username","email",  "titulacao", "condicao", "password1", "password2"] 
        #adição do campo "titulaçao", como multipla escolha e "condicao"
