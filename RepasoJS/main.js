// alert('Hola Mundo')

var nombre = "Andres Bernaola";
var altura = 190;

var concatenacion = nombre + " " + altura;

// document.write(nombre);
// document.write(altura);
// document.write(concatenacion);

var datos = document.getElementById("datos")
// datos.innerHTML = concatenacion
datos.innerHTML= `
    <h3> desde archivo main.js<h3/>
    <h4> HTML en un archivo JS<h4/>
    <h4> Mi nombre es ${nombre} y mi altura es ${altura}<h4/>
`;




