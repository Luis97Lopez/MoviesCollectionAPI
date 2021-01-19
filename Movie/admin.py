from django.contrib import admin
from Movie.models import Movie

class MovieAdminModel(admin.ModelAdmin):
    fields = ('name',)
    list_display = ['id', 'name']
    # list_editable = ['name']
    # list_display_links = ['name']

admin.site.register(Movie, MovieAdminModel)