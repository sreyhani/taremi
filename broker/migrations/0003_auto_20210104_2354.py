# Generated by Django 2.2.7 on 2021-01-04 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0002_auto_20210104_0049'),
    ]

    operations = [
        migrations.CreateModel(
            name='LongAnswer',
            fields=[
                ('answer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='broker.Answer')),
                ('value', models.TextField(verbose_name='long_text_value')),
            ],
            bases=('broker.answer',),
        ),
        migrations.CreateModel(
            name='LongQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='broker.Question')),
            ],
            bases=('broker.question',),
        ),
        migrations.AlterField(
            model_name='numericalanswer',
            name='value',
            field=models.IntegerField(default=0, verbose_name='int_value'),
        ),
    ]
