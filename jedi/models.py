from django.db import models


class Planet(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название планеты')

    def __str__(self):
        return self.name


class Jedi(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя Джедая')
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, verbose_name='Планета')

    def __str__(self):
        return self.name


class Candidate(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя кандидата')
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, verbose_name='Планета')
    age = models.PositiveIntegerField(verbose_name='Возраст')
    email = models.EmailField(verbose_name='Почта')
    jedi = models.ForeignKey(Jedi, null=True, on_delete=models.CASCADE, related_name='podavans')

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.TextField(verbose_name='Текст задания')
    order = models.ForeignKey(Planet, on_delete=models.CASCADE, verbose_name='Название ордена')

    def __str__(self):
        return self.text[:20] + "..."


class Answer(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='answers_table')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.BooleanField()

    class Meta:
        unique_together = (('candidate', 'question'),)

