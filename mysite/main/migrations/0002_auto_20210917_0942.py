# Generated by Django 3.2.7 on 2021-09-17 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sample',
            name='category',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='company',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Sample',
        ),
    ]