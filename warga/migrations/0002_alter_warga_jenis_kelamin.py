# Generated by Django 4.2.6 on 2023-10-20 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warga', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warga',
            name='jenis_kelamin',
            field=models.CharField(choices=[('LAKI-LAKI', 'LAKI-LAKI'), ('PEREMPUAN', 'PEREMPUAN')], max_length=10),
        ),
    ]
