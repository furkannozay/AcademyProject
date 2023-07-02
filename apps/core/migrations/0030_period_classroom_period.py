# Generated by Django 4.2.2 on 2023-07-02 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_users_force_password_change'),
    ]

    operations = [
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')),
                ('name', models.CharField(max_length=120, verbose_name='İsim')),
            ],
            options={
                'verbose_name': 'Dönem',
                'verbose_name_plural': 'Dönemler',
                'db_table': 'periods',
            },
        ),
        migrations.AddField(
            model_name='classroom',
            name='period',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.period', verbose_name='Dönem'),
        ),
    ]
