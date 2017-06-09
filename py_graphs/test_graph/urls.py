from django.conf.urls import url
from test_graph.views import IndexView
from test_graph.views import DataUpView
from test_graph.views import GraphView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^data_up$', DataUpView.as_view(), name='data_up'),
    url(r'^graph$', GraphView.as_view(), name='graph'),
]
