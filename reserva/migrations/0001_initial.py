# Generated by Django 4.2.13 on 2024-05-17 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeDoPet', models.CharField(max_length=50, verbose_name='Nome do PET')),
                ('nomeDoDono', models.CharField(max_length=50, verbose_name='Nome do Dono')),
                ('telefone', models.CharField(max_length=15)),
                ('dia', models.DateField(verbose_name='Dia da Reserva')),
                ('observacoes', models.TextField(verbose_name='Observações')),
                ('tamanho', models.IntegerField(choices=[(0, 'Pequeno'), (1, 'Médio'), (2, 'Grande')], verbose_name='Tamanho')),
                ('turno', models.CharField(choices=[('manha', 'Manhã'), ('tarde', 'Tarde')], max_length=5, verbose_name='Turno')),
            ],
        ),
    ]
