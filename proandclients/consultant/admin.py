from django.contrib import admin
from .models import Consultant

@admin.register(Consultant)
class ConsultantAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'profession', 'rate', 'experience')
    search_fields = ('name', 'expertise', 'profession')
    list_filter = ('gender', 'country', 'language')
