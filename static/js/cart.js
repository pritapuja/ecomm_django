var updateBtns = document.getElementsByClassName('update-cart')

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.order
        // var productId = this.dataset.produk_item
        var action = this.dataset.action
        console.log('productId:', productId, 'Action:', action)
    })
    
}

function addCookieItem(productId, action){
    console.log('Not logged in..')

    if (action == 'add'){
		if (OrderSummaryView[productId] == undefined){
		    OrderSummaryView[productId] = {'quantity':1}
		}else{
			OrderSummaryView[productId]['quantity'] += 1
		}
	}

    if (action == 'remove'){
		OrderSummaryView[productId]['quantity'] -= 1

		if (OrderSummaryView[productId]['quantity'] <= 0){
			console.log('Remove Item')
			delete OrderSummaryView[productId]
		}
	}

    console.log('Cart:', OrderSummaryView)
    document.cookie = 'OrderSummaryView=' + JSON.stringify(OrderSummaryView) + ";domain=;path=/"
    location.reload()
}

function updateUserOrder(productId, action) {
    console.log('User is logged in, sending data..')

    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action': action})
    })
    
    .then((response) =>{
        return response.json()
    })
    .then((data) =>{
        console.log('data:', data)
        location.reload()
    })
}