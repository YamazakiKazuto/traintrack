from django.forms import ModelForm
#from .models import MenuPost
from django import forms
from django.forms import inlineformset_factory
from .models import MenuItem,Record#,MenuPost

#class MenuPostForm(ModelForm):
#    class Meta:
#        model = MenuPost
#        fields = ['user','title']  # ユーザーはビュー側で紐づける

class MenuItemForm(ModelForm):
    class Meta:
        model = MenuItem
        fields = ['parts','content', 'weight','rep','memo']

class HistoryForm(ModelForm):
    class Meta:
        model = Record 
        fields = ['day','parts', 'content','weight','rep','memo']
        widgets = {
            'day': forms.TextInput(attrs={
                'placeholder': 'xxxx/xx/xx/',
            }),
        }

#どうやって
# MenuPost に紐づく MenuItem を最大5件まで登録可能にする
#MenuItemFormSet = inlineformset_factory(
#    MenuPost,MenuItem,
#    form=MenuItemForm,
#    extra=3,  # 初期表示件数
#    can_delete=True
#)
