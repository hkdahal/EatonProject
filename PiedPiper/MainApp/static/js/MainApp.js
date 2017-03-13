function initiate(url) {

    $('#loadingMessage').show();
    $.ajax({
        url: url,
        dataType: 'json',
        success: function (jsonData) {
            $('#datatable').dataTable({
                data: jsonData,
                columns: [
                    {
                        title: 'Track ID',
                        data: 'trackId',
                        defaultContent: 'Null'
                    },
                    {
                        title: 'Artist Name',
                        data: 'artistName',
                        defaultContent: 'Null'
                    },
                    {
                        title: 'Track Name',
                        data: 'trackName',
                        defaultContent: 'Null'
                    },
                    {
                        title: 'Release Date',
                        data: 'releaseDate',
                        defaultContent: 'Null'
                    }
                ]
            });
            $('#loadingMessage').hide();
            $('#myButton').show();

        }
    });

    $('#datatable').on('mouseover', 'tbody tr', function () {
        $(this).css({
            'cursor': 'pointer',
            'color': 'blue'
        });
    })

    $('#datatable').on('mouseout', 'tbody tr', function () {
        $(this).css({
            'cursor': 'default',
            'color': 'inherit'
        });
    })

    $('#datatable').on('click', 'tbody tr', function () {
        var url = window.location.href;
        url += 'details/' + $(this).children(':first').text();
        window.location.assign(url);
    });

}

function animateSaveFeature(url) {

    $.ajax({
        'url': url,
        'type': 'GET',
        beforeSend: function () {
            $('.theContent').hide();
            $('.uploadingMessage').show();
        },
        error: function () {
            alert('Error');
        },
        'success': function (data) {
            $('.uploadingMessage').hide();
            $('.savedMessage').show();
        }
    });
}