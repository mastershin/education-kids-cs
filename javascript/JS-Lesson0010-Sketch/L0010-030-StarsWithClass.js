/*
Displays many random stars with Javscript Class.
*/
class Star {
  constructor() {
    // Randomly position stars
    this.x = random(width);
    this.y = random(height);
    this.color = color(255);
    this.radius = 3;
  }

  display() {
    noStroke();
    fill(this.color);
    circle(this.x, this.y, this.radius); // Draw star as circle
  }
}

let stars = []; // Array to hold star objects

function setup() {
  createCanvas(800, 600); // Create canvas
  for (let i = 0; i < 1000; i++) {
    stars.push(new Star()); // Create 200 Star objects
  }
}

function draw() {
  background(0); // Set background to black
  for (let star of stars) {
    star.display(); // Display each star
  }
}

