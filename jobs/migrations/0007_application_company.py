# Generated by Django 3.1.7 on 2021-07-29 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_application'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='company',
            field=models.CharField(default='', max_length=200),
        ),
    ]
