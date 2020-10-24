$('#card_error').toggle(false)
    
var $form = $('#paymentForm');
Stripe.setPublishableKey("pk_test_51HH6ILLJd4vqWOkvtVrytneUXD8xqRuLvaDXeYJNLpPd9CYkbYyDgPKfxCs6K44qm9qm5112vVwCnv3DPirQ7g4900zypB8jHx");

$("#payBtn").on("click",function(e){
    $("#payBtn").prop("disabled",true)
    Stripe.card.createToken( $form, stripeResponseHandler);
})



function stripeResponseHandler(status, response) {
     
    var $form = $('#paymentForm');
    $("#payBtn").prop("disabled",true)
    if (response.error) {  
        $form.find(".alert").remove();
        $form.prepend('<p class="alert alert-danger">'+response.error.message+'</p>');
        $("#card_error").html('<p>'+response.error.message+'</p>');
        $form.find('button').prop('disabled', false); // Re-enable submission

    } else {  
        var token = response.id;
         $form.append($('<input type="hidden" name="stripeToken" />').val(token));
        
        //alert(token)
        AsyncSendDataAndToken(token)
        //$form.get(0).submit();

    }
}

function AsyncSendDataAndToken(token){ 
    var BASEURL=$('body').data("local")
	//var BASEURL=$('body').data("url")            
    if (token !==  null ){  
        data ={                    
            'token': token,                    
            'total': $(".totalprice").text(),                    
            'clientinfo': $("input[name=surname]").val()+ $("input[name=name]").val()+ $("input[name=email]").val()+ $("input[name=phone]").val(),                    
        },          
        $.ajax({
                url: BASEURL + 'pay/stripepay',
                data: {data:data},
                method: "post",
                beforeSend: function(){
                    alert("module suivi:  "+data.token+", prix: "+data.total);
                },
                dataType: 'json',

                success: function (data) {
                    if (data.success) {  
                                                    
                        swal(data.message +",Merci de Completer vos informations de Livraison");
                       // alert(data.message);

                        $(".order-btn").removeClass("btn-default").addClass("btn-info");
                        $(".directpay").toggle(true);
                        $('#paymentForm').find('button').prop('disabled', true);

                        
                    }else{
                        console.log("error: lors de l'nvoi du token")
                    }
                }
        });
    }
}