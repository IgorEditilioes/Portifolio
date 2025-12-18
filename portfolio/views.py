from django.shortcuts import render
from .models import Projeto
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    projetos = Projeto.objects.all()
    return render(request, 'index.html', {'projetos': projetos} )

def projeto_detalhes(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    return render(request, 'projetos_detalhes.html', {'projeto': projeto})