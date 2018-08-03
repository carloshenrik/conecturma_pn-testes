% include('header.tpl', title = 'Conecturma')
<div class="row">
    <div align="center" class="col-md-12">
        <h1>Update Turmas</h1>
        <form action="/turma/turma_update_controller" method="post">
            <input type="hidden" name='turma' value="{{turma['id']}}">
            Turma:* <input type="text" name="turma_nome" value="{{turma['nome']}}"/>

            %include('bottle/turma/bottle_turma_series.tpl')
            <div class="row">
                <div class="col-md-6">
                    <h1>Aluno</h1>
                    %include('bottle/turma/bottle_lista_alunos_sem_turma.tpl')
                </div>
                <div class="col-md-6">
                    <h1>Professor</h1>
                    %include('bottle/turma/bottle_lista_professor_sem_turma.tpl')
                </div>
            </div>
            <button type="submit">salvar</button>
        </form>
        <a href="/turma">
            <button>Voltar</button>
        </a>
    </div>
</div>
% include('footer.tpl')