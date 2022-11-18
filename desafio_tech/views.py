from django.shortcuts import  render, HttpResponse
from desafio_tech.forms import MeuFormulario
from desafio_tech.gerar_senha import gerador_senha
from desafio_tech.models import Usuario
from django.views.generic import ListView, DetailView


def cadastro(request):
    if request.method == 'GET':
        form = MeuFormulario()
        context = {'form': form}
        return render(request, 'cadastrar.html', context=context)
    else:
        form = MeuFormulario(request.POST)

        if (form.is_valid()):
            

            if form.cleaned_data['senha'] == None:
                form.cleaned_data['senha'] = gerador_senha()
                post_senha = form.cleaned_data['senha']
                post_nome = form.cleaned_data['nome']
                post_nasc = form.cleaned_data['data_nascimento']
                novo_post = Usuario(nome=post_nome, senha=post_senha, data_nascimento=post_nasc)
                novo_post.save()
                print(post_senha)
                return HttpResponse(f'Usuário cadastrado com sucesso!, sua senha gerada foi: {post_senha}')
                
            else:
                post_nome = form.cleaned_data['nome']
                post_nasc = form.cleaned_data['data_nascimento']
                post_senha = form.cleaned_data['senha']
                print(post_senha)
                novo_post = Usuario(nome=post_nome, senha=post_senha, data_nascimento=post_nasc)
                novo_post.save()
                

    return render(request, 'homepage.html')


class Homepage(ListView):
    template_name = 'homepage.html'
    model = Usuario
    paginate_by = 5

    def get_queryset(self):
        text_nome = self.request.GET.get('text_nome')
        if text_nome:
            usuario = Usuario.objects.filter(nome__icontains=text_nome)

        else:
            usuario = Usuario.objects.all()
        return usuario
        