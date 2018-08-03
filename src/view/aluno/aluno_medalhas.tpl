%include('./header.tpl', title="Conecturma")
<div class="row">
    <div align="center" class="col-md-12">
        <h1>Cadastro</h1>
        <form action="/aluno_cadastro" method="post">
         Nome do aluno:   <input type="text" name="aluno_nome"/><br>
         Senha :          <input type="password" name="senha"/><br>
         <button type="submit">Enviar</button>
        </form>
        <a href="/aluno"><button>Voltar</button></a>
    </div>
</div>
%include('footer.tpl')