# Generated by Django 3.1.3 on 2021-02-14 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0002_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
