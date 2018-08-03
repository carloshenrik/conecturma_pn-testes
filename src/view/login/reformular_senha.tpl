% include('header.tpl', title = 'Conecturma')
    <div class="row">
        <div align="center" class="col-md-12">
            <h1>Esqueci senha</h1>

                <form action="/controller_reformular_senha ", method="post">
                    <input type="hidden" name="id" value="{{id}}">
                    Email :<input type="text" id="email" name="email" value="{{email}}"/>
                    <br>
                    <br>
                    Nova senha : <input type="password" name="senha">

                    <button type="submit">Enviar</button>
                </form>
            <br>
        </div>
    </div>
% include('footer.tpl')