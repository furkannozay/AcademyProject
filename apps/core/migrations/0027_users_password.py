# Generated by Django 4.2.2 on 2023-06-29 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_remove_issues_category_delete_issuecategories_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='password',
            field=models.CharField(default=123123, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]
