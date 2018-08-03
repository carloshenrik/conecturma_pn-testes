% include('./header.tpl', title = 'Conecturma')
    <div class="row">
        <div align="center" class="col-md-12">
            <h1>Cadastro de Turmas</h1>
             <form action="/turma/cadastro_turma" method="post">
                 Turma:*  <input type="text" name="turma_nome"/>
                 Ano Letivo : <input type="text" name="ano_letivo" size="4"/><br>
                 Ano*:
                 <select name="serie">
                     <option value="0">pré-escola</option>
                     <option value="1">1ª Ano</option>
                     <option value="2">2ª Ano</option>
                     <option value="3">3ª Ano</option>
                 </select>
                 Escola*:
                 <select name="escola">
                    %if escolas == None and escolas == []:
                        <option value="0">Sem escola Cadastrada</option>
                    %elif isinstance(escolas, dict):
                        <option value="{{escolas['id']}}">{{escolas['nome']}}</option>
                    %else:
                        %for e in escolas:
                            <option value="{{e['id']}}">{{e['nome']}}</option>
                        %end
                    %end
                 </select><br>
                 <button type="submit">Enviar</button><br><br>
            </form>
            <a href="/turma"><button>Voltar</button></a>
        </div>
    </div>
% include('./footer.tpl')