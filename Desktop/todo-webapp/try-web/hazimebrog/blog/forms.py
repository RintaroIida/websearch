from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'intro','execution_date']
        labels = {
            'title': 'タイトル',
            'intro': '詳細',
            'execution_date': '実行日'
        }
        widgets = {
            'execution_date': forms.DateInput(attrs={'type': 'date'})  # カレンダーウィジェットを追加
        }

