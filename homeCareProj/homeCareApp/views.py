import json
import email
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed, HttpResponseServerError
from django.shortcuts import render

from .models import Pacientes, Medico, Enfermero, Auxiliar, Acompanante, HistoriaClinica

# Create your views here.
def home(request):
    return HttpResponse("Bienvenido")

###---------------------------------------------Pacientes--------------------------------------------------###

def newPaciente(request):
    if request.method == 'POST':
    
        try:
            data = json.loads(request.body)
            paciente = Pacientes(
                id = data["id"],
                nombres = data["nombres"],
                apellidos = data["apellidos"],
                fechaNacimiento = data["fechaNacimiento"],
                genero = data["genero"],
                direccion = data["direccion"],
                longitud = data["longitud"],
                latitud = data["latitud"],
                telefono = data["telefono"],
                ciudad = data["ciudad"],
                email = data["email"]
            )
            paciente.save()
            return HttpResponse("Paciente agregado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")
 

def readPaciente(request):
    if request.method =='GET':
        try:
            paciente = Pacientes.objects.all()
            allPacienteData = []
            for x in paciente:
                datos = {
                    "id":x.id, 
                    "nombres":x.nombres,
                    "apellidos":x.apellidos,
                    "fechaNacimiento": x.fechaNacimiento,
                    "genero": x.genero,
                    "direccion":x.direccion,
                    "longitud": x.longitud,
                    "latitud": x.latitud,
                    "telefono":x.telefono,
                    "ciudad": x.ciudad,
                    "email":x.email
                    }
                allPacienteData.append(datos)
            respuesta = HttpResponse()
            respuesta.headers['Content-Type'] = 'text/json'
            respuesta.content = json.dumps(allPacienteData)
            return respuesta
        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")


def readOnePaciente(request, id):
    if request.method == 'GET':
        try:
            paci = Pacientes.objects.filter(id = id).first()
            if (not paci):
                return HttpResponseBadRequest("No existe un paciente con ese documento")
            datos = {
                "id": paci.id,
                "nombres": paci.nombres,
                "apellidos": paci.apellidos,
                "fechaNacimiento": paci.fechaNacimiento,
                "genero": paci.genero,
                "direccion": paci.direccion,
                "longitud": paci.longitud,
                "latitud": paci.latitud,
                "telefono": paci.telefono,
                "ciudad": paci.ciudad,
                "Email": paci.email
            }
            resp = HttpResponse()
            resp.headers['Content-Type'] = 'text/json'
            resp.content = json.dumps(datos)
            return resp
        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")


def updatePaciente(request, id):
    if request.method == 'PUT':
        try:
            pacient = Pacientes.objects.filter(id = id).first()
            
            if (not pacient):
                return HttpResponseBadRequest("No existe un usuario con ese documento.")

            data = json.loads(request.body)
            pacient.nombres = data["nombres"]
            pacient.apellidos = data["apellidos"]
            pacient.fechaNacimiento = data["fechaNacimiento"],
            pacient.genero = data["genero"]
            pacient.direccion = data["direccion"]
            pacient.longitud = data["longitud"]
            pacient.latitud = data["latitud"]
            pacient.telefono = data["telefono"]
            pacient.ciudad = data["ciudad"]
            pacient.email = data["email"]

            pacient.save()
            return HttpResponse("Paciente actualizado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['PUT'], "Método inválido")


def deletePaciente(request,id):
    if request.method == 'DELETE':
        try:
            pacient = Pacientes.objects.filter(id = id).first()
            if (not pacient):
                return HttpResponseBadRequest("No existe un usuario con ese documento.")

            pacient.delete()
            return HttpResponse("Cliente eliminado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['DELETE'], "Método inválido")

###---------------------------------------------Medico--------------------------------------------------###
def newMedico(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            pacient = Pacientes.objects.filter(id = data["pacienteID"]).first()
            # print(pacient)
            medico = Medico(
                id = data["id"],
                nombres = data["nombres"],
                apellidos = data["apellidos"],
                genero = data["genero"],
                telefono = data["telefono"],
                registroMedico = data["registroMedico"],
                especialidad = data["especialidad"],
                pacienteID = pacient
            )
            print(medico)
            medico.save()
            return HttpResponse("Medico agregado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")


def readMedico(request):
    if request.method =='GET':
        try:
            medico = Medico.objects.all()
            allMedicoData = []
            for x in medico:
                datos = {
                    "id" : x.id,
                    "nombres" : x.nombres,
                    "apellidos" : x.apellidos,
                    "genero" : x.genero,
                    "telefono" : x.telefono,
                    "registroMedico" : x.registroMedico,
                    "especialidad" : x.especialidad,
                    "pacienteID_id": x.pacienteID_id,
                    }

                print(datos)
                allMedicoData.append(datos)
            respuesta = HttpResponse()
            respuesta.headers['Content-Type'] = 'text/json'
            respuesta.content = json.dumps(allMedicoData)
            return respuesta
        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")


def readOneMedico(request, id):
    if request.method == 'GET':
        try:
            medico = Medico.objects.filter(id = id).first()
            if (not medico):
                return HttpResponseBadRequest("No existe un medico con ese documento")
            datos = {
                "id": medico.id,
                "nombres": medico.nombres,
                "apellidos": medico.apellidos,
                "fecha de nacimiento": medico.fechaNacimiento,
                "genero": medico.genero,
                "registroMedico": medico.registroMedico,
                "especialidad": medico.especialidad,
                "pacienteID_id": medico.pacienteID_id,
            }
            resp = HttpResponse()
            resp.headers['Content-Type'] = 'text/json'
            resp.content = json.dumps(datos)
            return resp
        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")


def updateMedico(request, id):
    if request.method == 'PUT':
        try:
            medico = Medico.objects.filter(id = id).first()
            
            if (not medico):
                return HttpResponseBadRequest("No existe un usuario con ese documento.")

            data = json.loads(request.body)
            medico.nombres = data["nombres"]
            medico.apellidos = data["apellidos"]
            medico.genero = data["genero"]
            medico.telefono = data["telefono"]
            medico.registroMedico = data["registroMedico"]
            medico.especialidad = data["especialidad"]
            medico.save()
            return HttpResponse("Medico actualizado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['PUT'], "Método inválido")


def deleteMedico(request,id):
    if request.method == 'DELETE':
        try:
            medico = Medico.objects.filter(id = id).first()
            if (not medico):
                return HttpResponseBadRequest("No existe un medico con ese documento.")

            medico.delete()
            return HttpResponse("Medico eliminado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['DELETE'], "Método inválido")

###---------------------------------------------Enfermero-----------------------------------------------###
def newEnfermero(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            pacient = Pacientes.objects.filter(id = data["pacienteId"]).first()
            
            if (not pacient):
                return HttpResponseBadRequest("No existe un Paciente con ese documento.")
            
            enfermero = Enfermero(
                id = data["id"],
                nombres = data["nombres"],
                apellidos = data["apellidos"],
                genero = data["genero"],
                telefono = data["telefono"],
                pacienteID = pacient,
            )
            enfermero.save()
            return HttpResponse("Enfermero agregado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")


def readEnfermero(request):
    if request.method =='GET':
        try:
            enferemero = Enfermero.objects.all()
            allEnfermerosData = []
            for x in enferemero:
                datos = {
                    "id" : x.id,
                    "nombres" : x.nombres,
                    "apellidos" : x.apellidos,
                    "genero" : x.genero,
                    "telefono" : x.telefono,
                    "pacienteID_id": x.pacienteId_id,
                    }
                allEnfermerosData.append(datos)
            respuesta = HttpResponse()
            respuesta.headers['Content-Type'] = 'text/json'
            respuesta.content = json.dumps(allEnfermerosData)
            return respuesta
        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")


def readOneEnfermero(request, id):
    if request.method == 'GET':
        try:
            enfermero = Enfermero.objects.filter(id = id).first()
            if (not enfermero):
                return HttpResponseBadRequest("No existe un Enfermero con ese documento")
            datos = {
                "id" : enfermero.id,
                "nombres" : enfermero.nombres,
                "apellidos" : enfermero.apellidos,
                "genero" : enfermero.genero,
                "telefono" : enfermero.telefono,
                "pacienteID": enfermero.pacienteId_id,
            }
            resp = HttpResponse()
            resp.headers['Content-Type'] = 'text/json'
            resp.content = json.dumps(datos)
            return resp
        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")


def updateEnfermero(request, id):
    if request.method == 'PUT':
        try:
            enfermero = Enfermero.objects.filter(id = id).first()
            
            if (not enfermero):
                return HttpResponseBadRequest("No existe un Paciente con ese documento.")

            data = json.loads(request.body)

            enfermero.nombres = data["nombres"]
            enfermero.apellidos = data["apellidos"]
            enfermero.genero = data["genero"]
            enfermero.telefono = data["telefono"]
            
            enfermero.save()
            return HttpResponse("Enfermero actualizado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['PUT'], "Método inválido")


def deleteEnfermero(request,id):
    if request.method == 'DELETE':
        try:
            enfermero = Enfermero.objects.filter(id = id).first()
            if (not enfermero):
                return HttpResponseBadRequest("No existe un Paciente con ese documento.")

            enfermero.delete()
            return HttpResponse("Enfermero eliminado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['DELETE'], "Método inválido")

###---------------------------------------------Auxiliar------------------------------------------------###
def newAuxiliar(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            aux = Pacientes.objects.filter(id = data["pacienteId"]).first()
            
            if (not aux):
                return HttpResponseBadRequest("No existe un Paciente con ese documento.")
            
            auxiliar = Auxiliar(
                id = data["id"],
                nombres = data["nombres"],
                apellidos = data["apellidos"],
                genero = data["genero"],
                telefono = data["telefono"],
                pacienteID = aux,
            )
            auxiliar.save()
            return HttpResponse("Auxiliar agregado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")


def readAuxiliar(request):
    if request.method =='GET':
        try:
            auxiliar = Auxiliar.objects.all()
            allAuxiliarData = []
            for x in auxiliar:
                datos = {
                    "id" : x.id,
                    "nombres" : x.nombres,
                    "apellidos" : x.apellidos,
                    "genero" : x.genero,
                    "telefono" : x.telefono,
                    "pacienteID_id": x.pacienteId_id,
                    }
                allAuxiliarData.append(datos)
            respuesta = HttpResponse()
            respuesta.headers['Content-Type'] = 'text/json'
            respuesta.content = json.dumps(allAuxiliarData)
            return respuesta
        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")


def readOneAuxiliar(request, id):
    if request.method == 'GET':
        try:
            auxiliar = Auxiliar.objects.filter(id = id).first()
            if (not auxiliar):
                return HttpResponseBadRequest("No existe un auxiliar con ese documento")

            datos = {
                "id" : auxiliar.id,
                "nombres" : auxiliar.nombres,
                "apellidos" : auxiliar.apellidos,
                "genero" : auxiliar.genero,
                "telefono" : auxiliar.telefono,
                "pacienteID_id": auxiliar.pacienteId_id,
            }
            resp = HttpResponse()
            resp.headers['Content-Type'] = 'text/json'
            resp.content = json.dumps(datos)
            return resp
        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")


def updateAuxiliar(request, id):
    if request.method == 'PUT':
        try:
            auxiliar = Auxiliar.objects.filter(id = id).first()
            
            if (not auxiliar):
                return HttpResponseBadRequest("No existe un Paciente con ese documento.")

            data = json.loads(request.body)

            auxiliar.nombres = data["nombres"]
            auxiliar.apellidos = data["apellidos"]
            auxiliar.genero = data["genero"]
            auxiliar.telefono = data["telefono"]
            
            auxiliar.save()
            return HttpResponse("Auxiliar actualizado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['PUT'], "Método inválido")


def deleteAuxiliar(request,id):
    if request.method == 'DELETE':
        try:
            auxiliar = Auxiliar.objects.filter(id = id).first()
            if (not auxiliar):
                return HttpResponseBadRequest("No existe un auxiliar con ese documento.")

            auxiliar.delete()
            return HttpResponse("Auxiliar eliminado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['DELETE'], "Método inválido")

###---------------------------------------------Acompañante---------------------------------------------###
def newAcompanante(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            acom = Pacientes.objects.filter(id = data["pacienteId"]).first()
            
            if (not acom):
                return HttpResponseBadRequest("No existe un Paciente con ese documento.")
            
            acompañante = Acompanante(
                id = data["id"],
                nombres = data["nombres"],
                apellidos = data["apellidos"],
                genero = data["genero"],
                telefono = data["telefono"],
                parentezco = data["parentezco"],
                email = data["email"],
                pacienteID = acom
            )
            acompañante.save()
            return HttpResponse("Acompañante agregado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")


def readAcompanante(request):
    if request.method =='GET':
        try:
            acompanante = Acompanante.objects.all()
            allAcompananteData = []
            for x in acompanante:
                datos = {
                    "id" : x.id,
                    "nombres" : x.nombres,
                    "apellidos" : x.apellidos,
                    "genero" : x.genero,
                    "telefono" : x.telefono,
                    "parentezco" : x.parentezco,
                    "email" : x.email,
                    "pacienteID_id": x.pacienteId_id
                    }
                allAcompananteData.append(datos)
            respuesta = HttpResponse()
            respuesta.headers['Content-Type'] = 'text/json'
            respuesta.content = json.dumps(allAcompananteData)
            return respuesta
        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")


def readOneAcompanante(request, id):
    if request.method == 'GET':
        try:
            acompanante = Acompanante.objects.filter(id = id).first()
            if (not acompanante):
                return HttpResponseBadRequest("No existe un acompañante con ese documento")

            datos = {
                "id" : acompanante.id,
                "nombres" : acompanante.nombres,
                "apellidos" : acompanante.apellidos,
                "genero" : acompanante.genero,
                "telefono" : acompanante.telefono,
                "parentezco" : acompanante.parentezco,
                "email" : acompanante.email,
                "pacienteID_id": acompanante.pacienteId_id,
            }
            resp = HttpResponse()
            resp.headers['Content-Type'] = 'text/json'
            resp.content = json.dumps(datos)
            return resp
        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")


def updateAcompanante(request, id):
    if request.method == 'PUT':
        try:
            acompanante = Acompanante.objects.filter(id = id).first()
            
            if (not acompanante):
                return HttpResponseBadRequest("No existe un Acompañante con ese documento.")

            data = json.loads(request.body)

            acompanante.nombres = data["nombres"]
            acompanante.apellidos = data["apellidos"]
            acompanante.genero = data["genero"]
            acompanante.telefono = data["telefono"]
            acompanante.parentezco = data["parentezco"]
            acompanante.email = data["email"]
            
            acompanante.save()
            return HttpResponse("Acompañante actualizado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['PUT'], "Método inválido")


def deleteAcompanante(request,id):
    if request.method == 'DELETE':
        try:
            acompanante = Acompanante.objects.filter(id = id).first()
            if (not acompanante):
                return HttpResponseBadRequest("No existe un Acompañante con ese documento.")

            acompanante.delete()
            return HttpResponse("Acompañante eliminado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['DELETE'], "Método inválido")

###---------------------------------------------Historia clinica----------------------------------------###
def newHistoriaClinica(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            paciente = Pacientes.objects.filter(id = data["pacienteId"]).first()
            print(paciente)
            if (not paciente):
                return HttpResponseBadRequest("No existe un Paciente con ese documento.")
            
            historiaClinica = HistoriaClinica(
                diagnosticos = data["diagnosticos"],
                signos = data["signos"],
                oximetria = data["oximetria"],
                frecRespiratoria = data["frecRespiratoria"],
                frecCardiaca = data["frecCardiaca"],
                temperatura = data["temperatura"],
                presionArterial = data["presionArterial"],
                glicemias = data["glicemias"],
                sugerenciasCuidado = data["sugerenciasCuidado"],
                pacienteID = paciente
            )
            historiaClinica.save()
            print(historiaClinica)
            return HttpResponse("Historia Clinica agregado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")


def readHistoriaClinica(request):
    if request.method =='GET':
        try:
            historiaClinica = HistoriaClinica.objects.all()
            allHistoriaClinicaData = []
            for x in historiaClinica:
                datos = {
                    "id" : x.id,
                    "diagnosticos" : x.diagnosticos,
                    "signos" : x.signos,
                    "oximetria" : x.oximetria,
                    "frecRespiratoria" : x.frecRespiratoria,
                    "frecCardiaca" :x.frecCardiaca,
                    "temperatura" : x.temperatura,
                    "presionArterial":x.presionArterial,
                    "glicemias" : x.glicemias,
                    "sugerenciasCuidado":x.sugerenciasCuidado,
                    "pacienteID_id": x.pacienteID_id
                }
                allHistoriaClinicaData.append(datos)
            respuesta = HttpResponse()
            respuesta.headers['Content-Type'] = 'text/json'
            respuesta.content = json.dumps(allHistoriaClinicaData)
            return respuesta
        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")


def readOneHistoriaClinica(request, id):
    if request.method == 'GET':
        try:
            paciente = Pacientes.objects.filter(id = id).first()
            historiaClinica = HistoriaClinica.objects.filter(pacienteID = paciente).first()
            if (not historiaClinica):
                return HttpResponseBadRequest("No existe una historia del paciente")

            datos = {
                    "id" : historiaClinica.id,
                    "diagnosticos" : historiaClinica.diagnosticos,
                    "signos" : historiaClinica.signos,
                    "oximetria" : historiaClinica.oximetria,
                    "frecRespiratoria" : historiaClinica.frecRespiratoria,
                    "frecCardiaca" : historiaClinica.frecCardiaca,
                    "temperatura" : historiaClinica.temperatura,
                    "presionArterial" : historiaClinica.presionArterial,
                    "glicemias" : historiaClinica.glicemias,
                    "sugerenciasCuidado" : historiaClinica.sugerenciasCuidado,
                    "pacienteID": historiaClinica.pacienteID_id
                }
            resp = HttpResponse()
            resp.headers['Content-Type'] = 'text/json'
            resp.content = json.dumps(datos)
            return resp
        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")


def updateHistoriaClinica(request, id):
    if request.method == 'PUT':
        try:

            paciente = Pacientes.objects.filter(id = id).first()
            historiaClinica = HistoriaClinica.objects.filter(pacienteID = paciente).first()
            if (not historiaClinica):
                return HttpResponseBadRequest("No existe una historia del paciente")

            data = json.loads(request.body)

            historiaClinica.diagnosticos = data["diagnosticos"],
            historiaClinica.signos = data["signos"],
            historiaClinica.oximetria = data["oximetria"],
            historiaClinica.frecRespiratoria = data["frecRespiratoria"],
            historiaClinica.frecCardiaca = data["frecCardiaca"],
            historiaClinica.temperatura = data["temperatura"],
            historiaClinica.presionArterial = data["presionArterial"],
            historiaClinica.glicemias = data[" glicemias"],
            historiaClinica.sugerenciasCuidado = data["sugerenciasCuidado"],
            
            
            historiaClinica.save()
            return HttpResponse("Historia Clinica actualizada")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['PUT'], "Método inválido")


def deleteHistoriaClinica(request,id):
    if request.method == 'DELETE':
        try:
            paciente = Pacientes.objects.filter(id = id).first()
            historiaClinica = HistoriaClinica.objects.filter(pacienteID = paciente).first()
            if (not historiaClinica):
                return HttpResponseBadRequest("No existe una historia del paciente")

            historiaClinica.delete()
            return HttpResponse("Historia Clinica eliminada")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['DELETE'], "Método inválido")
