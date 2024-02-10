/*
@title: Various Stars with random brightness and radius
@lesson_code: L020-110-SolarSystem_EarthOrbit.js
@author: jae at Mastershin AI
@environment: p5.js
@link: https://editor.p5js.org/mastershin/sketches/K6HlTwpu6
(C)2024 MastershinAI.com. MIT License. All Rights Reserved.
*/
let angle = 0;

function setup() {
  createCanvas(400, 400);
  frameRate(20);
}

function draw_sun() {
  // Draw the Sun at the center
  fill(255, 255, 0); // Sun color (yellow)
  ellipse(width / 2, height / 2, 40, 40); // Draw Sun with diameter of 40 pixels
}

function draw_planet(x, y, r, g, b) {
  fill(r, g, b); // color
  ellipse(x, y, 20, 20); // Draw with diameter of 20 pixels
  
}

function draw() {
  background(0); // Set background to black

  draw_sun();
  
  // Calculate Earth's orbiting position
  let distance = 100;
  let x = width / 2 + cos(angle) * distance; // distance pixels away from the Sun
  let y = height / 2 + sin(angle) * distance;
  
  // draw earth
  draw_planet(x, y, 0, 128, 255);
  
  angle += 0.05; // Increment angle to rotate the Earth
}