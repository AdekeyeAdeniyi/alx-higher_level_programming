// Add a new list element on click event
$(function () {
  const div = $('#add_item');
  const listContainer = $('.my_list');

  div.on('click', function () {
    const newList = '<li> Item </li>';
    listContainer.append(newList);
  });
});
