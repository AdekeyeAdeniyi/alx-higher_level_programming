// Update HTML `<header>` text color on click
$(function () {
  const div = $('#red_header');
  const header = $('header');

  div.on('click', function () {
    header.css('color', '#FF0000');
  });
});
