/*
@title: Various Stars with random brightness and radius
@lesson_code: L0010-050-ShiningStars.js
@author: jae at Mastershin AI
(C)2024 MastershinAI.com. MIT License. All Rights Reserved.
*/

class Star {
  constructor() {
    // Randomly position stars
    this.x = random(width);
    this.y = random(height);
    
  }

  display() {
    
    this.brightness = random(0, 255);
    this.color = color(255, this.brightness); // White with varying brightness    
    this.radius = random(1, 2);
    
    noStroke();
    fill(this.color);
    
    circle(this.x, this.y, this.radius * 2); // Draw star as circle
  }
}

let stars = []; // Array to hold star objects

function setup() {
  createCanvas(800, 600); // Create canvas
  for (let i = 0; i < 1000; i++) {
    stars.push(new Star()); // Create 200 Star objects
  }
  frameRate(5);
}

function draw() {
  background(0); // Set background to black
  for (let star of stars) {
    star.display(); // Display each star
  }
}
