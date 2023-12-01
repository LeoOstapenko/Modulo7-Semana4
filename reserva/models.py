from django.db import models


class CategoriaAnimal(models.Model):
    nome = models.CharField('Nome', max_length=50)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Categoria do Animal'
        verbose_name_plural = 'Categorias de Animal'
        ordering = ['id']


class Reserva(models.Model):
    '''CATEGORIA_ANIMAL_OPCOES = (
        (0, 'Cachorro Mini - até 6kg'),
        (1, 'Cachorro Pequeno - 6 a 15kg'),
        (2, 'Cachorro Médio - 15 a 25kg'),
        (3, 'Cachorro Grande - 25 a 45kg'),
        (4, 'Cachorro Gigante - acima de 45kg'),
        (5, 'Gato'),
    )'''
    TURNO_OPCOES = (
        ('manhã', 'Manhã'),
        ('tarde', 'Tarde'),
    )
    nome = models.CharField(verbose_name='Nome', max_length=50)
    email = models.EmailField(verbose_name='E-mail')
    nome_pet = models.CharField(verbose_name='Nome Pet', max_length=50)
    data = models.DateField(verbose_name='Data da Reserva', help_text='dd/mm/aaaa')
    turno = models.CharField(verbose_name='Turno', max_length=10, choices=TURNO_OPCOES)
    categoria_animal = models.ForeignKey(CategoriaAnimal, models.CASCADE, verbose_name='Categoria do Animal', related_name='reservas_da_categoria')
    observacoes = models.TextField(verbose_name='Observações', blank=True)
    banho_conclusao = models.BooleanField('Banho concluído?', default=False)


    def __str__(self): # Função e Método para uma representação textual melhor em 'Admin'.
        return f'{self.nome}: {self.data} - {self.turno}'
    
    class Meta:
        verbose_name = 'Reserva de Banho'
        verbose_name_plural = 'Reservas de Banho'
        ordering = ['data', 'turno']
