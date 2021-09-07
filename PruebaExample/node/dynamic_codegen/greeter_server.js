const express = require('express');
const mysql = require('mysql');
const morgan = require('morgan');
//const myConnection = require('express-myconnection');

// configuracion
const app = express();
const config = {
  host    : 'localhost',
  user    : 'root',
  password: '1234',
  database: 'Distribuidos'
};
const connection = mysql.createConnection(config);

//funciones
app.use(morgan('dev'));

//GRPC-----------------------------------------------------------
var PROTO_PATH = __dirname + '/../../protos/helloworld.proto';

var grpc = require('@grpc/grpc-js');
var protoLoader = require('@grpc/proto-loader');
var packageDefinition = protoLoader.loadSync(
    PROTO_PATH,
    {keepCase: true,
     longs: String,
     enums: String,
     defaults: true,
     oneofs: true
    });
var hello_proto = grpc.loadPackageDefinition(packageDefinition).helloworld;

/**
 * Implements the SayHello RPC method.
 */
function sayHello(call, callback) {
  var codigo = 'W'
  respondio = esPrioritario('PCR-88578-9')
  console.log(respondio)
  respondio = verificar('DCR-88578-9')
  console.log(respondio)
  callback(null, {message: 'desde el server Hola, ' + call.request.name});
  console.log(call.request.name);
}

function ListaMedicamento(call, callback) {
  connection.query('select a.Id_medicamento, a.Numero, a.Comercial, a.Descripcion, a.Id_tipo, b.Nombre from medicamentos a inner join tipo b ON a.id_tipo = b.Id_tipo',
  function (error, results, fields) {
    if (error) throw error;
    console.log(results)
    callback(null, {Datos: results});
  })
}

function ListaTipo(call, callback) {
  //connection.query('SELECT * FROM tipo where Activo = 1', function (error, results, fields) {
  connection.query('SELECT * FROM tipo', function (error, results, fields) {
    if (error) throw error;
    console.log(results)
    callback(null, {Tipos: results});
  })
}

function ListaProducto(call, callback) {
  connection.query('SELECT * FROM producto', function (error, results, fields) {
    if (error) throw error;
    console.log(results)
    callback(null, {Productos: results});
  })
}

function AltaMedicamento(call, callback) {
  var Numero = call.request.Numero;
  var Comercial = call.request.Comercial;
  var Descripcion = call.request.Descripcion;
  var Tipo = call.request.Nombre;
  var validar = 1

  var query = connection.query('select Id_medicamento from medicamentos a order by Id_medicamento desc limit 1', function (error, results, fields) {
    if (error) throw error;
    contador = results[0].Id_medicamento
    contador = contador + 1
    console.log('Contador medicamentos: ', contador)

    var query = connection.query('select Id_tipo from tipo where Nombre = ?', [Tipo] ,function (error, results, fields) {
      var Id_tipo = results[0].Id_tipo

      var datos = {Id_medicamento: contador, Numero : Numero, Comercial : Comercial, Descripcion : Descripcion, Id_tipo : Id_tipo };
      var query = connection.query('INSERT INTO medicamentos SET ?', datos, function (error, results, fields) {
        if (error) throw error;
      });
    });
  });
  callback(null, {message: 'Recibido'});
}

/*
  `Numero` varchar(50),
  `Comercial` varchar(50),
  `Descripcion` varchar(50),
  `Tipo` varchar(50)
  //var Numero = results[i].id;
  //var Comercial = results[i].nombre;
  //var Descripcion = results[i].descripcion;
*/

//`Id_tipo` BIGINT(20) NOT NULL AUTO_INCREMENT,
//`Activo` BIT(1) NULL DEFAULT NULL,
//`Nombre` VARCHAR(255) NULL DEFAULT NULL,
function AltaTipo(call, callback) {
  var Id_tipo = call.request.Id_tipo;
  var Activo = call.request.Activo;
  var Nombre = call.request.Nombre;

    var query = connection.query('select Id_tipo from tipo a order by Id_tipo desc limit 1', function (error, results, fields) {
      if (error) throw error;
      contador = results[0].Id_tipo
      contador = contador + 1
      console.log('Contador Tipo: ', contador)

        var datos = {Id_tipo: contador, Activo : Activo, Nombre : Nombre};
        var query = connection.query('INSERT INTO tipo SET ?', datos, function (error, results, fields) {
          if (error) throw error;
        });
      });

  callback(null, {message: 'Recibido'});
}

                            //tipo, DatosList
function BuscarMedicamentoId(call, callback) {
  var nombreTipo = call.request.Nombre
  var IdTipo = 0

  connection.query('SELECT Id_tipo as Id_tipo FROM tipo WHERE Nombre = ?', [nombreTipo] , function (error, results, fields) {
    if (error) throw error;
    console.log('resultado: ', results)
    IdTipo = results[0].Id_tipo;
    
    connection.query('SELECT a.Id_medicamento, a.Numero, a.Comercial, a.Descripcion, a.Id_tipo, b.Nombre from medicamentos a inner join tipo b ON a.id_tipo = b.Id_tipo WHERE a.Id_tipo = ?', [IdTipo] , function (error, results, fields) {
      if (error) throw error;
      console.log(results)
      callback(null, {Datos: results});
    })
  });
}

function BuscarMedicamentoNombre(call, callback) {
  var Comercial = call.request.Comercial
  Comercial = Comercial + '%'
  connection.query('SELECT a.Id_medicamento, a.Numero, a.Comercial, a.Descripcion, a.Id_tipo, b.Nombre from medicamentos a inner join tipo b ON a.id_tipo = b.Id_tipo WHERE a.Comercial LIKE ?', [Comercial] , function (error, results, fields) {
    if (error) throw error;
    console.log(results)
    callback(null, {Datos: results});
  })
}
//UPDATE tipo SET Activo = 0 WHERE Id_tipo = ?;
function EliminarTipo(call, callback) {
  var Id_tipo = call.request.Id_tipo
  connection.query('UPDATE tipo SET Activo = 0 WHERE Id_tipo = ?', [Id_tipo] , function (error, results, fields) {
    if (error) throw error;
    console.log(results)
    callback(null, {message: 'Registro Eliminado'});
  })
}

function ValidarProducto(call, callback) {
  var prioritario = esPrioritario(call.request.Codigo)
  var verifica = verificar(call.request.Codigo)
  call.request.Prioritario = prioritario
  call.request.Verificar = verifica
  console.log('validar producto: ', call.request)
  callback(null, call.request);
}

function esPrioritario(codigo){
  var prioritario = false;
  //primer letra del codigo
  var digito = codigo.substring(0, 1);
  if(digito.toUpperCase() === "P" || digito.toUpperCase() === "W"){
      prioritario = true;
  }
  return(prioritario);
}

function verificar(codigo){
  var suma = 0;
  var suma2 = 0;
  verificado = false;
  //separo el codigo por " - " ejemplo: DCR-88578-9:
  var arr = []
  var ver = []
  arr = codigo.split("-");

  var num = 'a'
  var num2 = 'a'

  num = arr[1];
  ver = arr[2];

  numst = num.toString()
  //sumo los numeros

  for( i = 0; i < numst.length; i++){
      suma = suma + parseInt(numst.charAt(i))
      //suma = suma + parseInt(numst.substring(i, i+1),10);
  }

  //si suma mayor a dos digitos vuelvo a sumar
  num2 = suma.toString();
  for( j = 0; j < num2.length; j++){
      suma2 = suma2 + parseInt(num2.substring(j, j+1),10);
  }

  if(suma2 == parseInt(ver)){
      verificado = true;
  }
  return verificado;
}
/**
Arranque del GRPC
**/
function main() {
  var server = new grpc.Server();
  server.addService(hello_proto.Greeter.service, {sayHello: sayHello,
      AltaMedicamento: AltaMedicamento,
        ListaMedicamento: ListaMedicamento,
          AltaTipo: AltaTipo,
            EliminarTipo: EliminarTipo,
              ListaTipo: ListaTipo,
                BuscarMedicamentoId: BuscarMedicamentoId,
                  BuscarMedicamentoNombre: BuscarMedicamentoNombre,
                    ListaProducto: ListaProducto,
                      ValidarProducto: ValidarProducto});
  server.bindAsync('0.0.0.0:50051', grpc.ServerCredentials.createInsecure(), () => {
    server.start();
  });
}

main();