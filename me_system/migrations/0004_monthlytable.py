# Generated by Django 4.1.4 on 2022-12-28 18:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('me_system', '0003_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='thematic name')),
                ('month', models.DateField(default=django.utils.timezone.now, verbose_name='Date')),
                ('intro', models.TextField(max_length=200, verbose_name='introduction')),
                ('project1', models.CharField(max_length=200, verbose_name='project1')),
                ('project2', models.CharField(max_length=200, verbose_name='project2')),
                ('num_accomplished', models.IntegerField(verbose_name='number of accomplished')),
                ('activity_list', models.CharField(max_length=200, verbose_name='activit list')),
                ('num_not_accomplished', models.CharField(max_length=200, verbose_name='unaccomplished number')),
                ('unaccomplished_list', models.CharField(max_length=200, verbose_name='unacomplished list')),
                ('num_reason', models.CharField(max_length=200, verbose_name='number of reasons')),
                ('reason_list', models.CharField(max_length=200, verbose_name='reason list')),
                ('lesson', models.TextField(max_length=200, verbose_name='lesson learned')),
                ('challenges', models.TextField(max_length=200, verbose_name='Challenges')),
                ('share', models.CharField(max_length=200, verbose_name='share by')),
            ],
        ),
    ]