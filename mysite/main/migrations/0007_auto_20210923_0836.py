# Generated by Django 3.2.7 on 2021-09-23 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_category_company_material_product_sample'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sample',
            name='categorys',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='company',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='material',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='product',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Material',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Sample',
        ),
    ]