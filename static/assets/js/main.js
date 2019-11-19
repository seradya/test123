$(document).ready(function() {
    //form submission
    $('#feedback').submit(function (e) {
        e.preventDefault();

        var btn = $('#button-feedback');
        btn.text('ОТПРАВКА...');
        btn.attr('disabled', true);

        var data = {};
        data.name = $('#feedback [name="name"]').val();
        data.email = $('#feedback [name="email"]').val();
        data.csrfmiddlewaretoken = $('#feedback [name="csrfmiddlewaretoken"]').val();

        var url = $('#feedback').attr("action");
        console.log(data.name);
        console.log(data.email);
        console.log(data.csrfmiddlewaretoken);
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                $('#feedback [name="name"]').val('');
                $('#feedback [name="email"]').val('');
                btn.text('ОТПРАВИТЬ');
                btn.attr('disabled', false);
                alert(data.result);
            },
            error: function () {
                console.log("error");
            }
        });
    });
});