# Generated by Django 2.0.7 on 2018-07-30 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('muduryardimci', '0004_auto_20180730_2013'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SignUpForm',
        ),
        migrations.AlterField(
            model_name='note',
            name='site_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Note_site_id', to='muduryardimci.Site'),
        ),
    ]
