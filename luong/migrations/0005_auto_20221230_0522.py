# Generated by Django 2.2 on 2022-12-29 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('luong', '0004_auto_20221230_0516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamcongchitiet',
            name='Nhan_vien',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='enroll.Nhan_vien'),
        ),
    ]
