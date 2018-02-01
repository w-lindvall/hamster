from django.contrib import admin
from ideas.models import Medium, Idea


class MediumAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Medium, MediumAdmin)
admin.site.register(Idea)
