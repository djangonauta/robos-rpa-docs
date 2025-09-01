(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', function () {
    configurarAncoras();
    configurarImagens();
    Fancybox.bind('.data-fb', {});
  });

  function configurarAncoras() {
    const ancoras = document.querySelectorAll('[href^=http]');

    ancoras.forEach(function (ancora) {
      ancora.setAttribute('target', '_blank');
      ancora.setAttribute('rel', 'noopener noreferrer');
    });
  }

  function configurarImagens() {
    document.querySelectorAll('img.data-fb').forEach(function (img) {
      img.title = "Clique para ampliar a imagem";
    })
  }
})();
