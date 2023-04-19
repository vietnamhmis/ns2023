# Generated by Django 2.2 on 2023-03-11 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nhansu', '0017_auto_20230311_2056'),
        ('mota_cv', '0002_auto_20230304_2209'),
        ('luong', '0008_auto_20230201_0915'),
    ]

    operations = [
        migrations.CreateModel(
            name='bangluong_chinh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bac_1', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Bac_2', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Bac_3', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Bac_4', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Bac_5', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Boiso', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('tong_diem', models.IntegerField(null=True)),
                ('luong_toi_thieu', models.IntegerField(null=True)),
                ('Nhom_luong', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nhansu.TK_ngach')),
                ('diem', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mota_cv.Mota_Cv7')),
            ],
        ),
    ]
