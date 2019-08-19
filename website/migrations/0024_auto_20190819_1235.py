# Generated by Django 2.2.4 on 2019-08-19 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0023_auto_20190819_1149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='data_atualização',
        ),
        migrations.AddField(
            model_name='aluno',
            name='data_atualizacao',
            field=models.DateTimeField(auto_now=True, verbose_name='Data de atualização'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='data_criacao',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data de criação'),
        ),
    ]
