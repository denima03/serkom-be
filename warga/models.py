from django.db import models

# Create your models here.


class Warga(models.Model):
    jk_choice = (
        ('LAKI-LAKI', 'LAKI-LAKI'),
        ('PEREMPUAN', 'PEREMPUAN')
    )
    nik = models.CharField(max_length=17)
    nama = models.CharField(max_length=50)
    jenis_kelamin = models.CharField(max_length=10, choices=jk_choice)
    alamat = models.CharField(max_length=50)
    rt = models.CharField(max_length=3)
    rw = models.CharField(max_length=3)
