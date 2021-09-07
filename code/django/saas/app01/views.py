from django.shortcuts import render, HttpResponse
from utils.tencent.sms import send_sms_single
import random
from django.conf import settings

# Create your views here.
def send_sms(request):
    tpl = request.GET.get('tpl')
    template_id = settings.TENCENT_SMS_TEMPLATE['tpl']
    if not template_id:
        return HttpResponse('模板不存在')

    code = random.randrange(1000,9999)
    res = send_sms_single('17314893371',template_id,[code,])
    if res['result'] == 0:
        return HttpResponse('成功')
    else:
        return HttpResponse('失败')

from django import forms
from app01 import models
from django.core.validation import RegexValidator
from django.core.exception import ValidationError

class RegisterModelForm(forms.ModelForm):
    mobile_phone = forms.CharField(label='手机号',validators=)
    class Meta:
        model = models.UserInfo
        fields = '__all__'

def register(request):
    form = RegisterModelForm()
    return render(request,'app01/register.html',{'form':form})