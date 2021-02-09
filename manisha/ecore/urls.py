from django.urls import path

from ecore import views

urlpatterns = [
    path('Marchent/', views.MarchentClass.as_view()),
    path('marchent1', views.marchent_view),
    path("marchent1/<int:id>",views.marchentEdit),
    path('marchent/<int:pk>', views.MarchentClass1.as_view()),



    path('Lenin/', views.LeninClass.as_view()),
    path('lenin1/', views.lenin_view),
    path("lenin1/<int:id>", views.LeninEdit),

    path('Rfid/', views.RFIDClass.as_view()),
    path('rfid1/', views.Rfid_view),
    path('rfid1/<int:id>', views.RfidEdit),
]
