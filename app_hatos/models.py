from django.db import models

class Huzas(models.Model):

    idd = models.IntegerField()
    ev = models.IntegerField()
    het = models.IntegerField()

    class Meta:
        verbose_name = "huzas"
        verbose_name_plural = "huzasok"

    def __str__(self):
        return f'{self.idd} ({self.ev}.{self.het})'

class Huzott(models.Model):

    idd = models.IntegerField()
    huzasid = models.IntegerField()
    szam = models.IntegerField()

    class Meta:
        verbose_name = "Huzott"
        verbose_name_plural = "Huzottak"

    def __str__(self):
        return f'{self.idd} ({self.huzasid}.{self.szam})'

    

class Nyeremeny(models.Model):

    idd = models.IntegerField()
    huzasid = models.IntegerField()
    talalat = models.IntegerField()
    darab = models.IntegerField()
    ertek = models.IntegerField()
    

    class Meta:
        verbose_name = "Nyeremeny"
        verbose_name_plural = "Nyeremenyek"

    def __str__(self):
        return f'{self.idd} ({self.huzasid}.{self.talalat}.{self.darab}.{self.ertek})'

    

    

    

