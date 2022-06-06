var evt = new MouseEvent("click", {
    view: window,
    bubbles: true,
    cancelable: true,
    clientX: 20
});
var targetElement = document.getElementById("bigCookie");

targetElement.dispatchEvent(evt);


// var clicker = new Promise((resolve, reject) => {
//   for (var i = 0; i < 50; i++) {
//     targetElement.dispatchEvent(evt);
//   }
// });
