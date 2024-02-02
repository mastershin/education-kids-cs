/*
Displays large circle at the center.
*/
function setup() {
  createCanvas(800, 600); // Create canvas
}

function draw() {
  background(0); // Set background to black
  x = 400;
  y = 300;
  radius = 200;
  my_color = color(255);
  
  noStroke();
  fill(my_color);
  
  circle(x, y, radius);
}


