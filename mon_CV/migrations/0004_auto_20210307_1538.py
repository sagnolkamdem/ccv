# Generated by Django 3.0.3 on 2021-03-07 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mon_CV', '0003_auto_20210307_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formation',
            name='text_intro',
            field=models.TextField(blank=True),
        ),
    ]
