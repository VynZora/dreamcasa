from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return [
            'index', 'about', 'contact', 'booking', 'rooms',
            'room_details', 'near_by_places', 'our_gallery',
        ]

    def location(self, item):
        return reverse(item)


from .models import NearByPlace  # Make sure this matches your actual model name

class NearbyPlaceSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return NearByPlace.objects.all()

    def location(self, obj):
        return reverse('near_by_place_details', args=[obj.id])