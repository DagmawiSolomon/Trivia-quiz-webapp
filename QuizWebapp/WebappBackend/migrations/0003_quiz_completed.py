# Generated by Django 3.1.5 on 2021-02-04 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebappBackend', '0002_auto_20210204_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
