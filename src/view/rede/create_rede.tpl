%include('./header.tpl', title="Conecturma")


<div class="row">
    <div align="center" class="col-md-12">
        <h1>Cadastro</h1>
        <form action="/rede/criar_rede" method="post">
         Nome da rede  <input type="text" name="nome_rede"/><br>
         Telefone:      <input type="text" name="telefone" >
         <button type="submit">Enviar</button>
        </form>
        <a href="/rede"><button>Voltar</button></a>
    </div>
</div>

%include('footer.tpl')