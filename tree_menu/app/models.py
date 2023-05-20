from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=50, unique=True)
    url = models.CharField(max_length=50, null=True, blank=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name.capitalize()
