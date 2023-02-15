onload = principal;

let listaCamiones;

function principal() {
    listaCamiones = document.getElementById("listaCamiones");
    cargarServidorCamiones();
}

function cargarServidorCamiones() {
    //petición al servidor de la lista de camiones

    //crear el objeto XMLHttpRequest para acceder al servidor
    let jsonhttp = new XMLHttpRequest();

    // codigo para tratar la respuesta
    jsonhttp.onreadystatechange = function () {
        //evaluar la respuesta del servidor
        if (this.readyState == 4 && this.status == 200) {
            let arrayCamion = JSON.parse(this.responseText);

            console.log(arrayCamion)

            for (c in arrayCamion) {
                let camion = '\
                <div class="card m-3">\
                    <div class="row g-0">\
                    <div class="col-md-5">\
                        <img src="img/'+c[4]+' class="img-fluid rounded-start" alt="'+c[1]+'">\
                    </div>\
                    <div class="col-md-7">\
                        <div class="card-body">\
                        <h5 class="card-title">Modelo: '+c[1]+'</h5>\
                        <p class="card-text">Marca: '+c[0]+'</p>\
                        <p class="card-text">Precio: '+c[3]+'&euro;</p>\
                        <p class="card-text">Descripci&oacute;n: '+c[2]+'</p>\
                        </div>\
                    </div>\
                    </div>\
                </div>';
                listaCamiones.innerHTML += camion;
            }
        }
    }
    //construir la petición al servidor
    jsonhttp.open("GET", "listarCamiones.py", true);
    jsonhttp.send();


    //creación de elementos en el DOM dentro del div listaCamiones
    /*
    let camion1 = '\
    <div class="card m-3">\
        <div class="row g-0">\
        <div class="col-md-5">\
            <img src="img/scania.png" class="img-fluid rounded-start" alt="SCANIA R450 NTG">\
        </div>\
        <div class="col-md-7">\
            <div class="card-body">\
            <h5 class="card-title">Modelo: R450 NTG</h5>\
            <p class="card-text">Marca: SCANIA</p>\
            <p class="card-text">Precio: 58.000 &euro;</p>\
            <p class="card-text">Descripci&oacute;n: siempre en garage</p>\
            </div>\
        </div>\
        </div>\
    </div>';

    let camion2 = '\
    <div class="card m-3">\
        <div class="row g-0">\
        <div class="col-md-5">\
            <img src="img/volvo.png" class="img-fluid rounded-start" alt="VOLVO FH 500">\
        </div>\
        <div class="col-md-7">\
            <div class="card-body">\
            <h5 class="card-title">Modelo: FH 500</h5>\
            <p class="card-text">Marca: VOLVO</p>\
            <p class="card-text">Precio: 78.000 &euro;</p>\
            <p class="card-text">Descripci&oacute;n: poco uso</p>\
            </div>\
        </div>\
        </div>\
    </div>';
    listaCamiones.innerHTML=camion1+camion2;
    */
}

function enviarCamion(){
    //crear el objeto XMLHttpRequest para acceder al servidor
    let jsonhttp = new XMLHttpRequest();

    //datos para enviar al servidor
    let marca = document.getElementById("marca").value;
    let modelo = document.getElementById("modelo").value;
    let precio = document.getElementById("precio").value;
    let desc = document.getElementById("desc").value;

    //codigo que espera la respuesta del servidor
    jsonhttp.onreadystatechange = function () {
        //evaluar la respuesta del servidor
        if (this.readyState == 4 && this.status == 200) {
            let resultado = JSON.parse(this.responseText);
            if(resultado){
                camion=[marca,modelo,desc,precio,"img/volvo.png"]
                listaCamiones.insertBefore(creaCamion(camion),listaCamiones.firtsChild)
            }
        }
    }

}