	
	// Render the PayPal button into #paypal-button-container
	paypal_sdk.Buttons({
		style: {
			shape: 'pill',
			color: 'gold',
			layout: 'vertical',
			label: 'paypal',
			height: 40			
		},
		// Set up the transaction
		createOrder: function(data, actions) {
			return actions.order.create({
				purchase_units: [{
					amount: {
						value: $(".totalprice").text()
					}
				}]
			});
		},
		// Finalize the transaction
		onApprove: function(data, actions) {
			return actions.order.capture().then(function(details) {
				// Show a success message to the buyer
				alert('Transaction completed by ' + details.payer.name.given_name + '!'+ JSON.stringify(details));
				var data ={                    
					'name': details.payer.name.given_name,                    
					'total': $(".totalprice").text(),                    
					'clientinfo':   JSON.stringify(details)                  
				}

				$.ajax({
						url: BASEURL + 'pay/paypalpay',
						data: {data:data},
						method: "post",
						beforeSend: function(){
							alert("  suivi:  "+data.name+", prix: "+data.total);
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
								console.log("error: lors de l'nvoi du paypal")
							}
						}
				});
			});
		},
		onShippingChange: function(data, actions) {
			alert("shiping change" );
		},
		onCancel: function (data) {
		// Show a cancel page, or return to cart
			alert("cancel");
		},
		onError: function (err) {
		
		// Show an error page here, when an error occurs
			alert("error");
		}
	}).render('#paypal-button-container');