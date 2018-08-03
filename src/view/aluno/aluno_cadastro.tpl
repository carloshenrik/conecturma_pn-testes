%include('./header.tpl', title="Conecturma")
<div class="row">
    <div align="center" class="col-md-12">
        <h1>Cadastro</h1>
        <form action="/aluno_cadastro" method="post">
             Nome do aluno:   <input type="text" name="aluno_nome"/>
             sexo:  <select name="sexo">
                    <option value="masculino">Masculino</option>
                    <option value="feminino">Feminino</option>
                    </select><br>
             <!--Senha :          <input type="password" name="senha"/><br>-->
             Data de nascimento: <input type="date" name="data_nascimento"/><br>
             Matricula:       <input type="text" name="matricula"><br>
             Escola: <select name="escola">
                % if isinstance(escolas, dict):
                    <option value="{{escolas['id']}}">{{escolas['nome']}}</option>
                % else:
                    % for i in escolas:
                        <option value="{{i['id']}}">{{i['nome']}}</option>
                    % end
                % end
            </select><br>
            <button type="submit">Enviar</button>
        </form>
        <a href="/gestao_aprendizagem/usuario"><button>Voltar</button></a>
    </div>
</div>
%include('footer.tpl')