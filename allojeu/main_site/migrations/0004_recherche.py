# Generated by Django 4.2.7 on 2023-12-01 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0003_alter_post_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recherche',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recherche', models.TextField(null=True)),
            ],
        ),
    ]