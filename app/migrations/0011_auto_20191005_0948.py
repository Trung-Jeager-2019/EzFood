# Generated by Django 2.2.5 on 2019-10-05 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20191005_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='image',
            field=models.ImageField(default=None, upload_to='upload'),
        ),
    ]