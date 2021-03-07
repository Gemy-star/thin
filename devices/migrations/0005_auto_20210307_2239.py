# Generated by Django 3.1.7 on 2021-03-07 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0004_remove_thindevicesunits_updated_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='thindevicesunits',
            name='category',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='thindevicesunits',
            name='cdb',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='thindevicesunits',
            name='database_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='thindevicesunits',
            name='database_zone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='thindevicesunits',
            name='epg',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='thindevicesunits',
            name='short_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]