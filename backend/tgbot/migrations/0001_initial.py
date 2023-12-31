# Generated by Django 4.2.7 on 2023-11-11 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdsChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ads_chats',
            },
        ),
        migrations.CreateModel(
            name='Method',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True)),
            ],
            options={
                'db_table': 'methods',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.PositiveBigIntegerField(unique=True)),
                ('full_name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=128, null=True)),
            ],
            options={
                'db_table': 'telegram_users',
            },
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tgbot.method')),
            ],
            options={
                'db_table': 'fields',
                'unique_together': {('method', 'name')},
            },
        ),
    ]
