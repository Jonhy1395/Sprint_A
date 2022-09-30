//const getCostumer = 'http://mintic2022-ciclo3-grupo53-e4.herokuapp.com/readPacientes';
const getCostumer = 'http://127.0.0.1:8000/readPaciente';
let pacientes = [];

function getPaciente (){
  fetch(getCostumer)
    .then(response => {
      if (response.ok)
        return response.text()
      else
        throw new Error(response.status);
    })
    .then(data => {
      console.log("Datos: " + data);
      pacientes = JSON.parse(data);
      handlePaciente();
    })
    .catch(err => {
      console.error("ERROR: ", err.message);
      handleError();
    });
}

function handlePaciente() {
  const trs = [];
  pacientes.forEach((paci) => {
    const tr = document.createElement("tr");
    tr.innerHTML =
      `<tr>
        <td>${paci.id}</td>
        <td>${paci.nombres}</td>
        <td>${paci.apellidos}</td>
        <td>${paci.fechaNacimiento}</td>
        <td>${paci.genero}</td>
        <td>${paci.direccion}</td>
        <td>${paci.longitud}</td>
        <td>${paci.latitud}</td>
        <td>${paci.telefono}</td>
        <td>${paci.ciudad}</td>
        <td>${paci.email}</td>
      </tr>`;

    trs.push(tr);
  });
  const info = document.getElementById("cuerpoTabla");
  trs.forEach(tr => info.appendChild(tr));
}

function handleError() {
  //document.getElementById("cargando").remove();
  const message = document.createElement("p");
  message.innerHTML = "No se pudo cargar la información. Intente luego.";
  const info = document.getElementById("default");
  info.appendChild(message);
}

document.addEventListener("DOMContentLoaded", getPaciente);