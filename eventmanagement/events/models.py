from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField()
    slug = models.SlugField(
        unique=True,
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name', ]

    def __str__(self):
        return f'{self.name}'


class Event(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='events'
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Название мероприятия'
    )
    text = models.TextField()
    datetime = models.DateTimeField()
    category = models.ManyToManyField(
        Category,
        blank=True,
        null=True,
        through='EventCategory')
    image = models.ImageField()

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
        ordering = ['name', ]

    def __str__(self):
        return self.name



class EventCategory(models.Model):
    """Вспомогательная модель для категорий мероприятий."""
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['event', 'category'],
                name='unique_event_category'
            )
        ]