from django.shortcuts import render
import conexao
c = conexao.conectar()

# Create your views here.
def index(request):
    with c.cursor() as selecionar:
        sql = 'select * from tbcliente'
        selecionar.execute(sql)
        dados = selecionar.fetchall()
    return render(request, 'cliente/index.html', {'cliente' : dados})

def insere_cliente(request):
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')
    telefone = request.POST.get('telefone')
    data_nasc = request.POST.get('data_nasc')
    email = request.POST.get('email')

    with c.cursor() as inserir:
        sql = 'insert into tbcliente(nome, senha, data_nasc, telefone, email) values(%s, %s, %s, %s, %s)'
        inserir.execute(sql,(nome, senha, data_nasc , telefone, email))
        c.commit()
    return render(request, 'cliente/form_cliente.html')

def formulario(request):
    return render(request, 'cliente/form_cliente.html')

def home(request):
    return render(request, '../../home/templates/home/index.html')