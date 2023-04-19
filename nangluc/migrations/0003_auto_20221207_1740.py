# Generated by Django 2.2 on 2022-12-07 10:40

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nangluc', '0002_congviec_nangluc_stt'),
    ]

    operations = [
        migrations.AddField(
            model_name='danhgia_nluc',
            name='user',
            field=models.ForeignKey(default=datetime.datetime(2022, 12, 7, 10, 40, 40, 865292, tzinfo=utc), on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='danhgia_nluc',
            name='Diem_dat',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='danhgia_nluc',
            name='Diem_tieuchuan',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='danhgia_nluc',
            name='Ketqua_danhgia',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='danhgia_nluc',
            name='Kha_nang_dapung',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='danhgia_nluc',
            name='Quanly_danhgia',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='danhgia_nluc',
            name='tu_danhgia_dapung',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]