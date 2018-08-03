%include('./header.tpl', title="Conecturma")
<div class="row">
    <div align="center" class="col-md-12">
        <h1>Cadastro de item </h1>
        <form action="/cadastro_item" method="post">
         Nome do item:   <input type="text" name="nome"/><br>
         Preço :         <input type="text" name="preco"/><br>
         <select name="tipo">
           <option value="1">Cores</option>
           <option value="2">Rosto</option>
           <option value="3">Acessorios</option>
           <option value="4">Corpo</option>
         </select><br>
         <button type="submit">Enviar</button>
        </form>
        <a href="/"><button>Voltar</button></a>
    </div>
</div>
%include('footer.tpl')