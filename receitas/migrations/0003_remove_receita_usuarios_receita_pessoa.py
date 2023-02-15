# Generated by Django 4.1.6 on 2023-02-15 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0003_rename_pessoas_pessoa'),
        ('receitas', '0002_receita_publicada_receita_usuarios_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receita',
            name='usuarios',
        ),
        migrations.AddField(
            model_name='receita',
            name='pessoa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pessoas.pessoa'),
        ),
    ]