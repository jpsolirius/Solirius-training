from django import forms
from blog.models import Post, Category

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )

class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, member):
        return "%s" % member.name

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'categories')
    categories = CustomMMCF(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple
        )
