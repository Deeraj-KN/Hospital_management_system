# Generated by Django 4.2.3 on 2024-01-12 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0010_alter_patient_name_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
