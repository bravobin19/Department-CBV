# Generated by Django 4.0.3 on 2022-05-11 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0005_alter_employees_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='age',
            field=models.DateField(null=True),
        ),
    ]