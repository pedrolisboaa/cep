from django.shortcuts import render, HttpResponse
import requests
# Create your views here.

def index(request):
        
    if request.method == 'POST':
        
        cep = request.POST.get('cep')
        api_correio = f'https://cep.awesomeapi.com.br/json/{cep}'
        response = requests.get(api_correio)

        if response.status_code == 200:
            print('achei')
            endereco = response.json()
            conteudo = {
                'endereco':endereco
            }

            return render(request, 'index.html', conteudo) 
        else:
            texto = f'CEP {cep} não encontrado.'
            conteudo = {
                'texto': texto
            }
            return render(request, 'index.html', conteudo) 
        
        
    return render(request, 'index.html',)

    """
    api_url = 'https://cep.awesomeapi.com.br/json/71680385'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()

        conteudo = {
            'data': data
        }
        return render(request, 'index.html', conteudo)
    else:
        return render(request, 'index.html')
    """
