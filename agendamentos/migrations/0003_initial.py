# Generated by Django 5.2.4 on 2025-07-07 03:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agendamentos', '0002_initial'),
        ('profissionais', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consulta',
            name='profissional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultas', to='profissionais.profissionalsaude'),
        ),
    ]
