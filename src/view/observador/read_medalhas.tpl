<!--% include('./header.tpl', title = 'Conecturma')-->
<div class="row">
    <div align="center" class="col-md-12">
        <h1>Ver medalhas</h1>
        <br>
        <table>
            <tr>
            <tr>nome da medalha   </tr>   <tr>    tipo da medalha</tr>
            </tr>
            % for medalhas in medalhas:
            <tr>
                <td>
                    {{medalhas['nome']}}
                </td>
                <td>

                </td>
            </tr>
            %end
        </table>
        <a href="/">
            <button>voltar</button>
        </a>
    </div>
</div>
<!--% include('./footer.tpl')-->