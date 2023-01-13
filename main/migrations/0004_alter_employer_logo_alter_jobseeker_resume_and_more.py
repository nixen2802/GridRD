# Generated by Django 4.1 on 2023-01-13 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_jobseeker_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='logo',
            field=models.ImageField(default=None, null=True, upload_to='logos/'),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='Resume',
            field=models.FileField(default=None, null=True, upload_to='resumes/'),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='photo',
            field=models.ImageField(default=None, null=True, upload_to='photos/'),
        ),
    ]
