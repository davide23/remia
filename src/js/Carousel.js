const Carousel = (id) => {

  const carousel = {};

  const _transformCarousel = () => {
    carousel.content.style.webkitTransform = `translate3d(-${carousel.activeSetIndex * 100}%, 0, 0)`;
    carousel.content.style.transform = `translate3d(-${carousel.activeSetIndex * 100}%, 0, 0)`;
  };

  const _checkCarousel = () => {
    carousel.isTransitioning = false;
    carousel.content.classList.remove(carousel.transitionClass);

    setTimeout(() => {
      if (carousel.activeSetIndex === 0) {
        carousel.activeSetIndex = carousel.sets;
        _transformCarousel();
      } else if (carousel.activeSetIndex === carousel.sets + 1) {
        carousel.activeSetIndex = 1;
        _transformCarousel();
      }
    }, 0);
  };

  const _setActiveSet = () => {
    if (carousel.isTransitioning) {
      return;
    };

    carousel.content.classList.add(carousel.transitionClass);
    carousel.isTransitioning = true;

    if (carousel.direction === 'prev') {

      (carousel.activeSetIndex > 0)
        ? carousel.activeSetIndex -= 1
        : carousel.activeSetIndex = carousel.sets;
    } else if (carousel.direction === 'next') {

      (carousel.activeSetIndex < carousel.sets + 1)
        ? carousel.activeSetIndex += 1
        : carousel.activeSetIndex = 1;
    }

    carousel.indicators.forEach(item => item.classList.remove('carousel__indicator--is-active'));

    const activeIndicator = [].slice.call(carousel.indicators).filter(item => {
      if (carousel.activeSetIndex === 0) {
        return (parseInt(item.dataset.carouselIndicator) + 1) === carousel.sets;
      } else if (carousel.activeSetIndex === carousel.sets + 1) {
        return (parseInt(item.dataset.carouselIndicator) + 1) === 1;
      } else {
        return (parseInt(item.dataset.carouselIndicator) + 1) === carousel.activeSetIndex;
      }
    });

    activeIndicator[0].classList.add('carousel__indicator--is-active');

    _transformCarousel();
  };

  const _onTouchEnd = (e) => {
    if (carousel.offsetX === 0) {
      return;
    }

    _setActiveSet();
  };

  const _onTouchMove = (e) => {
    carousel.offsetX = e.touches[0].clientX - carousel.startX;
    carousel.offsetY = e.touches[0].clientY - carousel.startY;

    // Prevent vertical scroll if the user is swiping left or right
    if (Math.abs(carousel.offsetX) > Math.abs(carousel.offsetY) && e.cancelable) {
      e.preventDefault();
    }
    
    if (carousel.offsetX > 0) {
      carousel.direction = 'prev';
    } else if (carousel.offsetX < 0) {
      carousel.direction = 'next';
    }
  };

  const _onTouchStart = (e) => {
    if (carousel.isTransitioning) {
      return;
    };

    carousel.startX = e.touches[0].clientX;
    carousel.startY = e.touches[0].clientY;
    carousel.offsetX = 0;
    carousel.offsetY = 0;
  };

  const _cloneCarouselItems = () => {
    const firstItems = [];
    const lastItems = [];

    for (let i = 0; i < 3; i++) {
      const duplicate = carousel.items[i].cloneNode(true);
      firstItems.push(duplicate);
    }

    for (let i = carousel.items.length - 3; i < carousel.items.length; i++) {
      const duplicate = carousel.items[i].cloneNode(true);
      lastItems.push(duplicate);
    }

    firstItems.forEach(item => carousel.content.appendChild(item));
    lastItems.forEach(item => carousel.content.insertBefore(item, carousel.items[0].previousSibling));
  };

  const _createCarouselIndicators = () => {
    carousel.indicatorContainer = document.createElement('div');
    carousel.indicatorContainer.classList.add('carousel__indicators');

    for (let i = 0; i < carousel.sets; i++) {
      const indicator = document.createElement('DIV');
      indicator.classList.add('carousel__indicator');
      indicator.dataset.carouselIndicator = i;
      carousel.indicatorContainer.appendChild(indicator);
    }

    carousel.root.appendChild(carousel.indicatorContainer);
    carousel.indicators = [].slice.call(carousel.root.querySelectorAll('[data-carousel-indicator]'));
    carousel.indicators[0].classList.add('carousel__indicator--is-active');
  };

  const _setCarouselItems = () => {
    const itemsToAdd = 3 - (carousel.defaultItems.length % 3);

    if (itemsToAdd !== 3) {
      for (let i = 0; i < itemsToAdd; i++) {
        const fillerItem = document.createElement('DIV');
        fillerItem.classList.add('carousel__item');
        fillerItem.setAttribute('data-carousel-item', '');
        carousel.content.appendChild(fillerItem);
      }
    }

    carousel.items = [].slice.call(carousel.root.querySelectorAll('[data-carousel-item]'));
  }

  const construct = () => {
    carousel.activeSetIndex = 1;
    carousel.isTransitioning = false;
    carousel.transitionClass = 'carousel__content--is-transitioning';

    carousel.root = document.querySelector(`[data-carousel="${id}"]`);
    carousel.container = carousel.root.querySelector(`[data-carousel-container]`);
    carousel.content = carousel.root.querySelector(`[data-carousel-content]`);
    carousel.prevButton = carousel.root.querySelector('[data-carousel-button="prev"]');
    carousel.nextButton = carousel.root.querySelector('[data-carousel-button="next"]');
    carousel.defaultItems = [].slice.call(carousel.root.querySelectorAll('[data-carousel-item]'));

    _setCarouselItems();

    carousel.sets = Math.ceil(carousel.items.length / 3);

    _createCarouselIndicators();
    _cloneCarouselItems();

    carousel.container.addEventListener('touchstart', _onTouchStart);
    carousel.container.addEventListener('touchmove', _onTouchMove);
    carousel.container.addEventListener('touchend', _onTouchEnd);

    carousel.prevButton.addEventListener('click', () => {
      carousel.direction = 'prev';
      _setActiveSet();
    });

    carousel.nextButton.addEventListener('click', () => {
      carousel.direction = 'next';
      _setActiveSet();
    });

    carousel.content.addEventListener('transitionend', _checkCarousel);
  };

  return {
    init: construct
  };
};

export default Carousel;
