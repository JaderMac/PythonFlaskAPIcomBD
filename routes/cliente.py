from flask import Blueprint, render_template, request
from database.models.cliente import Cliente

cliente_route = Blueprint('clientes', __name__)

@cliente_route.route('/')
def listar_clientes():
    clientes = Cliente.select()
    return render_template('listar_clientes.html', clientes=clientes)

@cliente_route.route('/', methods=[('POST')])
def inserir_cliente():
    data = request.json
    novo_usuario = Cliente.create(
        nome = data['nome'],
        celular = data['celular'],
        email = data['email'],
    )
    return render_template('item_cliente.html', cliente=novo_usuario)


@cliente_route.route('/new')
def form_cliente():
    # formulario de criar clientes
    return render_template('form_cliente.html')

@cliente_route.route('/<int:cliente_id>')
def detalhar_cliente(cliente_id):
   # Exibir detalhes do cliente
   cliente = Cliente.get_by_id(cliente_id)
   return render_template('detalhar_cliente.html', cliente=cliente)

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    # formulario de editar clientes
    cliente = None
    cliente = Cliente.get_by_id(cliente_id)
    return render_template('form_cliente.html', cliente=cliente)

@cliente_route.route('/<int:cliente_id>/update', methods=[('PUT')])
def atualizar_cliente(cliente_id):
    # Atualiza cliente
    data = request.json

    cliente_editado = Cliente.get_by_id(cliente_id)
    cliente_editado.nome = data['nome']
    cliente_editado.celular = data['celular']
    cliente_editado.email = data['email']
    cliente_editado.save()
            
    return render_template('item_cliente.html', cliente=cliente_editado)

@cliente_route.route('/<int:cliente_id>/delete', methods=[('DELETE')])
def deletar_cliente(cliente_id):
    # deleta cliente
    cliente = Cliente.get_by_id(cliente_id)
    cliente.delete_instance()
    return{'deleted':'ok'}