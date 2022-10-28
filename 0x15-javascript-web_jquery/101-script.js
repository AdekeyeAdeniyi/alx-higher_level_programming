/*
    Script to:
    `Add`
    `Delete` and `Clear` List
*/
$(function () {
  const addList = $('#add_item');
  const removeList = $('#remove_item');
  const clearList = $('#clear_list');
  const listContainer = $('.my_list');

  // Add new list
  addList.on('click', function () {
    const newList = '<li> Item </li>';
    listContainer.append(newList);
  });

  // Remove list
  removeList.on('click', function () {
    listContainer.children().last().remove();
  });

  // Clear list
  clearList.on('click', function () {
    $('li').remove();
  });
});
