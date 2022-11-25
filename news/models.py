from django.db import models

class Article(models.Model):
    title = models.CharField('Название',max_length=50)
    anons = models.CharField('Анонс',max_length=250)
    full_text = models.TextField('Статья',)
    date = models.DateTimeField('Дата публикации',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class News(models.Model):
    title = models.CharField("Название", max_length=100)
    image = models.ImageField(upload_to='images')
    details = models.TextField("Подробности")
    price = models.CharField("Цена", max_length=10)

    def __str__(self):
        return self.title
