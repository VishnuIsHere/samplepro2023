# Generated by Django 4.2.5 on 2023-10-13 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_rename_book_games'),
    ]

    operations = [
        migrations.CreateModel(
            name='Private',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
            ],
        ),
    ]