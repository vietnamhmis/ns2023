# Generated by Django 2.2 on 2022-12-18 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nangluc', '0003_tong_nl_nhanvien_dg_nangluc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tong_nl',
            name='items',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nangluc.Danhgia_nluc'),
        ),
    ]
