//const getCostumer = 'http://mintic2022-ciclo3-grupo53-e4.herokuapp.com/readPacientes/';
const getOnePacienteUrl = 'http://127.0.0.1:8000/readOnePaciente/';


//const getCostumer = 'http://127.0.0.1:8000/readOnePaciente/';
var btn = document.getElementById("button");
btn.addEventListener('click',conseguirNumero);



function conseguirNumero(){
    const body = document.getElementById("cuerpoTabla");
    
    body.innerHTML = "";
    const num = document.getElementById("numero").value;
    console.log(num);
    
    function getOnePaciente (id){
        
        fetch(getOnePacienteUrl + id)
          .then(response => {
            if (response.ok)
              return response.text()
            else
              throw new Error(response.status);
          })
          .then(data => {
            console.log("Datos: " + data);
            paciente = JSON.parse(data);
            handlePaciente();
          })
          .catch(err => {
            console.error("ERROR: ", err.message);
            handleError();
          });
      }
    
    function handlePaciente() {
        const trs = [];
        const tr = document.createElement("tr");
          tr.innerHTML =
            `<tr>
              <td>${paciente.id}</td>
              <td>${paciente.nombres}</td>
              <td>${paciente.apellidos}</td>
              <td>${paciente.fechaNacimiento}</td>
              <td>${paciente.genero}</td>
              <td>${paciente.direccion}</td>
              <td>${paciente.longitud}</td>
              <td>${paciente.latitud}</td>
              <td>${paciente.telefono}</td>
              <td>${paciente.ciudad}</td>
              <td>${paciente.Email}</td>
            </tr>`;
      
          trs.push(tr);
        // pacientes.forEach((paci) => {
          
        // });
        const info = document.getElementById("cuerpoTabla");
        trs.forEach(tr => info.appendChild(tr));
      }
      
      function handleError() {
        const message = document.createElement("p");
        message.innerHTML = "No se pudo cargar la información. Intente luego.";
        const info = document.getElementById("default");
        info.appendChild(message);
      }
      
      document.addEventListener("DOMContentLoaded", getOnePaciente(num));

} 

