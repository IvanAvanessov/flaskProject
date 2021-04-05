
var message = "Please enter your nickname for this chat";

if (getCookie("nickname") == ""){
    console.log("nickname not found");
} else {
    $("#nickname").val(getCookie("nickname"));
    console.log("found nickname");
    console.log(getCookie("nickname"));
}

$("#overlay_message").text(message);
$(document).on('keypress', function(e){
    if(e.which == 13){
        if ($("#overlay_message").is(":visible")){
            enter_room();
        } else {
            send_message();
        }
        console.log("pressed Enter")
    }
})
// function hide_overlay(){
//     console.log("clicked");
//     $("#overlay").hide(100);
// }

function enter_room(){
    var nickname = $("#nickname").val()
    if (!nickname) {
        display_message("alert-danger", "You have to choose a nickname");
        console.log("empyty box");
        // no nickname created
    } else {
        setCookie("nickname", nickname, 1/24);
        $("#overlay").hide(100);
        $("#currentNickname").text(nickname);
    }
}

function send_message(){
    text = $("#messageBody").val();
    console.log("sending message");
    if(!text){
        display_message("alert-danger", "Cannot send empty message");
    } else {
        const Url = "/" + $("#roomID").val() + "/msg";
        $.ajax({
            url: Url,
            type: "POST",
            data: { message: text,
                    nickname: $("#nickname").val(),
                    roomID: $("#roomID").val()
            },
            success: function(result){
                if(is_true(result)){
                    console.log(result);
                    display_message("alert-success", "Message sent");
                    $("#messageBody").val("");
                }
            },
            error: function(error){
                console.log(error)
            }
        });
    }
}


function get_messages(messageID){
    var data = {};
    data.roomID = $("#roomID").val()
    if(typeof messageID !== 'undefined'){
        //console.log("you are here");
        data.messageID = messageID;
    }
    const Url = "/" + $("#roomID").val() + "/msg";
    $.ajax({
        url: Url,
        type: "GET",
        data: data,
        success: function(result){
            if(is_true(result)){
                for(var i = 0; i < result.length; i++){
                   var chatMessage = $("#messageTemplate").first().clone();
                   chatMessage.prop('id', result[i].id + "_message");
                   chatMessage.removeProp("id");
                   chatMessage.children(".nickname").text(result[i].username);
                   chatMessage.children(".message").text(result[i].message);
                   chatMessage.children(".messageTime").text(result[i].messageTime);
                   chatMessage.children(".messageID").text(result[i].id);
                   chatMessage.children(".exchangeRate").text(result[i].exchangeRate);
                   chatMessage.appendTo("#chatHistory");
                   chatMessage.show(100, function(){
                        $("#chatHistory").scrollTop($("#chatHistory")[0].scrollHeight);
                   });
                   console.log("printed a row");
                }
                
            }
            
        },
        error: function(error){
            console.log(error)
        }
    });

}

// setInterval(function(){
//     var lastMessage=$(".messageTemplate").last().children(".messageID").text();
//     lastMessage = parseInt(lastMessage);
//     get_messages(lastMessage);
//     //console.log("ajax refresh");
//     setCookie("nickname", $("#currentNickname").text(), 1/24);
// }, 1000);

get_messages();