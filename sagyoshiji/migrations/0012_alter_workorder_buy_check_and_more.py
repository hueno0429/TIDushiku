# Generated by Django 5.1.5 on 2025-03-10 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sagyoshiji', '0011_workorder_buy_check_workorder_publish_check_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workorder',
            name='buy_check',
            field=models.CharField(default='', max_length=30, verbose_name='購買確認'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='publish_check',
            field=models.CharField(default='', max_length=30, verbose_name='作成'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='recive_check',
            field=models.CharField(default='', max_length=30, verbose_name='受け取り確認'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='syounin_check',
            field=models.CharField(default='', max_length=30, verbose_name='承認'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='workset_check',
            field=models.CharField(default='', max_length=30, verbose_name='工数設定'),
        ),
    ]
