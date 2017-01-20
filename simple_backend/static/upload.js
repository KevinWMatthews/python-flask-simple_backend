$(function () {
    $('#fileupload').fileupload({
        dataType: 'json',       // Expect the server to return valid json.

        add: function (e, data) {
            // Add a button to allow the upload to start.
            // Then add a status message to the page during the upload.
            data.context = $('<button/>').text('Upload')
                .appendTo(document.body)
                .click(function () {
                    // This text replaces the Upload button
                    console.log('Upload add: user clicked upload button.');
                    data.context = $('<p/>').text('Uploading...').replaceAll($(this));
                    data.submit();
                }
            );
        },

        submit: function (e, data) {
            //TODO check if the file exists.
            //TODO reject files with wrong extension?
            console.log('Upload submit: ' + data.originalFiles[0].name);
            $('<p/>').text('Sending file to server: ' + data.originalFiles[0].name).appendTo(document.body);
        },

        // The docs say that this generally does not hit because the error callback hits when
        // the server returns a valid HTTP response? But it seem to be hitting....
        fail: function (e, data) {
            console.log('Upload fail: ' + data.textStatus + ' ' + data.errorThrown);
            $('<p/>').text('Upload failed: ' + data.errorThrown).appendTo(document.body);
        },

        // Not sure about the distinction between the error and fail callbacks,
        // but fail is giving a more descriptive errorThrown message.
        /* error: function (e, data) {
         *  $('<p/>').text('Upload error: ' + data.errorThrown).appendTo(document.body);
         *  console.log('Upload: ' + data.textStatus + ' ' + data.errorThrown);
        }, */

        progressall: function (e, data) {
            // This increments the progress bar.
            var progress = parseInt(data.loaded / data.total * 100, 10);
            $('#progress .bar').css(    // Why does '#progress .bar' need a space?
                'width',
                progress + '%'
            );
        },

        done: function (e, data) {
            console.log('Upload file - ' + data.result.name + ': ' + data.textStatus);
            $('<p/>').text('Upload finished!').appendTo(document.body);
        },
    });
});
