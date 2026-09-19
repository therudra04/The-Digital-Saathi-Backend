from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/blogs/', include('blogs.urls')),
    path('api/contact/', include('contact.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)










# One important thing: ListAPIView and RetrieveAPIView are DRF's generic API views. We're deliberately starting with read-only APIs because your frontend needs to read blogs. Creation/editing stays in Django Admin, which is exactly what we wanted.