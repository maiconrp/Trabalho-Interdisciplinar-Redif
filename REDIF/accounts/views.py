from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from accounts.forms import RegisterUserForm

# Create your views here.
def registrarUsuario(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            #troco redirect por HttpResponseRedirect
            return HttpResponseRedirect("/accounts/login")
    else:
        form = RegisterUserForm()

    context = {
        'form' : form
    }    

    return render(request, 'registration/registrar.html',context=context)