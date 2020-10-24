$(document).ready(function(){

    //var BASEURL=$('body').data("local")
	var BASEURL=$('body').data("url")  
	
	if  ( JSON.parse(sessionStorage.getItem('session')) !== null ){
		 
		$(".badgeCart").text(  JSON.parse(sessionStorage.getItem('session')).length );
	}
	
    $(".addToCartID").on("click", function(e){
		//e.preventDefault();		
		let id=$(this).data("id"),qte=$("#qteID").val();		
		StoreInCart(id);
		
	});
	$("#couponID").on("click", function(){
		let coupon=$("#coupon-code").val(); 
		let sum=$("#sumPriceID").text(); 
		 
		var url = BASEURL + 'boutique/addcoupon';
		var data={
            "sum": sum,  
            "coupon": coupon,  
        };
		var that=this;
		$.ajax({                                     
               url: url, 
               method      : "POST",
               data        : {data:data},
               dataType    : "JSON",
               beforeSend: function(){ 
                //alert(" coupon : " +data.coupon+", "+data.sum)
               },
               success: function(res){				  
				   if(res.success==true){ 
					  
					 window.location.reload();	 	
					 $(".shopping-coupon-code").remove();		
 				   }else{
					   if (res.message !== null){
						   
						   swal({
							title: " Reduction Introuvable !",
							text: " "+res.message+"...",
							timer: 1000,
							showConfirmButton: true
						}); 
					   }
				   }
              } 
		});
	});
	$(".searchSelectID").on("change", function(){
		var search = $('select[name=searchProd] option:selected').val()
		$("input[name=searchCriteria]").val(search);
		//alert(search+"  "+$("input[name=searchCriteria]").val())
		$("#searchFormID").submit();
		 
	});
	
	$(".removeCartID").on("click", function(){
		let id=$(this).data("id"); 
		 
		var url = BASEURL + 'boutique/removeProduct';
		var data={
            "id": id,  
        };
		var that=this;
		$.ajax({                                     
               url: url, 
               method      : "POST",
               data        : {data:data},
               dataType    : "JSON",
               beforeSend: function(){ 
                 //alert(" retirer: " +data.id)
               },
               success: function(res){				  
				   if(res.success==true){ 
					  // alert("suppression");
					 MinusInCart(data.id);
					 window.location.reload();				
				   }
              } 
		});
	});
	
	$(".prodQTE").on("change", function(){
		let id=$(this).data("id"),qte=$(this).val();
		let old=$(`#sum${id}`).text();
		 
		var url = BASEURL + 'boutique/changeqty';
		var data={
            "id": id,            
            "qte": qte,
			"oldsubsum": parseFloat(old.replace("$","")),
        };
		var that=this;
		$.ajax({                                     
               url: url, 
               method      : "POST",
               data        : {data:data},
               dataType    : "JSON",
               beforeSend: function(){ 
                 //alert(id+ " qte: "+data.qte+" , old: "+old+"  "+JSON.stringify(data) +"  "+$(`#sum${id}`).text() )
               },
               success: function(res){				  
				   if(res.success==true){ 
					$("#sum"+id).html("<span class='badge badge-info'>"+res.minisum+"</span>") 					
					$(".sumPriceID").html("<span >"+res.globalprice+"</span>") 					
				   }
              } 
		});
	});


	$("#addFAQID").on("click", function(){	 
		 
		var url = BASEURL + 'contacts/addcontact';
		var data={
            "name": $("#namefaq").val(),            
            "email": $("#emailfaq").val(),            
            "company": $("#companyfaq").val(),            
            "phone": $("#phonefaq").val(),            
            "message": $("#messagefaq").val(),             
        };
		if ( (data.message.length >= 3) && (data.name.length >3) && (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(data.email)) ){
			$.ajax({                                     
				url: url, 
				method      : "POST",
				data        : {data:data},
				dataType    : "JSON",
				beforeSend: function(){ 
					//alert(data.name+ " qte: "+data.email+" , old: "+data.company+"  "+JSON.stringify(data) +"  "+data.message )
				},
				success: function(res){				  
					if(res.success==true){ 
						swal({
							title: " Merci "+$("#namefaq").val()+" !",
							text: " Nous vous reviendrons très rapidement...",
							timer: 1000,
							showConfirmButton: true
						}); 					
					}
				} 
			});
		}else{
			swal({
				title: "Merci de donner toutes les informations!",
				text: "Oups!"+data.email,
				type: "error",
				timer: 2000,
				showConfirmButton: false
			});
		}
	});
	$("#addCommentforproductID").on("click", function(){	 
		 
		//var artid=$("#productid").val()
		var url = BASEURL + 'commentaire/addcommentforproduct';
		var data={
            "name": $("#authorcom").val(),            
            "email": $("#emailcom").val(),            
            "sujet": $("#sujetcom").val(),            
            "nbstar": $("#nbstar").val(),              
            "comment": $("#comment").val(),             
            "productid": $("#productid").val(),             
        };
		if ( (data.comment.length >= 3) && (data.name.length >3) && (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(data.email)) ){
			$.ajax({                                     
				url: url, 
				method      : "POST",
				data        : {data:data},
				dataType    : "JSON",
				beforeSend: function(){ 
					//alert(data.name+ " qte: "+data.email+"   "+JSON.stringify(data) +"  "+data.comment )
				},
				success: function(res){				  
					if(res.success==true){ 
						swal({
							title: " Merci "+$("#authorcom").val()+" !",
							text: " Nous vous reviendrons très rapidement...",
							timer: 1000,
							showConfirmButton: true
						}); 
						window.location.reload();					
					}
				} 
			});
		}else{
			swal({
				title: "Merci de donner toutes les informations!",
				text: "Oups!"+data.email,
				type: "error",
				timer: 2000,
				showConfirmButton: false
			});
		}
	});
	$("#addCommentID").on("click", function(){	 
		 
		var url = BASEURL + 'commentaire/addcomment';
		var data={
            "name": $("#authorcom").val(),            
            "email": $("#emailcom").val(),            
            //"website": $("#urlcom").val(),             
            "comment": $("#comment").val(),             
            "articleid": $("#articleid").val(),             
        };
		if ( (data.comment.length >= 3) && (data.name.length >3) && (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(data.email)) ){
			$.ajax({                                     
				url: url, 
				method      : "POST",
				data        : {data:data},
				dataType    : "JSON",
				beforeSend: function(){ 
					//alert(data.name+ " qte: "+data.email+"   "+JSON.stringify(data) +"  "+data.comment )
				},
				success: function(res){				  
					if(res.success==true){ 
						swal({
							title: " Merci "+$("#authorcom").val()+" !",
							text: " Nous vous reviendrons très rapidement...",
							timer: 1000,
							showConfirmButton: true
						}); 
						window.location.reload();					
					}
				} 
			});
		}else{
			swal({
				title: "Merci de donner toutes les informations!",
				text: "Oups!"+data.email,
				type: "error",
				timer: 2000,
				showConfirmButton: false
			});
		}
	});
	$(".buyID").on("click", function(e){ 
	
		e.preventDefault();	
		
		var url = BASEURL + 'boutique/getproducts';
		var datagoto=$(this).data('goto');
		cart = sessionStorage.getItem('session');
		
		if( cart !== null){
			
		cart=cart.replace("[","");
		cart=cart.replace("]","");
        var data={
            "cart": cart,            
        };
		$.ajax({                                     
               url: url,
               method      : "POST",
               data        : {data:data},
               dataType    : "JSON",
               beforeSend: function(){ 
                 	//alert( " redirection: "+datagoto)
               },
               success: function(res){				  
				   if(res.success==true){                      
						swal({
							title: " Excellent!",
							text: "Lets continue the process...",
							timer: 2000,
							showConfirmButton: true
						});
						console.log(res.products)							
						//alert(BASEURL+"customers/checkout");
						if(datagoto == "direct")
							window.location=BASEURL+"boutique/checkout";
						else
							window.location=BASEURL+"boutique/cart";

						
				   }
              } 
		});
		}else{
			swal({
				title: " OUPPSs!",
				text: "Merci de choisir un Produit à acheter...",
				timer: 2000,
				type: "warning",
				showConfirmButton: true
			});
			window.location=BASEURL+"boutique/";
		}
		
		 
	});
	
    $("#newsletterBTNID").on("click", function(){
		var email=$('input[name=EMAIL]').val();      
        var url = BASEURL + 'addnewsletter';
        var data={
            "email":email,            
        };
		if(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email)){
           $.ajax({                                     
               url: url,
               method      : "POST",
               data        : {data:data},
               dataType    : "JSON",
               beforeSend: function(){ 
                 
               },
              success: function(res){
				  
               if(res.success==true){                      
					swal({
						title: "Merci à vous!",
						text: "Nous vous reviendrons rapidement...",
						timer: 2000,
						showConfirmButton: false
					}); 
               }
              },
			  complete: function(res){
				  console.log(res)
			  }
           });
		}else{
			swal({
				title: "Merci d'entrer un email valide!",
				text: "Oups!"+email,
				type: "error",
				timer: 3000,
				showConfirmButton: false
			});
		}
    }); 
	
	function StoreInCart(data){
		var a = []; 
		// a = JSON.parse(localStorage.getItem('session')) || []; 
		a = JSON.parse(sessionStorage.getItem('session')) || []; 
		if ( a.includes(data) != true ){
			a.push(data);
			swal({
				title: " Excellent choice!" ,
				text: "Lets continue the process...",
				timer: 1000,
				showConfirmButton: false
			});
			$(".badgeCart").text(a.length);
			//alert(a+ " "+ JSON.stringify(a)); 
			sessionStorage.setItem('session', JSON.stringify(a));
		} 		 
		// localStorage.setItem('session', JSON.stringify(a));
	}
	function MinusInCart(data){
		var a = JSON.parse(sessionStorage.getItem('session')) || [];  
			const index = a.indexOf(data);
			if (index > -1){
				//alert("suppression : "+ index);
				a.splice(index,1);
				$(".badgeCart").text(a.length );
			}
			sessionStorage.setItem('session', JSON.stringify(a));
	}
});
   


