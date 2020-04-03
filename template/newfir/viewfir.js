function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#blah')
                .attr('src', e.target.result);
        };

        reader.readAsDataURL(input.files[0]);
    }
}
/*$('#nextbtn').click(function(e) {
    e.preventDefault();
    var info = $('#note-textarea').val();

    $.ajax({
        type: "POST",
        url: 'xxx',
        data: {text: info}
    });
}); 
$('#nextbtn').on('click', function(){
 $.ajax({
   type    : "get",
   url     : 'xxx',       
   success : function(data)
   {
     $('#demo').val(data);
   }
 });
});
*/