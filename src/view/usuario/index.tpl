%include('./header.tpl', title = 'Conecturma')
  <div class="row">
    <div align="center" class="col-md-12">

        <div align="right">
            <a href="/">
                <button>voltar</button>
            </a>
        </div>
        <h1>Listagem de Usuários</h1>
         <div class="col-md-5">
            <div class="row">
                <form action="/gestao_aprendizagem/usuario/redirect_cadastro">
                    %include('bottle/usuario/bottle_usuario_cadastro.tpl')
                    <button type="submit" >+ Usuário</button>
                </form>
            </div>
        </div>
         <div align="center" class="col-md-12">
            <div class="row">
                <div id="dropdown_filtros">
                    %include('bottle/usuario/bottle_usuario_filtros.tpl')
                </div>
            </div>
         </div>
        <br>
        <div class="row">
            <div class="col-md-2">
                <strong>Nome</strong>
            </div>
            <div class="col-md-2">
                <strong>Email</strong>
            </div>
            <div class="col-md-2">
                <strong>Turma</strong>
            </div>
            <div class="col-md-2">
                <strong>Escola</strong>
            </div>
            <div class="col-md-2">
                <strong>Rede</strong>
            </div>
            <div class="col-md-2">
                <strong>Tipo</strong>
            </div>
       </div>
        <div id="usuarios_sistema">
          %include('bottle/usuario/bottle_usuario_read_usuarios')
        </div>
     </div>
</div>
%include('footer.tpl')