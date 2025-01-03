"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import include, path
# from myapp.views import MessageFormView, ReceiveMessageFormView

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', MessageFormView.as_view(), name='message_form'),
#     path('', ReceiveMessageFormView.as_view(), name='receive'),
#     path('', include('myapp.urls')),
# ]


from django.contrib import admin
from django.urls import include, path
from myapp.views import MessageFormView, ReceiveMessageFormView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('message-form', MessageFormView.as_view(), name='message_form'),  # Unique path for message form
    path('receive/', ReceiveMessageFormView.as_view(), name='receive'),      # Unique path for receiving messages
    path('', include('myapp.urls')),  # Include API URLs under the /api/ path
]