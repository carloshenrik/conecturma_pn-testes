<!doctype html>
<html lang="pt_br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Jogar Conecturma</title>
    <link rel="icon" type="image/png" href="../static/img/logo-ico.png">
    <link rel="stylesheet" href="../static/reset.css">
    <link rel="stylesheet" href="../static/bootstrap.min.css">
    <link rel="stylesheet" href="../static/style.css">
</head>
<body>
    <div class="container-fluid bg">
		<div class="container">
			<div class="col-md-12">
				<div class="bg_login">
                    <main>
                        <div id="Login-div">
                                <img src="/static/img/login-img.png" id="login-img">
                                <section class="content-professor">
                                    <div class="professor">
                                        <img src="/static/img/professor-seta.png" id="professor-seta">
                                        <h2 class="h3 mb-3 font-weight-normal professor-text">Professor</h2>
                                        <label for="inputEmail" class="sr-only">Email</label>
                                        <input type="email" id="inputEmail" class="form-control class_email " placeholder="Email" required="">
                                        <label for="inputPassword" class="sr-only">Senha</label>
                                        <input type="password" id="inputPassword" class="form-control class_senha" placeholder="Senha" required="">
                                        <button onclick="login_professor()" id="btn-professor" style="cursor:pointer"></button>
                                        <a href="#" onclick="" class="lost-pass">Esqueci minha senha</a>
                                    </div>
                                </section>
                                <section class="content-login">
                                    <div class="student">
                                       <img src="/static/img/aluno-seta.png" id="aluno-seta">
		                                <span id="aluno" class="h3 mb-3 font-weight-normal">Aluno</span>
		                                </br>
		                                <label>Nome do usuário</label> <br>
		                                <input data-val="true" data-val-required="O Login do usuário é obrigatório" id="Login" name="Login" type="text" value="" placeholder="Login Aluno" >
                                    </div>
                                    <div class="pass">
                                        <img src="/static/img/btn-interrogacao.png" id="btn-interrogacao">
		                                <span class="pass-title">Senha</span>
		                                <div class="cartoons-pass">
                                            <div class="row">
                                                <div id="a" onmouseout="mouse_out('a')" onmouseover="mouse_in('a')" onclick="mudaEstado('a')" class="box-cartoons on">
		                                        <figure>
		                                        	<img class="img_selecionada" src="/static/img/avatar_01.png" data-imagem-selecionada="a" >
		                                    	</figure>
                                                </div>
                                                <div id="b" onmouseout="mouse_out('b')" onmouseover="mouse_in('b')" onclick="mudaEstado('b')" class="box-cartoons on">
                                                    <figure>
                                                    <img class="img_selecionada" src="/static/img/avatar_02.png" data-imagem-selecionada="b">
                                                    </figure>
                                                </div>
                                                <div id="c" onmouseout="mouse_out('c')" onmouseover="mouse_in('c')" onclick="mudaEstado('c')" class="box-cartoons on">
                                                    <figure>
                                                    <img class="img_selecionada" src="/static/img/avatar_03.png" data-imagem-selecionada="c">
                                                    </figure>
                                                </div>
                                                <div id="d" onmouseout="mouse_out('d')" onmouseover="mouse_in('d')" onclick="mudaEstado('d')" class="box-cartoons on">
                                                    <figure>
                                                    <img class="img_selecionada" src="/static/img/avatar_04.png" data-imagem-selecionada="d">
                                                    </figure>
                                                </div>
                                            </div>
                                            <div class="row">
                                                <div id="e" onmouseout="mouse_out('e')" onmouseover="mouse_in('e')" onclick="mudaEstado('e')" class="box-cartoons on">
		                                        <figure>
		                                        <img class="img_selecionada" src="/static/img/avatar_05.png" data-imagem-selecionada="e">
		                                    	</figure>
		                                        </div>
                                                <div  id="f" onmouseout="mouse_out('f')" onmouseover="mouse_in('f')" onclick="mudaEstado('f')"  class="box-cartoons on">
                                                    <figure>
                                                    <img class="img_selecionada" src="/static/img/avatar_06.png" data-imagem-selecionada="f">
                                                    </figure>
                                                </div>
                                                <div id="g" onmouseout="mouse_out('g')" onmouseover="mouse_in('g')" onclick="mudaEstado('g')" class="box-cartoons on">
                                                    <figure>
                                                    <img class="img_selecionada" src="/static/img/avatar_07.png" data-imagem-selecionada="g">
                                                    </figure>
                                                </div>
                                                <div id="h" onmouseout="mouse_out('h')" onmouseover="mouse_in('h')" onclick="mudaEstado('h')" class="box-cartoons on">
                                                    <figure>
                                                    <img class="img_selecionada" src="/static/img/avatar_08.png" data-imagem-selecionada="h">
                                                    </figure>
                                                </div>
                                            </div>
                                            <div class="row">
                                                <div id="i" onmouseout="mouse_out('i')" onmouseover="mouse_in('i')" onclick="mudaEstado('i')" class="box-cartoons on">
                                                    <figure>
                                                    <img  class="img_selecionada" src="/static/img/avatar_09.png" data-imagem-selecionada="i">
                                                    </figure>
                                                </div>
                                                <div id="j" onmouseout="mouse_out('j')" onmouseover="mouse_in('j')" onclick="mudaEstado('j')" class="box-cartoons on">
                                                    <figure>
                                                    <img class="img_selecionada" src="/static/img/avatar_10.png" data-imagem-selecionada="j">
                                                    </figure>
                                                </div>
                                                <div id="k" onmouseout="mouse_out('k')" onmouseover="mouse_in('k')" onclick="mudaEstado('k')" class="box-cartoons on">
                                                    <figure>
                                                    <img class="img_selecionada" src="/static/img/avatar_11.png" data-imagem-selecionada="k">
                                                    <figure>
                                                </div>
                                                <div id="l"  onmouseout="mouse_out('l')" onmouseover="mouse_in('l')" onclick="mudaEstado('l')" class="box-cartoons on">
                                                    <figure>
                                                    <img class="img_selecionada" src="/static/img/avatar_12.png" data-imagem-selecionada="l">
                                                    <figure>
                                                </div>
		                        	        </div>
                                            <div>
                                                <button id="botao_aluno" onclick="login_aluno()" style="cursor:pointer">
                                                </button>
                                            </div>
                                        </div>
                                    </div>
                                </section>
                        </div>
                    </main>
                </div>

            </div>
        </div>
        <footer class="logo" align="center">
            <img src="static/img/logo-company.png">
        </footer>
    </div>
    <!--
    <div class="row">
        <div align="center" class="col-md-12">
            <h1>Login</h1>
            <form action="login/login_observador" method="post">
                <h2>Observador</h2>
                Email  :<input type="text" name="observador_login_email"/>
                Senha :<input type="password" name="observador_senha"/>
                <button type="submit">Entrar</button>
            </form>
            <br>
            <a href="esqueci_senha"><button>Esquici a senha</button></a>
            <br>
            <form action="login/login_aluno" method="post">
                <h2>Aluno</h2>
                Nome  :<input type="text" name="aluno_login_nome"/>
                <pre>
                Senha :
                        <input type="checkbox" name="aluno_senha" value="a">a <input type="checkbox" name="aluno_senha" value="b">b <input type="checkbox" name="aluno_senha" value="c">c <input type="checkbox" name="aluno_senha" value="d">d <br>
                        <input type="checkbox" name="aluno_senha" value="e">e <input type="checkbox" name="aluno_senha" value="f">f <input type="checkbox" name="aluno_senha" value="g">g <input type="checkbox" name="aluno_senha" value="h">h <br>
                        <input type="checkbox" name="aluno_senha" value="i">i <input type="checkbox" name="aluno_senha" value="j">j <input type="checkbox" name="aluno_senha" value="l">l <input type="checkbox" name="aluno_senha" value="m">m <br>
                </pre>
                    <button type="submit">Entrar</button>
            </form>
            <a href="/formulario_cadastro"><button>Cadastrar</button></a>
        </div>
    </div>-->
    <script type="text/javascript" src="../static/js/jquery-3.3.1-min.js"></script>
    <script type="text/javascript" src="../static/js/script.js"></script>
</body>
</html>
