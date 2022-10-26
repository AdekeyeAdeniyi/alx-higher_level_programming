// Display all `title` from API GET request
const URL = 'https://swapi-api.hbtn.io/api/films/?format=json';

$(function () {
  const titleContainer = $('#list_movies');

  $.ajax({
    type: 'GET',
    url: URL,
    success: function (data) {
      const result = data.results;

      $.each(result, function (index, item) {
        const listTitle = `<li data-id=${index}> ${item.title} </li>`;
        titleContainer.append(listTitle);
      });
    }
  });
});
