function itemavailability() {
var element = document.getElementById('changeavailability');
var itemid = element.getAttribute('data-orderid');
var action = element.getAttribute('data-action');

changeavailability(itemid, action)

}

function changeavailability(itemid, action) {
    var url = '/change-availability/'

        fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken
        },

        body:JSON.stringify({'itemid': itemid, 'action': action })
    })
        .then((response) =>{
            return response.json()

        })

        .then((data) =>{

            if (data == 'Reject') {
                alert("Cant change status, you dont have authority to change the item availability")
            } else {
                 refresh_item_detail();
            }
        })

    }