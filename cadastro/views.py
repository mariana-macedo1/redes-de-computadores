from django.shortcuts import render, redirect
from .models import Aluno

def index(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        curso = request.POST.get("curso")

        Aluno.objects.create(nome=nome,curso=curso)

        return redirect("index")
    
    alunos  = Aluno.objects.all().order_by("-id")

    return render(
        request,
        "cadastro/index.html",
        {"alunos": alunos}
)

