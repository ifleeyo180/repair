from django.urls import path
from .views import *
from .api import api


# Local
# urlpatterns = [
#     path('', LogList.as_view(), name='log_list'),
#     path('create/', LogCreate.as_view(), name='log_create'),
#     path('<int:pk>/', LogView.as_view(), name='log_view'),
#     path('<int:pk>/reply/', LogReply.as_view(), name='log_reply'),
#     path('<int:pk>/delete/', LogDelete.as_view(), name='log_delete'),
# ]

urlpatterns = [
    path('', index, name='log_list'),
    path('create/', LogCreate.as_view(), name='log_create'),
    path('<int:pk>/', LogView.as_view(), name='log_view'),
    path('<int:pk>/reply/', LogReply.as_view(), name='log_reply'),
    path('<int:pk>/delete/', LogDelete.as_view(), name='log_delete'),
    path('api/', api.urls),
]