%include('./header.tpl', title = 'Conecturma')
<div class="row">
    <div align="center" class="col-md-12">
        <h1>Escrever anotações</h1>
        <form action="/anotacoes_on_aluno">
         <input type="hidden" name="usuario_id" value="{{id_user}}">
         <textarea name ="anotacoes" rows="5" cols="100">
digite as anotaçoes
        </textarea>
         <input value="Post " type="submit">
        </form>






        <a href="/aluno"><button>Voltar</button></a>
    </div>
</div>

%include('footer.tpl')