% include('header.tpl', title = 'Conecturma')
    <div class="row">
        <div align="center" class="col-md-12">
            <h1>Esqueci senha</h1>

                <br>

                Email :<input type="text" id="email" onChange="emailValidador()"/>
                <div id="mensagem_erro"></div>
                <br>
                <br>
                <button onclick="esqueci_senha()">Enviar</button>
            <br>
        </div>
    </div>
% include('footer.tpl')