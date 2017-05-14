from django import forms
from django_yaba import widgets
from .models import Story,Article,Gallery


class StoryAdminForm(forms.ModelForm):
    body=forms.CharField(widget=widgets.TinyMCEWidget())
    class Meta:
        model = Story
        fields = "__all__"


class ArticleAdminForm(forms.ModelForm):
    body=forms.CharField(widget=widgets.TinyMCEWidget())
    class Meta:
        model = Article
        fields = "__all__"


class GalleryAdminForm(forms.ModelForm):
    body=forms.CharField(widget=widgets.TinyMCEWidget())
    class Meta:
        model = Gallery
        fields = "__all__"

