# Generated by Django 2.2 on 2021-04-20 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('story_text', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Stories',
            },
        ),
    ]
