from django.db import models

# class Author(models.Model):
#     name = models.CharField(verbose_name='Имя автора', max_length=20)
#     surname = models.CharField(verbose_name='Фамилия', max_length=25)
#     birthday = models.DateField(verbose_name='Дата рождения')
#     bio = models.TextField(verbose_name='Биография')
#     desc = models.CharField('Умер или жив', default='Жив')

#     class Meta:
#         verbose_name = 'Автор'
#         verbose_name_plural = 'Авторы'
#         ordering = ['surname', 'name']
#         indexes = [
#             models.Index(fields=['surname'])
#         ]
#         constraints = [
#             models.UniqueConstraint(
#                 fields=['surname', 'bio'],
#                 condition = models.Q(desc="Жив"),
#                 name = 'unique_surname_bio'
#             ),
#         ]
#     def __str__(self):
#         return f"{self.surname} {self.name}"


# class Publisher(models.Model):
#     name = models.CharField(verbose_name='Название', unique=True)

# class Book(models.Model):
#     title = models.CharField(verbose_name='Название', max_length=50)
#     id_publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
#     is_author = models.ManyToManyField(Author)

class Clients(models.Model):
    full_name = models.CharField('ФИО', max_length=25)
    birth_date = models.DateField('Дата рождения')
    contacts = models.CharField('Контактные данные', max_length=100, unique=True)
    passport_number = models.CharField('Номер паспорта', max_length=30)
    hotel_room_id = models.ForeignKey(Hotel_rooms, on_delete=models.CASCADE)
    sex_id = models.ForeignKey(Sex, on_delete=models.CASCADE)




