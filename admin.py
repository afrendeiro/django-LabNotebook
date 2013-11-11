import models
from django.contrib import admin

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class CategoryToEntryInline(admin.TabularInline):
    model = models.CategoryToEntry
    extra = 1

class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    exclude = ('author',)
    inlines = [CategoryToEntryInline]

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

admin.site.register(models.Entry, EntryAdmin)
admin.site.register(models.Category, CategoryAdmin)