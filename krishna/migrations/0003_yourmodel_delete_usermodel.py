# Generated by Django 4.0.3 on 2023-12-10 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krishna', '0002_rename_yourmodel_usermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='YourModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='UserModel',
        ),
    ]
