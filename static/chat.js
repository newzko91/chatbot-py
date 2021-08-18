$(function () {

    /* 
        Ao clicar no botão enviar, o valor do campo texto é enviado para a função que 
        irá verificar se existe resposta na base para a "pergunta" e o campo texto é 
        setado em branco e é chamada também a função que vai escrever na tela a mensagem que 
        o usuário enviou e também a resposta do robô.
    */
    $('#btnEnviar').click(function (e) {
        $('#messageText').val('');
        e.preventDefault();
        $('#chatbot-form').submit();
    });
    
    /*
        Escreve na tela "VOCÊ:" e abaixo o valor que antes estava no campo "messageText".
        Através do método POST a resposta do robô é escrita na tela.
    */
    $('#chatbot-form').submit(function (e) {
        e.preventDefault();
        var whoschatting = 'VOCÊ: ';
        var message = $('#messageText').val();
        $(".media-list").append('<li class="media"><div class="media-body"><div class="media"><div style = "color : yellow" align="right" class="media-body">' + whoschatting + '<p style = "color : #2EFE2E" class="media-body">' + message + '<hr/></div></div></div></li>');
        $('#user-is-typing').html('<p style = "color : #f28df7" class="media-body">Adelaide está escrevendo...');

        $.ajax({
            type: "POST",
            url: "/atendimento",
            data: $(this).serialize(),
            success: function (response) {
                $('#messageText').val('');
                var attendant = 'ADELAIDE: ';
                var answer = response.answer;
                const chatPanel = document.getElementById("chatPanel");
                $('#user-is-typing').html('');
                $(".media-list").append('<li class="media"><div class="media-body"><div class="media"><div style = "color : #f28df7" class="media-body">' + attendant + '<p style = "color : #ffffff" class="media-body">' + answer + '<hr/></div></div></div></li>');
                $(".fixed-panel").stop().animate({ scrollTop: $(".fixed-panel")[0].scrollHeight }, 1000);

            },
            error: function (error) {
                console.log(error);
            }
        });
    });
});