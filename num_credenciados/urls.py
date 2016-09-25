from django.conf.urls import  url
from num_credenciados.views import total_credenciados

urlpatterns = [
	url(r'^$', total_credenciados, name="num-credenciados"),
]