# Generated by Django 2.2.5 on 2019-11-12 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_client_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.CharField(default=1, max_length=64, verbose_name='Почта'),
            preserve_default=False,
        ),
    ]