from django.contrib import admin


class ReadOnlyAdmin(admin.ModelAdmin):
    readonly_fields = (
        'created_at', 'modified_at', 'created_by', 'modified_by'
    )

class ReadOnlyStackedInline(admin.StackedInline):
    readonly_fields = (
        'created_at', 'modified_at', 'created_by', 'modified_by'
    )

class ReadOnlyTabularInline(admin.TabularInline):
    readonly_fields = (
        'created_at', 'modified_at', 'created_by', 'modified_by'
    )