document.addEventListener('DOMContentLoaded', function() {
  var typedStrings = [
    'Je suis en reconversion professionnelle',
    'Je suis en alternance',
    'Je suis en 2ème année de BTS SIO option SISR'
  ];

  setTimeout(function() {
    var typed = new Typed('#typing-effect', {
      strings: typedStrings,
      typeSpeed: 50,
      backSpeed: 50,
      loop: true,
      showCursor: true,
      cursorChar: '|',
      autoInsertCss: true
    });
  }, 4000); // Délai de 4000 millisecondes (4 secondes)
});
