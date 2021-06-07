from django.contrib import admin
from .models import *
from django.urls import reverse
from django.utils.html import format_html
from .tasks import clear_total_paid_task


def clear_total_paid(modeladmin, request, queryset):
    if queryset.count() >= 20:
        clear_total_paid_task.delay(modeladmin, request, queryset)
        queryset.update(salary=f'{1}')
    else:
        clear_total_paid_task(modeladmin, request, queryset)
        queryset.update(salary=f'{2}')


clear_total_paid.short_description = "Удалить информацию о выплаченной заработной плате"


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'second_name',
                    'position', 'link_to_chief', 'salary', 'total_paid',
                    )
    list_filter = ('position', 'level',)
    actions = [clear_total_paid]

    def link_to_chief(self, obj):
        link = reverse("admin:employee_employee_change", args=[obj.chief_id])
        return format_html('<a href="{}">{}</a>', link, obj.chief)

    link_to_chief.short_description = 'Начальник'


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Position)
