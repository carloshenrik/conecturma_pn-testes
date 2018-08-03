% include('./header.tpl', title = 'Conecturma')
<div class="row">
    <div align="center" class="col-md-12">
        <h1>Editar Observador</h1>
        <br>
        <form action="/observador/update_observador" method="post"> <br>
            nome*: <input type="text" name="nome" value="{{nome}}"> <br>
            telefone*:<input type="text" name="telefone" value="{{telefone}}"> <br>
            cpf*:<input type="text" name="cpf" value="{{cpf}}"> <br>
            email*:<input type="email" name="email" value="{{email}}"> <br>
            <button type="submit" name="id" value="{{id}}">Enviar</button>
        </form>
        <a href="/observador">
            <button>voltar</button>
        </a>
    </div>
</div>
% include('./footer.tpl')