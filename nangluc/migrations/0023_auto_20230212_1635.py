# Generated by Django 2.2 on 2023-02-12 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nangluc', '0022_auto_20230212_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='danhgia_nluc_thu',
            name='TenNangluc_congviec',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
