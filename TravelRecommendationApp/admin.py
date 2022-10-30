from django.contrib import admin
from .models import DreamDestination, RecommendedDestination_tag, RecommendedDestination_cat
# Register your models here.

admin.site.register(DreamDestination)
admin.site.register(RecommendedDestination_tag)
admin.site.register(RecommendedDestination_cat)