# Generated by Django 4.2 on 2023-04-07 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutwhereweoperate',
            name='branch_text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aboutwhereweoperate',
            name='coorprate_office',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aboutwhereweoperate',
            name='national_secretariat',
            field=models.TextField(),
        ),
    ]
