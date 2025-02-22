# Generated by Django 5.1.1 on 2024-11-16 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_cc', '0015_event_local'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProblemaReportado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plantio', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('data_reporte', models.DateTimeField(auto_now_add=True)),
                ('resolvido', models.BooleanField(default=False)),
            ],
        ),
    ]
