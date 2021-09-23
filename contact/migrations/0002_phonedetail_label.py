# Generated by Django 3.2.7 on 2021-09-22 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonedetail',
            name='label',
            field=models.CharField(choices=[('mobile', 'Mobile'), ('home', 'Home'), ('work', 'Work'), ('main', 'Main'), ('fax', 'Fax')], default='mobile', max_length=10),
        ),
    ]