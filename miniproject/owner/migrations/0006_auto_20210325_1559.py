# Generated by Django 3.1.7 on 2021-03-25 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0005_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='Type',
        ),
        migrations.AlterField(
            model_name='menu',
            name='Price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='menu',
            name='Type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owner.category'),
        ),
    ]
