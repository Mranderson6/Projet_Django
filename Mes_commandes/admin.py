from django.contrib import admin
from Mes_commandes.models import OrderItem, Ville, Mode_Payement, Quartier


# Register your models here.
class commandeAdmin(admin.ModelAdmin):
    list_display = ['code', 'nom', 'confirmer']
    list_filter = ['nom', 'vendeur']

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    exclude = ["product"]
    # readonly_fields = ["nom", "price", "quantity"]
    extra = 0

class VilleAdmin(admin.ModelAdmin):
    """"""


admin.site.register(Ville, VilleAdmin)


class Mode_PayementAdmin(admin.ModelAdmin):
    """"""


admin.site.register(Mode_Payement, Mode_PayementAdmin)
admin.site.register(OrderItem, commandeAdmin)

