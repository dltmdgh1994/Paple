from django import forms
from account.models import Group


class ModifyGroupInfoForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['group_name', 'group_img', 'group_link']
        labels = {
            'group_name': 'Group name',
            'group_img': 'Group Image',
            'group_link': 'Group Number'
        }
        widgets = {
            'group_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'group_link': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'readonly': True
                }
            )
        }


