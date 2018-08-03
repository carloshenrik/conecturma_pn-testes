% if professor == '' or professor == []:
    <h2>Não tem Professor para cadastrar na turma</h2>
% else:
    % for p in professor:
        <input type="checkbox" name="professor_{{p['id']}}"> {{p['nome']}}
    %end
%end

