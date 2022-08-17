
function perform_ajax_update_cart(id, action, page){
    if(action == 'CLEARCART'){
      var checkedBoxes = getCheckedBoxes("checkbox");
        if (checkedBoxes == null){
                        select_item_cart();
                    }
                    else {
                        clearusercart(id, action, checkedBoxes);
                    }
    } else {
          updateusercart(id, action, page);
    }
}

function perform_ajax_update_session_cart(id, quantity, action, page){
    if(action == 'CLEARCART'){
        var checkedBoxes = getCheckedBoxes("checkbox");
        if (checkedBoxes == null){
                        select_item_cart();
                    }
                    else {
                        clearsessioncart(id, action,quantity, checkedBoxes);
                    }

    } else {
       sessioncart(id,action,quantity,page)

    }
}


function clearsessioncart(itemid,c_action,item_quantity, checkedBoxes) {
    var url = '/session_cart/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },

        body: JSON.stringify({'ItemId': itemid, 'action': c_action, 'item_quantity': item_quantity, 'check': checkedBoxes})
    })
        .then((response) => {
            return response.json()

        })

         .then((data) => {
            refresh_session_order();
            refresh_current_cart_number();
        })
}




function sessioncart(itemid,c_action,item_quantity, page) {
    var url = '/session_cart/'

        fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken
        },

        body:JSON.stringify({'ItemId': itemid, 'action':c_action, 'item_quantity': item_quantity})
    })
        .then((response) =>{
            return response.json()

        })

        .then((data) =>{
            if (page == 'order'){
                refresh_session_order();
                refresh_current_cart_number();
            } else if (page == 'detail'){
                refresh_item_detail(data);
            } else {
                refresh_cart_number_items(data);
            }
        })

    }


function clearusercart(itemid, c_action, checkedBoxes) {

    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },

        body: JSON.stringify({'ItemId': itemid, 'action': c_action, 'check': checkedBoxes})
    })
        .then((response) => {
            return response.json()

        })

        .then((data) => {
            refresh_current_order();
            refresh_current_cart_number();
        })
}

function updateusercart(itemid, c_action, page) {
    var url = '/update_item/'

        fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken
        },

        body:JSON.stringify({'ItemId': itemid, 'action':c_action})
    })
        .then((response) =>{
            return response.json()

        })

        .then((data) =>{
            if (page == 'order'){
                refresh_current_order();
                refresh_current_cart_number();
            } else if (page == 'detail'){
                refresh_item_detail(data);
            } else {
                refresh_cart_number_items(data);
            }
        })
    }










var UpdateCart = document.getElementsByClassName("UpdateCart");

for (var i = 0; i < UpdateCart.length; i++)
{
    UpdateCart[i].addEventListener('click',
        function () {

            var itemid = this.dataset.product;
            var c_action = this.dataset.action;

            var checkedBoxes = getCheckedBoxes("checkbox");

            if (user == 'AnonymousUser') {
                var item_quantity = this.dataset.quantity;

                if (c_action == 'CLEARCART') {
                    if (checkedBoxes == null){
                        alert("kindly select item first which you want to delete")
                    }
                    else {
                       sessioncart1(itemid,c_action,item_quantity, checkedBoxes)
                    }

                } else {
                    sessioncart(itemid,c_action,item_quantity)
                }
            }  else {

                if (c_action == 'CLEARCART') {
                    if (checkedBoxes == null){
                        alert("kindly select item first which you want to delete")
                    }
                    else {
                        updateusercart1(itemid, c_action, checkedBoxes);
                    }
                } else {

                    updateusercart(itemid, c_action);
                }
            }

        })
}

function getCheckedBoxes(chkboxName) {
  var checkboxes = document.getElementsByName(chkboxName);
  var checkboxesChecked = [];
  for (var i=0; i<checkboxes.length; i++) {
     if (checkboxes[i].checked) {
        checkboxesChecked.push(checkboxes[i].value);
     }
  }
  return checkboxesChecked.length > 0 ? checkboxesChecked : null;
}