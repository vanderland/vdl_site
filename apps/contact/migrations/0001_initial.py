# Generated by Django 3.1.2 on 2020-10-17 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_first', models.CharField(max_length=50, verbose_name='First Name')),
                ('name_middle', models.CharField(blank=True, max_length=50, verbose_name='Middle Name')),
                ('name_last', models.CharField(max_length=50, verbose_name='Last Name')),
                ('email_address', models.EmailField(max_length=125, verbose_name='Email Address')),
                ('subject', models.CharField(max_length=150, verbose_name='Last Name')),
                ('message', models.TextField(verbose_name='Message')),
                ('create_on', models.DateTimeField(verbose_name='Created On')),
            ],
        ),
    ]