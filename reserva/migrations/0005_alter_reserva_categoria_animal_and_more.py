# Generated by Django 4.2.4 on 2023-10-15 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0004_alter_reserva_categoria_animal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='categoria_animal',
            field=models.IntegerField(choices=[(0, 'Cachorro Mini - até 6kg'), (1, 'Cachorro Pequeno - 6 a 15kg'), (2, 'Cachorro Médio - 15 a 25kg'), (3, 'Cachorro Grande - 25 a 45kg'), (4, 'Cachorro Gigante - acima de 45kg'), (5, 'Gato')], verbose_name='Categoria do Animal'),
        ),
        migrations.DeleteModel(
            name='CategoriaAnimal',
        ),
    ]
