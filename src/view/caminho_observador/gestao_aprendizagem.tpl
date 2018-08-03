%include('header.tpl', title="Conecturma")
        <div class="row">
            <div align="center" class="col-md-2" style="margin-top:50px;">
                <h2>Menu</h2>
                <h3>Relatórios</h3>

                <h3>Cadastros</h3>
                % if tipo == '3':
                    <a href="/gestao_aprendizagem/usuario">USUÁRIOS</a><br>
                    <a href="/medalha_cadastro">Criar medalha</a><br>
                    <a href="/ler_medalha">Ler medalhas criadas</a><br>
                % elif tipo == '2':
                    <a href="/turma">TURMA</a><br>
                    <a href="/gestao_aprendizagem/usuario">USUÁRIOS</a><br>
                % elif tipo == '1':
                    <a href="/escola">ESCOLA</a><br>
                    <a href="/turma">TURMA</a><br>
                    <a href="/gestao_aprendizagem/usuario">USUÁRIOS</a><br>
                % elif tipo == '0':
                    <a href="/rede">REDE</a><br>
                    <a href="/escola">ESCOLA</a><br>
                    <a href="/turma">TURMA</a><br>
                    <a href="/gestao_aprendizagem/usuario">USUÁRIOS</a><br>
                % end
            </div>
            <div class="col-md-10">
                <div align="center">
                    <h2>Bem Vindo {{usuario}} </h2>
                    <h3>A Conecturma!</h3>
                </div>
            </div>
        </div>
%include('footer.tpl')