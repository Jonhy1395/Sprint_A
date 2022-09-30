from django.db import models

# Create your models here.
class Pacientes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nombres = models.CharField("Nombres_paciente", max_length=50)
    apellidos = models.CharField("Apellido_paciente", max_length=50)
    fechaNacimiento = models.CharField("Fecha_nacimiento",max_length=50)
    genero = models.CharField("Genero",max_length=50, null=True)
    direccion = models.CharField("Direccion",max_length=50)
    longitud = models.CharField("Longitud_direccion",max_length=30, null=True)
    latitud = models.CharField("Latitud_direccion",max_length=30, null=True)
    telefono = models.BigIntegerField("Telefono")
    ciudad = models.CharField("Ciudad", max_length=30)
    email = models.EmailField("Email", max_length=100, unique=True)

class Medico(models.Model):
    id = models.BigIntegerField("Id", primary_key=True)
    nombres = models.CharField("Nombre_medico", max_length = 50)
    apellidos = models.CharField("Apellidos_medico", max_length = 50)
    genero = models.CharField("Genero_medico", max_length=50, null=True)
    telefono = models.BigIntegerField("Telefono_medico")
    registroMedico = models.CharField("Tarjeta_profesinal", max_length=50)
    especialidad = models.CharField("Especialidad", max_length=50)
    pacienteID = models.ForeignKey(Pacientes, related_name="medico", on_delete=models.CASCADE)

class Enfermero(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nombres = models.CharField('nombres_enfermero', max_length=50)
    apellidos = models.CharField('apellidos_enfermero', max_length=50)
    genero = models.CharField('genero_enfermero', max_length=30,null=True)
    telefono = models.BigIntegerField('telefono_enfermero')
    pacienteID = models.ForeignKey(Pacientes, related_name='enfermero', on_delete=models.CASCADE)
    
class Auxiliar(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nombres = models.CharField('nombres_auxiliar', max_length=50)
    apellidos = models.CharField('apellidos_auxiliar', max_length=50)
    genero = models.CharField('genero_auxiliar', max_length=30,null=True)
    telefono = models.BigIntegerField('telefono_auxiliar')
    pacienteID = models.ForeignKey(Pacientes, related_name='auxiliar', on_delete=models.CASCADE)
    
class Acompanante(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nombres = models.CharField('nombres_acompanante', max_length=50)
    apellidos = models.CharField('apellidos_acompanante', max_length=50)
    genero = models.CharField('genero_enfermero', max_length=30,null=True)
    telefono = models.BigIntegerField('telefono_acompañante')
    parentezco = models.CharField('parentezco', max_length=30)
    email = models.EmailField('Email', max_length=100, unique=True)
    pacienteID = models.ForeignKey(Pacientes, related_name='acompanante', on_delete=models.CASCADE)
    
class HistoriaClinica(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    diagnosticos = models.CharField('diagnostico', max_length=30)
    signos = models.CharField('signos', max_length=30)
    oximetria = models.CharField('oximetria', max_length=30)
    frecRespiratoria = models.CharField('frecuencia_respiratoria', max_length=30)
    frecCardiaca = models.CharField('frecuencia_cardiaca', max_length=30)
    temperatura = models.CharField('temperatura', max_length=30)
    presionArterial = models.CharField('presion_arterial', max_length=30)
    glicemias = models.CharField('glicemias', max_length=30)
    sugerenciasCuidado = models.CharField('sugerencias_cuidado', max_length=300)
    pacienteID = models.ForeignKey(Pacientes, related_name='historia_clinica', on_delete=models.CASCADE)
