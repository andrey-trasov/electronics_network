from django.db import models

NULLABLE = {'null': True, 'blank': True}
class Supplier(models.Model):
    """
    Компания
    """
    name = models.CharField(max_length=150, verbose_name="Название компании")
    provider = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name="Компания", **NULLABLE)
    level = models.IntegerField(verbose_name="Уровень поставщика", **NULLABLE)
    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"

    def __str__(self):
        return self.name


class Contacts(models.Model):
    """
    Контакты компании
    """
    company = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name="Компания")
    email = models.CharField(max_length=150, verbose_name="email")
    country = models.CharField(max_length=150, verbose_name="Страна")
    city = models.CharField(max_length=150, verbose_name="Город")
    street = models.CharField(max_length=150, verbose_name="Улица")
    house_number = models.CharField(max_length=150, verbose_name="Номер дома")

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return self.email


class Products(models.Model):
    """
    Продукты
    """
    name = models.CharField(max_length=100, verbose_name="Нозвание продукта")
    model = models.CharField(max_length=100, verbose_name="Модель продукта")
    price = models.IntegerField(verbose_name="Цена")
    quantity =models.IntegerField(verbose_name="Количество товара")
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT , verbose_name="Поставщик")
    date_of_market_launch = models.DateTimeField(verbose_name="Дата выхода на рынок")
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания', **NULLABLE)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name

class Arrears(models.Model):
    """
    Задолженности
    """
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT , verbose_name="Поставщик")
    arrears = models.FloatField(verbose_name="Задолженность перед поставщиком с точностью до копеек")
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания', **NULLABLE)

    class Meta:
        verbose_name = "Задолженность"
        verbose_name_plural = "Задолженности"

    def __str__(self):
        return f"{self.supplier} - {self.arrears} руб."
