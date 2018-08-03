% include('header.tpl', title = 'Conecturma')
    %for i in medalhas:
        Nome:{{i['nome']}}<br>
        Tipo:{{i['tipo_medalha']}}<br>
        Descrição: {{i['descricao']}}<br>
        Descrição Completa: {{i['descricao_completa']}}

    %end
% include('footer.tpl')