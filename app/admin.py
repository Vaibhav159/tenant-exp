from django.contrib import admin

from app.models import Client, Domain


class PublicMixin(admin.ModelAdmin):
    def has_view_permission(self, request, obj=None):
        return request.tenant.schema_name == 'public'

    def has_change_permission(self, request, obj=None):
        return request.tenant.schema_name == 'public'

    def has_delete_permission(self, request, obj=None):
        return request.tenant.schema_name == 'public'

    def has_add_permission(self, request):
        return request.tenant.schema_name == 'public'


# Register your models here.

@admin.register(Client)
class ClientAdmin(PublicMixin):
    pass


@admin.register(Domain)
class DomainAdmin(PublicMixin):
    pass
