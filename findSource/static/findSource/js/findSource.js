$("#search").click(function (){
    var department = $('#department').val();
    var term = $('#term').val();    
    if (department){
        current_url = window.location.pathname;
        window.location.href = current_url + department+'/'+term;
    }
});

// $('#user-input').keypress(function(e) {
//     if(e.which == 13) {
//         var input = $('#user-input').val();
//         if (input){
//             current_url = window.location.pathname;
//             window.location.href = current_url + input;
//         }
//     }
// });


// jQuery.fn.exists = function(){return this.length>0;}

// $(function() {
// 	$.post("/result", {
// 	    department: $('#department').val(),
// 	    term: $('#term').val(),
// 	}, function(data) {
// 	    if (data.success) {
// 	        window.location.href = data.redirect;
// 	    }
// 	    else {
// 	        alert("Input Error");
// 	    }
// 	});	
// }
