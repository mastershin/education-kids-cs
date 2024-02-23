const images = document.querySelectorAll('.image-container img');
let idx = 0;

// test
// images[0].classList.add('current');
// images[1].classList.add('current');
// images[2].classList.add('current');

function changeImage() {
  // This function will change the image every 3 seconds by
  // adding the 'current' class to the next image.
  
  // Remove the current class from the current image
  images[idx].classList.remove('current');
  
  // Increment the index
  idx ++;
  
  // Reset the index to 0 if it exceeds the length of the images array
  idx = idx % images.length;
  
  // Add the current class to the next image so that it is visible
  images[idx].classList.add('current');

  setTimeout(changeImage, 3000); // Change image every 3 seconds
}

setTimeout(changeImage);
