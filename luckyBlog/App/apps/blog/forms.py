# @Author: lucky
# @Date:   2017-04-29T22:42:34+08:00
# @Last modified by:   lucky
# @Last modified time: 2017-04-29T23:47:39+08:00



from django import forms

class CommentForm(forms.Form):
    url = forms.CharField(required = True)
    body = forms.CharField(required = True)

class ReplyForm(forms.Form):
    commentid = forms.CharField(required = True)
    body = forms.CharField(required = True)
