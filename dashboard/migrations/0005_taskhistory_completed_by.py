# Generated by Django 4.2.14 on 2024-07-17 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_taskhistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskhistory',
            name='completed_by',
            field=models.CharField(default='None', max_length=255),
        ),
    ]