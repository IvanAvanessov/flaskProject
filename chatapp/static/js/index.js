
$("#createRoom").click(function(){
    alert("connected2")
});

$("#joinRoom").click(function(){
    alert("joining room1")
});

function joinRoom(){
    text = $("#roomID").val();
    alert('atat')
    const Url = '/chatroom'
    $.ajax({
        url: Url,
        type: "GET",
        success: function(result){
            console.log(result)
        },
        error: function(error){
            console.log(error)
        }
    });
    alert(text);
}

function createRoom(){

}