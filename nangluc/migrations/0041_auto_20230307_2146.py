# Generated by Django 2.2 on 2023-03-07 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nangluc', '0040_auto_20230307_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdata',
            name='Diem_tu_danhgia',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
