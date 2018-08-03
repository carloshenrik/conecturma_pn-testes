%include('gestao_aprendizagem/header/header.tpl', title="Gestão Aprendizagem", css="css-gestao-aprendizagem.css")
%include('gestao_aprendizagem/menu/menu.tpl')
<div class="col-md-9 order-md-3 texto-inicial" style="margin-top: 70px;">
    <h1>Selecione o Aluno</h1>
    %for i in alunos:
        <a href="/relatorios/visualizar_relatorio_aluno?aluno={{i['id']}}">
            nome: {{i['nome']}}|
            turma: {{i['vinculo_turma']}}</a>
        <br>
    %end
</div>
%include('gestao_aprendizagem/footer/footer.tpl')