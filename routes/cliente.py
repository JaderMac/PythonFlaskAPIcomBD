from flask import Blueprint, render_template 
from banco.fakeBd import clientes

cliente_route = Blueprint('clientes', __name__)

cliente_id = 1 

@cliente_route.route('/')
def listar_clientes():
    clientesd=clientes
    return render_template('listar_clientes.html', clientesd=clientes)

@cliente_route.route('/<int:cliente_id>')
def detalhar_cliente(cliente_id):
   cliente=clientes[cliente_id]
   return render_template('detalhar_cliente.html', cliente=cliente)

@cliente_route.route('/', methods=[('POST')])
def inserir_cliente():
    # Adiciona um cliente
    pass

@cliente_route.route('/<int:cliente_id>/edit')
def form_atualizar_cliente(cliente_id):
    cliente=clientes[cliente_id]
    return render_template('form_atualizar_cliente.html', cliente=cliente)

@cliente_route.route('/<int:cliente_id>', methods=[('PUT')])
def atualizar_cliente(cliente_id):
    # Atualiza cliente
    pass

@cliente_route.route('/<int:cliente_id>/delete', methods=[('DELETE')])
def deletar_cliente(cliente_id):
    # Atualiza cliente
    pass