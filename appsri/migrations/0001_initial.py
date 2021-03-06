# Generated by Django 2.2.6 on 2019-11-08 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField()),
                ('res', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cate', models.CharField(max_length=30)),
                ('catee', models.ImageField(upload_to='cimg/')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('citys', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countrys', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Industries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indus', models.CharField(max_length=30)),
                ('ind', models.ImageField(upload_to='iimg/')),
            ],
        ),
        migrations.CreateModel(
            name='Interested',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobuser', models.IntegerField()),
                ('jobs', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Jobtype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobtype', models.CharField(max_length=30)),
                ('jobtt', models.ImageField(upload_to='jimg/')),
            ],
        ),
        migrations.CreateModel(
            name='Shortlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listuser', models.IntegerField()),
                ('listres', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('states', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=30)),
                ('userr_id', models.CharField(max_length=30)),
                ('frist', models.CharField(max_length=30)),
                ('second', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('designation', models.CharField(max_length=30)),
                ('experience', models.CharField(max_length=30)),
                ('expectpa', models.CharField(max_length=30)),
                ('skill', models.CharField(max_length=30)),
                ('photo', models.FileField(upload_to='file/')),
                ('resumess', models.FileField(upload_to='file/')),
                ('birth', models.DateField()),
                ('address', models.CharField(max_length=30)),
                ('zipcode', models.IntegerField()),
                ('highest', models.CharField(max_length=30)),
                ('year', models.IntegerField()),
                ('company', models.CharField(max_length=30)),
                ('disg', models.CharField(max_length=30)),
                ('dafrom', models.DateField()),
                ('dato', models.DateField()),
                ('facebook', models.CharField(max_length=30)),
                ('google', models.CharField(max_length=30)),
                ('twiteer', models.CharField(max_length=30)),
                ('linkedin', models.CharField(max_length=30)),
                ('Pinterest', models.CharField(max_length=30)),
                ('instagram', models.CharField(max_length=30)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appsri.Category')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appsri.City')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appsri.Country')),
                ('industt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appsri.Industries')),
                ('jobtypeeee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appsri.Jobtype')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appsri.State')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usrejob', models.CharField(max_length=30)),
                ('jobtitle', models.CharField(max_length=30)),
                ('cname', models.CharField(max_length=30)),
                ('position', models.CharField(max_length=30)),
                ('vacacy', models.IntegerField()),
                ('package', models.CharField(max_length=30)),
                ('logo', models.FileField(upload_to='file/')),
                ('minqul', models.CharField(max_length=30)),
                ('skills', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('website', models.CharField(max_length=30)),
                ('adrres', models.CharField(max_length=30)),
                ('zip', models.IntegerField()),
                ('facebook', models.CharField(max_length=30)),
                ('google', models.CharField(max_length=30)),
                ('twiteer', models.CharField(max_length=30)),
                ('linkedin', models.CharField(max_length=30)),
                ('Pinterest', models.CharField(max_length=30)),
                ('instagram', models.CharField(max_length=30)),
                ('cata', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appsri.Category')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appsri.City')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appsri.Country')),
                ('exper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appsri.Experience')),
                ('jobtypee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appsri.Jobtype')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appsri.State')),
            ],
        ),
    ]
