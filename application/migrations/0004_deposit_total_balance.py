# Generated by Django 5.0.1 on 2024-03-02 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_deposit_delete_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='total_balance',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]