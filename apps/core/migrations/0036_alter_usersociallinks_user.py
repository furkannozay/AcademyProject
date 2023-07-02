# Generated by Django 4.2.2 on 2023-07-02 15:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0035_remove_users_social_links_usersociallinks_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersociallinks',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_links', to=settings.AUTH_USER_MODEL, verbose_name='Üye'),
        ),
    ]
