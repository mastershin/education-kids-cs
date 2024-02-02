/*
Displays multiple small circles (stars) randomly.
*/
function setup() {
  createCanvas(800, 600); // Create canvas

  background(0);
  for (let i = 0; i < 1000; i++) {

    x = random(width);
    y = random(height);
    radius = 2

    star_color = color(255); // White with varying brightness
    
    noStroke();
    
    fill(star_color);
    
    circle(x, y, radius);
  
  }
}

