from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework.documentation import include_docs_urls
from users.views import RegistrationView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('token/refresh/',
         jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),

    path('login/',
         jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),

    path('api/', include('todos.urls')),
    path('users/', include('users.urls')),
    path('register/', RegistrationView.as_view(), name='registration'),
    path('docs/', include_docs_urls(title='Todo API'))
]
