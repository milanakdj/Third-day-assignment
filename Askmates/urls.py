from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
app_name='qna'


urlpatterns = [
    path('qna/',include('qna_app.urls')),
    path('user/',include('user_app.urls')),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

