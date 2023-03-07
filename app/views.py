from django.forms import inlineformset_factory
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.edit import (
    CreateView, UpdateView
)
from .forms import (
    EdificacoesForm, AmbientesForm, AmbientesFormSet
)
from .models import (
    Edificacoes,
    Ambientes
)

class EdificacoesInline():
    form_class = EdificacoesForm
    model = Edificacoes
    template_name = "addedif.html"

    def form_valid(self, form):
        named_formsets = self.get_named_formsets()
        if not all((x.is_valid() for x in named_formsets.values())):
            return self.render_to_response(self.get_context_data(form=form))

        self.object = form.save()

        # for every formset, attempt to find a specific formset save function
        # otherwise, just save.
        for name, formset in named_formsets.items():
            formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
            if formset_save_func is not None:
                formset_save_func(formset)
            else:
                data = []
                formset.save()
        return redirect(detalhes)

    def formset_ambientes_valid(self, formset):
        """
        Hook for custom formset saving.Useful if you have multiple formsets
        """
        ambientes = formset.save(commit=False)  # self.save_formset(formset, contact)
        # add this 2 lines, if you have can_delete=True parameter
        # set in inlineformset_factory func
        for obj in formset.deleted_objects:
            obj.delete()
        for ambiente in ambientes:
            ambiente.edificacoes = self.object
            ambiente.save()

class EdificacoesCreate(EdificacoesInline, CreateView):

    def get_context_data(self, **kwargs):
        ctx = super(EdificacoesCreate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        if self.request.method == "GET":
            return {
                'ambientes': AmbientesFormSet(prefix='ambientes'),
            }
        else:
            return {
                'ambientes': AmbientesFormSet(self.request.POST or None, self.request.FILES or None, prefix='ambientes'),
            }


class EdificacoesUpdate(EdificacoesInline, UpdateView):
    def get_context_data(self, **kwargs):
        ctx = super(EdificacoesUpdate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        return {
            'ambientes': AmbientesFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='ambientes', queryset=self.object.ambientes_set.all()),
        }

class EdificacoesDetailView(EdificacoesInline, DetailView):
    model = Edificacoes
    template_name = 'dashboard2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sg1'] = self.object.sg1
        context['sg2'] = self.object.sg2
        context['sg3'] = self.object.sg3
        context['sg4'] = self.object.sg4
        context['sg5'] = self.object.sg5
        context['sg6'] = self.object.sg6
        context['prespil1'] = self.object.prespil1
        context['prespil2'] = self.object.prespil2
        context['prespil3'] = self.object.prespil3
        context['prenv1'] = self.object.prenv1
        context['prenv2'] = self.object.prenv2
        context['potcond_total'] = self.object.potcond_total
        context['potilumg'] = self.object.potilumg
        contil = self.object.contil
        contcond = self.object.contcond
        contenv = self.object.contenv
        term = self.object.term
        ambientes = self.object.ambientes_set.all()


        sled = 0

        for ambiente in ambientes:
            if ambiente.led is not None:
                if ambiente.led == "SIM":
                    sled = 0 + sled
                else:
                    sled = sled + 1
            else:
                sled = 0

        context['sled'] = sled

        notailum = self.object.notailcorrigida
        notacond = self.object.notacondgeralcorrigida
        notaenv = self.object.notaiccorrigida

        notas_dict = {
            'A': 5,
            'B': 4,
            'C': 3,
            'D': 2,
            'E': 1
        }
        notacondinnum = notas_dict[notacond]
        context['notacondinnum'] = notacondinnum

        somaAB = 0
        somaCD = 0
        somaE = 0

        if notailum or notacond or notaenv == "E":
            somaE = somaE + 1
        elif notailum or notacond or notaenv == "D" or "C":
            somaCD = somaCD+1
        else:
            somaAB = somaAB+1

        context['somaE'] = somaE
        context['somaCD'] = somaCD
        context['somaAB'] = somaAB



        stts = "r"
        if term == "SIM":
            stts = "Cadastro finalizado"
        else:
            stts = "Cadastro em andamento"

        context['stts'] = stts

        pottot = 0

        if self.object.potilumg is not None:
            pottot = self.object.potilumg
            potilu = self.object.potilumg
        else:
            pottot = 1
            potilu = 0

        if self.object.potcond_total is not None:
            pottot = self.object.potcond_total + pottot
            potcond = self.object.potcond_total
        else:
            pottot = pottot
            potcond = 0

        if pottot == 0:
            relilu = 0
            relcond = 0
        else:
            relilu = int((potilu / pottot)*100)
            relcond = int((potcond / pottot) * 100)
        context['relilu'] = relilu
        context['relcond'] = relcond
        context['pottot'] = pottot


        soma = 0
        sg1l = ""
        sg2l = ""
        sg3l = ""
        sg4l = ""
        sg5l = ""
        sg6l = ""

        if self.object.sg1 == "SIM":
            soma = soma+1
            sg1l = "ATENDIDO"
        else:
            sg1l = "NÃO ATENDIDO"
        if self.object.sg2 == "SIM":
            soma = soma+1
            sg2l = "ATENDIDO"
        else:
            sg2l = "NÃO ATENDIDO"
        if self.object.sg3 == "SIM":
            soma = soma+1
            sg3l = "ATENDIDO"
        else:
            sg3l = "NÃO ATENDIDO"
        if self.object.sg4 == "SIM":
            soma = soma+1
            sg4l = "ATENDIDO"
        else:
            sg4l = "NÃO ATENDIDO"
        if self.object.sg5 == "SIM":
            soma = soma+1
            sg5l = "ATENDIDO"
        else:
            sg5l = "NÃO ATENDIDO"
        if self.object.sg6 == "SIM":
            soma = soma+1
            sg6l = "ATENDIDO"
        else:
            sg6l = "NÃO ATENDIDO"

        context['soma'] = soma
        context['sg1l'] = sg1l
        context['sg2l'] = sg2l
        context['sg3l'] = sg3l
        context['sg4l'] = sg4l
        context['sg5l'] = sg5l
        context['sg6l'] = sg6l

        notas_dict = {
            'A': 5,
            'B': 4,
            'C': 3,
            'D': 2,
            'E': 1
        }

        PT = self.object.valornotageral
        contil = int((contil/PT)*100)
        contcond = int((contcond/PT)*100)
        contenv = int((contenv/PT) * 100)

        context['contil'] = contil
        context['contcond'] = contcond
        context['contenv'] = contenv
        return context


class EdificacoesList(ListView):
    model = Edificacoes
    template_name = "index.html"
    context_object_name = "edificacoes"




def delete_ambientes(request, pk):
    try:
        ambientes = Ambientes.objects.get(id=pk)
    except Ambientes.DoesNotExist:
        messages.success(
            request, 'O objeto não existe'
        )
        return redirect('update_edificacoes', pk=ambientes.edificacoes.id)

    ambientes.delete()
    messages.success(
            request, 'Ambiente deletado com sucesso'
    )
    return redirect('update_edificacoes', pk=ambientes.edificacoes.id)

def edificacoes_delete(request, pk):
    edificacoes = Edificacoes.objects.get(id=pk)
    edificacoes.delete()

    return redirect(detalhes)



# Create your views here.
def home(request):
    return render(request,'newlg.html')

def detalhes(request):
        username = request.user.username
        edificacoes = Edificacoes.objects.exclude(id=None).all()
        context = {
            'edificacoes': edificacoes,
            'username': username
        }

        return render(request,'index.html', context)

#Inserção dos dados dos usuários no banco
def store(request):
    data = {}
    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'Senha e confirmação de senha diferentes!'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        user.user_permissions.add(27)
        data['msg'] = 'Usuário cadastrado com sucesso!'
        data['class'] = 'alert-success'
    return render(request,'register.html',data)



#Formulário do painel de login
#Processa o login
def dologin(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/dashboard/')
    else:
        data['msg'] = 'Usuário ou Senha incorretos.'
        data['class'] = 'alert-danger'
        return render(request,'login.html',data)

#Página inicial do dashboard
def dashboard(request):
    username = request.user.username
    edificacoes = Edificacoes.objects.all()
    num_edificacoes = Edificacoes.objects.count()
    somaTERN = edificacoes.filter(term__in=["NÃO"]).count()
    somaTERS = edificacoes.filter(term__in=["SIM"]).count()
    somaA = edificacoes.filter(notageral__in=["A"]).count()
    somaB = edificacoes.filter(notageral__in=["B"]).count()
    somaC = edificacoes.filter(notageral__in=["C"]).count()
    somaD = edificacoes.filter(notageral__in=["D"]).count()
    somaE = edificacoes.filter(notageral__in=["E"]).count()
    somasg1 = edificacoes.filter(sg1__in=["SIM"]).count()
    somasg2 = edificacoes.filter(sg2__in=["SIM"]).count()
    somasg3 = edificacoes.filter(sg3__in=["SIM"]).count()
    somasg4 = edificacoes.filter(sg4__in=["SIM"]).count()
    somasg5 = edificacoes.filter(sg5__in=["SIM"]).count()
    somasg6 = edificacoes.filter(sg6__in=["SIM"]).count()

    ss = 0
    for edificacao in edificacoes:
        for ambiente in edificacao.ambientes_set.all():
            if ambiente.led == "NÃO":
                ss = ss + 1
            else:
                ss = ss

    if num_edificacoes is not None:
        nume = num_edificacoes
    else:
        nume = 1

    if num_edificacoes == 0:
        nume = 1
    pa = int((somaA/nume)*100)
    pb = int((somaB/nume)*100)
    pc = int((somaC/nume)*100)
    pd = int((somaD/nume)*100)
    pe = int((somaE/nume)*100)
    pterm = int((somaTERS/nume)*100)

    ne = 0
    ndc = 0
    nba = 0

    for edif in edificacoes:
        if edif.notageral == 'E':
            ne = 1 + ne
        elif edif.notageral == 'C' or edif.notageral == 'D':
            ndc = 1 + ndc
        else:
            nba = 1 + nba

    context = {
        'edificacoes': edificacoes,
        'num_edificacoes': num_edificacoes,
        'somaTERN': somaTERN,
        'somaTERS': somaTERS,
        'pa': pa,
        'pb': pb,
        'pc': pc,
        'pd': pd,
        'pe': pe,
        'somasg1': somasg1,
        'somasg2': somasg2,
        'somasg3': somasg3,
        'somasg4': somasg4,
        'somasg5': somasg5,
        'somasg6': somasg6,
        'username': username,
        'ne': ne,
        'ndc': ndc,
        'nba': nba,
        'pterm': pterm,
        'somaA': somaA,
        'somaB': somaB,
        'somaC': somaC,
        'somaD': somaD,
        'somaE': somaE,
        'ss': ss,
    }
    return render(request, 'dashboard.html', context)

#Logout do sistema
def logouts(request):
    logout(request)
    return redirect('/login/')

#Alterar a senha
def changePassword(request):
    user = User.objects.get(email=request.user.email)
    user.set_password('troca123')
    user.save()
    logout(request)
    return redirect('/login/')

