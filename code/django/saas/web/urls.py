from django.conf.urls import url,include
from web.views import account

urlpatterns = [
    url(r'^register/$', account.register, name='register'),
    url(r'^send_sms/$', account.send_sms, name='send_sms'),
    url(r'^login/sms$', account.login_sms, name='login_sms'),

]