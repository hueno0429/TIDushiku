from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    employee_number = models.CharField("従業員番号", max_length=10, unique=True)
    name = models.CharField("氏名", max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="employee")

    def __str__(self):
        return self.name

class WorkLog(models.Model):
    WORK_CODE_CHOICES = [
        ('001', '材料受け入れ'),
        ('002', 'ノコ切断'),
        ('003', 'ガス切断'),
        ('004', 'G仕上げ'),
        ('005', '罫書・仮付け溶接'),
        ('006', '段取り替え'),
        ('007', '製品横持ち'),
        ('008', '本溶接'),
        ('009', 'ガス歪取り'),
        ('010', 'プレス歪取り'),
        ('011', 'ギザ加工'),
        ('012', '中間検査'),
        ('013', 'シャーリング切断'),
        ('014', 'プレス加工'),
        ('015', '曲げ加工'),
        ('016', 'ＮＣ加工'),
        ('017', '穴あけタップ手加工'),
        ('018', 'パネル組立・養生'),
        ('019', 'レーザー加工'),
        ('402', '塗装・タッチアップ'),
        ('602', '出荷'),
        ('701', '作図'),
        ('903', '現場出張'),
        ('908', '講習・試験'),
        ('909', '打ち合せ・会議'),
        ('999', 'その他'),
    ]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="work_logs")
    work_number = models.CharField("工番", max_length=10)
    subject = models.CharField("件名", max_length=20)
    work_code = models.CharField("作業コード", max_length=3, choices=WORK_CODE_CHOICES)
    work_hours = models.DecimalField("作業時間", max_digits=4, decimal_places=1)
    date = models.DateField("作業日", auto_now_add=False)

    def __str__(self):
        return f"{self.employee.name} - {self.work_number} ({self.date})"

