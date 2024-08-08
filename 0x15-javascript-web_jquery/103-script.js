/* global $ */
$(function () {
  function fetchTranslation() {
    var languageCode = $('#language_code').val();
    $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: languageCode })
      .done(function (data) {
        $('#hello').text(data.hello);
      })
      .fail(function () {
        $('#hello').text('Error fetching translation');
      });
  }

  // Fetch translation on button click
  $('#btn_translate').click(fetchTranslation);

  // Fetch translation on Enter key press while focused on input
  $('#language_code').keypress(function (e) {
    if (e.which === 13) { // Enter key pressed
      fetchTranslation();
    }
  });
});
