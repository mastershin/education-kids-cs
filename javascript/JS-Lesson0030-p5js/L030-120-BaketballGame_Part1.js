// Simple Basketball Game Part 1.
// Move Basketball to the position of mouse click
//
// Platform: editor.p5js.org
// (C) 2024. MastershinAI.com. All rights reserved. MIT License.

let ballX = 100, ballY = 100, ballSize = 50;

let velocityX, velocityY;

function drawCourt() {
  // Draw the court base
  //fill('#C0A050'); // Light brown color for the wooden floor
  fill('#604020'); // Dark brown color for the wooden floor
  
  rect(0, 0, width, height);

  // Draw the vertical divider line
  stroke(255); // White line color
  line(width / 2, 0, width / 2, height);

  // Draw the center circle
  noFill(); // No fill for the circle
  stroke(255); // White color for the circle
  ellipse(width / 2, height / 2, 100, 100); // Draw circle in the center  
}

function setup() {
  createCanvas(600, 400);
}
function drawBall() {
  fill(255, 128, 0);
  ellipse(ballX, ballY, ballSize, ballSize);
}

function drawGoal() {
  // backboard
  fill(255, 255, 0);
  noStroke();
  // Initialize goal
  let goalWidth = 10;
  let goalHeight = 100;
  let goalX = width - 40;
  let goalY = height / 2 - goalHeight/2;

  
  rect(goalX, goalY, goalWidth, goalHeight);
  
  // orange hoop
  noFill();
  strokeWeight(3);
  stroke(255, 100, 0)  
  ellipse(goalX - goalWidth - ballSize/2, goalY + goalHeight/2, ballSize*2, ballSize);
}
function mousePressed() {
  ballX = mouseX;
  ballY = mouseY;
}

function draw() {
  background(220);
  drawCourt();
  drawBall();
  drawGoal();
}
