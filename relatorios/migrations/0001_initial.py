# Generated by Django 5.2.4 on 2025-07-07 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Relatorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('tipo', models.CharField(max_length=100)),
                ('gerado_em', models.DateTimeField(auto_now_add=True)),
                ('conteudo', models.TextField()),
            ],
        ),
    ]
