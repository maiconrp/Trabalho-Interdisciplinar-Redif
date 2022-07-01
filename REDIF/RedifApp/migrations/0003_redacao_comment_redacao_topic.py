# Generated by Django 4.0.3 on 2022-07-01 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RedifApp', '0002_redacao_delete_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='redacao',
            name='comment',
            field=models.CharField(blank=True, default=None, max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='redacao',
            name='topic',
            field=models.CharField(default='topic', max_length=45),
        ),
    ]