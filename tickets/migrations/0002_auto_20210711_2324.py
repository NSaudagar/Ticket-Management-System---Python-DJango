# Generated by Django 3.2.5 on 2021-07-11 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='employeeId',
        ),
        migrations.AddField(
            model_name='ticket',
            name='employeeName',
            field=models.CharField(choices=[('Ajay', 'Ajay'), ('Akshay', 'Akshay'), ('Amir', 'Amir')], default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ticket',
            name='priority',
            field=models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], max_length=50),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Assigned', 'Assigned'), ('Work in Progress', 'Work in Progress'), ('Completed', 'Completed'), ('Closed', 'Closed'), ('Re-Opened', 'Re-Opened')], max_length=50),
        ),
    ]