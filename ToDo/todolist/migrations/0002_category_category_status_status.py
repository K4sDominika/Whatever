# Generated by Django 4.1.7 on 2023-03-12 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('NEW', 'unassigned'), ('URGENT_AND_IMPORTANT', 'urgent and important'), ('URGENT_AND_NOT_IMPORTANT', 'urgent and not important'), ('URGENT_BUT_NOT_IMPORTANT', 'urgent but not important'), ('NOT_URGENT_AND_NOT_IMPORTANT', 'not urgent and not important')], default='NEW', max_length=100),
        ),
        migrations.AddField(
            model_name='status',
            name='status',
            field=models.CharField(choices=[('NOT_STARTED_YET', 'not started yet'), ('IN_PROGRESS', 'in progress'), ('PENDING', 'pending'), ('DONE', 'done')], default='NOT_STARTED_YET', max_length=50),
        ),
    ]
