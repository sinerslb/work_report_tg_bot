from django.db import models


class Building(models.Model):
    name = models.TextField(
        verbose_name='Название объекта',
        max_lenght=50,
        unique=True,
        blank=False,
    )
    address = models.TextField(
        verbose_name='Адрес объекта',
        max_lenght=50,
        blank=False,
    )

    def __str__(self) -> str:
        return self.name


class Malfunction(models.Model):
    date = models.DateField(
        verbose_name='Дата обнаружения неисправности',
        blank=False,
    )
    description = models.TextField(
        verbose_name='Описание неисправности',
        blank=False,
    )
    cause = models.TextField(
        verbose_name='Причина неисправности',
    )
    building = models.ForeignKey(
        Building,
        on_delete=models.PROTECT,
        related_name='malfunctions',
        blank=False,
    )
    date_of_fix = models.DateField(
        blank=True,
    )


class CompletedWork(models.Model):
    description = models.TextField(
        verbose_name='Описание работ',
        blank=False,
    )
    building = models.ForeignKey(
        Building,
        on_delete=models.PROTECT,
        related_name='completed_work',
        blank=True,
    )
    malfunction = models.ForeignKey(
        Malfunction,
        on_delete=models.DO_NOTHING,
        blank=True,
    )
