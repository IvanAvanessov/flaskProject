function join_room(){
    text = $("#roomID").val();
    //alert('trying to access room now')
    if (text) {
        const Url = '/' + text
        $.ajax({
            url: Url,
            type: "POST",
            success: function(result){
                if(result) { // room exists
                    if (is_true(result)){
                        console.log(result)
                        window.location.href = "/" + text //redirect to room
                    } else {
                        display_message("alert-danger", "Could not find the room. Please check the room ID")
                        console.log('Room not found')
                    }
                    //window.location.href = '/' + text
                } else {
                    display_message("alert-danger", "Could not connect to Server")
                    console.log('Error searching for room')
                }
            },
            error: function(error){
                console.log(error)
            }
        });
        //alert(text);
        //style="display:none"
    } else {
        display_message("alert-danger", "Room ID cannot be blank")
    }
}

function create_room(){
    //alert('creating room now')
    const Url = '/'
    $.ajax({
        url: Url,
        type: "POST",
        success: function(result){
            if(is_true(result)){
                console.log(result)
                window.location.href = "/" + result
            }
        },
        error: function(error){
            console.log(error)
        }
    });
}

