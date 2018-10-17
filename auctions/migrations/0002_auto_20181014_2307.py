# Generated by Django 2.0.6 on 2018-10-15 06:07

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailQueue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('auction', models.ForeignKey(blank=True, null=True, on_delete=None, to='auctions.Auction')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='bid',
            name='email_sent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bid',
            name='email_sent_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='emailqueue',
            name='bid',
            field=models.ForeignKey(blank=True, null=True, on_delete=None, to='auctions.Bid'),
        ),
    ]