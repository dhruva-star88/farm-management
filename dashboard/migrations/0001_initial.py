# Generated by Django 4.2.14 on 2024-07-13 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment', models.CharField(choices=[('plough', 'Plough'), ('seed-drill', 'Seed Drill'), ('sprayer', 'Sprayer'), ('harvester', 'Harvester')], max_length=20)),
                ('status', models.CharField(choices=[('available', 'Available'), ('un_available', 'Un-Available')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SupplierDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier', models.CharField(choices=[('supplier1', 'Supplier 1'), ('supplier2', 'Supplier 2'), ('supplier3', 'Supplier 3'), ('supplier4', 'Supplier 4')], max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='WorkerDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='TaskDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(choices=[('ploughing', 'Ploughing'), ('sowing', 'Sowing'), ('watering', 'Watering'), ('harvesting', 'Harvesting')], max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('equipment_required', models.ManyToManyField(related_name='tasks', to='dashboard.equipmentdetails')),
                ('task_assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.workerdetails')),
            ],
        ),
        migrations.AddField(
            model_name='equipmentdetails',
            name='supplied_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipment_supplied', to='dashboard.supplierdetails'),
        ),
        migrations.CreateModel(
            name='CropDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crop', models.CharField(choices=[('wheat', 'Wheat'), ('rice', 'Rice'), ('maize', 'Maize'), ('millet', 'Millet')], max_length=20)),
                ('planting_date', models.DateField()),
                ('harvesting_date', models.DateField()),
                ('task_assigned', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.taskdetails')),
            ],
        ),
    ]
