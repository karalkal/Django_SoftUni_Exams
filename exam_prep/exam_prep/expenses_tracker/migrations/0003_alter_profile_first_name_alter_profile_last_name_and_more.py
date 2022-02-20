# Generated by Django 4.0.2 on 2022-02-18 20:33

import django.core.validators
from django.db import migrations, models
import exam_prep.expenses_tracker.validators


class Migration(migrations.Migration):

    dependencies = [
        ('expenses_tracker', '0002_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), exam_prep.expenses_tracker.validators.verify_letters_only]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), exam_prep.expenses_tracker.validators.verify_letters_only]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/', validators=[exam_prep.expenses_tracker.validators.CheckMaxSizeInMb(5)]),
        ),
    ]