function add_carro() {
    const container = document.getElementById("form-carro");

    const id = `carro-${Date.now()}`; // Gera um ID único para cada linha
    const html = `
        <br id="br-${id}">
        <div class="row" id="${id}">
            <div class="col-md">
                <input type="text" placeholder="Carro" class="form-control" name="carro" required>
            </div>
            <div class="col-md">
                <input type="text" placeholder="Placa" class="form-control" name="placa" required>
            </div>
            <div class="col-md">
                <input type="text" placeholder="Ano" class="form-control" name="ano" required>
            </div>
            <div class="col-md-auto">
                <button type="button" class="btn btn-danger" onclick="remove_carro('${id}')">X</button>
            </div>
        </div>
    `;

    container.innerHTML += html;
}

function remove_carro(id) {
    const carroElement = document.getElementById(id);
    const brElement = document.getElementById(`br-${id}`);
    if (carroElement) carroElement.remove();
    if (brElement) brElement.remove();
}

function exibir_form(tipo){
    add_cliente = document.getElementById('adicionar-cliente')
    att_cliente = document.getElementById('atualizar_cliente')

    if (tipo == '1'){
        att_cliente.style.display = 'none'
        add_cliente.style.display = 'block'
        
    } else if(tipo == '2'){
        att_cliente.style.display = 'block'
        add_cliente.style.display = 'none'
    }
}

function dados_clientes() {
    id_cliente = document.getElementById('cliente-select').value
    csrf_token = document.getElementsByName('csrfmiddlewaretoken')[0].value

    data = new FormData()
    data.append('id_cliente', id_cliente)

    fetch("/clientes/atualiza_cliente/",{
        method: "POST",
        headers:{
            'X-CSRFToken': csrf_token,
        },
        body: data
    }).then(function(result){
        return result.json()
    }).then(function(data){

        document.getElementById('form-atualiza-cliente').style.display = 'block'
        nome = document.getElementById('nome')
        nome.value = data['nome']

        sobrenome = document.getElementById('sobrenome')
        sobrenome.value = data['sobrenome']

        email = document.getElementById('email')
        email.value = data['email']

        cpf = document.getElementById('cpf')
        cpf.value = data['cpf']

    })

}