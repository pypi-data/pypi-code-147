# Generated by Django 4.1.5 on 2023-01-12 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            'music',
            '0004_alter_artist_options_alter_album_musicbrainz_id_and_more',
        ),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='cover_image',
            field=models.ImageField(
                blank=True, null=True, upload_to='albums/'
            ),
        ),
    ]
