# Generated by Django 4.0.1 on 2022-01-15 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='address'),
        ),
    ]
