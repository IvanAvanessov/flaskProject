
var messageAppearTime = 200; // milliseconds
var messageDisplayTime = 5000; //5 seconds
var messageDisappearTime = 100;
var messageUniqueID = 1;
var messageDIV = '<div class="alert alert-danger" role="alert" id="' + messageUniqueID + '" style="display:none;margin:0 auto; \
    position:fixed">' +
    '' +
    '<button type="button" class="close" data-dismiss="alert">&times;</button> \
    </div>';

function display_message(alertType, messageText){
    messageUniqueID += 1;
    var thisMessageUniqueID = messageUniqueID
    var messageDIV = 
                '<div class="mx-auto alert ' + alertType + ' role="alert" id="' + thisMessageUniqueID.toString() + 
                '" style="margin:0 auto;display:none;' +
                'position:float;z-index:' + thisMessageUniqueID * 100 + ';"> ' +
                messageText +
                ' <button type="button" class="close" data-dismiss="alert">&times;</button>' +
                '</div>' 
    $("#messageContainer").prepend(messageDIV);
    var width = $("#" + thisMessageUniqueID.toString() ).width();
    width = width * 1.3;
    var leftMargin = $(document).innerWidth();
    leftMargin = leftMargin/2 - width/2;
    $("#" + thisMessageUniqueID.toString() ).width(width);
    //$("#" + thisMessageUniqueID.toString() ).css('left',leftMargin);
    //$("#" + thisMessageUniqueID.toString() ).attr('left','10%');   
    $("#" + thisMessageUniqueID.toString() ).show(messageAppearTime);
    setTimeout(function(){ 
        $("#" + thisMessageUniqueID.toString()).hide(messageDisappearTime, function() {$("#" + thisMessageUniqueID.toString()).remove();}); 
        } , messageDisplayTime
    );
}

function is_true(text){
    if(text == "False"){
        return false
    } else {
        return true
    }
}


function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    var expires = "expires="+d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}
  
function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

  
function cookieExists(cname) {
    var value = getCookie(cname);
    if (value != "") {
        return true;
    } else {
        return false;
    }
}
