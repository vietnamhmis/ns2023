# Generated by Django 2.2 on 2022-11-20 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bo_phan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ma_bp', models.CharField(max_length=7, null=True)),
                ('ten_bp', models.CharField(blank=True, max_length=50, null=True)),
                ('nv_bp', models.FileField(blank=True, null=True, upload_to='CNNV_bp')),
            ],
        ),
        migrations.CreateModel(
            name='coso_KCB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ma_ckcb', models.CharField(blank=True, max_length=5, null=True)),
                ('ten_benhvien', models.CharField(blank=True, max_length=90, null=True)),
                ('dangki_KCB', models.CharField(blank=True, max_length=130, null=True)),
                ('Ghichu', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dan_toc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MA_DAN_TOC', models.CharField(max_length=5, null=True)),
                ('TEN_DAN_TOC', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Don_vi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ma_DV', models.CharField(blank=True, max_length=7, null=True)),
                ('Ten_DV', models.CharField(blank=True, max_length=50, null=True)),
                ('diachi', models.CharField(blank=True, max_length=100, null=True)),
                ('khoi_SXKD', models.CharField(blank=True, choices=[('sx', 'Sản xuất'), ('vp', 'Văn phòng'), ('kd', 'Kinh doanh'), ('BT', 'QLDA-BOT')], max_length=10, null=True)),
                ('nv_dv', models.FileField(upload_to='CNNV_dv')),
                ('so_nhanvien', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Loai_laodong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ma_loai_laodong', models.CharField(max_length=6)),
                ('name', models.CharField(max_length=170)),
            ],
        ),
        migrations.CreateModel(
            name='Loai_nangluc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Mt_laodong_41',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=270)),
                ('titrong', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('diem', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Muc_ah_cty_11',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=175)),
                ('titrong', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('diem', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Muc_ah_nv_12',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=270)),
                ('titrong', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('diem', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Muc_rui_ro_42',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=270)),
                ('titrong', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('diem', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nang_luc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('ma_nangluc', models.CharField(blank=True, max_length=4, null=True)),
                ('MoTa_nangluc', models.CharField(max_length=4000)),
                ('NL_muc_1', models.CharField(max_length=4000)),
                ('NL_muc_2', models.CharField(max_length=8000)),
                ('NL_muc_3', models.CharField(blank=True, max_length=10000, null=True)),
                ('NL_muc_4', models.CharField(blank=True, max_length=10000, null=True)),
                ('NL_muc_5', models.CharField(blank=True, max_length=10000, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('label_nang_luc', models.CharField(blank=True, choices=[('P', 'primary'), ('S', 'secondary'), ('D', 'danger'), ('I', 'info'), ('W', 'warning'), ('S', 'success'), ('g', 'good')], max_length=1, null=True)),
                ('loai_nang_luc', models.CharField(blank=True, choices=[('CL', 'Năng lực chung'), ('QL', 'Năng lực quản lý'), ('CM', 'NL Chuyên môn')], max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('num_of_products', models.IntegerField()),
                ('Ten_DV', models.CharField(blank=True, max_length=50, null=True)),
                ('diachi', models.CharField(blank=True, max_length=100, null=True)),
                ('nv_dv', models.FileField(upload_to='CNNV_dv')),
                ('so_nhanvien', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quocgia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MA_QUOC_GIA_NGUON_GOC', models.CharField(max_length=5, null=True)),
                ('TEN_QUOC_GIA', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ten_ngheDH',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ma_nghe', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=155)),
                ('dacdiem_nghe', models.CharField(max_length=155)),
                ('loai_dh', models.CharField(max_length=155)),
                ('vanban_qd', models.CharField(max_length=155)),
            ],
        ),
        migrations.CreateModel(
            name='Thanhphan_gd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('THANH_PHAN', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tinh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ma_tinh', models.CharField(blank=True, max_length=2, null=True)),
                ('TEN_TINH', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tinh_HK',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ma_tinh', models.CharField(blank=True, max_length=2, null=True)),
                ('TEN_TINH', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tinh_que',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ma_tinh', models.CharField(blank=True, max_length=2, null=True)),
                ('TEN_TINH', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tinh_sinh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ma_tinh', models.CharField(blank=True, max_length=2, null=True)),
                ('TEN_TINH', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ton_giao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TEN_TON_GIAO', models.CharField(default='Không', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='trinh_do_ct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TEN_TRINH_DO', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='trinh_do_qlnn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TEN_TRINH_DO', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trinhdo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TEN_TRINH_DO', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trinhdovh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TEN_TRINH_DO', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ycau_CNTT_24',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=270)),
                ('titrong', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('diem', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ycau_cuongdo_35',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=270)),
                ('titrong', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('diem', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ycau_doclap_33',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=270)),
                ('titrong', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('diem', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ycau_giaotiep_34',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=270)),
                ('titrong', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('diem', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ycau_k_nghiem_22',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=270)),
                ('titrong', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('diem', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ycau_kehoach_31',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=270)),
                ('titrong', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('diem', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ycau_Ngoaingu_23',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=170)),
                ('titrong', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('diem', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ycau_sangtao_32',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=270)),
                ('titrong', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('diem', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ycau_trinhdocm_21',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=270)),
                ('titrong', models.IntegerField(blank=True, null=True)),
                ('diem', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Yeu_to_1_trinh_do',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=270)),
                ('titrong', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('diem', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Yeu_to_2_Ky_nang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=270)),
                ('titrong', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('diem', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Yeu_to_3_Trach_nhiem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=270)),
                ('titrong', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('diem', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Yeu_to_4_Anh_huong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=270)),
                ('titrong', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('diem', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Yeu_to_5_Sangtao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=270)),
                ('titrong', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('diem', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Yeu_to_6_Giaotiep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=270)),
                ('titrong', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('diem', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Yeu_to_7_DK_lamviec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=270)),
                ('titrong', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('diem', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Yeu_to_khac',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=470)),
                ('titrong', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('diem', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='To_nhom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ma_to', models.CharField(blank=True, max_length=7)),
                ('ten_to', models.CharField(blank=True, max_length=50)),
                ('nv_tn', models.FileField(blank=True, upload_to='CNNV_tn')),
                ('bo_phan', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='nhansu.Bo_phan')),
            ],
        ),
        migrations.CreateModel(
            name='Quan_huyen_HK',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ma_huyen', models.CharField(blank=True, max_length=2, null=True)),
                ('Ten_quan', models.CharField(blank=True, max_length=30, null=True)),
                ('Tinh_thanh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nhansu.Tinh')),
            ],
        ),
        migrations.CreateModel(
            name='Quan_huyen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ma_huyen', models.CharField(blank=True, max_length=2, null=True)),
                ('Ten_quan', models.CharField(blank=True, max_length=30, null=True)),
                ('Tinh_thanh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nhansu.Tinh')),
            ],
        ),
        migrations.CreateModel(
            name='Phuong_xa_HK',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ma_xa', models.CharField(blank=True, max_length=5, null=True)),
                ('Ten_xa', models.CharField(max_length=30, null=True)),
                ('Quan_huyen', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nhansu.Quan_huyen')),
                ('Tinh_thanh', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nhansu.Tinh')),
            ],
        ),
        migrations.CreateModel(
            name='Phuong_xa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ma_xa', models.CharField(blank=True, max_length=5, null=True)),
                ('Ten_xa', models.CharField(max_length=30, null=True)),
                ('Quan_huyen', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nhansu.Quan_huyen')),
                ('Tinh_thanh', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nhansu.Tinh')),
            ],
        ),
        migrations.CreateModel(
            name='Nang_luc_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=70, null=True)),
                ('ma_nangluc', models.CharField(blank=True, max_length=4, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('MoTa_nangluc', models.CharField(max_length=4000)),
                ('NL_muc_1', models.CharField(max_length=4000)),
                ('NL_muc_2', models.CharField(max_length=8000)),
                ('NL_muc_3', models.CharField(max_length=10000)),
                ('NL_muc_4', models.CharField(max_length=10000)),
                ('NL_muc_5', models.CharField(max_length=10000)),
                ('ngay_tao', models.DateField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('label_nang_luc', models.CharField(blank=True, choices=[('P', 'primary'), ('S', 'secondary'), ('D', 'danger'), ('I', 'info'), ('W', 'warning'), ('S', 'success'), ('g', 'good')], max_length=1, null=True)),
                ('loai_nang_luc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nhansu.Loai_nangluc')),
            ],
            options={
                'ordering': ['loai_nang_luc', 'name'],
            },
        ),
        migrations.AddField(
            model_name='bo_phan',
            name='don_vi',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='nhansu.Don_vi'),
        ),
    ]