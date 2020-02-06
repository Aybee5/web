# Generated by Django 2.2.4 on 2020-01-18 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('townsquare', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='view_count',
            field=models.IntegerField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='offer',
            name='key',
            field=models.CharField(choices=[('secret', 'secret'), ('random', 'random'), ('daily', 'daily'), ('weekly', 'weekly'), ('monthly', 'monthly'), ('other', 'other')], db_index=True, max_length=50),
        ),
    ]
