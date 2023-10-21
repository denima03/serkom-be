# Generated by Django 4.2.6 on 2023-10-20 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Warga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nik', models.CharField(max_length=17)),
                ('nama', models.CharField(max_length=50)),
                ('jenis_kelamin', models.CharField(choices=[('Laki-Laki', 'Laki-Laki'), ('Perempuan', 'Perempuan')], max_length=10)),
                ('alamat', models.CharField(max_length=50)),
                ('rt', models.CharField(max_length=3)),
                ('rw', models.CharField(max_length=3)),
            ],
        ),
    ]