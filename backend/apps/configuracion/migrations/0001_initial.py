# Generated by Django 4.1.1 on 2022-10-13 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuracion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_sensores', models.PositiveIntegerField(default=8)),
            ],
            options={
                'verbose_name': 'configuracion',
                'verbose_name_plural': 'configuraciones',
                'db_table': 'configuraciones',
            },
        ),
    ]
