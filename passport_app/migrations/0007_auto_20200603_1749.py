# Generated by Django 2.2.5 on 2020-06-03 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passport_app', '0006_auto_20200528_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='', max_length=1024),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_ru',
            field=models.CharField(default='', max_length=1024),
        ),
        migrations.AlterField(
            model_name='category',
            name='point',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
    ]
