from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def calcular(request):
    if request.method == 'POST':
        numero1 = float(request.POST['Digite o custo do produto + frete'])
        #numero2 = float(request.POST['numero2'])
        numero2 = numero1 * 175 / 100
        resultado = numero1 + numero2  # Implemente o cálculo desejado
        taxa_servicos = resultado * 8.87 / 100
        custos = taxa_servicos + numero1
        marketing = resultado * 25 / 100
        lucro = resultado - custos - marketing


        numero1_format = f'R${numero1:.2f}'
        lucro_format = f'R${lucro:.2f}'
        custos_format = f'R${custos:.2f}'
        resultado_format = f'R${resultado:.2f}'
        marketing_format = f'R${marketing:.2f}'


        context = {
            'resultado_format': resultado_format,
            'custos_format': custos_format,
            'lucro_format': lucro_format,
            'marketing_format': marketing_format,
            'numero1_format': numero1_format,
        }

        return render(request, 'resultado.html', context)
