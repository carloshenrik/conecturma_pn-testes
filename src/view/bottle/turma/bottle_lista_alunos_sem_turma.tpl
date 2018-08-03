% if aluno == '' or aluno == []:
    <h2>Não tem Aluno para cadastrar na turma</h2>
% else:
    % for a in aluno:
        <input type="checkbox" name="alunos_{{a['id']}}"> {{a['nome']}}
    %end
%end

