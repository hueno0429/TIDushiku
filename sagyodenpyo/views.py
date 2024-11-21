from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import WorkLog
from .forms import WorkLogForm

from django.contrib.auth.views import LogoutView
class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        """GET リクエストでもログアウトを許可"""
        return self.post(request, *args, **kwargs)


@login_required
def log_work(request):
    if request.method == "POST":
        form = WorkLogForm(request.POST)
        if form.is_valid():
            work_log = form.save(commit=False)
            work_log.employee = request.user.employee  # ログイン中の従業員を紐付け
            work_log.save()
            return redirect('work_log_list')
    else:
        form = WorkLogForm()
    return render(request, 'sagyodenpyo/log_work.html', {'form': form})

@login_required
def edit_work_log(request, pk):
    work_log = get_object_or_404(WorkLog, pk=pk, employee=request.user.employee)
    if request.method == "POST":
        form = WorkLogForm(request.POST, instance=work_log)
        if form.is_valid():
            form.save()
            return redirect('work_log_list')
    else:
        form = WorkLogForm(instance=work_log)
    return render(request, 'sagyodenpyo/edit_work_log.html', {'form': form})

from django.http import HttpResponseForbidden

@login_required
def work_log_list(request):
    try:
        employee = request.user.employee
    except Employee.DoesNotExist:
        return HttpResponseForbidden("このユーザーには対応する従業員情報がありません。管理者に問い合わせてください。")

    work_logs = WorkLog.objects.filter(employee=employee).order_by('-date')
    return render(request, 'sagyodenpyo/work_log_list.html', {'work_logs': work_logs})

# 全員の作業履歴を取得し、日付ごとにグループ化してテンプレートに渡すビュー
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import WorkLog
from django.db.models import Prefetch
from itertools import groupby
from operator import itemgetter

@login_required
def all_work_logs_by_date(request):
    # 全ての作業履歴を日付順に取得
    work_logs = WorkLog.objects.select_related('employee').order_by('date', 'employee__name')

    # 日付ごとにグループ化
    grouped_logs = {}
    for date, logs in groupby(work_logs, key=lambda log: log.date):
        grouped_logs[date] = list(logs)

    return render(request, 'sagyodenpyo/all_work_logs_by_date.html', {'grouped_logs': grouped_logs})

#for CSV download
import csv
from django.http import HttpResponse
from .models import WorkLog

@login_required
def export_work_logs_csv(request):
    # Shift-JIS 対応のレスポンス設定
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="work_logs.csv"'

    # Shift-JIS でエンコードされた CSV データを生成
    writer = csv.writer(response, quoting=csv.QUOTE_MINIMAL)

    # ヘッダー行（日本語）
    header = ['従業員名', '工番', '件名', '作業コード', '作業時間', '作業日']
    response.write(",".join(header).encode('shift_jis') + b"\r\n")

    # データ行
    work_logs = WorkLog.objects.select_related('employee').all()
    for log in work_logs:
        row = [
            log.employee.name,
            log.work_number,
            log.subject,
            log.work_code,
            str(log.work_hours),
            log.date.strftime("%Y-%m-%d"),
        ]
        response.write(",".join(row).encode('shift_jis') + b"\r\n")

    return response




