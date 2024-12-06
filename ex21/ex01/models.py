from django.db import models

# Create your models here.
class PesquisaOpiniao(models.Model):
    questao = models.CharField(max_length=200)
    data_publicacao = models.DateTimeField('data publicada')
    def __unicode__(self):
        return self.questao


class Escolhas(models.Model):
    opniao = models.ForeignKey(PesquisaOpiniao, on_delete=models.CASCADE)
    escolha = models.CharField(max_length=200)
    votos = models.IntegerField()
    def __unicode__(self):
        return self.escola