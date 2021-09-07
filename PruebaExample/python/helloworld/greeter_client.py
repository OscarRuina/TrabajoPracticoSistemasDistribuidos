from __future__ import print_function

#Para la pagina web
from flask import Flask, render_template, request, redirect, url_for, flash

import logging

import grpc
from numpy.core.arrayprint import array2string
import helloworld_pb2
import helloworld_pb2_grpc
import numpy

from helloworld_pb2 import DatosList, Medicamento, TipoList, Tipo, Producto, ProductoList

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
	arrMedicamentos = [ ]
	arrTipos = [ ]
	arrProductos = [ ]
	with grpc.insecure_channel('localhost:50051') as channel: 
			stub = helloworld_pb2_grpc.GreeterStub(channel)
			TipoList = stub.ListaTipo(helloworld_pb2.Tipo())
			print(TipoList)
			for i in range(0,len(TipoList.Tipos)):
				Id_tipo = TipoList.Tipos[i].Id_tipo
				Activo = TipoList.Tipos[i].Activo
				Nombre = TipoList.Tipos[i].Nombre
				arrTipos.append([Id_tipo, Activo, Nombre])

			DatosList = stub.ListaMedicamento(helloworld_pb2.Medicamento())
			print(DatosList)
			for i in range(0,len(DatosList.Datos)):
				codigo = DatosList.Datos[i].Numero
				comercial = DatosList.Datos[i].Comercial
				descripcion = DatosList.Datos[i].Descripcion
				tipo = DatosList.Datos[i].Nombre
				arrMedicamentos.append([codigo, comercial, descripcion, tipo])
			
			ProductoList = stub.ListaProducto(helloworld_pb2.Producto())
			print(ProductoList)
			for i in range(0,len(ProductoList.Productos)):
				Id_producto = ProductoList.Productos[i].Id_producto
				Codigo = ProductoList.Productos[i].Codigo

				arrProductos.append([Id_producto, Codigo])

			print('arr Productos: ', arrProductos)
			print('arr medicamentos: ', arrMedicamentos)
			print('arr tipos: ', arrTipos)
			return render_template('home.html', Medicamentos = arrMedicamentos, Tipos = arrTipos)


@app.route('/AddMedicamento', methods=['POST'])
def AddMedicamento():
	if request.method == 'POST':
		codigo = request.form['codigo']
		comercial = request.form['comercial']
		descripcion = request.form['descripcion']
		tipo = request.form['tipo']

		with grpc.insecure_channel('localhost:50051') as channel: 
			stub = helloworld_pb2_grpc.GreeterStub(channel)
			response = stub.AltaMedicamento(helloworld_pb2.Medicamento(Numero = codigo, Comercial = comercial, Descripcion = descripcion, Nombre = tipo))
			print("Cliente Recibe: " + response.message)

		return redirect(url_for('home'))


@app.route('/AddTipo', methods=['POST'])
def AddTipo():
	if request.method == 'POST':
		Activo = request.form['Activo']
		Nombre = request.form['Nombre']
		Activo = int(Activo)

		with grpc.insecure_channel('localhost:50051') as channel: 
			stub = helloworld_pb2_grpc.GreeterStub(channel)
			response = stub.AltaTipo(helloworld_pb2.Tipo(Activo = Activo, Nombre = Nombre))
			print("Cliente Recibe: " + response.message)
		return redirect(url_for('home'))


@app.route('/deleteTipo/<string:id>')
def deleteTipo(id):
	Id_tipo = int(id)
	with grpc.insecure_channel('localhost:50051') as channel: 
			stub = helloworld_pb2_grpc.GreeterStub(channel)
			response = stub.EliminarTipo(helloworld_pb2.Tipo(Id_tipo = Id_tipo))
			print("Cliente Recibe: " + response.message)
	return redirect(url_for('home'))


@app.route('/BuscarMedicamentoId', methods=['POST'])
def BuscarMedicamentoId():
	arrMedicamentos = [ ]
	arrTipos = [ ]
	if request.method == 'POST':
		NombreFiltro = request.form['NombreFiltro']
		with grpc.insecure_channel('localhost:50051') as channel:

			stub = helloworld_pb2_grpc.GreeterStub(channel)
			DatosList = stub.BuscarMedicamentoId(helloworld_pb2.Tipo(Nombre = NombreFiltro))
			print('datos de la lista filtrados:')
			print(DatosList)

			for i in range(0,len(DatosList.Datos)):
				codigo = DatosList.Datos[i].Numero
				comercial = DatosList.Datos[i].Comercial
				descripcion = DatosList.Datos[i].Descripcion
				tipo = DatosList.Datos[i].Nombre
				arrMedicamentos.append([codigo, comercial, descripcion, tipo])

			stub = helloworld_pb2_grpc.GreeterStub(channel)
			TipoList = stub.ListaTipo(helloworld_pb2.Tipo())
			print(TipoList)
			for i in range(0,len(TipoList.Tipos)):
				Id_tipo = TipoList.Tipos[i].Id_tipo
				Activo = TipoList.Tipos[i].Activo
				Nombre = TipoList.Tipos[i].Nombre
				arrTipos.append([Id_tipo, Activo, Nombre])

		return render_template('home.html', Medicamentos = arrMedicamentos, Tipos = arrTipos)


@app.route('/BuscarMedicamentoNombre', methods=['POST'])
def BuscarMedicamentoNombre():
	arrMedicamentos = [ ]
	arrTipos = [ ]

	if request.method == 'POST':
		Comercial = request.form['NomComercial']
		with grpc.insecure_channel('localhost:50051') as channel:
			stub = helloworld_pb2_grpc.GreeterStub(channel)
			DatosList = stub.BuscarMedicamentoNombre(helloworld_pb2.Medicamento(Comercial = Comercial))
			print(DatosList)
			for i in range(0,len(DatosList.Datos)):
				codigo = DatosList.Datos[i].Numero
				comercial = DatosList.Datos[i].Comercial
				descripcion = DatosList.Datos[i].Descripcion
				tipo = DatosList.Datos[i].Nombre
				arrMedicamentos.append([codigo, comercial, descripcion, tipo])

			stub = helloworld_pb2_grpc.GreeterStub(channel)
			TipoList = stub.ListaTipo(helloworld_pb2.Tipo())
			print(TipoList)
			for i in range(0,len(TipoList.Tipos)):
				Id_tipo = TipoList.Tipos[i].Id_tipo
				Activo = TipoList.Tipos[i].Activo
				Nombre = TipoList.Tipos[i].Nombre
				arrTipos.append([Id_tipo, Activo, Nombre])

		return render_template('home.html', Medicamentos = arrMedicamentos, Tipos = arrTipos)


def start():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='desde el cliente, saluda'))
    print("Cliente Recibe: " + response.message)

if __name__ == '__main__':
	logging.basicConfig()
	start()
	app.run()