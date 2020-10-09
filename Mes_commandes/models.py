from django.db import models

#from shop.models import Product
import string
import random


def get_random_code(length=12):
    length = length
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(length))


class Ville(models.Model):
    name = models.CharField(max_length=150, db_index=True, verbose_name="ville", default="", unique=True)

    class Meta:
        verbose_name = 'Ville'
        verbose_name_plural = 'Villes'

    def __str__(self):
        return self.name


class Quartier(models.Model):
    name = models.CharField(max_length=150, db_index=True, verbose_name="ville", default="", unique=True)
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE)
    SHIRT_SIZES = (
        ('zone 1', ' zone 1'),
        ('zone 2', ' zone 2'),
        ('zone 3', ' zone 3'),
    )
    zone = models.CharField(max_length=150, db_index=True, choices=SHIRT_SIZES, default='zone 1')
    prix_livraison = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Quartier'
        verbose_name_plural = 'Quartiers'

    def __str__(self):
        return self.name


class Mode_Payement(models.Model):
    SHIRT_SIZES = (
        (' à la livraison', ' à la livraison'),
        ('Mobile money', 'Mobile money'),
        ('paypal', 'paypal'),
        ('carte de crédit', 'carte de crédit'),
        ('Bitcoin', 'Bitcoin'),
    )
    mode = models.CharField(max_length=150, db_index=True, verbose_name="paiement", choices=SHIRT_SIZES)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Mode De Paiement'
        verbose_name_plural = 'Modes De Paiements'

    def __str__(self):
        return self.mode


class Order(models.Model):
    SHIRT_SIZES = (
        ('à domicile : par nawa delivery ', 'à domicile : Par nawa delivery'),
        ('à domicile : par le vendeur', ' à domicile : par le vendeur'),
        ('pas besoin de livraison', 'pas besoin de livraison'),
    )
    code = models.CharField(max_length=12, verbose_name="Code", unique=True)
    nom = models.CharField(max_length=120)
    prenom = models.CharField(max_length=120, default="")
    email = models.EmailField(blank=True)
    tel = models.CharField(max_length=150)
    tel2 = models.CharField(max_length=150, blank=True, help_text="numéro optinelle")
    livraison = models.CharField(max_length=100, db_index=True, choices=SHIRT_SIZES,
                                 default='à domicile : Par nawa delivery')
    ville = models.ForeignKey(Ville, related_name='villes', on_delete=models.CASCADE)
    quartier = models.CharField(max_length=100, default="")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    payement = models.ForeignKey(Mode_Payement, related_name='Mode_Payement', on_delete=models.CASCADE, default=1,
                                 verbose_name="Paiement")
    total = models.IntegerField(verbose_name="prix total de la commande", default=0)
    reduct = models.DecimalField(max_digits=10, decimal_places=1, verbose_name="prix total de réduction", default=0)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Commande'
        verbose_name_plural = 'Commandes'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def save(self, *args, **kwargs):
        if self.code == "":
            self.code = "%s" % (get_random_code())
        else:
            pass
        super().save(*args, **kwargs)  # Call the "real" save() method.


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
   # product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    code = models.CharField(max_length=10, default="")
    nom = models.CharField(max_length=100, default="")
    vendeur = models.CharField(max_length=100, default="")
    price = models.IntegerField()
    quantity = models.PositiveIntegerField(default=1)
    confirmer = models.BooleanField(default=False)
    payer = models.BooleanField(default=False)
    annuler = models.BooleanField(default=False)
    confier_votre = models.BooleanField(default=False, verbose_name='confier votre liraison', help_text="confier votre liraison à bekeymarkets")
    prix_livraison = models.IntegerField(verbose_name="prix de la livraison",
                                         help_text="Laisser vide temps que la commande n'est pas payer ", default=0)
    livraison_day = models.DateTimeField(
        "Jour de livraison de la commande ", blank=True, null=True,
        help_text="Laisser vide temps que la commande n'est pas payer ")
    total = models.IntegerField(verbose_name="prix total", default=0)

    class Meta:
        verbose_name = 'Produit De La Commande'
        verbose_name_plural = 'Produits De La Commande'

    def __str__(self):
        return '{}'.format(self.code)

    def get_cost(self):
        return self.price * self.quantity

    def save(self, *args, **kwargs):
        self.code = self.product.code
        self.vendeur = self.product.boutique
        self.nom = self.product.name
        self.total = (self.price * self.quantity)+self.prix_livraison
        # mise à jour de la facture totale
        item_1 = OrderItem.objects.filter(order=self.order)
        totale_facture = []
        for i in item_1:
            totale_facture.append(i.total)
        commande = Order.objects.filter(id=self.order.id)
        commande.update(total=sum(totale_facture))
        # mise à jour des item du meme vendeur
        item = OrderItem.objects.filter(order=self.order).filter(vendeur=self.vendeur)
        for i in item:
            OrderItem.objects.filter(id=i.id).update(confirmer=self.confirmer, payer=self.payer, livraison_day=self.livraison_day)
        super().save(*args, **kwargs)  # Call the "real" save() method.