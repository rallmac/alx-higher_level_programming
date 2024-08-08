/* global $ */
$(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=json=fr', function (data) {
    $('#hello').text(data.hello);
  });
});
