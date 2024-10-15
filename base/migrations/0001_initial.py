# Generated by Django 5.0.9 on 2024-10-13 23:32

import django.db.models.deletion
import uuid
import wagtail.fields
import wagtail.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0094_alter_page_locale'),
        ('wagtailimages', '0026_delete_uploadedimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='NavigationContentSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_url', models.URLField(blank=True, null=True, verbose_name='Facebook Profile Link')),
                ('whatsapp_url', models.URLField(blank=True, null=True, verbose_name='Whatsapp Group URL')),
                ('twitter_url', models.URLField(blank=True, null=True, verbose_name='Twitter Profile Link')),
                ('linkedin_url', models.URLField(blank=True, null=True, verbose_name='LinkedIn Profile Link')),
                ('instagram_url', models.URLField(blank=True, null=True, verbose_name='Instagram Profile Link')),
                ('youtube_url', models.URLField(blank=True, null=True, verbose_name='Youtube Profile Link')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FooterContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('translation_key', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('live', models.BooleanField(default=True, editable=False, verbose_name='live')),
                ('has_unpublished_changes', models.BooleanField(default=False, editable=False, verbose_name='has unpublished changes')),
                ('first_published_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='first published at')),
                ('last_published_at', models.DateTimeField(editable=False, null=True, verbose_name='last published at')),
                ('go_live_at', models.DateTimeField(blank=True, null=True, verbose_name='go live date/time')),
                ('expire_at', models.DateTimeField(blank=True, null=True, verbose_name='expiry date/time')),
                ('expired', models.BooleanField(default=False, editable=False, verbose_name='expired')),
                ('heading_title', wagtail.fields.RichTextField(blank=True)),
                ('footer_body', wagtail.fields.RichTextField(blank=True)),
                ('image', models.ForeignKey(blank=True, help_text='Portrait mode only, recommended at least 300 x 300 px Transparent Background', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('latest_revision', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.revision', verbose_name='latest revision')),
                ('live_revision', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.revision', verbose_name='live revision')),
                ('locale', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailcore.locale', verbose_name='locale')),
            ],
            options={
                'verbose_name': 'footer content',
                'verbose_name_plural': 'footer contents',
                'abstract': False,
                'unique_together': {('translation_key', 'locale')},
            },
            bases=(wagtail.models.PreviewableMixin, models.Model),
        ),
        migrations.CreateModel(
            name='FooterContentSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('footer_content', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='base.footercontent')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
