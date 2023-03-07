from django.db import models
import numpy as np
# Create your models here.

class Edificacoes(models.Model):

    OPCOES_PRER = (
        ('SIM', 'SIM'),
        ('NÃO', 'NÃO'),
    )

    OPCOES_TERM = (
        ('NÃO', 'NÃO'),
        ('SIM', 'SIM'),
    )

    term = models.CharField(max_length=3, blank=True, choices=OPCOES_TERM)
    nome = models.CharField(max_length=150)
    nomepre = models.CharField(max_length=150, null=True)
    short_description = models.TextField(max_length=100)
    Data = models.DateField(null=True, blank=True)
    numerodepisos = models.PositiveIntegerField(null=True, blank=True)
    zb = models.PositiveIntegerField(null=True, blank=True)
    apcob = models.FloatField(null=True, blank=True)
    atot = models.FloatField(null=True, blank=True)
    aenv = models.FloatField(null=True, blank=True)
    vtot = models.FloatField(null=True, blank=True)
    somaabertura = models.FloatField(null=True, blank=True)
    atotfachada = models.FloatField(null=True, blank=True)
    fsvidro = models.FloatField(null=True, blank=True)
    avs = models.FloatField(null=True, blank=True)
    ahs = models.FloatField(null=True, blank=True)
    ape = models.FloatField(null=True, blank=True)
    ucobncond = models.FloatField(null=True, blank=True)
    ucobcond = models.FloatField(null=True, blank=True)
    upar = models.FloatField(null=True, blank=True)
    abscob = models.FloatField(null=True, blank=True)
    absrev = models.FloatField(null=True, blank=True)
    paz = models.FloatField(null=True, blank=True)
    fspaz = models.FloatField(null=True, blank=True)
    prgeral = models.CharField(max_length=3, blank=True, choices=OPCOES_PRER)
    prcond = models.CharField(max_length=3, blank=True, choices=OPCOES_PRER)
    potcond_total = models.FloatField(null=True, editable=False, blank=True)
    calcnotacond = models.FloatField(null=True, editable=False, blank=True)
    notacondgeral = models.CharField(max_length=1, null=True, editable=False, blank=True)
    notacondgeralcorrigida = models.CharField(max_length=1, null=True, editable=False, blank=True)
    icenv = models.FloatField(null=True, editable=False, blank=True)
    icmax = models.FloatField(null=True, editable=False, blank=True)
    icmin = models.FloatField(null=True, editable=False, blank=True)
    notaic = models.CharField(max_length=1, null=True, editable=False, blank=True)
    notaiccorrigida = models.CharField(max_length=1, null=True, editable=False, blank=True)
    somacol1 = models.FloatField(null=True, editable=False, blank=True)
    somacol2 = models.FloatField(null=True, editable=False, blank=True)
    somacol3 = models.FloatField(null=True, editable=False, blank=True)
    somacol4 = models.FloatField(null=True, editable=False, blank=True)
    potilumg = models.FloatField(null=True, editable=False, blank=True)
    calcnotail = models.CharField(max_length=1, null=True, editable=False, blank=True)
    somapril1 = models.FloatField(null=True, editable=False, blank=True)
    somapril2 = models.FloatField(null=True, editable=False, blank=True)
    somapril3 = models.FloatField(null=True, editable=False, blank=True)
    notailcorrigida = models.CharField(max_length=1, null=True, editable=False, blank=True)
    autotal = models.FloatField(null=True, editable=False, blank=True)
    actotal = models.FloatField(null=True, editable=False, blank=True)
    notageral = models.CharField(max_length=1, null=True, editable=False, blank=True)
    sg1 = models.CharField(max_length=3, blank=True, choices=OPCOES_PRER)
    sg2 = models.CharField(max_length=3, blank=True, choices=OPCOES_PRER)
    sg3 = models.CharField(max_length=3, blank=True, choices=OPCOES_PRER)
    sg4 = models.CharField(max_length=3, blank=True, choices=OPCOES_PRER)
    sg5 = models.CharField(max_length=3, blank=True, choices=OPCOES_PRER)
    sg6 = models.CharField(max_length=3, blank=True, choices=OPCOES_PRER)
    prespil1 = models.CharField(max_length=3, blank=True, editable=False)
    prespil2 = models.CharField(max_length=3, blank=True, editable=False)
    prespil3 = models.CharField(max_length=3, blank=True, editable=False)
    prenv1 = models.CharField(max_length=3, blank=True, editable=False)
    prenv2 = models.CharField(max_length=3, blank=True, editable=False)
    prenv3 = models.CharField(max_length=3, blank=True, editable=False)
    valornotageral = models.FloatField(null=True, editable=False, blank=True)
    contil = models.FloatField(null=True, editable=False, blank=True)
    contcond = models.FloatField(null=True, editable=False, blank=True)
    contenv = models.FloatField(null=True, editable=False, blank=True)
    somasg = models.PositiveIntegerField(null=True, blank=True, editable=False)
    somareq = models.PositiveIntegerField(null=True, blank=True, editable=False)

#------------------------------- FUNÇÕES REFERENTES A EMVOLTÓRIA ----------------------------------------------
    def __str__(self):
        return self.nome

    def __iter__(self):
        return iter(self.nome)

    def save(self, *args, **kwargs):
        self.icenv = self.calcular_ICenv()
        self.icmax = self.calcular_ICmax()
        self.icmin = self.calcular_ICmin()
        self.notaic = self.calcular_I()
        self.notacondgeralcorrigida = self.corrigircond()
        self.notaiccorrigida = self.corrigirenv()
        self.calcnotail = self.calcularnotailum()
        self.notailcorrigida = self.calcularnotailumcorrigida()
        self.notageral = self.calcularnotageral()
        super(Edificacoes, self).save(*args, **kwargs)

    def calcular_ICenv(self):
        if self.apcob is not None:
            zb = self.zb
        else:
            zb = 1
        if self.apcob is not None and self.atot is not None:
            FA = (self.apcob / self.atot)
        else:
            FA = 1
        if self.atotfachada is not None and self.vtot is not None:
            FF = self.atotfachada / self.vtot
        else:
            FF = 1
        if self.somaabertura is not None and self.atot is not None:
            PAFT = (self.somaabertura / self.atot)
        else:
            PAFT = 1
        if self.fsvidro is not None:
            FS = self.fsvidro
        else:
            FS = 0
        if self.avs is not None:
            AVS = self.avs
        else:
            AVS = 0
        if self.ahs is not None:
            AVS = self.ahs
        else:
            AHS = 0

        if self.ape is not None:
            self.ape = self.ape
        else:
            self.ape = 0

        #ZONA BIOCLIMÁTICA 1
        if zb == 1 and self.ape <= 500:
            #LIMITES PARA O FATOR DE FORMA
            if FF > 0.6:
                FF = 0.6

            ICenv = (-43.0 * FA) - (316.62 * FF) + (16.83 * PAFT) + (7.39 * FS) - (0.20 * AVS) + (0.20 * AHS) + (
                        132.5 * FA / FF) - (77.0 * FA * FF) - (0.92 * FF * PAFT * AHS) + 182.66
        if zb == 1 and self.ape > 500:
            #LIMITES PARA O FATOR DE FORMA
            if FF < 0.17:
                FF = 0.17

            ICenv = 10.47 * FA + 298.74 * FF + 38.41 * PAFT - 1.11 * FS - 0.11 * AVS + 0.24 * AHS - 0.54 * PAFT * AHS + 47.53

        # ZONA BIOCLIMÁTICA 2 e 3
        if (zb == 2 or 3) and self.ape <= 500:
            if FF > 0.7:
                FF = 0.7
            ICenv = -175.30 * FA - 212.79 * FF + 21.86 * PAFT + 5.59 * FS - 0.19 * AVS + 0.15 * AHS + 275.19 * FA / FF + (
                    213.35 * FA * FF) - 0.04 * PAFT * FS * AVS - 0.45 * PAFT * AHS + 190.42

        if (zb == 2 or 3) and self.ape > 500:
            if FF<0.15:
                FF = 0.15

            ICenv = -14.14 * FA - 113.94 * FF + 50.82 * PAFT + 4.86 * FS - 0.32 * AVS + 0.26 * AHS - 35.75 / FF - 0.54 * PAFT * AHS + 277.98

        # ZONA BIOCLIMÁTICA 4 e 5
        if (zb == 4 or 5) and self.ape <= 500:
            if FF>0.75:
                FF = 0.75

            ICenv = 105.39 * FA - 207.12 * FF + 4.61 * PAFT + 8.08 * FS - 0.31 * AVS - 0.07 * AHS - 82.34 * FA * FF + 3.45 * PAFT * FS - 0.005 * PAFT * FS * AVS * AHS + 171.27

        if (zb == 4 or 5) and self.ape>500:
            ICenv = 511.12 * FA + 0.92 * FF - 95.71 * PAFT - 99.79 * FS - 0.52 * AVS - 0.29 * AHS - 380.83 * FA * FF + 4.27 / FF + 729.20 * PAFT * FS + 77.15

        # ZONA BIOCLIMÁTICA 7
        if zb == 7 and self.ape <= 500:
            if FF>0.6:
                FF = 0.6
            ICenv = 32.62 * FA - 580.03 * FF - 8.59 * PAFT + 18.48 * FS - 0.62 * AVS - 0.47 * AHS + 200.0 * FA / FF - 192.5 * FA * FF + 70.22 * FF * PAFT - 0.55 * PAFT * AHS + 318.65

        if zb == 7 and self.ape > 500:
            if FF<0.17:
                FF = 0.17
            ICenv = -69.48 * FA + 1347.78 * FF + 37.74 * PAFT + 3.03 * FS - 0.13 * AVS - 0.19 * AHS + 19.25 / FF + 0.04 * AHS / (
                        PAFT * FS) - 306.35

        # ZONA BIOCLIMÁTICA 6 e 8
        if (zb == 6 or 8) and self.ape <= 500:
            if FF>0.48:
                FF = 0.48
            ICenv = 454.47 * FA - 1641.37 * FF + 33.47 * PAFT + 7.06 * FS + 0.31 * AVS - 0.29 * AHS - 1.27 * PAFT * AVS + 0.33 * PAFT * AHS + 718

        if (zb == 6 or 8) and self.ape > 500:
            if FF<0.17:
                FF = 0.17
            ICenv = -160.36 * FA + 1277.29 * FF - 19.21 * PAFT + 2.95 * FS - 0.36 * AVS - 0.16 * AHS + 290.25 * FF * PAFT + 0.01 * PAFT * AVS * AHS - 120.58

        return ICenv

    def calcular_ICmax(self):
        zb = self.zb
        if self.apcob is not None and self.atot is not None:
            FA = (self.apcob / self.atot)
        else:
            FA = 1
        if self.atotfachada is not None and self.vtot is not None:
            FF = self.atotfachada / self.vtot
        else:
            FF = 1
        PAFT = 0.6
        FS = 0.61
        AVS = 0
        AHS = 0

        #ZONA BIOCLIMÁTICA 1
        if zb == 1 and self.ape <= 500:
            #LIMITES PARA O FATOR DE FORMA
            if FF>0.6:
                FF = 0.6

            ICenv = (-43.0 * FA) - (316.62 * FF) + (16.83 * PAFT) + (7.39 * FS) - (0.20 * AVS) + (0.20 * AHS) + (
                        132.5 * FA / FF) - (77.0 * FA * FF) - (0.92 * FF * PAFT * AHS) + 182.66
        if zb == 1 and self.ape > 500:
            #LIMITES PARA O FATOR DE FORMA
            if FF < 0.17:
                FF = 0.17

            ICenv = 10.47 * FA + 298.74 * FF + 38.41 * PAFT - 1.11 * FS - 0.11 * AVS + 0.24 * AHS - 0.54 * PAFT * AHS + 47.53

        # ZONA BIOCLIMÁTICA 2 e 3
        if (zb == 2 or 3) and self.ape <= 500:
            if FF > 0.7:
                FF = 0.7
            ICenv = -175.30 * FA - 212.79 * FF + 21.86 * PAFT + 5.59 * FS - 0.19 * AVS + 0.15 * AHS + 275.19 * FA / FF + (
                    213.35 * FA * FF) - 0.04 * PAFT * FS * AVS - 0.45 * PAFT * AHS + 190.42

        if (zb == 2 or 3) and self.ape > 500:
            if FF<0.15:
                FF = 0.15

            ICenv = -14.14 * FA - 113.94 * FF + 50.82 * PAFT + 4.86 * FS - 0.32 * AVS + 0.26 * AHS - 35.75 / FF - 0.54 * PAFT * AHS + 277.98

        # ZONA BIOCLIMÁTICA 4 e 5
        if (zb == 4 or 5) and self.ape <= 500:
            if FF>0.75:
                FF = 0.75

            ICenv = 105.39 * FA - 207.12 * FF + 4.61 * PAFT + 8.08 * FS - 0.31 * AVS - 0.07 * AHS - 82.34 * FA * FF + 3.45 * PAFT * FS - 0.005 * PAFT * FS * AVS * AHS + 171.27

        if (zb == 4 or 5) and self.ape>500:
            ICenv = 511.12 * FA + 0.92 * FF - 95.71 * PAFT - 99.79 * FS - 0.52 * AVS - 0.29 * AHS - 380.83 * FA * FF + 4.27 / FF + 729.20 * PAFT * FS + 77.15

        # ZONA BIOCLIMÁTICA 7
        if zb == 7 and self.ape <= 500:
            if FF>0.6:
                FF = 0.6
            ICenv = 32.62 * FA - 580.03 * FF - 8.59 * PAFT + 18.48 * FS - 0.62 * AVS - 0.47 * AHS + 200.0 * FA / FF - 192.5 * FA * FF + 70.22 * FF * PAFT - 0.55 * PAFT * AHS + 318.65

        if zb == 7 and self.ape > 500:
            if FF<0.17:
                FF = 0.17
            ICenv = -69.48 * FA + 1347.78 * FF + 37.74 * PAFT + 3.03 * FS - 0.13 * AVS - 0.19 * AHS + 19.25 / FF + 0.04 * AHS / (
                        PAFT * FS) - 306.35

        # ZONA BIOCLIMÁTICA 6 e 8
        if (zb == 6 or 8) and self.ape <= 500:
            if FF>0.48:
                FF = 0.48
            ICenv = 454.47 * FA - 1641.37 * FF + 33.47 * PAFT + 7.06 * FS + 0.31 * AVS - 0.29 * AHS - 1.27 * PAFT * AVS + 0.33 * PAFT * AHS + 718

        if (zb == 6 or 8) and self.ape > 500:
            if FF<0.17:
                FF = 0.17
            ICenv = -160.36 * FA + 1277.29 * FF - 19.21 * PAFT + 2.95 * FS - 0.36 * AVS - 0.16 * AHS + 290.25 * FF * PAFT + 0.01 * PAFT * AVS * AHS - 120.58

        return ICenv

    def calcular_ICmin(self):
        zb = self.zb
        if self.apcob is not None and self.atot is not None:
            FA = (self.apcob / self.atot)
        else:
            FA = 1
        if self.atotfachada is not None and self.vtot is not None:
            FF = self.atotfachada / self.vtot
        else:
            FF = 1
        PAFT = 0.05
        FS = 0.87
        AVS = 0
        AHS = 0

        #ZONA BIOCLIMÁTICA 1
        if zb == 1 and self.ape <= 500:
            #LIMITES PARA O FATOR DE FORMA
            if FF>0.6:
                FF = 0.6

            ICenv = (-43.0 * FA) - (316.62 * FF) + (16.83 * PAFT) + (7.39 * FS) - (0.20 * AVS) + (0.20 * AHS) + (
                        132.5 * FA / FF) - (77.0 * FA * FF) - (0.92 * FF * PAFT * AHS) + 182.66
        if zb == 1 and self.ape > 500:
            #LIMITES PARA O FATOR DE FORMA
            if FF < 0.17:
                FF = 0.17

            ICenv = 10.47 * FA + 298.74 * FF + 38.41 * PAFT - 1.11 * FS - 0.11 * AVS + 0.24 * AHS - 0.54 * PAFT * AHS + 47.53

        # ZONA BIOCLIMÁTICA 2 e 3
        if (zb == 2 or 3) and self.ape <= 500:
            if FF > 0.7:
                FF = 0.7
            ICenv = -175.30 * FA - 212.79 * FF + 21.86 * PAFT + 5.59 * FS - 0.19 * AVS + 0.15 * AHS + 275.19 * FA / FF + (
                    213.35 * FA * FF) - 0.04 * PAFT * FS * AVS - 0.45 * PAFT * AHS + 190.42

        if (zb == 2 or 3) and self.ape > 500:
            if FF<0.15:
                FF = 0.15

            ICenv = -14.14 * FA - 113.94 * FF + 50.82 * PAFT + 4.86 * FS - 0.32 * AVS + 0.26 * AHS - 35.75 / FF - 0.54 * PAFT * AHS + 277.98

        # ZONA BIOCLIMÁTICA 4 e 5
        if (zb == 4 or 5) and self.ape <= 500:
            if FF>0.75:
                FF = 0.75

            ICenv = 105.39 * FA - 207.12 * FF + 4.61 * PAFT + 8.08 * FS - 0.31 * AVS - 0.07 * AHS - 82.34 * FA * FF + 3.45 * PAFT * FS - 0.005 * PAFT * FS * AVS * AHS + 171.27

        if (zb == 4 or 5) and self.ape>500:
            ICenv = 511.12 * FA + 0.92 * FF - 95.71 * PAFT - 99.79 * FS - 0.52 * AVS - 0.29 * AHS - 380.83 * FA * FF + 4.27 / FF + 729.20 * PAFT * FS + 77.15

        # ZONA BIOCLIMÁTICA 7
        if zb == 7 and self.ape <= 500:
            if FF>0.6:
                FF = 0.6
            ICenv = 32.62 * FA - 580.03 * FF - 8.59 * PAFT + 18.48 * FS - 0.62 * AVS - 0.47 * AHS + 200.0 * FA / FF - 192.5 * FA * FF + 70.22 * FF * PAFT - 0.55 * PAFT * AHS + 318.65

        if zb == 7 and self.ape > 500:
            if FF<0.17:
                FF = 0.17
            ICenv = -69.48 * FA + 1347.78 * FF + 37.74 * PAFT + 3.03 * FS - 0.13 * AVS - 0.19 * AHS + 19.25 / FF + 0.04 * AHS / (
                        PAFT * FS) - 306.35

        # ZONA BIOCLIMÁTICA 6 e 8
        if (zb == 6 or 8) and self.ape <= 500:
            if FF>0.48:
                FF = 0.48
            ICenv = 454.47 * FA - 1641.37 * FF + 33.47 * PAFT + 7.06 * FS + 0.31 * AVS - 0.29 * AHS - 1.27 * PAFT * AVS + 0.33 * PAFT * AHS + 718

        if (zb == 6 or 8) and self.ape > 500:
            if FF<0.17:
                FF = 0.17
            ICenv = -160.36 * FA + 1277.29 * FF - 19.21 * PAFT + 2.95 * FS - 0.36 * AVS - 0.16 * AHS + 290.25 * FF * PAFT + 0.01 * PAFT * AVS * AHS - 120.58

        return ICenv

    def calcular_I(self):
        icmax = self.icmax
        icmin = self.icmin
        i = (icmax-icmin)/4
        nota = "R"

        if self.icenv < (icmax-3*i):
            nota = "A"
        elif self.icenv < (icmax-2*i):
            nota = "B"
        elif self.icenv < (icmax-i):
            nota = "C"
        elif self.icenv < icmax:
            nota = "D"
        else:
            nota = "E"

        return nota


    def corrigirenv(self):
        nota = self.notaic
        zb = self.zb
        prenv1 = "r"
        prenv2 = "r"
        prenv3 = "r"

        if self.ucobncond is not None:
            ucobncond = self.ucobncond
        else:
            ucobncond = 5
        if self.ucobcond is not None:
            ucobcond = self.ucobcond
        else:
            ucobcond = 5
        if self.upar is not None:
            upar = self.upar
        else:
            upar = 5
        if self.abscob is not None:
            abscob = self.abscob
        else:
            abscob = 5
        if self.absrev is not None:
            absrev = self.absrev
        else:
            absrev = 5

        notac1 = "R"
    #Síntese das exigências para transmitância térmica de cobertura para os diferentes níveis de eficiência e Zonas Bioclimáticas
        if zb == 1 or 2:
            if ucobcond < 0.5 and ucobncond < 1:
                if nota == "A":
                    notac1 = nota
                    prenv1 = "SIM"
                else:
                    notac1 = nota
                    prenv1 = "SIM"
            elif ucobcond < 1 and ucobncond < 1.5:
                if nota == "A":
                    notac1 = "B"
                    prenv1 = "NÃO"
                else:
                    nota = nota
                    prenv1 = "NÃO"
            elif ucobcond < 2 and ucobncond < 2:
                if nota == "A" or "B":
                    notac1 = "C"
                    prenv1 = "NÃO"
                else:
                    notac1 = nota
                    prenv1 = "NÃO"
            else:
                notac1 = "E"
                prenv1 = "NÃO"
        if zb == 3 or 8:
            if ucobcond < 1 and ucobncond < 2:
                if nota == "A":
                    notac1 = nota
                    prenv1 = "SIM"
            elif ucobcond < 1.5 and ucobncond < 2:
                if nota == "A":
                    notac1 = "B"
                    prenv1 = "NÃO"
                else:
                    notac1 = nota
                    prenv1 = "NÃO"
            elif ucobcond < 2 and ucobncond < 2:
                if nota == "A" or "B":
                    notac1 = "C"
                    prenv1 = "NÃO"
                else:
                    notac1 = nota
                    prenv1 = "NÃO"
            else:
                notac1 = "E"
                prenv1 = "NÃO"
        else:
            notac1 = nota
            prenv1 = "SIM"

#Síntese das exigências para transmitância térmica de paredes externas os diferentes níveis de eficiência e Zonas Bioclimáticas

            notac2 ="R"

        if zb == 1 or 2:
            if upar < 1:
                if nota == "A":
                    notac2 = "A"
                    prenv1 = "SIM"
                else:
                    notac2 = nota
                    prenv1 = "SIM"
            elif upar < 2:
                if nota == "A":
                    notac2 = "B"
                    prenv1 = "NÃO"
                else:
                    notac2 = nota
                    prenv1 = "NÃO"
            elif upar < 3.7:
                if nota == "A" or "B":
                    notac2 = "C"
                    prenv1 = "NÃO"
                else:
                    notac2 = nota
                    prenv1 = "NÃO"
            else:
                notac2: "E"
                prenv1 = "SIM"

        if zb == 3 or 6:
            if upar < 3.7:
                notac2 = nota
                prenv1 = "SIM"
            else:
                notac2 = "E"
                prenv1 = "NÃO"

        if zb == 7 or 8:
            if upar < 3.7:
                notac2 = nota
                prenv1 = "SIM"
            else:
                notac2 = "E"
                prenv1 = "NÃO"

        if zb == 2 or 3 or 4 or 5 or 6 or 7 or 8:
            if nota == 5 or 4:
                if 0.5 > (abscob or absrev):
                    prenv2 = "SIM"
                    nota = nota
                else:
                    prenv2 = "NÃO"
                    nota = 3
            else:
                nota = nota
                prenv2 = "NÃO"
        elif zb == None:
            prenv2 = "NÃO"
        else:
            prenv2 = "SIM"

        notas_dict = {
            'A': 5,
            'B': 4,
            'C': 3,
            'D': 2,
            'E': 1
        }
        notac1n = notas_dict[notac1]
        notac2n = notas_dict[notac2]

        if notac1n < notac2n:
            nota = notac1
        else:
            nota = notac2


        self.prenv1 = prenv1
        self.prenv2 = prenv2
        return nota



# ------------------------------- CORREÇÃO - CONDICIONAEMNTO DE AR ----------------------------------------------
    def corrigircond(self):
        nota = self.notacondgeral
        prereqesp = self.prcond

        if nota == "A" and prereqesp == "SIM":
            nota = "A"
        elif nota == "A" and prereqesp == "NÃO":
            nota = "B"
        else:
            nota = nota

        return nota

    def calcularnotailum(self):
        if self.potilumg is not None:
            potilumg = self.potilumg
        else:
            potilumg = 0

        if self.somacol1 is not None:
            somacol1 = self.somacol1
        else:
            somacol1 = 0

        if self.somacol2 is not None:
            somacol2 = self.somacol2
        else:
            somacol2 = 0

        if self.somacol3 is not None:
            somacol3 = self.somacol3
        else:
            somacol3 = 0

        if self.somacol4 is not None:
            somacol4 = self.somacol4
        else:
            somacol4 = 0

        nota = "R"
        if potilumg < somacol1:
            nota = "A"
        elif potilumg < somacol2:
            nota = "B"
        elif potilumg < somacol3:
            nota = "C"
        elif potilumg < somacol4:
            nota = "D"
        else:
            nota = "E"

        return nota

    def calcularnotailumcorrigida(self):
        notacalc = self.calcnotail
        if self.somapril1 is not None:
            somapril1 = self.somapril1
        else:
            somapril1 = 1
        if self.somapril2 is not None:
            somapril2 = self.somapril2
        else:
            somapril2 = 1
        if self.somapril3 is not None:
            somapril3 = self.somapril3
        else:
            somapril3 = 1

        nota = "R"

        if notacalc == "A":
            if somapril1 < 1 and somapril2 < 1 and somapril3 < 1:
                nota = "A"
            elif somapril1 < 1 and somapril2 < 1:
                nota = "B"
            elif somapril1 < 1:
                nota = "C"
            else:
                nota = "D"
        elif notacalc == "B":
            if somapril1 < 1 and somapril2 < 1 and somapril3 < 1:
                nota = "B"
            elif somapril1 < 1 and somapril2 < 1:
                nota = "B"
            elif somapril1 < 1:
                nota = "C"
            else:
                nota = "D"
        elif notacalc == "C":
            if somapril1 < 1 and somapril2 < 1 and somapril3 < 1:
                nota = "C"
            elif somapril1 < 1 and somapril2 < 1:
                nota = "C"
            elif somapril1 < 1:
                nota = "C"
            else:
                nota = "D"
        else:
            nota = notacalc
        return nota


    def calcularnotageral(self):
        ssg = 0
        sspr = 0
        if self.notaiccorrigida is not None:
            notaenv = self.notaiccorrigida
        else:
            notaenv = "E"

        if self.notacondgeralcorrigida is not None:
            notacond = self.notacondgeralcorrigida
        else:
            notacond = "E"

        if self.notailcorrigida is not None:
            notail = self.notailcorrigida
        else:
            notail = "E"

        if self.actotal is not None:
            ac = self.actotal
            if self.actotal == 0:
                ac = 1
        else:
            ac = 1

        if self.autotal is not None:
            au = self.autotal
            if self.autotal == 0:
                au = 1
        else:
            au = 1

        nota = "R"

        notas_dict = {
            'A': 5,
            'B': 4,
            'C': 3,
            'D': 2,
            'E': 1
        }
        notaenvn = notas_dict[notaenv]
        notailn = notas_dict[notail]
        notacondn = notas_dict[notacond]
        PT = 0.3 * (notaenvn * ac/au) + 0.3 * notailn + 0.4 * (notacondn * ac/au)
        pil = 0.3 * notailn
        pcond = 0.4 * (notacondn * ac/au)
        penv = 0.3 * (notaenvn * ac/au)

        if PT >= 4.5:
            nota = "A"
        elif PT >= 3.5:
            nota = "B"
        elif PT >= 2.5:
            nota = "C"
        elif PT >= 1.5:
            nota = "D"
        else:
            nota = "E"

        if self.sg1 == "SIM":
            ssg = ssg+1
        if self.sg2 == "SIM":
            ssg = ssg+1
        if self.sg3 == "SIM":
            ssg = ssg+1
        if self.sg4 == "SIM":
            ssg = ssg+1
        if self.sg5 == "SIM":
            ssg = ssg+1
        if self.sg6 == "SIM":
            ssg = ssg+1

        if self.prenv1 == "SIM":
            sspr = sspr+2
        if self.prenv2 == "SIM":
            sspr = sspr + 1
        if self.prcond == "SIM":
            sspr = sspr + 1
        if self.prespil1 == "SIM":
            sspr = sspr + 1
        if self.prespil2 == "SIM":
            sspr = sspr + 1
        if self.prespil3 == "SIM":
            sspr = sspr + 1
        if self.prgeral == "SIM":
            sspr = sspr + 1

        self.somareq = sspr
        self.somasg = ssg
        self.contil = pil
        self.contcond = pcond
        self.contenv = penv
        self.valornotageral = PT
        return nota


class Ambientes(models.Model):
    edificacoes = models.ForeignKey(
        Edificacoes, on_delete=models.CASCADE, null=True, related_name='ambientes_set',
        )

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

    nomeambiente = models.CharField(max_length=100)
    areaambiente = models.FloatField(null=True)
    nlamp = models.PositiveIntegerField(blank=False)
    ptlamp = models.DecimalField(max_digits=12, decimal_places=2)
    nar = models.PositiveIntegerField(blank=False)
    ptar = models.DecimalField(max_digits=12, decimal_places=2)
    notaar = models.CharField(max_length=3, blank=True, choices=OPCOES_NOTA)
    ativ = models.CharField(max_length=55, blank=True, choices=OPCOES_ATIV)
    pril1 = models.CharField(max_length=3, blank=True, choices=OPCOES_PREIL12)
    pril2 = models.CharField(max_length=3, blank=True, choices=OPCOES_PREIL12)
    pril3= models.CharField(max_length=3, blank=True, choices=OPCOES_PREIL12)
    #ILUMINAÇÃO -> Cálculos
    potilum = models.FloatField(null=True, editable=False)
    densilum = models.FloatField(null=True, editable=False)
    #CONDICIONAMENTO DE AR -> Cálculos
    eqvnota = models.PositiveIntegerField(default=1, editable=False)
    potcond = models.FloatField(null=True, editable=False)
    relacao_potencia = models.FloatField(null=True, editable=False)
    contribcond = models.FloatField(null=True, editable=False)
    col1 = models.FloatField(null=True, editable=False)
    col2 = models.FloatField(null=True, editable=False)
    col3 = models.FloatField(null=True, editable=False)
    col4 = models.FloatField(null=True, editable=False)
    areaabertura = models.FloatField(null=True)
    led = models.CharField(max_length=3, blank=True, choices=OPCOES_PREIL12)

    def __str__(self):
        return f"{self.edificacoes.nome} - {self.nomeambiente}"

    def __init__(self, *args, **kwargs):
        super(Ambientes, self).__init__(*args, **kwargs)
        self.potcond_total = 0



    # SAVE DOS CÁLCULOS GERAIS
    def save(self, *args, **kwargs):
        # CALCULANDO OS PARÂMETRO NECESSÁRIOS PARA A NOTA DA ILUMINAÇÃO
        self.potilum = self.nlamp * float(self.ptlamp)
        self.densilum = self.potilum / float(self.areaambiente)
        self.potcond = self.nar * float(self.ptar)
        # CALCULANDO OS PARÂMETROS NECESSÁRIOS PARA A NOTA DE CONDICIONAMENTO DE AR
        # CORRESPONDENCIAS DE NOTAS
        notas_dict = {
            'A': 5,
            'B': 4,
            'C': 3,
            'D': 2,
            'E': 1
        }

        if self.notaar in notas_dict:
            self.eqvnota = notas_dict[self.notaar]

        # Chama o método save() do modelo para salvar os dados no banco de dados
        super(Ambientes, self).save(*args, **kwargs)
        self.update_edificacoes_potcond_total()
        self.update_ambientes_potcond_relation()
        self.update_ambientes_contribcond()
        self.update_calcnotacond()
        self.define_nota()
        self.encontrar_atividade()
        self.update_cols()
        self.somapril()
        self.update_edificacoes_autotal()
        self.update_edificacoes_actotal()



# ------------------------------- FUNÇÕES REFERENTES AO SISTEMA DE CONDICIONAMENTO DE AR ----------------------------
    def update_edificacoes_potcond_total(self):
        if self.edificacoes:
            ambientes = self.edificacoes.ambientes_set.all()
            pot_total = sum([amb.potcond for amb in ambientes])
            self.edificacoes.potcond_total = pot_total
            self.edificacoes.save()

    def update_edificacoes_autotal(self):
        if self.edificacoes:
            ambientes = self.edificacoes.ambientes_set.all()
            autotal = sum([amb.areaambiente for amb in ambientes])
            self.edificacoes.autotal = autotal
            self.edificacoes.save()

    def update_edificacoes_actotal(self):
        if self.edificacoes:
            ambientes = self.edificacoes.ambientes_set.all()
            actotal = 0
            for amb in ambientes:
                if amb.nar > 0:
                    actotal = actotal + amb.areaambiente

            self.edificacoes.actotal = actotal
            self.edificacoes.save()


    def delete(self, *args, **kwargs):
        # Remove o ambiente
        super().delete(*args, **kwargs)
        # Atualiza a potência total da edificação
        if self.edificacoes:
            ambientes = self.edificacoes.ambientes_set.all()
            pot_total = sum([amb.potcond for amb in ambientes])
            self.edificacoes.potcond_total = pot_total
            self.update_ambientes_potcond_relation()
            self.update_ambientes_contribcond()
            self.encontrar_atividade()
            self.update_cols()
            self.somapril()
            self.update_edificacoes_autotal()
            self.update_edificacoes_actotal()
            self.edificacoes.save()


    def update_ambientes_potcond_relation(self):
        if self.edificacoes:
            pot_total = self.edificacoes.potcond_total
            ambientes = self.edificacoes.ambientes_set.all()
            updates = []
            for ambiente in ambientes:
                if pot_total == 0:
                    relacao_potencia = 0
                else:
                    relacao_potencia = ambiente.potcond / pot_total
                updates.append(Ambientes(id=ambiente.id, relacao_potencia=relacao_potencia))
            Ambientes.objects.bulk_update(updates, ['relacao_potencia'])

    def update_ambientes_contribcond(self):
        if self.edificacoes:
            ambientes = self.edificacoes.ambientes_set.all()
            updates = []
            for ambiente in ambientes:
                if ambiente.eqvnota and ambiente.relacao_potencia:
                    contribcond = ambiente.eqvnota * ambiente.relacao_potencia
                else:
                    contribcond = 0
                updates.append(Ambientes(id=ambiente.id, contribcond=contribcond))
            Ambientes.objects.bulk_update(updates, ['contribcond'])

    def update_calcnotacond(self):
        if self.edificacoes:
            ambientes = self.edificacoes.ambientes_set.all()
            calcnotacond = sum([amb.contribcond for amb in ambientes])
            self.edificacoes.calcnotacond = calcnotacond
            self.edificacoes.save()

    def define_nota(self):
        if self.edificacoes:
            calcnotacond = self.edificacoes.calcnotacond
            if calcnotacond >= 4.5 and calcnotacond <= 5:
                notacond = "A"
            elif calcnotacond >= 3.5 and calcnotacond < 4.5:
                notacond = "B"
            elif calcnotacond >= 2.5 and calcnotacond < 3.5:
                notacond = "C"
            elif calcnotacond >= 1.5 and calcnotacond < 2.5:
                notacond = "D"
            else:
                notacond = "E"
        self.edificacoes.notacondgeral = notacond
        self.edificacoes.save()

#-----------------------------------------ILUMINAÇÃO---------------------------------------
    def encontrar_atividade(self):
        # Cria um dicionário com as atividades e as colunas correspondentes
        tabela = np.array([
            ['Armazém, Atacado - Material pequeno/leve', 10.20, 12.24, 14.28, 16.32],
            ['Armazém, Atacado - Material médio/volumoso', 5.00, 6.00, 7.00, 8.00],
            ['Átrio - por metro de altura-até 12,20 m de altura', 0.30, 0.36, 0.42, 0.48],
            ['Átrio - por metro de altura -acima de 12,20 m de altura', 0.20, 0.24, 0.28, 0.32],
            ['Auditórios e Anfiteatros - Auditório', 8.50, 10.20, 11.90, 13.60],
            ['Auditórios e Anfiteatros - Centro de Convenções', 8.80, 10.56, 12.32, 14.08],
            ['Auditórios e Anfiteatros - Cinema', 5.00, 6.00, 7.00, 8.00],
            ['Auditórios e Anfiteatros - Teatro', 26.20, 31.44, 36.68, 41.92],
            ['Banco/Escritório - Área de atividades bancárias', 14.90, 17.88, 20.86, 23.84],
            ['Banheiros', 5.00, 6.00, 7.00, 8.00],
            ['Biblioteca - Área de arquivamento', 7.80, 9.36, 10.92, 12.48],
            ['Biblioteca - Área de leitura', 10.00, 12.00, 14.00, 16.00],
            ['Biblioteca - Área de estantes', 18.40, 22.08, 25.76, 29.44],
            ['Casa de Máquinas', 6.00, 7.20, 8.40, 9.60],
            ['Centro de Convenções - Espaço de exposições', 15.60, 18.72, 21.84, 24.96],
            ['Circulação', 7.10, 8.52, 9.94, 11.36],
            ['Comércio - Área de vendas', 18.10, 21.72, 25.34, 28.96],
            ['Comércio - Pátio de área comercial', 11.80, 14.16, 16.52, 18.88],
            ['Comércio - Provador', 10.20, 12.24, 14.28, 16.32],
            ['Cozinhas', 10.70, 12.84, 14.98, 17.12],
            ['Depósitos', 5.00, 6.00, 7.00, 8.00],
            ['Dormitórios – Alojamentos', 4.10, 4.92, 5.74, 6.56],
            ["Escadas", 7.40, 8.88, 10.36, 11.84],
            ["Escritório", 11.90, 14.28, 16.66, 19.04],
            ["Escritório – Planta livre", 10.50, 12.60, 14.70, 16.80],
            ["Garagem", 2.00, 2.40, 2.80, 3.20],
            ["Ginásio/Academia - Área de Ginástica", 7.80, 9.36, 10.92, 12.48],
            ["Ginásio/Academia - Arquibancada", 7.50, 9.00, 10.50, 13.00],
            ["Ginásio/Academia - Esportes de ringue", 28.80, 34.56, 40.32, 46.08],
            ["Ginásio/Academia - Quadra de esportes – classe 42", 7.80, 9.36, 10.92, 12.48],
            ["Ginásio/Academia - Quadra de esportes – classe 33", 12.90, 15.48, 18.06, 20.64],
            ["Ginásio/Academia - Quadra de esportes – classe 24", 20.70, 24.84, 28.98, 33.12],
            ["Ginásio/Academia - Quadra de esportes – classe 15", 32.40, 38.88, 45.36, 51.84],
            ["Hall de Entrada - Vestíbulo", 8.00, 9.60, 11.20, 12.80],
            ["Hall de Entrada - Vestíbulo- Cinemas", 8.00, 9.60, 11.20, 12.80],
            ["Hall de Entrada - Vestíbulo- Hotel", 8.00, 9.60, 11.20, 12.80],
            ["Hall de Entrada - Vestíbulo - Salas de Espetáculos", 8.00, 9.60, 11.20, 12.80],
            ["Hospital - Circulação", 9.60, 11.52, 13.44, 15.36],
            ["Hospital - Emergência", 24.30, 29.16, 34.02, 38.88],
            ["Hospital - Enfermaria", 9.50, 11.40, 13.30, 15.20],
            ["Hospital - Exames/Tratamento", 17.90, 21.48, 25.06, 28.64],
            ["Hospital - Farmácia", 12.30, 14.76, 17.22, 19.68],
            ["Hospital - Fisioterapia", 9.80, 11.76, 13.72, 15.68],
            ["Hospital - Sala de espera, estar", 11.50, 13.80, 16.10, 18.40],
            ["Hospital - Radiologia", 14.20, 17.04, 19.88, 22.72],
            ["Hospital - Recuperação", 12.40, 14.88, 17.36, 19.84],
            ["Hospital - Sala de Enfermeiros", 9.40, 11.28, 13.16, 15.04],
            ["Hospital - Sala de Operação", 20.30, 24.36, 28.42, 32.48],
            ["Hospital - Quarto de pacientes", 6.70, 8.04, 9.38, 10.72],
            ["Hospital - Suprimentos médicos", 13.70, 16.44, 19.18, 21.92],
            ["Igreja, templo - Assentos", 16.50, 19.80, 23.10, 26.40],
            ["Igreja, templo - Altar, Coro", 16.50, 19.80, 23.10, 26.40],
            ["Igreja, templo - Sala de comunhão - nave", 6.90, 8.28, 9.66, 11.04],
            ["Laboratórios - para Salas de Aula", 10.20, 12.24, 14.28, 16.32],
            ["Laboratórios - Médico/Ind./Pesq", 19.50, 23.40, 27.30, 31.20],
            ["Lavanderia", 6.50, 7.80, 9.10, 10.40],
            ["Museu - Restauração", 11.00, 13.20, 15.40, 17.60],
            ["Museu - Sala de exibição", 11.30, 13.56, 15.82, 18.08],
            ["Oficina – Seminário, cursos", 17.10, 20.52, 23.94, 27.36],
            ["Oficina Mecânica", 6.00, 7.20, 8.40, 9.60],
            ["Quartos de Hotel", 7.50, 9.00, 10.50, 13.00],
            ["Refeitório", 11.50, 13.80, 16.10, 18.40],
            ["Restaurante - salão", 9.60, 11.52, 13.44, 15.36],
            ["Restaurante - salão - Hotel", 8.80, 10.56, 12.32, 14.08],
            ["Restaurante - salão - Lanchonete/Café", 7.00, 8.40, 9.80, 11.20],
            ["Restaurante - salão - Bar/Lazer", 14.10, 16.92, 19.74, 22.56],
            ["Sala de Aula, Treinamento", 10.20, 12.24, 14.80, 16.32],
            ["Sala de espera, convivência", 6.00, 7.20, 8.40, 9.60],
            ["Sala de Reuniões, Conferência, Multiuso", 11.90, 14.28, 16.66, 19.04],
            ["Vestiário", 8.10, 9.72, 11.34, 12.96],
            ["Transportes - Área de bagagem", 7.50, 9.00, 10.50, 12.00],
            ["Transportes-Aeroporto – Pátio", 3.90, 4.68, 5.46, 6.24],
            ["Transportes-Assentos - Espera", 5.80, 6.96, 8.12, 9.28],
            ["Transportes-Terminal - bilheteria", 11.60, 13.92, 16.24, 18.56],
        ])

        # Encontra a linha correspondente à atividade
        if self.edificacoes:
            ambientes = self.edificacoes.ambientes_set.all()
            updates = []
            for ambiente in ambientes:
                col1 = 0
                col2 = 0
                col3 = 0
                col4 = 0
                for tabela_item in tabela:
                    if ambiente.ativ == tabela_item[0]:
                        col1 = self.areaambiente * float(tabela_item[1])
                        col2 = self.areaambiente * float(tabela_item[2])
                        col3 = self.areaambiente * float(tabela_item[3])
                        col4 = self.areaambiente * float(tabela_item[4])
                updates.append(
                    Ambientes(
                        id=ambiente.id,
                        col1=col1,
                        col2=col2,
                        col3=col3,
                        col4=col4,
                    )
                )
            Ambientes.objects.bulk_update(updates, ['col1', 'col2', 'col3', 'col4'])

    def update_cols(self):
        if self.edificacoes:
            ambientes = self.edificacoes.ambientes_set.all()
            somacol1 = sum([amb.col1 for amb in ambientes])
            somacol2 = sum([amb.col2 for amb in ambientes])
            somacol3 = sum([amb.col3 for amb in ambientes])
            somacol4 = sum([amb.col4 for amb in ambientes])
            potilumg = sum([amb.potilum for amb in ambientes])
            self.edificacoes.somacol1 = somacol1
            self.edificacoes.somacol2 = somacol2
            self.edificacoes.somacol3 = somacol3
            self.edificacoes.somacol4 = somacol4
            self.edificacoes.potilumg = potilumg
            self.edificacoes.save()

    def somapril(self):
        if self.edificacoes:
            ambientes = self.edificacoes.ambientes_set.all()
            soma1 = 0
            soma2 = 0
            soma3 = 0
            prespil1 = "r"
            prespil2 = "r"
            prespil3 = "r"
            for amb in ambientes:
                if amb.pril1 == "SIM":
                    soma1 = soma1 + 0
                else:
                    soma1 = soma1 + 1
                if amb.pril2 == "SIM":
                    soma2 = soma2 + 0
                else:
                    soma2 = soma2 + 1
                if amb.pril3 == "SIM":
                    soma3 = soma3 + 0
                else:
                    soma3 = soma3 + 1

            if soma1 > 0:
                prespil1 = "NÃO"
            else:
                prespil1 = "SIM"

            if soma2 > 0:
                prespil2 = "NÃO"
            else:
                prespil2 = "SIM"

            if soma3 > 0:
                prespil3 = "NÃO"
            else:
                prespil3 = "SIM"

        self.edificacoes.prespil1 = prespil1
        self.edificacoes.prespil2 = prespil2
        self.edificacoes.prespil3 = prespil3
        self.edificacoes.somapril1 = soma1
        self.edificacoes.somapril2 = soma2
        self.edificacoes.somapril3 = soma3

        self.edificacoes.save()
# ------------------------------- FUNÇÕES REFERENTES AO SISTEMA ILUMINAÇÃO ------------------------------------------#