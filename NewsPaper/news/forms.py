from django.forms import ModelForm, BooleanField
from .models import Post


class PostForm(ModelForm):
    check_box = BooleanField(label='подтвердить')

    class Meta:
        model = Post
        fields = ['title', 'text', 'category', 'author_post', 'post_news', 'check_box']
