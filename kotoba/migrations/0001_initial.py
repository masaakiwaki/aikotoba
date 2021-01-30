# Generated by Django 3.1.5 on 2021-01-30 05:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aikotoba',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('kotoba', models.CharField(max_length=255, unique=True, verbose_name='合言葉')),
                ('dengon', models.TextField(max_length=10000, verbose_name='伝言')),
            ],
        ),
    ]
