# Generated by Django 3.2.8 on 2021-10-11 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20211011_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='_slug',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]