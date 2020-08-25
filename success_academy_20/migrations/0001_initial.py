# Generated by Django 3.1 on 2020-08-25 00:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cluster_name', models.CharField(max_length=255)),
                ('cluster_created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['cluster_name'],
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=255)),
                ('district_created_at', models.DateTimeField(auto_now_add=True)),
                ('district_cluster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='success_academy_20.cluster')),
                ('district_created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['district_name'],
            },
        ),
        migrations.CreateModel(
            name='DistrictGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_group_name', models.CharField(max_length=255)),
                ('district_group_created_at', models.DateTimeField(auto_now_add=True)),
                ('district_group_created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Group of Districts',
                'ordering': ['district_group_name'],
            },
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participant_firstname', models.CharField(max_length=150)),
                ('participant_lastname', models.CharField(max_length=150)),
                ('participant_title', models.CharField(choices=[('', 'Choose'), ('MR', 'MR'), ('MS', 'MISS'), ('MRS', 'MRS')], max_length=10)),
                ('participant_gender', models.CharField(choices=[('M', 'MALE'), ('FM', 'FEMALE')], max_length=10)),
                ('participant_phone_number', models.CharField(max_length=11)),
                ('participant_email', models.EmailField(max_length=254)),
                ('participant_home_address_1', models.CharField(max_length=150)),
                ('participant_home_address_2', models.CharField(max_length=150, null=True)),
                ('participant_school_name', models.CharField(max_length=255, null=True)),
                ('participant_class', models.CharField(max_length=150, null=True)),
                ('participant_church_denomination', models.CharField(max_length=255)),
                ('participant_membership_status', models.CharField(choices=[('VSR', 'VISITOR'), ('MBR', 'MEMBER'), ('WKR', 'WORKER'), ('LDR', 'LEADER'), ('PSR', 'PASTOR')], max_length=255)),
                ('participant_prayer_request', models.TextField()),
                ('participant_registration_date', models.DateTimeField(auto_now_add=True)),
                ('participant_cluster_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='success_academy_20.cluster')),
                ('participant_district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='success_academy_20.district')),
                ('participant_group_of_districts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='success_academy_20.districtgroup')),
            ],
            options={
                'ordering': ['-participant_registration_date'],
            },
        ),
        migrations.CreateModel(
            name='LGA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LGA_name', models.CharField(max_length=255)),
                ('LGA_state', models.CharField(default='OYO', max_length=150)),
                ('LGA_created_at', models.DateTimeField(auto_now_add=True)),
                ('LGA_created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['LGA_name'],
            },
        ),
        migrations.AddField(
            model_name='districtgroup',
            name='district_group_lga',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='success_academy_20.lga'),
        ),
        migrations.AddField(
            model_name='district',
            name='district_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='success_academy_20.districtgroup'),
        ),
        migrations.AddField(
            model_name='cluster',
            name='cluster_LGA',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='success_academy_20.lga'),
        ),
        migrations.AddField(
            model_name='cluster',
            name='cluster_created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cluster',
            name='cluster_district_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='success_academy_20.districtgroup'),
        ),
    ]