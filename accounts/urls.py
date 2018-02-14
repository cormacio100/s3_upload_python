from django.conf.urls import url
from . import views

# specific app URL pointable from template
app_name = 'accounts'

urlpatterns = [
    url(r'^upload/',views.upload, name="upload"),
    url(r'^submit_form/',views.submit_form, name="submit_form"),
    url(r'^sign_s3/',views.sign_s3, name="sign_s3"),
]
