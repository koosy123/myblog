# Generated by Django 2.2 on 2019-07-22 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio',
            old_name='desciption',
            new_name='description',
        ),
    ]
