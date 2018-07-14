from django import forms

class DiscussionForm(forms.Form):
    discussion_text = forms.CharField(label='Create discussion', max_length=1500)