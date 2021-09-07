const express = require('express');
const path = require('path');
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
  callback(null, {message: 'desde el server Hola, ' + call.request.name});
  console.log(call.request.name);
}

function AltaMedicamento(call, callback) {
  var Numero = call.request.Numero;
  var Comercial = call.request.Comercial;
  var Descripcion = call.request.Descripcion;
  var Tipo = call.request.Nombre;

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
function ListaMedicamento(call, callback) {
  connection.query('select a.Id_medicamento, a.Numero, a.Comercial, a.Descripcion, a.Id_tipo, b.Nombre from medicamentos a inner join tipo b ON a.id_tipo = b.Id_tipo',
  function (error, results, fields) {
    if (error) throw error;
    console.log(results)
    callback(null, {Datos: results});
  })
}

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

function ListaTipo(call, callback) {
  connection.query('SELECT * FROM tipo', function (error, results, fields) {
    if (error) throw error;
    console.log(results)
    callback(null, {Tipos: results});
  })
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

function EliminarTipo(call, callback) {
  var Id_tipo = call.request.Id_tipo
  connection.query('DELETE FROM tipo WHERE Id_tipo = ?', [Id_tipo] , function (error, results, fields) {
    if (error) throw error;
    console.log(results)
    callback(null, {message: 'Registro Eliminado'});
  })
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
                  BuscarMedicamentoNombre: BuscarMedicamentoNombre});
  server.bindAsync('0.0.0.0:50051', grpc.ServerCredentials.createInsecure(), () => {
    server.start();
  });
}

main();