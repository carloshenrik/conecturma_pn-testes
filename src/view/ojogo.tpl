<!doctype html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Conecturma</title>
</head>
<body>
    <h1>Você está jogando o Jogo</h1>
    <h2>{{nome_jogo}}</h2>
    <form action="/ponto" method="get">
        <input type="hidden" name = "jogo" value='{{nome_jogo}}'/>
        <button type="submit" name = "ponto" value="1">Acertou</button>
        <button type="submit" name = "ponto" value="0">Errou</button>
    </form>
    <a href="/">
            <button>Voltar</button>
        </a>
</body>
</html>