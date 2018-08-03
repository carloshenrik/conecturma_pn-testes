<table class="table table-bordered" style="margin-top:-3px;">
    <thead style="background-color:#9ed0f6;">
      <tr style="color:#fff;">

        <th scope="col">Descritor</th>
        <th scope="col">Desempenho</th>
        <th scope="col"> <a href="#" > <i class="fas fa-exclamation-circle "></i> </a> </th>
      </tr>
    </thead>
    <tbody style="background-color:#f3f3f3;">
        
        %teste = 0
        %for i in oa:
              <tr>
                <td>
                    <a href="/relatorios/visualizar_relatorio_oa_aluno?aluno={{aluno['id']}}&oa={{i['sigla_oa']}}" style="color:#000; text-decoration: none;">
                        {{i['descricao_descritor']}}
                    </a>
                </td>
                  <td>
                      %if porcentagem[teste] == None:
                        %pass
                      %elif int(porcentagem[teste]) >= 70:
                        <div class="container" style="height:30px; width:30px; border-radius:50%;background-color:green;"></div>
                      %elif int(porcentagem[teste]) >= 50 and int(porcentagem[teste]) <= 69:
                        <div class="container" style="height:30px; width:30px; border-radius:50%;background-color:yellow;"></div>
                      %elif int(porcentagem[teste]) >= 0 and int(porcentagem[teste]) <= 49:
                        <div class="container" style="height:30px; width:30px; border-radius:50%;background-color:red;"></div>
                      %end
                  </td>
                  %teste+=1
                <td></td>
              </tr>
        %end
    </tbody>
  </table>