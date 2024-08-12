# Generated by Django 5.0.6 on 2024-07-30 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_teacherrequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacherrequest',
            name='approved',
        ),
        migrations.RemoveField(
            model_name='teacherrequest',
            name='rejected',
        ),
        migrations.AddField(
            model_name='teacherrequest',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending', max_length=10),
        ),
    ]
