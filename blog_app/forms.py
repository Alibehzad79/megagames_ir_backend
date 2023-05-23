from django import forms
from blog_app.models import Comment
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ("name", "email", "text")
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'bg-black text-white border-0 p-3 rounded w-100'