# Generated by Django 4.2.7 on 2023-12-01 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0004_recherche'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=90)),
                ('name', models.CharField(max_length=90)),
                ('email', models.EmailField(max_length=254)),
                ('content', models.TextField(null=True)),
            ],
        ),
    ]