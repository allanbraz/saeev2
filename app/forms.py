from django import forms
from django.forms import inlineformset_factory

from .models import (
    Edificacoes, Ambientes,
)


class EdificacoesForm(forms.ModelForm):

    OPCOES_PRER = (
        ('SIM', 'SIM'),
        ('NÃO', 'NÃO'),
    )

    OPCOES_TERM = (
        ('NÃO', 'NÃO'),
        ('SIM', 'SIM'),
    )

    term = forms.ChoiceField(choices=OPCOES_TERM,
                                label='Todos os dados já foram preenchidos',
                                widget=forms.Select(attrs={'class': 'form-control'}))
    prgeral = forms.ChoiceField(choices=OPCOES_PRER, label='Pré-requisito geral: separação dos circuitos de iluminação e condicinamento de ar', widget=forms.Select(attrs={'class': 'form-control'}))
    prcond = forms.ChoiceField(choices=OPCOES_PRER, label='Pré-requisito específico: isolamento para dutos de ar',widget=forms.Select(attrs={'class': 'form-control'}))
    sg1 = forms.ChoiceField(choices=OPCOES_PRER,
                            label='Os circuitos presentes na instalação são protegidos por algum equipamento de diferencial residual (sejam dispositivos ou interruptores)    (Banheiros, copas e laboratorios) ',
                            widget=forms.Select(attrs={'class': 'form-control'}))
    sg2 = forms.ChoiceField(choices=OPCOES_PRER,
                            label='Todos os ambientes possuem separação dos circuitos de acordo com a natureza da carga (Iluminação, tomadas de uso geral ou específico)',
                            widget=forms.Select(attrs={'class': 'form-control'}))
    sg3 = forms.ChoiceField(choices=OPCOES_PRER,
                            label='O quadro de alimentação está em boas condições de uso (Sinais de oxidação e/ou fissuras na estanqueidade do quadro)',
                            widget=forms.Select(attrs={'class': 'form-control'}))
    sg4 = forms.ChoiceField(choices=OPCOES_PRER,
                            label='Existe no quadro a identificação dos circuitos que compõe a instalação',
                            widget=forms.Select(attrs={'class': 'form-control'}))
    sg5 = forms.ChoiceField(choices=OPCOES_PRER, label='Em caso de o quadro ser metálico, existe aterramento do mesmo',
                            widget=forms.Select(attrs={'class': 'form-control'}))
    sg6 = forms.ChoiceField(choices=OPCOES_PRER,
                            label='Existe no quadro diagramas esquemáticos da organização dos circuitos',
                            widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Edificacoes
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nomepre': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'short_description': forms.TextInput(
                attrs={
                    'class': 'form-control'
                    }
                ),
            'Data': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type' : 'date'
                }
            ),
            'numerodepisos': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'zb': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'apcob': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'atot': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'aenv': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'vtot': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'somaabertura': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'atotfachada': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'fsvidro': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'avs': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'ahs': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'ape': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'ucobncond': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'ucobcond': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'upar': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'abscob': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'absrev': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'paz': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'fspaz': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }

        labels = {
            'nome': 'Nome da edificação',
            'short_description': 'Descreva a edificação mediante a atividade desenvolvida',
            'Data': 'Data de início da avaliação',
            'numerodepisos': 'Número de pavimentos',
            'zb': 'Zona Bioclimática em que a edificação está localizada',
            'apcob':'Área de projeção da cobertura',
            'atot': 'Área total construída',
            'aenv':'Área de envoltoria',
            'vtot': 'Volume da edificação',
            'somaabertura': 'Soma das aberturas envidraçadas (opcional)',
            'atotfachada': 'Área total de fachada',
            'fsvidro': 'Fator solar dos vidros das aberturas',
            'avs': 'Ângulo vertical de sombreamento',
            'ahs': 'Ângulo horizontal de sombreamento',
            'ape': 'Área de projeção da edificação',
            'ucobncond': 'Transmitância térmica da cobertura (ambientes climatizados)',
            'ucobcond': 'Transmitância térmica da cobertura (ambientes não climatizados)',
            'upar': 'Transmitância térmica das paredes',
            'abscob': 'Absorvidade térmica da cobertura',
            'absrev': 'Absorvidade térmica do revestimento',
            'paz': 'Percentual de abertura zenital',
            'fspaz': 'Fator solar dos vidros da abertura zenital',
            'nomepre': 'Responsável pela avaliação',
        }


class AmbientesForm(forms.ModelForm):

    OPCOES_ATIV = (
        ('Armazém, Atacado - Material pequeno/leve', 'Armazém, Atacado - Material pequeno/leve'),
        ('Armazém, Atacado - Material médio/volumoso', 'Armazém, Atacado - Material médio/volumoso'),
        ('Átrio - por metro de altura-até 12,20 m de altura', 'Átrio - por metro de altura-até 12,20 m de altura'),
        ('Átrio - por metro de altura -acima de 12,20 m de altura',
         'Átrio - por metro de altura -acima de 12,20 m de altura'),
        ('Auditórios e Anfiteatros - Auditório', 'Auditórios e Anfiteatros - Auditório'),
        ('Auditórios e Anfiteatros - Centro de Convenções', 'Auditórios e Anfiteatros - Centro de Convenções'),
        ('Auditórios e Anfiteatros - Cinema', 'Auditórios e Anfiteatros - Cinema'),
        ('Auditórios e Anfiteatros - Teatro', 'Auditórios e Anfiteatros - Teatro'),
        ('Banco/Escritório - Área de atividades bancárias', 'Banco/Escritório - Área de atividades bancárias'),
        ('Banheiros', 'Banheiros'),
        ('Biblioteca - Área de arquivamento', 'Biblioteca - Área de arquivamento'),
        ('Biblioteca - Área de leitura', 'Biblioteca - Área de leitura'),
        ('Biblioteca - Área de estantes', 'Biblioteca - Área de estantes'),
        ('Casa de Máquinas', 'Casa de Máquinas'),
        ('Centro de Convenções - Espaço de exposições', 'Centro de Convenções - Espaço de exposições'),
        ('Circulação', 'Circulação'),
        ('Comércio - Área de vendas', 'Comércio - Área de vendas'),
        ('Comércio - Pátio de área comercial', 'Comércio - Pátio de área comercial'),
        ('Comércio - Provador', 'Comércio - Provador'),
        ('Cozinhas', 'Cozinhas'),
        ('Depósitos', 'Depósitos'),
        ('Dormitórios – Alojamentos', 'Dormitórios – Alojamentos'),
        ('Escadas', 'Escadas'),
        ('Escritório', 'Escritório'),
        ('Escritório – Planta livre', 'Escritório – Planta livre'),
        ('Garagem', 'Garagem'),
        ('Ginásio/Academia - Área de Ginástica', 'Ginásio/Academia - Área de Ginástica'),
        ('Ginásio/Academia - Arquibancada', 'Ginásio/Academia - Arquibancada'),
        ('Ginásio/Academia - Esportes de ringue', 'Ginásio/Academia - Esportes de ringue'),
        ('Ginásio/Academia - Quadra de esportes – classe 42', 'Ginásio/Academia - Quadra de esportes – classe 42'),
        ('Ginásio/Academia - Quadra de esportes – classe 33', 'Ginásio/Academia - Quadra de esportes – classe 33'),
        ('Ginásio/Academia - Quadra de esportes – classe 24', 'Ginásio/Academia - Quadra de esportes – classe 24'),
        ('Ginásio/Academia - Quadra de esportes – classe 15', 'Ginásio/Academia - Quadra de esportes – classe 15'),
        ('Hall de Entrada - Vestíbulo', 'Hall de Entrada - Vestíbulo'),
        ('Hall de Entrada - Vestíbulo- Cinemas', 'Hall de Entrada - Vestíbulo- Cinemas'),
        ('Hall de Entrada - Vestíbulo- Hotel', 'Hall de Entrada - Vestíbulo- Hotel'),
        ('Hall de Entrada - Vestíbulo - Salas de Espetáculos', 'Hall de Entrada - Vestíbulo - Salas de Espetáculos'),
        ('Hospital - Circulação ', 'Hospital - Circulação '),
        ('Hospital - Emergência ', 'Hospital - Emergência '),
        ('Hospital - Enfermaria', 'Hospital - Enfermaria'),
        ('Hospital - Exames/Tratamento ', 'Hospital - Exames/Tratamento '),
        ('Hospital - Farmácia ', 'Hospital - Farmácia '),
        ('Hospital - Fisioterapia ', 'Hospital - Fisioterapia '),
        ('Hospital - Sala de espera, estar ', 'Hospital - Sala de espera, estar '),
        ('Hospital - Radiologia ', 'Hospital - Radiologia '),
        ('Hospital - Recuperação ', 'Hospital - Recuperação '),
        ('Hospital - Sala de Enfermeiros ', 'Hospital - Sala de Enfermeiros '),
        ('Hospital - Sala de Operação ', 'Hospital - Sala de Operação '),
        ('Hospital - Quarto de pacientes ', 'Hospital - Quarto de pacientes '),
        ('Hospital - Suprimentos médicos ', 'Hospital - Suprimentos médicos '),
        ('Igreja, templo - Assentos ', 'Igreja, templo - Assentos '),
        ('Igreja, templo - Altar, Coro', 'Igreja, templo - Altar, Coro'),
        ('Igreja, templo - Sala de comunhão - nave', 'Igreja, templo - Sala de comunhão - nave'),
        ('Laboratórios - para Salas de Aula ', 'Laboratórios - para Salas de Aula '),
        ('Laboratórios - Médico/Ind./Pesq', 'Laboratórios - Médico/Ind./Pesq'),
        ('Lavanderia', 'Lavanderia'),
        ('Museu - Restauração ', 'Museu - Restauração '),
        ('Museu - Sala de exibição ', 'Museu - Sala de exibição '),
        ('Oficina – Seminário, cursos', 'Oficina – Seminário, cursos'),
        ('Oficina Mecânica', 'Oficina Mecânica'),
        ('Quartos de Hotel', 'Quartos de Hotel'),
        ('Refeitório', 'Refeitório'),
        ('Restaurante - salão', 'Restaurante - salão'),
        ('Restaurante - salão - Hotel', 'Restaurante - salão - Hotel'),
        ('Restaurante - salão - Lanchonete/Café', 'Restaurante - salão - Lanchonete/Café'),
        ('Restaurante - salão - Bar/Lazer', 'Restaurante - salão - Bar/Lazer'),
        ('Sala de Aula, Treinamento', 'Sala de Aula, Treinamento'),
        ('Sala de espera, convivência', 'Sala de espera, convivência'),
        ('Sala de Reuniões, Conferência, Multiuso', 'Sala de Reuniões, Conferência, Multiuso'),
        ('Vestiário', 'Vestiário'),
        ('Transportes - Área de bagagem', 'Transportes - Área de bagagem'),
        ('Transportes-Aeroporto – Pátio', 'Transportes-Aeroporto – Pátio'),
        ('Transportes-Assentos - Espera', 'Transportes-Assentos - Espera'),
        ('Transportes-Terminal - bilheteria', 'Transportes-Terminal - bilheteria'),

    )

    OPCOES_PREIL12 = (
        ('SIM', 'SIM'),
        ('NÃO', 'NÃO'),
    )
    OPCOES_NOTA = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
    )
    ativ = forms.ChoiceField(choices=OPCOES_ATIV, widget=forms.Select(attrs={'class': 'form-control'}))
    pril1 = forms.ChoiceField(choices=OPCOES_PREIL12, widget=forms.Select(attrs={'class': 'form-control'}))
    pril2 = forms.ChoiceField(choices=OPCOES_PREIL12, widget=forms.Select(attrs={'class': 'form-control'}))
    pril3 = forms.ChoiceField(choices=OPCOES_PREIL12, widget=forms.Select(attrs={'class': 'form-control'}))
    notaar = forms.ChoiceField(choices=OPCOES_NOTA, widget=forms.Select(attrs={'class': 'form-control'}))
    led = forms.ChoiceField(choices=OPCOES_PREIL12, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Ambientes
        fields = '__all__'
        widgets = {
            'nomeambiente': forms.TextInput(
                attrs={
                    'class': 'form-control'
                    }
                ),
            'areaambiente': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nlamp': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                    }
                ),
            'ptlamp': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                    }
                ),
            'nar': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'ptar': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'areaabertura': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


AmbientesFormSet = inlineformset_factory(
    Edificacoes, Ambientes, extra=1, form=AmbientesForm, can_delete=True, can_delete_extra=True,
)

