// Display `hello` value from API GET request
const URL = 'https://fourtonfish.com/hellosalut/?lang=fr';

$(function () {
  const div = $('#hello');

  $.ajax({
    type: 'GET',
    url: URL,
    contentType: 'application/json',
    success: function (data) {
      div.text(data.hello);
    }
  });
});
