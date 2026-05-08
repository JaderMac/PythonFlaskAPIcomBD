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
    data = request.json

    novo_usuario = {
        "id": len(clientes)+1,
        "nome": data['nome'],
        "email":data['email'],
        "celular":data['celular']
    }
    clientes.append(novo_usuario)
    return render_template('item_cliente.html', cliente=novo_usuario)


@cliente_route.route('/new')
def form_cliente():
    # formulario de criar clientes
    return render_template('form_cliente.html')

@cliente_route.route('/<int:cliente_id>')
def detalhar_cliente(cliente_id):
   cliente=clientes[cliente_id] 
   return render_template('detalhar_cliente.html', cliente=cliente)

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    # formulario de editar clientes
    cliente = None
    
    for c in clientes:
        if c['id'] == cliente_id:
            cliente=c

    return render_template('form_cliente.html', cliente=cliente)

@cliente_route.route('/<int:cliente_id>/update', methods=[('PUT')])
def atualizar_cliente(cliente_id):
    # Atualiza cliente
    pass

@cliente_route.route('/<int:cliente_id>/delete', methods=[('DELETE')])
def deletar_cliente(cliente_id):
    # deleta cliente
    global clientes
    clientes = [c for c in clientes if c['id'] != cliente_id]
    return{'deleted':'ok'}