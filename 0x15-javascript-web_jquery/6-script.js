// Update HTML `<header>` text on click event
$(function () {
  const div = $('#update_header');
  const header = $('header');

  div.on('click', function () {
    header.text('New Header!!!');
  });
});
