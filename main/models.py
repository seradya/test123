from django.db import models


class Client(models.Model):
    name = models.CharField(verbose_name="Имя", null=False, blank=False, max_length=64)
    email = models.CharField(verbose_name="Почта", null=False, blank=False, max_length=64)

    def __str__(self):
        return "Пользователь - {}".format(self.name)

    class Meta:
        verbose_name = "клиента"
        verbose_name_plural = "Клиенты"

class Service(models.Model):
    is_active = models.BooleanField(verbose_name="Активность", default=False)
    img = models.ImageField(verbose_name="Фото", upload_to="")
    article = models.CharField(verbose_name="Название", max_length=32)
    description = models.TextField(verbose_name="Описание", max_length=256)
    price = models.PositiveIntegerField(verbose_name="Цена")

    def __str__(self):
        return "Товар - {}".format(self.article)

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "Товары"
        ordering = ("is_active","id",)


