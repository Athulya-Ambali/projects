from django.contrib import admin
from django.http.request import HttpRequest

from .models import Sport, Turf, Slot, Booking,Hour

class SportAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False

class TurfAdmin(admin.ModelAdmin):
    # filter_horizontal = ("sports", )
    # def has_delete_permission(self, request, obj=None):
    #     return False
    pass


# Register your models here.
admin.site.register(Sport, SportAdmin)
admin.site.register(Turf, TurfAdmin)
admin.site.register(Slot)
admin.site.register(Booking)
admin.site.register(Hour)