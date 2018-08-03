% include('header.tpl', title = 'Conecturma')
<div class="row">
    <div align="center" class="col-md-12">
        <h1>Usuarios inativos</h1>
        <br>
        <table>
            <tr>
                <th>Nome </th><th>Telefone </th><th>rua </th><th>numero </th><th>estado </th><th>cidade </th>
            </tr>

            % for usuarios in usuarios:
            <tr>
                <td>
                    {{usuarios['nome']}}
                </td>
                <td>
                    {{usuarios['telefone']}}
                </td>
                <td>
                    {{usuarios['senha']}}
                <td>
                    {{usuarios['numero']}}
                </td>
                <td>
                    {{usuarios['estado']}}
                </td>
                <td>
                    {{usuarios['vinculo_escola']}}
                </td>
                <td>
                    {{usuarios['tipo_aluno']}}
                </td>
                <td>
                    {{usuarios['tipo_usuario']}}
                </td>
                <td>
                    <form action="/escola/editar">
                        <button type="submit" name="nome" value="{{usuarios['nome']}}">Editar</button>
                    </form>
                </td>
            </tr>
            %end
        </table>
        <a href="/">
            <button>voltar</button>
        </a>
    </div>
</div>

% include('footer.tpl')