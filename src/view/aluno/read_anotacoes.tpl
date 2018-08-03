%include('./header.tpl', title = 'Conecturma')
<div class="row">
    <div align="center" class="col-md-12">
        <h1>Escrever anotações</h1>
         <table>
            % for x in alunois:
             <tr>
                 {{x}}<br>
                 ------------------------------
                 <br>
             </tr>
            % end
         </table>
        <a href="/aluno"><button>Voltar</button></a>
    </div>
</div>

%include('footer.tpl')