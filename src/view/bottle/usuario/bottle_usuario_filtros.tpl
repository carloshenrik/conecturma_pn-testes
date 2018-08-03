    <select id="filtro_rede" onChange="filtro_usuario()">
            %if observador_tipo is '0':
                <option value="0">---- Selecione rede ----</option>
                % for r in redes:
                    <option value="{{r['id']}}" >{{r['nome']}}</option>
                % end
            %elif redes == None or redes == '':
                <option value="0">---- Selecione rede ----</option>
            %else:
                %for i in redes:
                    <option value="{{i['id']}}">{{i['nome']}}</option>
                %end
            %end
    </select>
    <select id="filtro_escola" onChange="filtro_usuario()" class='dropdown_filtros' >
                %if observador_tipo is '0':
                    <option value="0" >---- Selecione escola ----</option>
                    % for e in escolas:
                        <option value="{{e['id']}}">{{e['nome']}}</option>
                    % end
                %elif escolas == None or escolas == '':
                    <option value="0">---- Selecione escola ----</option>
                %else:
                    %for i in escolas:
                        <option value="{{i['id']}}">{{i['nome']}}</option>
                    %end
                %end
    </select>

    <select id="filtro_turma" onChange="filtro_usuario()" class='dropdown_filtros'>
        <option value="0">---- Selecione turma ----</option>
        % for t in turmas:
            <option value="{{t['id']}}">{{t['nome']}}</option>
        % end
        </div>
    </select>
    <select id="filtro_tipo_usuario" onChange="filtro_usuario()">
        <option value="0">---- Selecione Tipo do usuário ----</option>
        <option value="1">Gestor</option>
        <option value="2">Diretor</option>
        <option value="3">Professor</option>
        <option value="6">Aluno</option>
    </select>
