# Generated by Django 2.2 on 2022-12-25 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nangluc', '0009_danhgia_nluc_kha_nang_dapung'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='danhgia_nluc',
            options={'ordering': ['Nhanvien_dg_nangluc', 'TenNangluc_congviec']},
        ),
    ]
