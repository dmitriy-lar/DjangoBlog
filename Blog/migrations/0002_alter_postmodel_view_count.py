# Generated by Django 4.0.5 on 2022-06-30 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='view_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
