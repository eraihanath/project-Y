# Generated by Django 4.2 on 2024-05-30 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=25)),
                ('Subject', models.CharField(max_length=34)),
                ('Message', models.TextField()),
                ('Date', models.CharField(default='DD-MM-YYYY', max_length=12)),
            ],
        ),
    ]
