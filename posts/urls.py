from django.conf.urls import url
from . import views

# specific app URL pointable from template
app_name = 'accounts'

urlpatterns = [
    url(r'^$', views.posts, name="posts"),
    url(r'^post_details/',views.post_details, name="post_details"),
]
