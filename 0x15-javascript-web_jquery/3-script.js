// Add `.red' class to HTML `<header>` on click
$(function () {
  const div = $('#red_header');
  const header = $('header');

  div.on('click', function () {
    header.addClass('red');
  });
});
