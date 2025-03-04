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
        ('001', '001'),
        ('002', '002'),
        ('003', '003'),
        ('004', '004'),
        ('005', '005'),
        ('006', '006'),
        ('007', '007'),
        ('008', '008'),
        ('009', '009'),
        ('010', '010'),
        ('011', '011'),
        ('012', '012'),
        ('013', '013'),
        ('014', '014'),
        ('015', '015'),
        ('016', '016'),
        ('017', '017'),
        ('018', '018'),
        ('019', '019'),
        ('402', '402'),
        ('602', '602'),
        ('701', '701'),
        ('903', '903'),
        ('908', '908'),
        ('909', '909'),
        ('999', '999'),
    ]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="work_logs")
    work_number = models.CharField("工番", max_length=10)
    subject = models.CharField("件名", max_length=20)
    work_code = models.CharField("作業コード", max_length=3, choices=WORK_CODE_CHOICES)
    work_hours = models.DecimalField("作業時間", max_digits=4, decimal_places=1)
    date = models.DateField("作業日", auto_now_add=False)

    def __str__(self):
        return f"{self.employee.name} - {self.work_number} ({self.date})"

#display user name(all)
from django.contrib.auth.models import User

users = User.objects.all().values('id', 'username', 'first_name', 'last_name')

for user in users:
    full_name = f"{user['first_name']} {user['last_name']}"
    print(f"ユーザID：{user['id']}, ユーザ名：{user['username']},  フルネーム：({full_name})")

#display user name(select)
def get_full_name(user_name):
    try:
        user = User.objects.get(username=user_name)
        full_name = f"{user.first_name} {user.last_name}"
        print(f"ユーザ名：{user.username}, フルネーム：{full_name}")
    except User.DoesNotExist:
        print(f"指定したIDのユーザIDのユーザは存在しません.")
get_full_name('tid100')