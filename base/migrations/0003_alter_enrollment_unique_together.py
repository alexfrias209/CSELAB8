# Generated by Django 4.1.7 on 2023-04-07 03:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_course_students_course_schedule_enrollment'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='enrollment',
            unique_together={('student', 'course')},
        ),
    ]
