from django.contrib import admin

# Register your models here.

from .models import Jeux
from .models import Post


@admin.register(Jeux)
class JeuxAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'active')
    list_filter = ('active', 'date')
    search_fields = ('name',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'jeux', 'avis', 'active')

