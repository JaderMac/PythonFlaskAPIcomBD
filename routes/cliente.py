from flask import Blueprint, render_template, request
from database.fakeBd import clientes

cliente_route = Blueprint('clientes', __name__)

"""
Rota de clientes
    /clientes/ (GET) - listar os clientes
    /clientes/ (POST) - Insere cliente
    /clientes/new (GET) - renderizar o formulario para inserir cliente
    /clientes/<id> (GET) - obter dados de um cliente
    /clientes/<id>/edit (GET) - renderizar o formulario editar dados de um cliente
    /clientes/<id>/update (PUT) - atualiza dados de um cliente
    /clientes/<id>/delete (DELETE)- deleta dados de um cliente
"""

cliente_id = 1 

@cliente_route.route('/')
def listar_clientes():
    return render_template('listar_clientes.html', clientes=clientes)

@cliente_route.route('/', methods=[('POST')])
def inserir_cliente():
    print(request.json)
    return {"ok":"ok"}
    # return render_template('form_atualizar_cliente.html')

# @cliente_route.route('/new', methods=[('POST')])
@cliente_route.route('/new')
def form_cliente():
    # formulario de criar clientes
    print(request.json)
    return {"ok":"ok"}
    # return render_template('form_atualizar_cliente.html')

@cliente_route.route('/<int:cliente_id>')
def detalhar_cliente(cliente_id):
   cliente=clientes[cliente_id] 
   return render_template('detalhar_cliente.html', cliente=cliente)

@cliente_route.route('/<int:cliente_id>/edit')
def form_atualizar_cliente(cliente_id):
    # formulario de editar clientes
    cliente=clientes[cliente_id]
    return render_template('form_atualizar_cliente.html', cliente=cliente)

@cliente_route.route('/<int:cliente_id>/update', methods=[('PUT')])
def atualizar_cliente(cliente_id):
    # Atualiza cliente
    pass

@cliente_route.route('/<int:cliente_id>/delete', methods=[('DELETE')])
def deletar_cliente(cliente_id):
    # deleta cliente
    pass