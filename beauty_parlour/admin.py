from django.contrib import admin

from .models import Master, Services, Request
# from modeltranslation.admin import TranslationAdmin
# from ckeditor.widgets import CKEditorWidget
# from django import forms


# class MasterClassForm(forms.ModelForm):
    
#     class Meta:
#         model = Master
#         fields = ['name', 'information', 'experience', 'position']
        
        
# @admin.register(Theme)
# class ThemesAdmin(TranslationAdmin):
#     list_display = ['title',]


# @admin.register(MasterClass)
# class MasterClassAdmin(TranslationAdmin):
#     form = MasterClassForm
#     list_display = ['title', 'themes', 'created']
#     list_filter = ['created', 'themes']
#     search_fields = ['title', 'overview']


admin.site.register(Master)
admin.site.register(Services)
admin.site.register(Request)
