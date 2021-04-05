# Generated by Django 3.1.7 on 2021-03-26 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0008_auto_20210325_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='category',
            field=models.CharField(choices=[('Veg', 'Veg'), ('Non-Veg', 'Non-Veg')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='Email',
            field=models.EmailField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='Name',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='Roll',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='Username',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
