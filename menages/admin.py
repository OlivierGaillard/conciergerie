from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from django_mptt_admin.admin import DjangoMpttAdmin
# from mptt_tree_editor.admin import TreeEditor  Bug pour Python 3.5
from .models import Sejour, Work, TissueCategory, Tissue, WorkCategory

admin.site.register(Sejour)
admin.site.register(Work)
admin.site.register(Tissue)

class TissueCategoryAdmin(DjangoMpttAdmin):
    list_display = ['title',]

admin.site.register(TissueCategory, TissueCategoryAdmin)

class WorkCategoryAdmin(DjangoMpttAdmin):
    list_display = ['title',]

admin.site.register(WorkCategory, WorkCategoryAdmin)
# Register your models here.
