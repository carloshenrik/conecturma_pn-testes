%include('./header.tpl', title = 'Conecturma')
<div class="row">
        <div align="center" class="col-md-12">
            <a href="/rede/create_rede">
            <button>criar rede</button>
            </a>

            <a href="/rede/read_rede">
            <button>ver redes</button>
            </a>
            <a href="/">
            <button>voltar</button>
                </a>
            <table>
                <tr>
                    <th>Nome da rede</th><th>telefone</th>
                </tr>
                    % if redes is None:
                        <h1>Nenhuma rede cadastrada</h1>
                    %else:
                    %   for r in redes:
                            <tr>
                                <td>
                                    {{r['nome']}}
                                </td>
                                <td>
                                    {{r['telefone']}}
                                </td>
                            </tr>
                    %   end
                    %end
            </table>
        </div>
    </div>

%include('footer.tpl')