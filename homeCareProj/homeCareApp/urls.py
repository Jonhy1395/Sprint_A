from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('newPaciente', views.newPaciente, name="NewPaciente"),
    path('readPaciente', views.readPaciente, name="readPaciente"),
    path('readOnePaciente/<int:id>',views.readOnePaciente, name="readOnePaciente"),
    path('updatePaciente/<int:id>', views.updatePaciente, name="updatePaciente"),
    path('deletePaciente/<int:id>', views.deletePaciente, name="deletePaciente"),

    path('newMedico',views.newMedico, name="newMedico"),
    path('readMedico',views.readMedico, name="readMedico"),
    path('readOneMedico/<int:id>',views.readOneMedico, name="readOneMedico"),
    path('updateMedico/<int:id>', views.updateMedico, name="updateMedico"),
    path('deleteMedico/<int:id>', views.deleteMedico, name="deleteMedico"),

    path('newEnfermero',views.newEnfermero, name="newEnfermero"),
    path('readEnfermero',views.readEnfermero, name="readEnfermero"),
    path('readOneEnfermero/<int:id>',views.readOneEnfermero, name="readOneEnfermero"),
    path('updateEnfermero/<int:id>', views.updateEnfermero, name="updateEnfermero"),
    path('deleteEnfermero/<int:id>', views.deleteEnfermero, name="deleteEnfermero"),

    path('newAuxiliar',views.newAuxiliar, name="newAuxiliar"),
    path('readAuxiliar',views.readAuxiliar, name="readAuxiliar"),
    path('readOneAuxiliar/<int:id>',views.readOneAuxiliar, name="readOneAuxiliar"),
    path('updateAuxiliar/<int:id>', views.updateAuxiliar, name="updateAuxiliar"),
    path('deleteAuxiliar/<int:id>', views.deleteAuxiliar, name="deleteAuxiliar"),

    path('newAcompanante', views.newAcompanante, name="newAcompanante"),
    path('readAcompanante', views.readAcompanante, name="readAcompanante"),
    path('readOneAcompanante/<int:id>',views.readOneAcompanante, name="readOneAcompanante"),
    path('updateAcompanante/<int:id>', views.updateAcompanante, name="updateAcompanante"),
    path('deleteAcompanante/<int:id>', views.deleteAcompanante, name="deleteAcompanante"),

    path('newHistoriaClinica', views.newHistoriaClinica, name="newHistoriaClinica"),
    path('readHistoriaClinica', views.readHistoriaClinica, name="readHistoriaClinica"),
    path('readOneHistoriaClinica/<int:id>',views.readOneHistoriaClinica, name="readOneHistoriaClinica"),
    path('updateHistoriaClinica/<int:id>', views.updateHistoriaClinica, name="updateHistoriaClinica"),
    path('deleteHistoriaClinica/<int:id>', views.deleteHistoriaClinica, name="deleteHistoriaClinica"),
]
