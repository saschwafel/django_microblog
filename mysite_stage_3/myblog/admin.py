from django.contrib import admin
from myblog.models import Post, Category

class CategoryInline(admin.StackedInline):
    model = Category.posts.through

class CategoryAdmin(admin.ModelAdmin):
    print 'Cats -', Category._meta.get_all_field_names()
    exclude = ['posts']
#    pass

class PostAdmin(admin.ModelAdmin):
    print 'Posts -', Post._meta.get_all_field_names()
    readonly_fields = ('created_date', 'modified_date')
    inlines = [CategoryInline]
    list_display = ('title', 'author', 'created_date', 'modified_date')
    list_display_links = ('author',)
#    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
