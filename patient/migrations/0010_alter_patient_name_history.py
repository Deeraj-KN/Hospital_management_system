# Generated by Django 4.2.3 on 2024-01-12 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0009_alter_patient_dob_alter_patient_ph_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateField(auto_now_add=True)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='patient.hospital')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='patient.patient')),
            ],
        ),
    ]
