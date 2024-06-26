# Generated by Django 4.2.11 on 2024-04-12 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='github',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='telegram',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='twitter',
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='contact_method',
            field=models.CharField(blank=True, choices=[('email', 'Email'), ('discussion', 'Discussion page'), ('wiki', 'Meta-Wiki talk page'), ('IRC', 'IRC')], max_length=10, verbose_name='Preferred contact method'),
        ),
    ]
