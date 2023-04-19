# Generated by Django 2.2 on 2022-11-20 16:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enroll', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nhansu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bangluong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nhom_luong', models.CharField(max_length=20, null=True)),
                ('Heso', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Bac', models.CharField(choices=[('Bậc 1', 'Bậc 1'), ('Bậc 2', 'Bậc 2'), ('Bậc 3', 'Bậc 3'), ('Bậc 4', 'Bậc 4'), ('Bậc 5', 'Bậc 5'), ('Bậc 6', 'Bậc 6'), ('Bậc 7', 'Bậc 7'), ('Bậc 8', 'Bậc 8'), ('Bậc 9', 'Bậc 9'), ('Bậc 10', 'Bậc 10')], max_length=20, null=True)),
                ('Boiso', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Muc_luong', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Chamcongchitiet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thang', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], default='4', max_length=2, null=True)),
                ('Nam', models.CharField(choices=[('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025')], default='2022', max_length=4, null=True)),
                ('Ngay_1', models.CharField(choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True)),
                ('Ngay_2', models.CharField(choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True)),
                ('Ngay_3', models.CharField(choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True)),
                ('Ngay_4', models.CharField(choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True)),
                ('Ngay_5', models.CharField(choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True)),
                ('Ngay_6', models.CharField(choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True)),
                ('Ngay_7', models.CharField(choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True)),
                ('Ngay_8', models.CharField(choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True)),
                ('Ngay_9', models.CharField(choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True)),
                ('Ngay_10', models.CharField(choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True)),
                ('Ngay_11', models.CharField(choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True)),
                ('Ngay_12', models.CharField(choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True)),
                ('Ngay_13', models.CharField(choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True)),
                ('Ngay_14', models.CharField(choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True)),
                ('Ngay_15', models.CharField(choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True)),
                ('Ngay_16', models.CharField(choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True)),
                ('Ngay_17', models.CharField(choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True)),
                ('Ngay_18', models.CharField(choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True)),
                ('Ngay_19', models.CharField(choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True)),
                ('Ngay_20', models.CharField(choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True)),
                ('Ngay_21', models.CharField(choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True)),
                ('Ngay_22', models.CharField(choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True)),
                ('Ngay_23', models.CharField(choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True)),
                ('Ngay_24', models.CharField(choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True)),
                ('Ngay_25', models.CharField(choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True)),
                ('Ngay_26', models.CharField(choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True)),
                ('Ngay_27', models.CharField(choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True)),
                ('Ngay_28', models.CharField(choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True)),
                ('Ngay_29', models.CharField(choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True)),
                ('Ngay_30', models.CharField(choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True)),
                ('Ngay_31', models.CharField(choices=[('Ô', 'Ốm, điều dưỡng'), ('X', 'làm việc')], default='X', max_length=3, null=True)),
                ('Ngay_truc24', models.CharField(choices=[('T', 'Trực'), ('N', 'Nghỉ')], default='Trực', max_length=6, null=True)),
                ('Ngay_cong', models.IntegerField(blank=True, null=True)),
                ('Ngaycham', models.DateField(blank=True, null=True)),
                ('Nhan_vien', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='enroll.Nhan_vien')),
                ('bo_phan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nhansu.Bo_phan')),
                ('don_vi', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nhansu.Don_vi')),
                ('to_nhom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nhansu.To_nhom')),
            ],
        ),
        migrations.CreateModel(
            name='hd_laodong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('So_hopdong', models.CharField(max_length=20, null=True)),
                ('Hoten_nhanvien', models.CharField(blank=True, default='Họ tên', max_length=150, null=True)),
                ('Loai_hd', models.CharField(choices=[('Có thời hạn', 'Có thời hạn'), ('Không thời hạn', 'Không thời hạn'), ('Thử việc', 'Thử việc')], default='Không thời hạn', max_length=20, null=True)),
                ('Tu_ngay', models.DateField(blank=True, null=True)),
                ('Den_ngay', models.DateField(blank=True, null=True)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('Ht_traluong', models.CharField(choices=[('Khoán', 'Khoán'), ('Thời gian', 'Thời gian'), ('Sản phẩm', 'Sản phẩm')], default='Khoán', max_length=20, null=True)),
                ('Heso', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Bac', models.CharField(max_length=10, null=True)),
                ('Muc_luong', models.IntegerField(blank=True, null=True)),
                ('Loai_hd_kth', models.BooleanField(default=True)),
                ('Loai_hd_coth', models.BooleanField(default=False)),
                ('Loai_hd_thu_viec', models.BooleanField(default=False)),
                ('Nang_luong', models.BooleanField(default=False)),
                ('Dieudong', models.BooleanField(default=False)),
                ('Bo_nhiem', models.BooleanField(default=False)),
                ('Ly_do', models.CharField(max_length=10, null=True)),
                ('Ngay_nangluong_sau', models.DateField(auto_now_add=True)),
                ('Thu_nhap', models.IntegerField(blank=True, null=True)),
                ('Ho_ten', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='enroll.Nhan_vien')),
                ('bangluong', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='luong.bangluong')),
            ],
            options={
                'ordering': ['Tu_ngay', 'id'],
            },
        ),
        migrations.CreateModel(
            name='nhanvientest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_danhmuc', models.CharField(blank=True, max_length=60, null=True)),
                ('kyhieu_cc', models.CharField(blank=True, max_length=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='luongthang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Thang_tra_luong', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], default='2', max_length=2, null=True)),
                ('Nam', models.CharField(blank=True, choices=[('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025')], default='2022', max_length=4, null=True)),
                ('Muc_luongBHXH', models.IntegerField(blank=True, null=True)),
                ('Tam_ung', models.IntegerField(blank=True, null=True)),
                ('Muc_luong', models.IntegerField(blank=True, null=True)),
                ('luong_p2', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('luong_p3', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Gio_lam_them', models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True)),
                ('Gio_lam_them_CT', models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True)),
                ('Gio_lam_them_le', models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True)),
                ('phucap_knhiem', models.IntegerField(blank=True, null=True)),
                ('phucap_khac', models.IntegerField(blank=True, null=True)),
                ('Tien_an', models.IntegerField(blank=True, null=True)),
                ('Luong_thang', models.IntegerField(blank=True, null=True)),
                ('Ngay_cong', models.IntegerField(blank=True, null=True)),
                ('Boiduong_dochai', models.IntegerField(blank=True, null=True)),
                ('Thu_nhap', models.IntegerField(blank=True, null=True)),
                ('kn_thuetncn', models.IntegerField(blank=True, null=True)),
                ('kn_BHXH_BYTT', models.IntegerField(blank=True, null=True)),
                ('kn_KPCĐ', models.IntegerField(blank=True, null=True)),
                ('kn_khac', models.IntegerField(blank=True, null=True)),
                ('luong_themgio', models.IntegerField(blank=True, null=True)),
                ('Luong_lamthemT7', models.IntegerField(blank=True, null=True)),
                ('Luong_lamthemle', models.IntegerField(blank=True, null=True)),
                ('Thu_nhapthuclinh', models.IntegerField(blank=True, null=True)),
                ('Heso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='luong.hd_laodong')),
                ('bo_phan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nhansu.Bo_phan')),
                ('cham_cong', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='luong.Chamcongchitiet')),
                ('don_vi', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nhansu.Don_vi')),
                ('hoten_nhanvien', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='enroll.Nhan_vien')),
                ('to_nhom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nhansu.To_nhom')),
            ],
        ),
        migrations.CreateModel(
            name='DmChamcong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_danhmuc', models.CharField(blank=True, max_length=60, null=True)),
                ('kyhieu_cc', models.CharField(blank=True, max_length=6, null=True)),
                ('nhanvien', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='luong.nhanvientest')),
            ],
        ),
        migrations.CreateModel(
            name='Chamcong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kyhieu_cc', models.CharField(blank=True, max_length=6, null=True)),
                ('Ngay_1', models.CharField(default='X', max_length=3, null=True)),
                ('Ngay_2', models.CharField(default='X', max_length=3, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
