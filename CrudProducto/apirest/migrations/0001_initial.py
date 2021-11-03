# Generated by Django 3.2.9 on 2021-11-03 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=250)),
                ('marca', models.CharField(max_length=50, null=True)),
                ('serie', models.CharField(max_length=20)),
                ('precio', models.CharField(max_length=20, null=True)),
                ('cantidad', models.EmailField(max_length=50)),
                ('disponible', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
    ]