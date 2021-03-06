# Generated by Django 3.1.3 on 2020-11-24 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('EmployeeId', models.AutoField(primary_key=True, serialize=False)),
                ('EmployeeName', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('Phone', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Image', models.ImageField(upload_to='gallery')),
            ],
        ),
    ]
