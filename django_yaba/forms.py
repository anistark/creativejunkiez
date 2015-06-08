from django import forms
from django_yaba import widgets
from .models import Story,Article,Gallery


class StoryAdminForm(forms.ModelForm):
    body=forms.CharField(widget=widgets.TinyMCEWidget())
    class Meta:
        model = Story


class ArticleAdminForm(forms.ModelForm):
    body=forms.CharField(widget=widgets.TinyMCEWidget())
    class Meta:
        model = Article


class GalleryAdminForm(forms.ModelForm):
    body=forms.CharField(widget=widgets.TinyMCEWidget())
    class Meta:
        model = Gallery

