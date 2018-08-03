
<%
    if turma['serie'] == '0':
%>
    Ano*:
         <select name="serie">
             <option value="0">pré-escola</option>
             <option value="1">1ª Ano</option>
             <option value="2">2ª Ano</option>
             <option value="3">3ª Ano</option>
         </select>

% elif turma['serie'] == '1':
    Ano*:
         <select name="serie">
             <option value="1">1ª Ano</option>
             <option value="0">pré-escola</option>
             <option value="2">2ª Ano</option>
             <option value="3">3ª Ano</option>
         </select>
% elif turma['serie'] == '2':
    Ano*:
         <select name="serie">
             <option value="2">2ª Ano</option>
             <option value="0">pré-escola</option>
             <option value="1">1ª Ano</option>
             <option value="3">3ª Ano</option>
         </select>
% elif turma['serie'] == '3':
    Ano*:
         <select name="serie">
             <option value="3">3ª Ano</option>
             <option value="0">pré-escola</option>
             <option value="1">1ª Ano</option>
             <option value="2">2ª Ano</option>
         </select>
%   end