function esqueci_senha(){
    email = document.getElementById('email')
    if(validar_se_email_existe(email)){
         window.location="/view_reformular_senha?email="+email.value;
    }
    else{
        document.getElementById('mensagem_erro').innerHTML='Email digitado não existe =('
    }
}

function filtro_usuario(){
   filtro_escola = document.getElementById('filtro_escola').value;
   filtro_rede = document.getElementById('filtro_rede').value;
   filtro_turma =  document.getElementById('filtro_turma').value;
   filtro_tipo_usuario =  document.getElementById('filtro_tipo_usuario').value;

   teste();

  $.post('/filtro_usuario', {escola:filtro_escola, rede:filtro_rede, turma:filtro_turma,tipo_usuario:filtro_tipo_usuario},function(data){
       $('#usuarios_sistema').html(data);


  });

  return false;
}
function teste(){
 $.post('/filtro_pesquisa', {escola:filtro_escola, rede:filtro_rede, turma:filtro_turma,tipo_usuario:filtro_tipo_usuario},function(data){
       console.log("log",data);
       $('#dropdown_filtros').html(data);
  });
}


function cadastro_observador(){
    tipo = document.getElementById('tipo');
    nome = document.getElementById('nome');
    senha = document.getElementById('senha');
    telefone =  document.getElementById('telefone');
    cpf = document.getElementById('cpf');
    email = document.getElementById('email');
    escola = document.getElementById('escola');
    rede = document.getElementById('rede');
    turma = document.getElementById('turma');

    if(!validar_campo_vazio(nome)){
        if(!validar_campo_vazio(senha)){
            if(!validar_campo_vazio(telefone)){
                if(!validar_campo_vazio(email)){
                    if(!validar_se_email_existe(email) && !validar_campo_vazio(cpf) && !validar_campo_vazio(rede) && !validar_campo_vazio(escola)){
                        $.post('/create_observador', {tipo:tipo.value,nome:nome.value,senha:senha.value,telefone:telefone.value,cpf:cpf.value,email:email.value,escola:escola.value,rede:rede.value,turma:turma.value},function(){
                        });
                        window.location="/gestao_aprendizagem/usuario";
                    }
                    else{
                        document.getElementById('erro_email').innerHTML = "Email já foi cadastrado";
                    }
                }
            }
        }
    }
}

function validar_campo_vazio(parametro){
    if(parametro.value == ''){
        document.getElementById(parametro.id).style.boxShadow = "0px 0px 12px #fe1313";
        return true;
    }
    else{
        document.getElementById(parametro.id).style.boxShadow = "0px 0px 0px #fe1313";
        return false;
    }
}

function emailValidador(){
    var email = document.getElementById("email");
    var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if(!email.value.match(mailformat)){
        document.getElementById("email").style.boxShadow = "0px 0px 12px #fe1313";
    }
    else{
        document.getElementById("email").style.boxShadow = "0px 0px 0px";
    }
}


function validar_se_email_existe(email){
    var retorno;
    $.ajax({
        url:    "/observador/email_existe",
        type:   "post",
        data:   {teste_email:email.value},
        async: false,

        success: function( data ){
            retorno = data;
        }
    });
    if(retorno == email.value){
        return true;
    }
    else{
        return false;
    }
}

var letras_senha = {'a':false, 'b':false, 'c':false, 'd':false, 'e':false, 'f':false, 'g':false, 'h':false, 'i':false, 'k':false, 'l':false};

function mudaEstado(letra){
 	var imagem = document.getElementById(letra);
 	var num = 3;
 	var selecionada = false;
 	if (!letras_senha[letra]){
 		imagem.style.background= 'rgba(229, 255, 84, 0.5)';
 		letras_senha[letra] = letra
 	}else{
 		imagem.style.background = ' rgba(113, 194, 117, 0.5)';
 		letras_senha[letra] = false
 	}
}

function mouse_in(letra){
 	var imagem = document.getElementById(letra);
  if (!letras_senha[letra]){
 	  imagem.style.background= 'rgba(229, 255, 84, 0.5)';
  }
}

function mouse_out(letra){
 	var imagem = document.getElementById(letra);
  if (!letras_senha[letra]){
 	  imagem.style.background= 'rgba(113, 194, 117, 0.5)';
  }
}

function login_aluno(){
  nome = document.getElementById('Login').value;
  senha = [];
  for (var i in letras_senha){
    if (letras_senha[i]){
      senha.push(letras_senha[i]);
    }
  }
  senha = senha.join('')
  $.post('/login/login_aluno', {aluno_login_nome:nome, aluno_senha:senha},function(data){
      console.log(data);
     window.location.replace(data);
  });
}

function login_professor(){
  email = document.getElementById('inputEmail').value;
  senha = document.getElementById('inputPassword').value;
  if (email != '' && senha !=''){
    $.post('/login/login_observador', {observador_login_email:email, observador_senha:senha},function(data){
        console.log(data);
       window.location.replace(data);
    });
  }
}


function filtro_relatorio_aluno_detalhe(teste){
    portugues = document.getElementById('portugues');
    matematica = document.getElementById('matematica');
    if (!portugues.checked){
        diciplina = '2'
    }
    else if (!matematica.checked){
        diciplina = '1'
    }
    else{
        diciplina = '0'
    }
    
    $.get('/trazer_oas', {aluno:teste, diciplina:diciplina},function(data){
        $('#teste').html(data);
   });

}