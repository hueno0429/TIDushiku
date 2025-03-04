from django import forms
from django.forms.models import inlineformset_factory
from .models import WorkOrder, WorkOrderProgress

class WorkOrderForm(forms.ModelForm):
    class Meta:
        model = WorkOrder
        fields = [
            'work_order_number', 'release_date', 'work_number', 'work_trenum', 'subject', 
            'process_pattern', 'manager', 'work_group', 'work_hours', 
            'next_process', 'start_date', 'end_date', 'work_type', 'work_range', 'planed_value',
        ]
        labels = {
            'work_order_number': '作業指示票番号',
            'release_date': '発行日',
            'work_number': '工番',
            'work_trenum': '枝番',
            'subject': '件名',
            'process_pattern': '製造工程パタン',
            'manager': '製造管理担当者',
            'work_group': '製作グループ',
            'work_hours': '作業工数時間',
            'next_process': '次工程',
            'start_date': '作業開始日',
            'end_date': '終了予定日',
            'work_type': '作業種別',
            'work_range': '作業範囲',
            'planed_value': '計画数',
        }
        widgets = {
            'release_date': forms.TextInput(attrs={'type': 'date'})  # HTML5の日付入力ウィジェット
        }

# 作業進捗用のフォームセット
WorkOrderProgressFormSet = inlineformset_factory(
    WorkOrder, WorkOrderProgress,
    fields=('work_date', 'achievement', 'daily_result', ),
    extra=12,  # 12個分のフォームを表示
    max_num=12,
    can_delete=False
)
