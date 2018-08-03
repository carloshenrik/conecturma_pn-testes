% include('./header.tpl', title = 'Conecturma')
<div class="row">
    <div align="center" class="col-md-12">
        <h1>Editar Observador</h1>
        <br>
        <form action="/escola/update_escola" method="post"> <br>
            nome: <input type="text" name="nome" value="{{nome}}"> <br>
            telefone:<input type="text" name="telefone" value="{{telefone}}"> <br>
            rua:<input type="text" name="rua" value="{{rua}}"> <br>
            numero:<input type="text" name="numero" value="{{numero}}"> <br>
            Cidade:<input type="text" name="cidade" value="{{cidade}}"> <br>
            Estado:<input type="text" name="estado" value="{{estado}}"><br>
            Rede :<input type="text" name="rede_pertencente" value="{{rede_pertencente}}"> <br>
            Codigo de identificaçao da escola:<input type="text" name="cod_identificacao" value="{{cod_identificacao}}"> <br>
            <button type="submit" name="id" value="{{id}}">Enviar</button>
        </form>
        <a href="/user_menu">
            <button>voltar</button>
        </a>
    </div>
</div>
% include('./footer.tpl')