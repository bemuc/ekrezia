from django.shortcuts import render
from .models import *
from .forms import *
from .filters import *
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def loginPage(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')

        user = authenticate(request, username=user_name, password=pass_word)

        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
            messages.info(request,'username or password incorect')
            return render(request,'loging/login.html')

    return render(request,'loging/login.html')

def logout_page(request):
    logout(request)
    return redirect('login')

# def login(request):
#     return render(request,'loging/login.html')

def homepage(request):
    return render(request,'homepage/home.html')

def amasaka(request):
    amasaka = amsakaramentu.objects.filter(status ='actif')
    myfilter = amasakaFilter(request.GET, queryset=amasaka)
    amasaka = myfilter.qs
    context = {
        'amasaka':amasaka, 
        'myfilter':myfilter,
        # 'name':poste,
        }
    # return render(request,'gestionclient/Clientts/listeClient.html',context)
    return render(request,'homepage/amasaka.html',context)


def ajoutamasaka(request):
    # amasaka = amsakaramentu.objects.filter(status ='actif')
    if request.method == 'POST':
        form = amasakaramentuForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Enregistrement reussi')
            return redirect('ajoutamasaka')
        else:
            messages.error(request, f'Enregistrement non reussi')
    else:
        form = amasakaramentuForm()
    
    context = {
        'form':form,
        'titre': "Ajouter",
        # 'name':poste,
    }
    # return render(request,'gestionclient/Clientts/ajoutClient.html',context)
    return render(request,'homepage/ajoutMasaka.html',context)


def voiramasaka(request,pk):
    amasaka = amsakaramentu.objects.get(id = pk)
    
    context = {
        # 'form':form,  
        'amasaka':amasaka,
        # 'titre': "Ajouter",
        # 'name':poste,
    }
    # return render(request,'gestionclient/Clientts/ajoutClient.html',context)
    return render(request,'homepage/voiramasaka.html',context)

def modifieramasaka(request,pk):
    amasaka = amsakaramentu.objects.get(id = pk)
    
    form = amasakaramentuForm(instance=amasaka)
    if request.method == 'POST':
        form = amasakaramentuForm(request.POST,instance=amasaka)
        if form.is_valid():
            form.save()
            return redirect ('voiramasaka',pk=pk)
    
    context = {
        'form':form,
        'titre':"Modifier",
        # 'name':poste,
        }

    # return render(request,'gestionclient/Clientts/ajoutClient.html',context)
    
    # context = {
    #     # 'form':form,  
    #     'amasaka':amasaka,
    #     # 'titre': "Ajouter",
    #     # 'name':poste,
    # }
    # return render(request,'gestionclient/Clientts/ajoutClient.html',context)
    return render(request,'homepage/ajoutMasaka.html',context)
