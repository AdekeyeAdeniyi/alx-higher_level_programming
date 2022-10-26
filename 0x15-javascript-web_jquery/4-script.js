// Toogle `.red' or '.green' class on HTML `<header>` on click
$(function () {
  const div = $('#toggle_header');
  const header = $('header');

  div.on('click', function () {
    header.toggleClass('red green');
  });
});
