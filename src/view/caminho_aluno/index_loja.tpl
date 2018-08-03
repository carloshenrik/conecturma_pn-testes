% include('./header.tpl', title = 'Conecturma')
<div class="row">
    <div align="center" class="col-md-12">
        <h1>Loja</h1>
        <br>
        <form action="/compras_loja">
            <div class="row">
                <%
                    if itens:
                        for x in itens:
                            if str(x['id']) not in itens_comprados:
                %>

                                <div class="col-md-3">
                                    {{x['nome']}}<br>
                                    R${{x['preco']}},00<br>
                                    <button type="submit" name="id" value="{{x['id']}}">Comprar</button>
                                </div>
                                <br>

                            %else:
                                <div class="col-md-3">
                                    {{x['nome']}}<br>
                                    R${{x['preco']}},00
                                </div>
                                <br>
                <%
                            end
                        end
                    else:
                %>
                    <h1>Não possui Itens cadastrados</h1>
                %end
            </div>
        </form>
        <a href="/">
            <button>voltar</button>
        </a>
    </div>
</div>
        % include('./footer.tpl')