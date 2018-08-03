% include('./header.tpl', title = 'Conecturma')
<div class="row">
    <div align="center" class="col-md-12">
        <h1>Cadastro</h1>
        <br>
        <form action="/create_medalha" method="post" >
            nome: <input type="text" name="nome"/> <br>
             <select name="tipos">
        <option value="1">1</option>
        <option value="2">2</option>
        </select>
            <button type="submit">Enviar</button>
        </form>
        <a href="/gestao_aprendizagem">
            <button>voltar</button>
        </a>
    </div>
</div>
% include('./footer.tpl')