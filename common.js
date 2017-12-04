(function() {
    $('.js-like').on('click', function() {
        //console.log('click');
        var $btn = $(this);
        $.ajax({
            url: '/like/',
            type: 'POST',
            dataType: 'json',
            data: {
                article_id: $btn.data('id'),
                csrfmiddlewaretokken: $()
            }
        }).done(function(resp) {
            if (resp && resp.status && resp.status == 'ok'{
                window.location.reload();
            }
        });
        return false;
    });

})();
