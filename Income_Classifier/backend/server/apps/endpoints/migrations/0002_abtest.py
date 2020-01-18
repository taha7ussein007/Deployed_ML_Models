# Generated by Django 2.2.5 on 2020-01-18 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ABTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10000)),
                ('created_by', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ended_at', models.DateTimeField(blank=True, null=True)),
                ('summary', models.CharField(blank=True, max_length=10000, null=True)),
                ('parent_mlalgorithm_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_mlalgorithm_1', to='endpoints.MLAlgorithm')),
                ('parent_mlalgorithm_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_mlalgorithm_2', to='endpoints.MLAlgorithm')),
            ],
        ),
    ]
