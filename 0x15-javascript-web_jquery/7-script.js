// Get `name' from API GET request
const URL = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

$(function () {
  const characterContainer = $('#character');

  $.ajax({
    type: 'GET',
    url: URL,
    success: function (data) {
      characterContainer.text(`${data.name}`);
    }
  });
});
