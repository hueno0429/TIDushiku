from django.db import models

class WorkOrder(models.Model):
    work_order_number = models.PositiveIntegerField("作業指示票番号", unique=True)  # 7桁の整数
    work_number = models.CharField("工番", max_length=20)  # 英数字20文字
    subject = models.CharField("件名", max_length=20)  # 漢字20文字
    process_pattern = models.CharField("製造工程パタン", max_length=10)  # 英数字10文字
    manager = models.CharField("製造管理担当者", max_length=20)  # 漢字20文字
    work_hours = models.DecimalField("作業工数時間", max_digits=4, decimal_places=1)  # 小数点以下1桁
    next_process = models.CharField("次工程", max_length=20)  # 漢字20文字
    start_date = models.DateField("作業開始日")
    end_date = models.DateField("終了予定日")

    def __str__(self):
        return f"{self.work_order_number} - {self.subject}"

    class Meta:
        verbose_name = "作業指示票"
        verbose_name_plural = "作業指示票"

class WorkOrderProgress(models.Model):
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE, related_name="progresses")
    work_date = models.DateField("作業日")
    achievement = models.DecimalField("出来高（％）", max_digits=5, decimal_places=2)
    daily_result = models.DecimalField("当日実績", max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.work_order} - {self.work_date}"

    class Meta:
        verbose_name = "作業進捗"
        verbose_name_plural = "作業進捗"
