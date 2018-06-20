import Carousel from './Carousel';

const App = (() => {

  const mobile = {};

  const _toggleCopy = (e) => {
    e.currentTarget.classList.toggle('content__toggle--open');

    (e.currentTarget.classList.contains('content__toggle--open'))
      ? e.currentTarget.textContent = 'Lees minder'
      : e.currentTarget.textContent = 'Lees meer';

    mobile.copy.classList.toggle('content__copy--open');
    mobile.carousel.classList.toggle('carousel--visible');
  };

  window.addEventListener('load', () => {
    mobile.copy = document.querySelector('[data-copy]');
    mobile.carousel = document.querySelector('[data-carousel]');
    mobile.copyToggle = document.querySelector('[data-toggle-copy]');
    mobile.copyToggle.addEventListener('click', _toggleCopy);

    Carousel('instagram').init();
  });

})();