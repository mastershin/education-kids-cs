/*
@title: Multiple Orbitting planets
@lesson_code: L020-180-SolarSystem_MultiplePlanets.js
@author: jae at Mastershin AI
@link: https://editor.p5js.org/mastershin/sketches/IRJrFor0k
@source: https://github.com/mastershin/learn-coding-101/
(C)2024 MastershinAI.com. MIT License. All Rights Reserved.
*/
class Planet {
  constructor(diameter, distance, angle_step, r, g, b) {
    this.angle = 0;
    this.x = 0;
    this.y = 0;
    this.width = diameter;
    this.height = diameter;
    this.distance = distance;
    // angle of rotation
    this.angle = 0;
    this.angle_step = angle_step;
    // color
    this.r = r;
    this.g = g;
    this.b = b;
  }
  draw() {
    let x = width / 2 + cos(this.angle) * this.distance; // distance pixels away from the Sun
    let y = height / 2 + sin(this.angle) * this.distance;
    fill(this.r, this.g, this.b); // color
    ellipse(x, y, this.width, this.height);    

    this.angle += this.angle_step;
  }
}
planets = [];
function setup() {
  
  createCanvas(400, 400);
  frameRate(20);
  
  // Sun
  diameter = 40;  
  sun = new Planet(diameter, 0, 0, 255, 255, 0);
  planets.push(sun);

  // Multiple Planets
  for (i = 0; i < 10; i++ ) {
    diameter = 5 + Math.random() * 10;
    angle_step = 0.05 + Math.random() * 0.1;
    distance = 50 + Math.random() * 100;
    r = Math.random() * 255;
    g = Math.random() * 255;
    b = Math.random() * 255;
    planet = new Planet(diameter, distance, angle_step, r, g, b);
    planets.push(planet);
  }
  
}

function draw() {
  
  background(0); // Set background to black

  for (const p of planets) {
    p.draw();
  }
}