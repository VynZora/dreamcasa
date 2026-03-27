from django.db import migrations, models
from django.utils.text import slugify


def populate_nearbyplace_slug(apps, schema_editor):
    NearByPlace = apps.get_model('dream_casa_app', 'NearByPlace')
    for place in NearByPlace.objects.all():
        if place.slug:
            continue
        base = slugify(place.name) if place.name else 'nearby-place'
        candidate = base
        counter = 1
        while NearByPlace.objects.filter(slug=candidate).exclude(pk=place.pk).exists():
            counter += 1
            candidate = f"{base}-{counter}"
        place.slug = candidate
        place.save(update_fields=['slug'])


def noop_reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('dream_casa_app', '0009_chatmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='nearbyplace',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.RunPython(populate_nearbyplace_slug, noop_reverse),
    ]
