# Generated by Django 4.1.1 on 2022-10-20 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_alter_usuario_mina_alter_usuario_zona'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='zona',
        ),
        migrations.AddField(
            model_name='usuario',
            name='area',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Area de la mina a la que es asignado el usuario'),
        ),
    ]
