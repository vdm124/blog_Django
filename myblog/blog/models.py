from django.db import models


# Create your models here.
class Post(models.Model):
    '''данные о посте'''
    title = models.CharField('Заголовок', max_length=100)
    description = models.TextField('Контент')
    author = models.CharField('Автор', max_length=100)
    date = models.DateField('Дата публикации')
    img = models.ImageField('Изображение', upload_to='img/%Y/%m/%d')

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Запись'
