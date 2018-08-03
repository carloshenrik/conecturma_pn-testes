% include('./header.tpl', title = 'Professor')
<div class="row">
    <div align="left" class="col-md-12">
        <h1>Cadastro</h1>
        <br>
        <input type="hidden" id="tipo"name="tipo_observador" value="{{tipo}}">
            %include('bottle/observador/bottle_create_observador.tpl')
        <button onclick="cadastro_observador()">Enviar</button>
    </div>
</div>
% include('./footer.tpl')