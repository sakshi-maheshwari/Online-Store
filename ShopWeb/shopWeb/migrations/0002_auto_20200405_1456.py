# Generated by Django 3.0.4 on 2020-04-05 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopWeb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField()),
                ('Product_Image', models.ImageField(upload_to='')),
                ('Category', models.CharField(max_length=150)),
                ('Description', models.TextField()),
                ('Price', models.CharField(max_length=150)),
            ],
        ),
        migrations.DeleteModel(
            name='AcademicCourseComplaint',
        ),
        migrations.DeleteModel(
            name='Complaint',
        ),
    ]
