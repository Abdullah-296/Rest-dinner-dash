
function updatestatusmethod(itemid, c_action) {
    var url = '/update_status/'

        fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken
        },
        body:JSON.stringify({'OrderId': itemid, 'action':c_action})
    })
        .then((response) =>{
            return response.json()

        })

        .then((data) =>{
            refresh_selected_category();
        })

    }