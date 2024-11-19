# Generated by Django 5.1.3 on 2024-11-19 05:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='my_Qc_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qc_file', models.FileField(upload_to='qc')),
                ('from_date', models.CharField(max_length=100, null=True)),
                ('to_date', models.CharField(max_length=100, null=True)),
                ('start', models.IntegerField(default=0)),
                ('date', models.DateField(auto_now=True)),
                ('end', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='My_Upload_file',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('count', models.IntegerField(null=True)),
                ('o_len', models.IntegerField(null=True)),
                ('from_date', models.CharField(max_length=100, null=True)),
                ('to_date', models.CharField(max_length=100, null=True)),
                ('status', models.BooleanField(default=False)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ED_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Editor_push',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rec_length', models.IntegerField()),
                ('date', models.DateField(auto_now=True)),
                ('sta', models.BooleanField(default=False)),
                ('Editior', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='krimaApp.ed_user')),
                ('qc_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='krimaApp.my_qc_data')),
            ],
        ),
        migrations.CreateModel(
            name='Final_data_PM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('status', models.BooleanField(default=False)),
                ('Edited_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='krimaApp.editor_push')),
                ('Editior', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='krimaApp.ed_user')),
            ],
        ),
        migrations.AddField(
            model_name='my_qc_data',
            name='my_file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='krimaApp.my_upload_file'),
        ),
        migrations.CreateModel(
            name='Qc_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='my_qc_data',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='krimaApp.qc_user'),
        ),
        migrations.AddField(
            model_name='editor_push',
            name='qc_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='krimaApp.qc_user'),
        ),
        migrations.CreateModel(
            name='Doubt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sr_no', models.CharField(max_length=100)),
                ('msg', models.CharField(max_length=2000)),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='krimaApp.my_qc_data')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='krimaApp.qc_user')),
            ],
        ),
    ]
