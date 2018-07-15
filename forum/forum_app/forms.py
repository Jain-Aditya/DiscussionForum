from django import forms

class DiscussionForm(forms.Form):
    discussion = forms.CharField(label='Create discussion', max_length=1500)

class CommentForm(forms.Form):
    comment = forms.CharField(label='Add Comment', max_length=1500)    
   