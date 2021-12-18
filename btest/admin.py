from django.contrib import admin
from .models import Mapclient
from .models import Bolnichnyepalaty
from .models import Spisokperiodov


class MapclientAdmin(admin.ModelAdmin):
   list_display = ('familija', 'name', 'otchestvo', 'nomer', 'strahovojpolis', 'datecreation','patientaddress','passportseries','passportid')
   list_display_links = ('familija', 'strahovojpolis')
   search_fields = ('familija', 'strahovojpolis', 'patientaddress', 'passportseries', 'passportid')

class BolnichnyepalatyAdmin(admin.ModelAdmin):
   list_display = ('jetazh', 'nomer', 'vmeshhaemost')
   list_display_links = ('jetazh', 'nomer')
   search_fields = ('jetazh', 'nomer', 'vmeshhaemost')

class SpisokperiodovAdmin(admin.ModelAdmin):
   list_display = ('pacient', 'datapostuplenija', 'diagnoz', 'datavypiski', 'palata')
   list_display_links = ('pacient', 'datapostuplenija')
   search_fields = ('pacient', 'diagnoz')

admin.site.register(Mapclient, MapclientAdmin)
admin.site.register(Bolnichnyepalaty, BolnichnyepalatyAdmin)
admin.site.register(Spisokperiodov, SpisokperiodovAdmin)