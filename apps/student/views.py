from django.shortcuts import render
from student.models import Student
# 引入JsonResponse模塊
from django.http import JsonResponse
# 導入json模塊
import json
# 導入Q查詢
from django.db.models import Q
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie, requires_csrf_token,  csrf_protect, csrf_exempt


def get_csrf(request):
    token = get_token(request)  # 獲取 token
    return JsonResponse({'csrfToken': token})


# Create your views here.
def get_students(request):
    # 使用ORM獲取所有學生訊息
    try:
        obj_students = Student.objects.all().values()
        # 把結果轉為List
        students = list(obj_students)
        return JsonResponse({'code': 1, 'data': students})
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': "Error!: " + str(e)})


@csrf_exempt
def query_students(request):
    # 查詢學生訊息
    # 接收傳遞過來的查詢條件--axios默認json--字典類型('inputstr')--data['inputstr']
    data = json.loads(request.body.decode('utf-8'))
    try:
        #使用ORM 獲取滿足條件的學生訊息 並把對象轉為字典格式
        obj_students = Student.objects.filter(Q(student_ID__icontains=data['inputstr']) | Q(name__icontains=data['inputstr']) |
                                              Q(gender__icontains=data['inputstr']) | Q(address__icontains=data['inputstr']) |
                                              Q(mobile__icontains=data['inputstr']) | Q(email__icontains=data['inputstr'])).values()
        # 把結果轉為List
        students = list(obj_students)
        return JsonResponse({'code': 1, 'data': students})
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': "Error!: " + str(e)})