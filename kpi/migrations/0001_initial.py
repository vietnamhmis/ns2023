# Generated by Django 2.2 on 2022-11-20 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enroll', '0001_initial'),
        ('mota_cv', '0001_initial'),
        ('nhansu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='dmkpi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ten_KPI', models.CharField(blank=True, max_length=500)),
                ('Don_vi_tinh', models.CharField(choices=[('dg', 'Tỷ đồng'), ('kwx', 'kwh/tấn xi măng'), ('kwc', 'kcal/kg clanhke'), ('kwx', 'tr.đồng/người'), ('kwx', 'Tấn'), ('kwx', 'ngày'), ('kg', 'kg'), ('sk', 'sk'), ('%', '%')], default='%', max_length=20, null=True)),
                ('Tan_xuat_d_gia', models.CharField(choices=[('th', 'Tháng'), ('qu', 'Quý'), ('na', 'Năm')], default='Tháng', max_length=20, null=True)),
                ('Ti_trong', models.DecimalField(decimal_places=1, max_digits=5)),
                ('Ngaytao', models.DateTimeField(auto_now_add=True)),
                ('Ngay_update', models.DateTimeField(auto_now=True)),
                ('LoaiCV', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mota_cv.Mota_Cv')),
            ],
            options={
                'ordering': ['-id', 'LoaiCV'],
            },
        ),
        migrations.CreateModel(
            name='Don_vi_tinh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Don_vi_tinh', models.TextField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Phan_KPI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Diem_manh', models.TextField(blank=True, max_length=10, null=True)),
                ('Nguoigiao', models.CharField(blank=True, max_length=5, null=True)),
                ('Ti_trong', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('Chitieu', models.IntegerField(blank=True, null=True)),
                ('Ketqua_cn', models.IntegerField(blank=True, null=True)),
                ('ketqua_dv', models.IntegerField(blank=True, null=True)),
                ('ketqua_cuoi', models.IntegerField(blank=True, null=True)),
                ('ti_le_ht', models.IntegerField(blank=True, null=True)),
                ('diem_CV', models.IntegerField(blank=True, null=True)),
                ('diemtrongso', models.IntegerField(blank=True, null=True)),
                ('Cap_KPI', models.IntegerField(blank=True, null=True)),
                ('Dv_quanly_KPI', models.TextField(max_length=10)),
                ('KPI_cha', models.IntegerField(blank=True)),
                ('Vien_canh_cluoc', models.CharField(choices=[('tc', 'VC Tài chính'), ('kh', 'VC Khách hàng'), ('nb', 'VC Quy trình nội bộ'), ('hh', 'VC Học hỏi, phát triển')], max_length=20, null=True)),
                ('Mtieu_cluoc', models.TextField(blank=True, max_length=55, null=True)),
                ('Tan_xuat_d_gia', models.CharField(choices=[('th', 'Tháng'), ('qu', 'Quý'), ('na', 'Năm')], max_length=20, null=True)),
                ('Chi_tieu_c_bo', models.TextField(blank=True, max_length=5, null=True)),
                ('Don_vi_nhan_c_bo', models.TextField(blank=True, max_length=5, null=True)),
                ('Cviec_phan_KPI', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mota_cv.Mota_Cv')),
                ('DVi_giao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='nhansu.Bo_phan')),
                ('DVi_nhan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nhansu.To_nhom')),
                ('Don_vi_tinh', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='kpi.Don_vi_tinh')),
                ('Nguoi_nhan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='enroll.Nhan_vien')),
                ('Ten_KPI', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='kpi.dmkpi')),
            ],
        ),
        migrations.CreateModel(
            name='List_kpi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Don_vi_tinh', models.CharField(choices=[('dg', 'Tỷ đồng'), ('kwx', 'kwh/tấn xi măng'), ('kwc', 'kcal/kg clanhke'), ('kwx', 'tr.đồng/người'), ('kwx', 'Tấn'), ('kwx', 'ngày'), ('kg', 'kg'), ('sk', 'sk'), ('%', '%')], default='%', max_length=20, null=True)),
                ('Tan_xuat_d_gia', models.CharField(choices=[('th', 'Tháng'), ('qu', 'Quý'), ('na', 'Năm')], default='Tháng', max_length=20, null=True)),
                ('Ti_trong', models.DecimalField(decimal_places=1, max_digits=5)),
                ('Ngaytao', models.DateTimeField(auto_now_add=True)),
                ('Ngay_update', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField()),
                ('LoaiCV', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mota_cv.Mota_Cv')),
            ],
            options={
                'ordering': ['-id', 'LoaiCV'],
            },
        ),
        migrations.CreateModel(
            name='giao_KPI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ky_giao_KPI', models.TextField(blank=True, max_length=10, null=True)),
                ('Nguoigiao', models.CharField(blank=True, max_length=5, null=True)),
                ('Ti_trong', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('Chitieu', models.IntegerField(blank=True, null=True)),
                ('Ketqua_cn', models.IntegerField(blank=True, null=True)),
                ('ketqua_dv', models.IntegerField(blank=True, null=True)),
                ('ketqua_cuoi', models.IntegerField(blank=True, null=True)),
                ('ti_le_ht', models.IntegerField(blank=True, null=True)),
                ('diem_CV', models.IntegerField(blank=True, null=True)),
                ('diemtrongso', models.IntegerField(blank=True, null=True)),
                ('Cap_KPI', models.IntegerField(blank=True, null=True)),
                ('Dv_quanly_KPI', models.TextField(max_length=10)),
                ('KPI_cha', models.IntegerField(blank=True)),
                ('Vien_canh_cluoc', models.CharField(choices=[('tc', 'VC Tài chính'), ('kh', 'VC Khách hàng'), ('nb', 'VC Quy trình nội bộ'), ('hh', 'VC Học hỏi, phát triển')], max_length=20, null=True)),
                ('Mtieu_cluoc', models.TextField(blank=True, max_length=55, null=True)),
                ('Tan_xuat_d_gia', models.CharField(choices=[('th', 'Tháng'), ('qu', 'Quý'), ('na', 'Năm')], max_length=20, null=True)),
                ('Chi_tieu_c_bo', models.TextField(blank=True, max_length=5, null=True)),
                ('Don_vi_nhan_c_bo', models.TextField(blank=True, max_length=5, null=True)),
                ('Cviec_phan_KPI', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mota_cv.Mota_Cv')),
                ('DVi_giao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='nhansu.Bo_phan')),
                ('DVi_nhan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nhansu.To_nhom')),
                ('Don_vi_tinh', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='kpi.Don_vi_tinh')),
                ('Nguoi_nhan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='enroll.Nhan_vien')),
                ('Ten_KPI', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='kpi.dmkpi')),
            ],
        ),
        migrations.CreateModel(
            name='Dmkpi_dv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ma_KPo', models.TextField(blank=True, max_length=10, null=True)),
                ('Ten_KPo', models.TextField(max_length=255)),
                ('Ten_KPI', models.TextField(max_length=305)),
                ('Don_vi_tinh', models.CharField(choices=[('dg', 'Tỷ đồng'), ('kwx', 'kwh/tấn xi măng'), ('kwc', 'kcal/kg clanhke'), ('kwx', 'tr.đồng/người'), ('kwx', 'Tấn'), ('kwx', 'ngày'), ('kg', 'kg'), ('sk', 'sk'), ('%', '%')], max_length=20, null=True)),
                ('Chitieu_KPI', models.IntegerField(blank=True)),
                ('Ti_trong', models.DecimalField(blank=True, decimal_places=1, max_digits=5)),
                ('Cap_KPI', models.IntegerField(blank=True, null=True)),
                ('Vien_canh_cluoc', models.CharField(choices=[('tc', 'VC Tài chính'), ('kh', 'VC Khách hàng'), ('nb', 'VC Quy trình nội bộ'), ('hh', 'VC Học hỏi, phát triển')], max_length=20, null=True)),
                ('Tan_xuat_d_gia', models.CharField(choices=[('th', 'Tháng'), ('qu', 'Quý'), ('na', 'Năm')], max_length=20, null=True)),
                ('Ngay_update', models.DateTimeField(auto_now=True)),
                ('Dv_quanly_KPI', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='nhansu.Don_vi')),
            ],
            options={
                'ordering': ['-id', 'Ten_KPI'],
            },
        ),
    ]
