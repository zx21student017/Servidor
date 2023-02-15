onload = principal;

class Calcula {
    constructor() {
        this.operando1 = 0;
        this.operando2 = 0;
        this.operacion = 0; //1 -> + ; 2 -> - ; 3 -> * ; 4 -> /
    }

    completaOper1(n) {
        this.operando1 = this.operando1 * 10 + n;
    }
    completaOper2(n) {
        this.operando2 = this.operando2 * 10 + n;
    }

    igual() {
        switch (this.operacion) {
            case 1:
                return cal.suma()
                break;
            case 2:
                return cal.resta()
                break;
            case 3:
                return cal.multiplicacion()
                break;
            case 4:
                return cal.division()
                break;
            default:
                return -1;
        }
    }

    suma() {
        return this.operando1 + this.operando2;
    }
    resta() {
        return this.operando1 - this.operando2;
    }
    multiplicacion() {
        return this.operando1 * this.operando2;
    }
    division() {
        if (this.operando2 == 0) {
            //para el dividir entre 0
            return "Division por 0"
        } else {
            return (this.operando1 / this.operando2).toFixed(2);//para que redonde a dos decimales
        }

    }
}

let sM = "+";
let rT = "-";
let mT = "*";
let dV = "/";
let cM = ",";
let iG = "=";

let listaBotones;
let simboloBotones = [7, 8, 9, sM, 4, 5, 6, rT, 1, 2, 3, mT, cM, 0, iG, dV];
let cal = new Calcula();

let estado = 0;

let oper = document.createElement("p");

let op1 = document.createElement("span");
let sig = document.createElement("span");
let op2 = document.createElement("span");
let igual = document.createElement("span");

let n1 = "";
let n2 = "";
let simb = "";
let ress = "";

function principal() {
    dibujaCalculadora();
}

function dibujaCalculadora() {

    let calculadora = document.getElementById("calculadoraId");

    listaBotones = document.getElementById("calculadoraId").childNodes;
    for (let index = 1; index < 17; index++) {
        let texto = document.createElement("p");
        texto.setAttribute("class", "boton");
        texto.setAttribute("onclick", "pulsado(" + index + ")");
        calculadora.appendChild(texto);
        listaBotones[index].innerHTML = simboloBotones[index - 1];
    }
}

function pulsado(n) {
    console.log(n);

    let pantalla = document.getElementById("num");

    if (estado == -1) {
        n1 = "";
        n2 = "";
        ress = "";
        simb = "";

        oper.innerHTML = "";
        estado = 0;
    }

    if ((n == 1 || n == 2 || n == 3 || n == 5 || n == 6 || n == 7 || n == 9 || n == 10 || n == 11 || n || 14) && (estado == 0 || estado == 1 || estado == 2 || estado == 3)) {
        if (estado == 0 || estado == 1) {
            switch (n) {
                case 1:
                    n1 = n1 + "7";
                    op1.innerHTML = n1;
                    oper.appendChild(op1);
                    pantalla.appendChild(oper);
                    estado = 1;
                    break;
                case 2:
                    n1 = n1 + "8";
                    op1.innerHTML = n1;
                    oper.appendChild(op1);
                    pantalla.appendChild(oper);
                    estado = 1;
                    break;
                case 3:
                    n1 = n1 + "9";
                    op1.innerHTML = n1;
                    oper.appendChild(op1);
                    pantalla.appendChild(oper);
                    estado = 1;
                    break;
                case 5:
                    n1 = n1 + "4";
                    op1.innerHTML = n1;
                    oper.appendChild(op1);
                    pantalla.appendChild(oper);
                    estado = 1;
                    break;
                case 6:
                    n1 = n1 + "5";
                    op1.innerHTML = n1;
                    oper.appendChild(op1);
                    pantalla.appendChild(oper);
                    estado = 1;
                    break;
                case 7:
                    n1 = n1 + "6";
                    op1.innerHTML = n1;
                    oper.appendChild(op1);
                    pantalla.appendChild(oper);
                    estado = 1;
                    break;
                case 9:
                    n1 = n1 + "1";
                    op1.innerHTML = n1;
                    oper.appendChild(op1);
                    pantalla.appendChild(oper);
                    estado = 1;
                    break;
                case 10:
                    n1 = n1 + "2";
                    op1.innerHTML = n1;
                    oper.appendChild(op1);
                    pantalla.appendChild(oper);
                    estado = 1;
                    break;
                case 11:
                    n1 = n1 + "3";
                    op1.innerHTML = n1;
                    oper.appendChild(op1);
                    pantalla.appendChild(oper);
                    estado = 1;
                    break;
                case 14:
                    n1 = n1 + "0";
                    op1.innerHTML = n1;
                    oper.appendChild(op1);
                    pantalla.appendChild(oper);
                    estado = 1;
                    break;

            }
        } else if (estado == 2 || estado == 3) {
            switch (n) {
                case 1:
                    n2 = n2 + "7";
                    op2.innerHTML = n2;
                    oper.appendChild(op2);
                    pantalla.appendChild(oper);
                    estado = 3;
                    break;
                case 2:
                    n2 = n2 + "8";
                    op2.innerHTML = n2;
                    oper.appendChild(op2);
                    pantalla.appendChild(oper);
                    estado = 3;
                    break;
                case 3:
                    n2 = n2 + "9";
                    op2.innerHTML = n2;
                    oper.appendChild(op2);
                    pantalla.appendChild(oper);
                    estado = 3;
                    break;
                case 5:
                    n2 = n2 + "4";
                    op2.innerHTML = n2;
                    oper.appendChild(op2);
                    pantalla.appendChild(oper);
                    estado = 3;
                    break;
                case 6:
                    n2 = n2 + "5";
                    op2.innerHTML = n2;
                    oper.appendChild(op2);
                    pantalla.appendChild(oper);
                    estado = 3;
                    break;
                case 7:
                    n2 = n2 + "6";
                    op2.innerHTML = n2;
                    oper.appendChild(op2);
                    pantalla.appendChild(oper);
                    estado = 3;
                    break;
                case 9:
                    n2 = n2 + "1";
                    op2.innerHTML = n2;
                    oper.appendChild(op2);
                    pantalla.appendChild(oper);
                    estado = 3;
                    break;
                case 10:
                    n2 = n2 + "2";
                    op2.innerHTML = n2;
                    oper.appendChild(op2);
                    pantalla.appendChild(oper);
                    estado = 3;
                    break;
                case 11:
                    n2 = n2 + "3";
                    op2.innerHTML = n2;
                    oper.appendChild(op2);
                    pantalla.appendChild(oper);
                    estado = 3;
                    break;
                case 14:
                    n2 = n2 + "0";
                    op2.innerHTML = n2;
                    oper.appendChild(op2);
                    pantalla.appendChild(oper);
                    estado = 3;
                    break;
            }
        }
    }

    if ((n == 4 || n == 8 || n == 12 || n == 16) && estado == 1) {
        switch (n) {
            case 4:
                simb = " + ";
                sig.innerHTML = simb;
                oper.appendChild(sig);
                pantalla.appendChild(oper);
                estado = 2;
                cal.operacion = 1;
                break;
            case 8:
                simb = " - ";
                sig.innerHTML = simb;
                oper.appendChild(sig);
                pantalla.appendChild(oper);
                estado = 2;
                cal.operacion = 2;
                break;
            case 12:
                simb = " * ";
                sig.innerHTML = simb;
                oper.appendChild(sig);
                pantalla.appendChild(oper);
                estado = 2;
                cal.operacion = 3;
                break;
            case 16:
                simb = " / ";
                sig.innerHTML = simb;
                oper.appendChild(sig);
                pantalla.appendChild(oper);
                estado = 2;
                cal.operacion = 4;
                break;
        }
    }
    if (n == 15 && estado == 3) {
        cal.operando1 = parseFloat(n1);
        cal.operando2 = parseFloat(n2);
        ress = " = " + cal.igual();
        igual.innerHTML = ress;
        oper.appendChild(igual);
        pantalla.appendChild(oper);
        estado = -1;
    }

}