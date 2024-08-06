from django.contrib import admin
from .models import HomeModel, ElectronicItem, ReportModel


class HomeSearch(admin.ModelAdmin):
    search_fields = ('home_owner',)


class ElectronicSearch(admin.ModelAdmin):
    search_fields = ('item',)


class ReportSearch(admin.ModelAdmin):
    search_fields = ('report_type',)


admin.site.register(HomeModel, HomeSearch,
                    list_display=['home_owner', 'home_address', 'home_electronic', 'phone_number', 'connected_telegram',
                                  'date_joined', 'last_updated'])
admin.site.register(ElectronicItem, ElectronicSearch, list_display=['item', 'related_home'])
admin.site.register(ReportModel, ReportSearch, list_display=['report_type', 'report_description', 'report_file'])
