from django.urls import path
from . import views, api
urlpatterns=[
    path('', views.test),
    #path("api", api.Dlist, name='json'),
    path("api/post", api.Dhtviews.as_view(), name='json'),
    path('data/', views.dht_tab, name='Data'),
    path('download_csv/', views.download_csv, name='download_csv'),
    path('index/', views.table, name='table'),
    path('table_view/',views.table_view,name='table_view'),
    path('myChart/', views.graphique, name='myChart'),
    path('chart-data/',views.chart_data, name='chart-data'),
    path('chart-data-jour/',views.chart_data_jour,name='chart-data-jour'),
    path('chart-data-semaine/',views.chart_data_semaine,name='chart-data-semaine'),
    path('chart-data-mois/',views.chart_data_mois,name='chart-data-mois'),
]

