# Generated by Django 3.0.5 on 2023-02-24 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('massage', models.CharField(max_length=10000)),
            ],
        ),
        migrations.DeleteModel(
            name='contactus',
        ),
    ]
