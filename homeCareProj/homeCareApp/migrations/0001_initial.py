# Generated by Django 4.1.1 on 2022-09-23 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=50, verbose_name='Nombres_paciente')),
                ('apellidos', models.CharField(max_length=50, verbose_name='Apellido_paciente')),
                ('fechaNacimiento', models.CharField(max_length=50, verbose_name='Fecha_nacimiento')),
                ('genero', models.CharField(max_length=50, null=True, verbose_name='Genero')),
                ('direccion', models.CharField(max_length=50, verbose_name='Direccion')),
                ('longitud', models.CharField(max_length=30, null=True, verbose_name='Longitud_direccion')),
                ('latitud', models.CharField(max_length=30, null=True, verbose_name='Latitud_direccion')),
                ('telefono', models.BigIntegerField(verbose_name='Telefono')),
                ('ciudad', models.CharField(max_length=30, verbose_name='Ciudad')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='Id')),
                ('nombres', models.CharField(max_length=50, verbose_name='Nombre_medico')),
                ('apellidos', models.CharField(max_length=50, verbose_name='Apellidos_medico')),
                ('genero', models.CharField(max_length=50, null=True, verbose_name='Genero_medico')),
                ('telefono', models.BigIntegerField(verbose_name='Telefono_medico')),
                ('registroMedico', models.CharField(max_length=50, verbose_name='Tarjeta_profesinal')),
                ('especialidad', models.CharField(max_length=50, verbose_name='Especialidad')),
                ('pacienteID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medico', to='homeCareApp.pacientes')),
            ],
        ),
        migrations.CreateModel(
            name='HistoriaClinica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('diagnosticos', models.CharField(max_length=30, verbose_name='diagnostico')),
                ('signos', models.CharField(max_length=30, verbose_name='signos')),
                ('oximetria', models.CharField(max_length=30, verbose_name='oximetria')),
                ('frecRespiratoria', models.CharField(max_length=30, verbose_name='frecuencia_respiratoria')),
                ('frecCardiaca', models.CharField(max_length=30, verbose_name='frecuencia_cardiaca')),
                ('temperatura', models.CharField(max_length=30, verbose_name='temperatura')),
                ('presionArterial', models.CharField(max_length=30, verbose_name='presion_arterial')),
                ('glicemias', models.CharField(max_length=30, verbose_name='glicemias')),
                ('sugerenciasCuidado', models.CharField(max_length=300, verbose_name='sugerencias_cuidado')),
                ('pacienteID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historia_clinica', to='homeCareApp.pacientes')),
            ],
        ),
        migrations.CreateModel(
            name='Enfermero',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=50, verbose_name='nombres_enfermero')),
                ('apellidos', models.CharField(max_length=50, verbose_name='apellidos_enfermero')),
                ('genero', models.CharField(max_length=30, null=True, verbose_name='genero_enfermero')),
                ('telefono', models.BigIntegerField(verbose_name='telefono_enfermero')),
                ('pacienteID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enfermero', to='homeCareApp.pacientes')),
            ],
        ),
        migrations.CreateModel(
            name='Auxiliar',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=50, verbose_name='nombres_auxiliar')),
                ('apellidos', models.CharField(max_length=50, verbose_name='apellidos_auxiliar')),
                ('genero', models.CharField(max_length=30, null=True, verbose_name='genero_auxiliar')),
                ('telefono', models.BigIntegerField(verbose_name='telefono_auxiliar')),
                ('pacienteID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auxiliar', to='homeCareApp.pacientes')),
            ],
        ),
        migrations.CreateModel(
            name='Acompanante',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=50, verbose_name='nombres_acompanante')),
                ('apellidos', models.CharField(max_length=50, verbose_name='apellidos_acompanante')),
                ('genero', models.CharField(max_length=30, null=True, verbose_name='genero_enfermero')),
                ('telefono', models.BigIntegerField(verbose_name='telefono_acompa??ante')),
                ('parentezco', models.CharField(max_length=30, verbose_name='parentezco')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
                ('pacienteID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acompanante', to='homeCareApp.pacientes')),
            ],
        ),
    ]
