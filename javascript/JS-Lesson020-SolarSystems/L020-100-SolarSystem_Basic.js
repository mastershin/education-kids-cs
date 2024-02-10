/*
@title: Various Stars with random brightness and radius
@lesson_code: L020-100-SolarSystem_Basic.js
@author: jae at Mastershin AI
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
  
  let x = width / 2;
  let y = 50;
  
  // draw earth
  draw_planet(x, y, 0, 128, 255);
  
}