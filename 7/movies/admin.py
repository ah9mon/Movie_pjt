from django.contrib import admin
from .models import Actor, Movie, Review

# Register your models here.

class ActorAdmin(admin.ModelAdmin):
    pass

class MovieAdmin(admin.ModelAdmin):
    pass

class ReviewAdmin(admin.ModelAdmin):
    pass

admin.site.register(Actor, ActorAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Review, ReviewAdmin)