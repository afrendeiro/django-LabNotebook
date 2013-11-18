import models
from django.contrib import admin

class NotebookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    exclude = ('author',)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


admin.site.register(models.Notebook, NotebookAdmin)
admin.site.register(models.Entry, EntryAdmin)
admin.site.register(models.Category, CategoryAdmin)