# Generated by Django 4.2 on 2023-08-08 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agmcms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agmprograms',
            name='program_attached_file_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
