# Generated by Django 5.1.6 on 2025-02-20 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_anuncio_imagem_imagemanuncio'),
    ]

    operations = [
        migrations.AddField(
            model_name='anuncio',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='imagens_anuncios/'),
        ),
        migrations.DeleteModel(
            name='ImagemAnuncio',
        ),
    ]
