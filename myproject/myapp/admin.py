from django.contrib import admin

from .models import Team, Person, Osoba, Stanowisko 

class OsobaAdmin(admin.ModelAdmin):
    list_display = ['name', 'nazwisko']
    readonly_fields = ['data_dodania']

class StanowiskoAdmin(admin.ModelAdmin):
    list_display = ['nazwa']

admin.site.register(Team)
admin.site.register(Person)
admin.site.register(Osoba, OsobaAdmin)
admin.site.register(Stanowisko, StanowiskoAdmin)
