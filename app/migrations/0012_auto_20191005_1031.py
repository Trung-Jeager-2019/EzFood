# Generated by Django 2.2.5 on 2019-10-05 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20191005_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='active',
            field=models.CharField(default='yes', max_length=5),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='image',
            field=models.ImageField(default='default.svg', upload_to='upload'),
        ),
    ]
