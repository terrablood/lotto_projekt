from django.db import models

class Huzas(models.Model):

    id = models.models.IntegerField(_("256"))
    ev = models.models.IntegerField(_("256"))
    het = models.models.IntegerField(_("256"))

    class Meta:
        verbose_name = _("huzas")
        verbose_name_plural = _("huzasok")

    def __str__(self):
        return f'{self.id} ({self.ev}.{self.het})'


    

    

