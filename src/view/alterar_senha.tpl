% include('header.tpl', title = 'Conecturma')
    <div class="row">
        <div align="center" class="col-md-12">
            <h1>Mudar senha</h1>
            <form action="/new_senha" , method='post'>
                Nome  :<input type="text" name="usuario"/><br>
                Senha antiga :<input type="password" name="senha"/><br>
                Senha nova :<input type="password" name="senha_nova"/><br>
                Confirme a nova senha:<input type="password" name="senha_conf"/><br>
                <br>
                <button type="submit">Entrar</button>
            </form>
            <a href="/">
            <button>Voltar</button>
        </a>
        </div>
    </div>
% include('footer.tpl')