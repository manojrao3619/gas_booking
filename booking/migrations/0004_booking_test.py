# Generated by Django 3.1.7 on 2021-03-29 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20210306_0810'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='test',
            field=models.DateTimeField(null=True),
        ),
    ]
