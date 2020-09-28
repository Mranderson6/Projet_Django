from django.contrib import admin
from Blog.models import Categorie, Article, contact_image


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date','categorie','apercu_contenu')
    list_filter = ('auteur', 'categorie',)
    fields = ('titre', 'slug', 'auteur', 'categorie', 'contenu')
    prepopulated_fields = {'slug': ('titre',), }
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('titre', 'contenu')

    def apercu_contenu(self, article):
         text = article.contenu[0:40]
         if len(article.contenu) > 40:
            return '%s...' % text
         else:
          return text

class contactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'addresse')
    fields = ('nom', 'addresse', 'photo')
    search_fields = ('nom', 'addresse')


admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)
admin.site.register(contact_image,contactAdmin)
