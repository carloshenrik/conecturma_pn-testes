%include('gestao_aprendizagem/header/header.tpl', title="Gestão Aprendizagem", css="relatorio_aluno.css")
%include('gestao_aprendizagem/menu/menu.tpl')
    <div class="col-md-9 order-md-3 texto-inicial" style="margin-top: 15px;">
        <div class="col-md text-rel" style="padding-left:0px;">
          <h2>Relatório de aluno </h2>
        </div>

        <div class="col-md nome_aluno" style="padding-left:0px;">
          <span> {{aluno['nome']}} </span> - Turma: <span id="turma-num">{{aluno['vinculo_turma']}}</span>
        </div>

        <div class="input-group checkbox-group">
            <input type="checkbox" onchange="filtro_relatorio_aluno_detalhe({{aluno['id']}})" id="portugues" value="portugues" checked> <label  class="portugues" for="portugues">Língua Portuguesa</label>
            <input type="checkbox" onchange="filtro_relatorio_aluno_detalhe({{aluno['id']}})" id="matematica" value="matematica" checked> <label class="matematica" for="matematica">Matemática</label>
        </div>
        <div class="col-md-12" align="right" style="width:100%;">
            <a href="" onclick="window.print();" class="offset-md-11" > <img src="/static/img/print-icon.png" alt="" style="width:2%; height:auto;"> </a>
        </div>
        <div id="teste">
            %include('gestao_aprendizagem/relatorios/aluno/teste_table.tpl')
        </div>
    </div>
    <br>
%include('gestao_aprendizagem/footer/footer.tpl')