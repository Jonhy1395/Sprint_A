
//const newPacienteUrl = 'http://mintic2022-ciclo3-grupo53-e4.herokuapp.com/'
const newPacienteUrl = 'http://127.0.0.1:8000/newPaciente';

function collectData(evt){
    evt.preventDefault();
    const id = document.registro.id.value;
    const nombres = document.registro.nombres.value;
    const apellidos = document.registro.apellidos.value;
    const fechaNacimiento = document.registro.fechaNacimiento.value;
    const genero = document.registro.genero.value;
    const direccion = document.registro.direccion.value;
    const longitud = document.registro.longitud.value;
    const latitud = document.registro.latitud.value;
    const telefono = document.registro.telefono.value;
    const ciudad = document.registro.ciudad.value;
    const email = document.registro.email.value;

    const paciente = {
        id: id,
        nombres: nombres,
        apellidos: apellidos,
        fechaNacimiento: fechaNacimiento,
        genero: genero,
        direccion: direccion,
        longitud: longitud,
        latitud: latitud,
        telefono: telefono,
        ciudad: ciudad,
        email: email
    }

    console.log(paciente);

    // alert(
    //     `Usuario creado con:
    //     ${paciente.id}, ${paciente.nombres}, ${paciente.apellidos}`
    // );

    const dataToSend = JSON.stringify(paciente);
    sendData(dataToSend);
}


function sendData (data){
    fetch(newPacienteUrl, 
        {
            method: "POST",
            headers:{
                "Content-Type": "text/json"
            },
            body: data
        })


      .then(response => {
        if (response.ok)
          return response.text()
        else
          throw new Error(response.status);
      })
      .then(data => {
        console.log(data);
        handleSuccess();
      })
      .catch(err => {
        console.error("ERROR: ", err.message);
        handleError();
      });
  }

  function handleSuccess(){
    document.getElementById("formulario").remove();
    const messeage = document.createElement("p");
    messeage.innerHTML = "Cliente Creado de manera exitosa.";
    const info = document.getElementById("principal");
    info.appendChild(messeage);
  }

  function handleError() {
    document.getElementById("principal").remove();
    const messeage = document.createElement("p");
    messeage.innerHTML = "Cliente no pudo ser creado.";
    const info = document.getElementById("principal");
    info.appendChild(messeage);
  }
/*-----------------------------------------------------------------------------*/
  document.registro.addEventListener('submit', collectData);