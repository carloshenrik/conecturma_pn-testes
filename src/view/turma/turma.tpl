% include('./header.tpl', title = 'Conecturma')
    <div class="row">
        <div align="center" class="col-md-12">
           <h1>Turmas</h1>
            <a href="/turma/turma_cadastro"><button>Cadastro turma</button></a>
            <a href="/"><button>Voltar</button></a>
        </div>
    </div>
    <div class="row">
        <div class="col-md-12">
            <div class="row">
                <div class="col-md-2">
                </div>
                <div class="col-md-2">
                    Nome
                </div>
                <div class="col-md-2">
                    Professor(es)
                </div>
                <div class="col-md-2">
                    Escola
                </div>
                <div class="col-md-2">
                    Série
                </div>
            </div>
            <br>
            <%
                if turma == None:
            %>
            <h1> Sem turma Cadastrada</h1>
            <%
                else:
                    for t in turma:
            %>
            <div class="row">
                <div class="col-md-2">
                    <form action="/turma/turma_update" method="post">
                        <button name="id_turma" value="{{t['id']}}">Editar</button>
                    </form>
                </div>
                <div class="col-md-2">
                    {{t['nome']}}
                </div>
                <div class="col-md-2">
                </div>
                <div class="col-md-2">
                    {{t['vinculo_escola']}}
                </div>
                <div class="col-md-2">
                    {{t['serie']}}
                </div>
            </div>
            <br>
            <%
                end
            %>
        </div>
    </div>

% include('./footer.tpl')