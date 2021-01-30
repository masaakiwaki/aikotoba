from django.db import models
import uuid

class Aikotoba(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
        )


    kotoba = models.CharField(
        verbose_name='合言葉',
        max_length=255,
        unique=True,
        )

    dengon = models.TextField(
        verbose_name='伝言',
        max_length=10000,
        )

    def __str__(self):
            return self.kotoba