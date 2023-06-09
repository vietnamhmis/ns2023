# Generated by Django 2.2 on 2022-12-29 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('luong', '0002_hd_laodong_hieuluc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamcong',
            name='Ngay_1',
            field=models.CharField(blank=True, default='X', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='chamcong',
            name='Ngay_2',
            field=models.CharField(blank=True, default='X', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='chamcongchitiet',
            name='Nam',
            field=models.CharField(blank=True, choices=[('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025')], default='2022', max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='chamcongchitiet',
            name='Ngay_1',
            field=models.CharField(blank=True, choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='chamcongchitiet',
            name='Ngay_10',
            field=models.CharField(blank=True, choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='chamcongchitiet',
            name='Ngay_11',
            field=models.CharField(blank=True, choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='chamcongchitiet',
            name='Ngay_12',
            field=models.CharField(blank=True, choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='chamcongchitiet',
            name='Ngay_13',
            field=models.CharField(blank=True, choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='chamcongchitiet',
            name='Ngay_14',
            field=models.CharField(blank=True, choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='chamcongchitiet',
            name='Ngay_15',
            field=models.CharField(blank=True, choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='chamcongchitiet',
            name='Ngay_16',
            field=models.CharField(blank=True, choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='chamcongchitiet',
            name='Ngay_17',
            field=models.CharField(blank=True, choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='chamcongchitiet',
            name='Ngay_18',
            field=models.CharField(blank=True, choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='chamcongchitiet',
            name='Ngay_19',
            field=models.CharField(blank=True, choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='chamcongchitiet',
            name='Ngay_2',
            field=models.CharField(blank=True, choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='chamcongchitiet',
            name='Ngay_20',
            field=models.CharField(blank=True, choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='chamcongchitiet',
            name='Ngay_21',
            field=models.CharField(blank=True, choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='chamcongchitiet',
            name='Ngay_22',
            field=models.CharField(blank=True, choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='chamcongchitiet',
            name='Ngay_23',
            field=models.CharField(blank=True, choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='chamcongchitiet',
            name='Ngay_24',
            field=models.CharField(blank=True, choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='chamcongchitiet',
            name='Ngay_25',
            field=models.CharField(blank=True, choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='chamcongchitiet',
            name='Ngay_26',
            field=models.CharField(blank=True, choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='chamcongchitiet',
            name='Ngay_27',
            field=models.CharField(blank=True, choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='chamcongchitiet',
            name='Ngay_28',
            field=models.CharField(blank=True, choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='chamcongchitiet',
            name='Ngay_29',
            field=models.CharField(blank=True, choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='chamcongchitiet',
            name='Ngay_3',
            field=models.CharField(blank=True, choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='chamcongchitiet',
            name='Ngay_30',
            field=models.CharField(blank=True, choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='chamcongchitiet',
            name='Ngay_31',
            field=models.CharField(blank=True, choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='chamcongchitiet',
            name='Ngay_4',
            field=models.CharField(blank=True, choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='chamcongchitiet',
            name='Ngay_5',
            field=models.CharField(blank=True, choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='chamcongchitiet',
            name='Ngay_6',
            field=models.CharField(blank=True, choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='chamcongchitiet',
            name='Ngay_7',
            field=models.CharField(blank=True, choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='chamcongchitiet',
            name='Ngay_8',
            field=models.CharField(blank=True, choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='chamcongchitiet',
            name='Ngay_9',
            field=models.CharField(blank=True, choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='chamcongchitiet',
            name='Nhan_vien',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='enroll.Nhan_vien'),
        ),
        migrations.AlterField(
            model_name='chamcongchitiet',
            name='thang',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], default='4', max_length=2, null=True),
        ),
    ]
