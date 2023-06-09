# Generated by Django 2.2 on 2023-02-12 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nangluc', '0020_studentdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Danhgia_nluc_thu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Landanhgia_nagluc', models.CharField(blank=True, max_length=20, null=True)),
                ('tu_danhgia_dapung', models.IntegerField(blank=True, null=True)),
                ('Ketqua_danhgia', models.IntegerField(blank=True, null=True)),
                ('start_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('TenNangluc_congviec', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nangluc.Congviec_nangluc')),
            ],
        ),
    ]
