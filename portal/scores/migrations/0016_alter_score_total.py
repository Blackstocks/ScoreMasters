# Generated by Django 4.2.9 on 2024-01-27 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0015_remove_score_panel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='total',
            field=models.FloatField(default=None),
        ),
    ]