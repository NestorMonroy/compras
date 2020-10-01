from django.db import models

from bases.models import ClaseModelo

# Create your models here.


class Cliente(ClaseModelo):
    NAT = 'Natural'
    JUR = 'Jurídica'

    TIPO_CLIENTE = [
        (NAT, 'Natural'),
        (JUR, 'Jurídica')
    ]
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    celular = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    tipo = models.CharField(
        max_length=10,
        choices=TIPO_CLIENTE,
        default=NAT
    )

    def __str__(self):
        return '{} {}'.format(self.apellidos, self.nombre)

    def save(self):
        self.nombre = self.nombre.upper()
        self.apellidos = self.apellidos.upper()
        super(Cliente, self).save()

    class Meta:
        verbose_name_plural = "Clientes"
