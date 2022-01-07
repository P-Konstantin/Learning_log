"""learning_log URL Configuration"""

from django.urls import include, path
from django.contrib import admin
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^users/', include(('users.urls', 'users'), namespace='users')),
    url(r'', include(('learning_logs.urls', 'learning_logs'), namespace='learning_logs')),
]
