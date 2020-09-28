from django.shortcuts import render
from Mes_commandes.models import OrderItem, Order
# Create your views here.

def Les_commandes (request):
    order = Order.objects.all()

    return render(request, 'mes_commandes/HTML/Main.index.html', {'orders': order})