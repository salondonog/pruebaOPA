# Generated by Django 3.2.5 on 2022-12-31 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Excursion', '0002_auto_20221231_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elemento',
            name='ID',
            field=models.PositiveSmallIntegerField(auto_created=True, max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='selelemento',
            name='ID',
            field=models.PositiveSmallIntegerField(auto_created=True, max_length=50, primary_key=True, serialize=False),
        ),
    ]