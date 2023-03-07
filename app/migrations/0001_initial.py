# Generated by Django 4.1.1 on 2023-02-19 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edificacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('short_description', models.TextField(max_length=100)),
                ('Data', models.DateField(blank=True, null=True)),
                ('numerodepisos', models.PositiveIntegerField(blank=True, null=True)),
                ('zb', models.PositiveIntegerField(blank=True, null=True)),
                ('apcob', models.FloatField(blank=True, null=True)),
                ('atot', models.FloatField(blank=True, null=True)),
                ('aenv', models.FloatField(blank=True, null=True)),
                ('vtot', models.FloatField(blank=True, null=True)),
                ('somaabertura', models.FloatField(blank=True, null=True)),
                ('atotfachada', models.FloatField(blank=True, null=True)),
                ('fsvidro', models.FloatField(blank=True, null=True)),
                ('avs', models.FloatField(blank=True, null=True)),
                ('ahs', models.FloatField(blank=True, null=True)),
                ('ape', models.FloatField(blank=True, null=True)),
                ('ucobncond', models.FloatField(blank=True, null=True)),
                ('ucobcond', models.FloatField(blank=True, null=True)),
                ('upar', models.FloatField(blank=True, null=True)),
                ('abscob', models.FloatField(blank=True, null=True)),
                ('absrev', models.FloatField(blank=True, null=True)),
                ('paz', models.FloatField(blank=True, null=True)),
                ('fspaz', models.FloatField(blank=True, null=True)),
                ('prgeral', models.CharField(blank=True, choices=[('SIM', 'SIM'), ('NÃO', 'NÃO')], max_length=55)),
                ('prcond', models.CharField(blank=True, choices=[('SIM', 'SIM'), ('NÃO', 'NÃO')], max_length=55)),
                ('potcond_total', models.FloatField(blank=True, editable=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ambientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeambiente', models.CharField(max_length=100)),
                ('areaambiente', models.FloatField(null=True)),
                ('nlamp', models.PositiveIntegerField()),
                ('ptlamp', models.DecimalField(decimal_places=2, max_digits=12)),
                ('nar', models.PositiveIntegerField()),
                ('ptar', models.DecimalField(decimal_places=2, max_digits=12)),
                ('notaar', models.CharField(max_length=2)),
                ('ativ', models.CharField(blank=True, choices=[('Armazém, Atacado - Material pequeno/leve', 'Armazém, Atacado - Material pequeno/leve'), ('Armazém, Atacado - Material médio/volumoso', 'Armazém, Atacado - Material médio/volumoso'), ('Átrio - por metro de altura-até 12,20 m de altura', 'Átrio - por metro de altura-até 12,20 m de altura'), ('Átrio - por metro de altura -acima de 12,20 m de altura', 'Átrio - por metro de altura - acima de 12,20 m de altura'), ('Auditórios e Anfiteatros - Auditório', 'Auditórios e Anfiteatros - Auditório'), ('Auditórios e Anfiteatros - Centro de Convenções', 'Auditórios e Anfiteatros - Centro de Convenções'), ('Auditórios e Anfiteatros - Cinema', 'Auditórios e Anfiteatros - Cinema'), ('Auditórios e Anfiteatros - Teatro', 'Auditórios e Anfiteatros - Teatro'), ('Banco/Escritório - Área de atividades bancárias', 'Banco / Escritório - Área de atividades bancárias'), ('Banheiros', 'Banheiros'), ('Biblioteca-Área de arquivamento', 'Biblioteca-Área de arquivamento'), ('Biblioteca-Área de leitura', 'Biblioteca-Área de leitura'), ('Biblioteca-Área de estantes', 'Biblioteca-Área de estantes'), ('Casa de Máquinas', 'Casa de Máquinas'), ('Centro de Convenções - Espaço de exposições', 'Centro de Convenções - Espaço de exposições'), ('Circulação', 'Circulação'), ('Comércio-Área de vendas', 'Comércio-Área de vendas'), ('Comércio-Pátio de área comercial', 'Comércio-Pátio de área comercial'), ('Comércio-Provador', 'Comércio-Provador'), ('Cozinhas', 'Cozinhas'), ('Depósitos', 'Depósitos'), ('Dormitórios – Alojamentos', 'Dormitórios – Alojamentos'), ('Escadas', 'Escadas'), ('Escritório', 'Escritório'), ('Escritório – Planta livre', 'Escritório – Planta livre'), ('Garagem', 'Garagem'), ('Ginásio/Academia - Área de Ginástica', 'Ginásio/Academia - Área de Ginástica'), ('Ginásio/Academia - Arquibancada', 'Ginásio/Academia - Arquibancada'), ('Ginásio/Academia - Esportes de ringue', 'Ginásio/Academia - Esportes de ringue'), ('Ginásio/Academia - Quadra de esportes – classe 42', 'Ginásio/Academia - Quadra de esportes – classe 42'), ('Ginásio/Academia - Quadra de esportes – classe 33', 'Ginásio/Academia - Quadra de esportes – classe 33'), ('Ginásio/Academia - Quadra de esportes – classe 24', 'Ginásio/Academia - Quadra de esportes – classe 24'), ('Ginásio/Academia - Quadra de esportes – classe 15', 'Ginásio/Academia - Quadra de esportes – classe 15'), ('Hall de Entrada - Vestíbulo- Cinemas', 'Hall de Entrada - Vestíbulo- Cinemas'), ('Hall de Entrada - Vestíbulo- Hotel', 'Hall de Entrada - Vestíbulo- Hotel'), ('Hall de Entrada - Vestíbulo - Salas de Espetáculos', 'Hall de Entrada - Vestíbulo - Salas de Espetáculos'), ('Hospital - Circulação ', 'Hospital - Circulação '), ('Hospital - Emergência ', 'Hospital - Emergência '), ('Hospital - Enfermaria', 'Hospital - Enfermaria'), ('Hospital - Exames/Tratamento ', 'Hospital - Exames/Tratamento '), ('Hospital - Farmácia ', 'Hospital - Farmácia '), ('Hospital - Fisioterapia ', 'Hospital - Fisioterapia '), ('Hospital - Sala de espera, estar ', 'Hospital - Sala de espera, estar '), ('Hospital - Radiologia ', 'Hospital - Radiologia '), ('Hospital - Recuperação ', 'Hospital - Recuperação '), ('Hospital - Sala de Enfermeiros ', 'Hospital - Sala de Enfermeiros '), ('Hospital - Sala de Operação ', 'Hospital - Sala de Operação '), ('Hospital - Quarto de pacientes ', 'Hospital - Quarto de pacientes '), ('Hospital - Suprimentos médicos ', 'Hospital - Suprimentos médicos '), ('Igreja, templo - Assentos ', 'Igreja, templo - Assentos '), ('Igreja, templo - Altar, Coro', 'Igreja, templo - Altar, Coro'), ('Igreja, templo-Sala de comunhão - nave', 'Igreja, templo-Sala de comunhão - nave'), ('Laboratórios - para Salas de Aula ', 'Laboratórios - para Salas de Aula '), ('Laboratórios - Médico/Ind./Pesq', 'Laboratórios - Médico/Ind./Pesq'), ('Lavanderia', 'Lavanderia'), ('Museu - Restauração ', 'Museu - Restauração '), ('Museu - Sala de exibição ', 'Museu - Sala de exibição '), ('Oficina – Seminário, cursos', 'Oficina – Seminário, cursos'), ('Oficina Mecânica', 'Oficina Mecânica'), ('Quartos de Hotel', 'Quartos de Hotel'), ('Refeitório', 'Refeitório'), ('Restaurante - salão-Hotel', 'Restaurante - salão-Hotel'), ('Restaurante - salão-Lanchonete/Café', 'Restaurante - salão-Lanchonete/Café'), ('Restaurante - salão-Bar/Lazer', 'Restaurante - salão-Bar/Lazer'), ('Sala de Aula, Treinamento', 'Sala de Aula, Treinamento'), ('Sala de espera, convivência', 'Sala de espera, convivência'), ('Sala de Reuniões, Conferência, Multiuso', 'Sala de Reuniões, Conferência, Multiuso'), ('Vestiário', 'Vestiário'), ('Transportes-Área de bagagem', 'Transportes-Área de bagagem'), ('Transportes-Aeroporto – Pátio', 'Transportes-Aeroporto – Pátio'), ('Transportes-Assentos - Espera', 'Transportes-Assentos - Espera'), ('Transportes-Terminal - bilheteria', 'Transportes-Terminal - bilheteria')], max_length=55)),
                ('pril1', models.CharField(blank=True, choices=[('SIM', 'SIM'), ('NÃO', 'NÃO')], max_length=55)),
                ('pril2', models.CharField(blank=True, choices=[('SIM', 'SIM'), ('NÃO', 'NÃO')], max_length=55)),
                ('pril3', models.CharField(blank=True, choices=[('SIM', 'SIM'), ('NÃO', 'NÃO'), ('NSP', 'NSP')], max_length=55)),
                ('potilum', models.FloatField(editable=False, null=True)),
                ('densilum', models.FloatField(editable=False, null=True)),
                ('eqvnota', models.PositiveIntegerField(default=1, editable=False)),
                ('potcond', models.FloatField(editable=False, null=True)),
                ('relacao_potencia', models.FloatField(editable=False, null=True)),
                ('edificacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ambiente_set', to='app.edificacoes')),
            ],
        ),
    ]
