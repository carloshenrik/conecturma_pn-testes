%include('./header.tpl', title = 'Conecturma')
   <div align="center" class="col-md-12">
        <h1>Ver Itens</h1>
        <div class="row">
            <%
                for itens in lista_itens:

            %>
                    <div class="col-md-3">
                        {{itens['nome']}}<br>
                    <form action="/equipar_item" method="post">
                        <button name="id" value="{{itens['id']}}">Equipar</button>
                    </form>
                    </div>
            <%
                end
            %>

        </div>
        <a href="/aluno/area_aluno"><button>Voltar</button></a>
   </div>

% include('footer.tpl')