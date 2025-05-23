# Generated by Django 5.1.7 on 2025-03-26 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('evento', 'Evento'), ('anuncios', 'Anúncio')], max_length=10)),
                ('titulo', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('likes', models.IntegerField(default=0)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
