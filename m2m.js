const mediumToMarkdown = require('medium-to-markdown');
 
// Enter url here
mediumToMarkdown.convertFromUrl('https://joelatwar.medium.com/why-does-my-steering-wheel-shake-when-i-brake-hard-in-my-honda-121e3e95a3fe')
.then(function (markdown) {
  console.log(markdown); //=> Markdown content of medium post
});