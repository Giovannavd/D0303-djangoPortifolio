from django.shortcuts import render

# Create your views here.
def home(request):
    nome = 'Giovanna'
    conhecimentos = ['HTML', 'CSS', 'JavaScrips', 'Python', 'Django', 'Git','Tamborim', 'Dar Cambalhotas', 'Plantar bananeira']

# parâmetros: requisição, qual o template, quais os valores do template(escrito em linguagem de ovjeto: entre colxetes)
    return render(request, 'index.html', {'conhecimento': conhecimentos, 'nome': nome})
