# Generated by Django 4.2.9 on 2024-01-27 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default='img.jpg', upload_to='img/%Y/%m/%d', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]
