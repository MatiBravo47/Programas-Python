//1-Escribe un programa de una sola línea que haga que aparezca en la pantalla un
//alert que diga “Hello World”.

//alert("Hello World")

//2. Escribe un programa de una sola línea que escriba en la pantalla un texto que
//diga “Hello World” (document.write).

//document.write("Hello World")

//3. Escribe un programa de una sola línea que escriba en la pantalla el resultado
//de sumar 3 + 5.

//document.write(3+5)

//4. Escribe un programa de dos líneas que pida el nombre del usuario con un
//prompt y escriba un texto que diga “Hola nombreUsuario”

//var nombre = prompt ("Ingrese su nombre", "")
//document.write("Hola " + nombre)

//5. Escribe un programa de tres líneas que pida un número, pida otro número y
//escriba el resultado de sumar estos dos números.

//var num1 = prompt ('Ingrese un numero');
//var num2 = prompt ("Ingrese otro numero ");
//document.write("la suma es: " + (parseInt(num1)+parseInt(num2)))

//6. Escribe un programa que pida dos números y escriba en la pantalla cual es el
//mayor

//var num1 = prompt ('Ingrese un numero');
//var num2 = prompt ("Ingrese otro numero ");
//if (num1>num2) {
//    document.write(num1)
//}else{
// document.write ("el mayor es: " + num2) }

//7. Escribe un programa que pida 3 números y escriba en la pantalla el mayor de
//los tres                                                                                     NO ME SALIO!!!

//var n1 = prompt("Escribe un número");
//var n2 = prompt("Escribe otro número");
//var n3 = prompt("Escribe otro número");
//if (n1 > n2 && n1 > n3) {
//document.write(n1);
//} else if (n2 > n1 && n2 > n3) {
//document.write(n2);
//} else if (n3 > n1 && n3 > n2){
//document.write(n3);
//}

//8. Escribe un programa que pida un número y diga si es divisible por 2

//var n1 = prompt("Ingrese un numero");
//if (n1%2===0) {
//    document.write("El numero "+ n1 + " es divisible ")
//} else {
//    document.write("El numero "+n1 + " no es divisible")
//}
//9. Escribe un programa que pida una frase y escriba cuantas veces aparece la
//letra a

//10. Escribe un programa que pida una frase y escriba las vocales que aparecen
// var text = prompt("Ingrese una frase ");
// var nText = text.length;
// var i;
// for (i = 0; i < nText; i++ ) {
// if (text.substr(i,1) === "a" || text.substr(i,1) === "e" ||
// text.substr(i,1) === "i" || text.substr(i,1) === "o" 
// || text.substr(i,1) === "u" ){
// document.write (text.substring(i,1));
// }
// }
// 11. Escribe un programa que pida una frase y escriba cuántas de las letras que
// tiene son vocales
// 12. Escribe un programa que pida una frase y escriba cuántas veces aparecen
// cada una de las vocales