# Generated by Django 4.0.1 on 2022-01-11 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=0, max_length=10)),
                ('image', models.ImageField(blank=True, max_length=254, upload_to='media/')),
            ],
        ),
    ]