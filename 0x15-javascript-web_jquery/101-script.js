$(function($){
  let lista = $("UL.my_list");
  $('DIV#add_item').click(() => lista.append('<li>Item</li>'));
  $('DIV#remove_item').click(() => lista.children().last().remove());
  $('DIV#clear_list').click(() => lista.empty());
})
