# Generated by Django 3.1.5 on 2021-02-04 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebappBackend', '0004_auto_20210204_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
