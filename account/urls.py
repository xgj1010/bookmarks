from django.conf.urls import url
from .views import user_login, dashboard

urlpatterns = [
    # url(r'^login/$', user_login, name='login'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^logout-then-login/$', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),
    url(r'^$', dashboard, name='dashboard'),
    url(r'password-change/$','django.contrib.auth.views.password_change', name='password_change'),
    url(r'password-change/done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),
]
