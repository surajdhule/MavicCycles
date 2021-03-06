# Generated by Django 2.2.14 on 2020-09-25 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Cycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=50)),
                ('cycle_img_main', models.ImageField(default='', upload_to='cycles/images')),
                ('cycle_img_sub1', models.ImageField(default='', upload_to='cycles/images')),
                ('cycle_img_sub2', models.ImageField(default='', upload_to='cycles/images')),
                ('cycle_img_sub3', models.ImageField(default='', upload_to='cycles/images')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cycles.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daily_rental', models.IntegerField()),
                ('weekly_rental', models.IntegerField()),
                ('monthly_rental', models.IntegerField()),
                ('cycle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cycles.Cycle')),
            ],
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cycle_type', models.CharField(max_length=40)),
                ('frame_material', models.CharField(max_length=40)),
                ('frame_size', models.CharField(max_length=40)),
                ('suspension', models.CharField(max_length=40)),
                ('brake_type', models.CharField(max_length=40)),
                ('number_of_speeds', models.CharField(max_length=40)),
                ('wheel_size', models.CharField(max_length=40)),
                ('cycle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cycles.Cycle')),
            ],
        ),
    ]
