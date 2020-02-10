# Generated by Django 3.0.1 on 2020-01-29 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0006_auto_20200128_1738'),
    ]

    operations = [
        migrations.CreateModel(
            name='acousticdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acousticdatatype', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='assemblymethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assemblymethodtype', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='condition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conditiontype', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='cutsofwood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cutsofwoodtype', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='edges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edgestype', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='glasstreatment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('glasstreatmenttype', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='included',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('includedtype', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ISratings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isratingstype', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locationtype', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='materials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materialstype', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='metal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metaltype', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='metalaging',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metalagingtype', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='metalfinishes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metalfinishestype', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='metaltexture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metaltexturetype', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='origin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origintype', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='suitability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suitabilitytype', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='timber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timbertype', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='timberfinishes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timberfinishestype', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='transparency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transparencytype', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='thing',
            name='age',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='thing',
            name='careinstructions',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='thing',
            name='maximumweightcapacity',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='thing',
            name='overallproductweight',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='thing',
            name='productwarranty',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='thing',
            name='reflectionfactor',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='thing',
            name='specialimageblock',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='thing',
            name='thickness',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='thing',
            name='ISratings',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='things', to='Library.ISratings'),
        ),
        migrations.AddField(
            model_name='thing',
            name='acousticdata',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='things', to='Library.acousticdata'),
        ),
        migrations.AddField(
            model_name='thing',
            name='assemblymethod',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='things', to='Library.assemblymethod'),
        ),
        migrations.AddField(
            model_name='thing',
            name='condition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='things', to='Library.condition'),
        ),
        migrations.AddField(
            model_name='thing',
            name='cutsofwood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='things', to='Library.cutsofwood'),
        ),
        migrations.AddField(
            model_name='thing',
            name='edges',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='things', to='Library.edges'),
        ),
        migrations.AddField(
            model_name='thing',
            name='glasstreatment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='things', to='Library.glasstreatment'),
        ),
        migrations.AddField(
            model_name='thing',
            name='included',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='things', to='Library.included'),
        ),
        migrations.AddField(
            model_name='thing',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='things', to='Library.location'),
        ),
        migrations.AddField(
            model_name='thing',
            name='materials',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='things', to='Library.materials'),
        ),
        migrations.AddField(
            model_name='thing',
            name='metal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='things', to='Library.metal'),
        ),
        migrations.AddField(
            model_name='thing',
            name='metalaging',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='things', to='Library.metalaging'),
        ),
        migrations.AddField(
            model_name='thing',
            name='metalfinishes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='things', to='Library.metalfinishes'),
        ),
        migrations.AddField(
            model_name='thing',
            name='metaltexture',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='things', to='Library.metaltexture'),
        ),
        migrations.AddField(
            model_name='thing',
            name='origin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='things', to='Library.origin'),
        ),
        migrations.AddField(
            model_name='thing',
            name='suitability',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='things', to='Library.suitability'),
        ),
        migrations.AddField(
            model_name='thing',
            name='timber',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='things', to='Library.timber'),
        ),
        migrations.AddField(
            model_name='thing',
            name='timberfinishes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='things', to='Library.timberfinishes'),
        ),
        migrations.AddField(
            model_name='thing',
            name='transparency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='things', to='Library.transparency'),
        ),
    ]