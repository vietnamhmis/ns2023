# Generated by Django 2.2 on 2023-03-21 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0006_auto_20230321_1049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nhan_vien',
            name='Bac_cu',
        ),
        migrations.RemoveField(
            model_name='nhan_vien',
            name='Bang_luong_cu',
        ),
        migrations.RemoveField(
            model_name='nhan_vien',
            name='Heso_cu',
        ),
        migrations.RemoveField(
            model_name='nhan_vien',
            name='Luong_BHXH',
        ),
        migrations.RemoveField(
            model_name='nhan_vien',
            name='Luong_cb',
        ),
        migrations.RemoveField(
            model_name='nhan_vien',
            name='Nang_luc',
        ),
        migrations.RemoveField(
            model_name='nhan_vien',
            name='Ngay_giu_lg_cu',
        ),
        migrations.RemoveField(
            model_name='nhan_vien',
            name='So_ngayphep',
        ),
    ]
