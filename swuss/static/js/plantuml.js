$(function() {
    $("#plantuml-submit").on("click", function() {
        var text = $("#plantuml-input").val();
        console.log(text);
        $.post({
            type: "POST",
            url: "/plantuml/generate",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify({
                text: text
            }),
        }).done(function(data) {
            console.log(data);
            $("#plantuml-output").html(data);
        });
    });
});
