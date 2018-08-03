% include('header.tpl', title = 'Conecturma')
    <div class="row">
        <div align="center" class="col-md-3">
            <h1>Avatar </h1>
            Cor:{{avatar['cor']}}<br/>
            Rosto:{{avatar['rosto']}}<br/>
            Acessorio:{{avatar['acessorio']}}<br/>
            Corpo:{{avatar['corpo']}}<br/>
        </div>
        <div align="left" class="col-md-3">
            moedas:{{moedas}} &ensp; &ensp; vidas : {{vidas}}
        </div>
        <a href="/medalhas"> Medalhas </a>
        <div align="center" class="col-md-6">
            <h1>Bem Vindo {{usuario}} </h1>
            <h2>A Conecturma!</h2>
            <a><button>Jogo</button></a>
            <iframe src="/jogo" width="1024px" height="1000px"></iframe>
            <br>
            <a href="/aluno/loja"><button>Loja</button></a>
            <a href="/aluno/ver_itens_comprados"><button>Ver Itens</button></a>
            <a href="/sair"><button>Sair</button></a>
        </div>
    </div>
    <script>
        window.addEventListener("message", function (event) {
            console.log("PostMessage recebido.");
            var origemEvento = event.origin;
            console.log("message origin: " + event.origin);
            console.log("message source: " + event.source);
            console.log("message data: " + event.data);
            var parametros = JSON.parse(event.data);
            enviarRequisicaoAjax(
                parametros,
                function (data, textStatus, jqXhr) {
                    console.log("callback de sucesso ajax: " + textStatus);
                    var resposta = {};
                    try {
                        resposta = data;
                    } catch (ex) {
                        resposta = {
                            mensagensErro: ["Ocoreu um erro inesperado."],
                            tipoErro: "inesperado"
                        };
                    }
                    resposta.uuid = parametros.uuid;
                    event.source.postMessage(resposta, event.origin);
                },
                function (jqXhr, textStatus, errorThrown) {
                    console.log("callback de erro ajax: " + textStatus + ", " + errorThrown);
                    var respostaErro;
                    if (errorThrown === "Internal Server Error") {
                        respostaErro = {
                            mensagensErro: ["Ocoreu um erro inesperado."],
                            tipoErro: "inesperado"
                        };
                    } else {
                        respostaErro = {
                            mensagensErro: ["Não foi possível comunicar com o servidor."],
                            tipoErro: "conexaoServidor"
                        };
                    }
                    respostaErro.uuid = parametros.uuid;
                    event.source.postMessage(respostaErro, event.origin);
                }
            );
        });
        function enviarRequisicaoAjax(parametros, callbackSucesso, callbackErro) {
            console.log("enviarRequisicaoAjax parametros", parametros);
            console.log(parametros.operacao);
            var jqXhr = jQuery.ajax({
                type: "POST",
                url: "http://localhost:8080/" + "api/plataforma/" + parametros.operacao,
                traditional: true,
                data: JSON.stringify(parametros),
                contentType: "application/json; charset=utf-8",
                dataType: "json"
            })
            .done(callbackSucesso)
            .fail(callbackErro);
        }
    </script>
% include('footer.tpl')