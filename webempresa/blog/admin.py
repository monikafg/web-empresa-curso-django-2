from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display=('title','author','published', 'post_categories')
    ordering = ('author', 'published')  # Si solo dejamos un campo de ordenación tenemos que dejar la coma también sino no funciona
    search_fields = ('title', 'content', 'author__username', 'categories__name')
    date_hierarchy = 'published'
    list_filter = ('author__username', 'categories__name')

    #Para mostrar campos con relaciones ManyToMany
    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorías"


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

