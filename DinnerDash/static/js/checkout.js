function submitorder() {
var element = document.getElementById('submitorderbutton');
var dataID = element.getAttribute('data-orderid');

orderfood(dataID)

}

function orderfood(itemid) {
    var url = '/checkout-ajax/'

        fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken
        },

        body:JSON.stringify({'Orderid': itemid})
    })
        .then((response) =>{
            return response.json()

        })

        .then((data) =>{
            if (data == 'Reject') {
                alert("Something went wrong, kindly submit it again");
            } else {
                  location.replace(window.location.origin + '/previous_orders');
            }
        })

    }