from django.contrib import admin
from .models import Equipment

class EquipmentAdmin(admin.ModelAdmin):

    class Meta:
        model = Equipment

    def save_model(self, request, obj, form, change):
        obj.save()


admin.site.register(Equipment, EquipmentAdmin)
