$(document).ready(function () {
    console.log("ready!")
    $(".add-watchlist-btn").on('click', function() {
        button_id = "#watchlist-btn-" + $(this).val().toString()
        data = {pid: $(this).val().toString(), add: $(this).hasClass("fa-plus")}
        console.log(data)
        $.ajax({
            url: '/api/watchlist/add',
            data: JSON.stringify(data),
            type: 'POST', 
            success: function (response) {
                $(button_id).toggleClass("fa-minus fa-plus")
                $(button_id).toggleClass("btn-primary btn-outline-danger")
            },
            error: function (error) {
                console.log("ERROR");
                console.log(error);
            },
            dataType: "json",
            contentType: 'application/json;charset=UTF-8'
        })
    });
});
