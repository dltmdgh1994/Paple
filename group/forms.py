from django import forms
from account.models import Group


class ModifyGroupInfoForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['group_name', 'group_code']
        labels = {
            'group_name': 'Group Name',
            'group_code': 'Group Code'
        }
        widgets = {
            'group_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'group_code': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'readonly': True
                }
            )
        }


class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ['group_name', 'group_code']

        labels = {
            'group_name': '그룹명',
            'group_code': '그룹 코드'
        }

        widgets = {
            'group_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'group_code': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }
