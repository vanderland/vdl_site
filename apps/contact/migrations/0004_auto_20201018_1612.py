# Generated by Django 3.1.2 on 2020-10-18 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20201017_1611'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='create_on',
            new_name='created_on',
        ),
    ]
