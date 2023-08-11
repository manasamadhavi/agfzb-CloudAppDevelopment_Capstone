from django.contrib import admin
from .models import CarMake, CarModel 


# Register your models here.
class CarModelInline(admin.StackedInline):
    model = CarModel
# CarModelInline class

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('car_model', 'dealerId', 'type', 'car_year')
    list_filter = ['dealerId']
    search_fields = ['car_model']
# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ('car_make',)
    list_filter = ['car_make']
    search_fields = ['car_make', 'description']
# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)