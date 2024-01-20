const card = document.getElementById("card");
const dropZone = document.getElementById("drop-zone");
const dragZone = document.getElementById("drag-zone");
card.addEventListener("dragstart", function (event) {
  console.log(event);
});
dropZone.addEventListener("dragover", function (event) {
  event.preventDefault();
});
dragZone.addEventListener("dragover", function (event) {
  event.preventDefault();
});
dropZone.addEventListener("drop", function (event) {
  dropZone.prepend(card);
});
