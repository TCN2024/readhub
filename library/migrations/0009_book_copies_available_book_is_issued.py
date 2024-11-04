# Generated by Django 5.1.2 on 2024-11-04 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_auto_20200412_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='copies_available',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='book',
            name='is_issued',
            field=models.BooleanField(default=False),
        ),
    ]
