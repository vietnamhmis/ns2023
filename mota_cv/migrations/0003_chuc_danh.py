# Generated by Django 2.2 on 2023-03-16 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mota_cv', '0002_auto_20230304_2209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chuc_danh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ten', models.TextField(blank=True, max_length=115, null=True)),
                ('Chuc_trach', models.TextField(blank=True, max_length=10000, null=True)),
                ('TC_daotao', models.TextField(blank=True, max_length=7000, null=True)),
                ('TC_kthuc_kn', models.TextField(blank=True, max_length=7000, null=True)),
                ('TC_khac', models.TextField(blank=True, max_length=10000, null=True)),
            ],
        ),
    ]
