# Generated by Django 4.2.7 on 2024-06-10 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Icons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
