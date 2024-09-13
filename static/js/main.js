document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});


// JavaScript to fade out the alert box after 2 seconds
setTimeout(function() {
  var alertBox = document.querySelector('.alert');
  alertBox.style.opacity = '0';
  
  setTimeout(function() {
      alertBox.style.display = 'none';
  }, 500); // Wait for the transition to complete
}, 2000); // 2 seconds


document.addEventListener('DOMContentLoaded', function () {
  var carouselElement = document.querySelector('#restaurantCarousel');
  if (carouselElement) {
    var carousel = new bootstrap.Carousel(carouselElement, {
      interval: 3000, // Adjust the interval for auto-sliding (in milliseconds)
      ride: 'carousel' // Automatically start the carousel
    });

    // Add event listener for arrow keys
    document.addEventListener('keydown', function (event) {
      if (event.key === 'ArrowLeft') {
        carousel.prev(); // Slide to the previous item
      } else if (event.key === 'ArrowRight') {
        carousel.next(); // Slide to the next item
      }
    });
  }
});