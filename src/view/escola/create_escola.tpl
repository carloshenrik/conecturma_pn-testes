%include('./header.tpl', title="Conecturma")
<div class="row">
    <div align="left" class="col-md-12">
        <h1>Cadastro</h1>
        <form action="/escola/criar_escola" method="post">
         Nome da escola:   <input type="text" name="nome"/> &ensp;

         Telefone:         <input type="text" name="telefone"/>
            CNPJ:             <input type="text" name="cnpj" size="15"/><br><br>
         Logradouro:    <input type="text" name="logradouro"/> &ensp;
         Bairro:    <input type="text" name="bairro" size="13"/>
         Numero: <input type="text" name="numero" size="3"/><br><br>
         Comlemento :<input type="text" name="complemento"/> &ensp;
         Cep:              <input type="text" name="cep" size="10"/><br><br>

         Estado:            <input type="text" name="estado" size="12" /> &ensp;
         Uf:
              <select name="uf">
                <option value="">-- Selecione --</option>
                <option value="AC">Acre</option>
                <option value="AL">Alagoas</option>
                <option value="AP">Amapá</option>
                <option value="AM">Amazonas</option>
                <option value="BA">Bahia</option>
                <option value="CE">Ceará</option>
                <option value="DF">Distrito Federal</option>
                <option value="ES">Espírito Santo</option>
                <option value="GO">Goiás</option>
                <option value="MA">Maranhão</option>
                <option value="MT">Mato Grosso</option>
                <option value="MS">Mato Grosso do Sul</option>
                <option value="MG">Minas Gerais</option>
                <option value="PA">Pará</option>
                <option value="PB">Paraíba</option>
                <option value="PR">Paraná</option>
                <option value="PE">Pernambuco</option>
                <option value="PI">Piauí</option>
                <option value="RJ">Rio de Janeiro</option>
                <option value="RN">Rio Grande do Norte</option>
                <option value="RS">Rio Grande do Sul</option>
                <option value="RO">Rondônia</option>
                <option value="RR">Rorâima</option>
                <option value="SC">Santa Catarina</option>
                <option value="SP">São Paulo</option>
                <option value="SE">Sergipe</option>
                <option value="TO">Tocantins</option>
            </select> &ensp;
         Municipio : <input type="text" name="municipio"/><br><br>

         Rede:
            <select name = "rede">
                <option value="0"></option>
                %if isinstance(rede, dict):
                    <option value="{{rede['id']}}">{{rede['nome']}}</option>
                % else:
                    % for e in rede:
                        <option value="{{e['id']}}">{{e['nome']}}</option>
                    % end
                    %end
                % end
            </select><br><br>
         <button type="submit">Enviar</button>
        </form>
        <a href="/escola"><button>Voltar</button></a>


    </div>
</div>
%include('footer.tpl')