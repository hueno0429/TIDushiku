from django import forms
from .models import WorkLog

class WorkLogForm(forms.ModelForm):
    class Meta:
        model = WorkLog
        fields = ['date', 'work_number', 'subject', 'work_code', 'work_hours']
        labels = {
            'date': '作業日',
            'work_number': '工番',
            'subject': '件名',
            'work_code': '作業コード',
            'work_hours': '作業時間 (小数点以下1桁)',
        }
        widgets = {
            'date': forms.TextInput(attrs={'type': 'date'})  # HTML5の日付入力ウィジェット
        }
