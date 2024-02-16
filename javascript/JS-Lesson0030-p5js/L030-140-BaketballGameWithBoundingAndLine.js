// Simple Basketball Game - Part 2
// Add SHOOT button, with power/angle variable.
//
// Platform: editor.p5js.org
// (C) 2024. MastershinAI.com. All rights reserved. MIT License.

let ballX = 100, ballY = 100, ballSize = 30;
let goalX, goalY, goalWidth, goalHeight;

let velocityX, velocityY;
let gravity = 2.0;

function drawCourt() {
  // Draw the court base
  //fill('#C0A050'); // Light brown color for the wooden floor
  fill('#604020'); // Dark brown color for the wooden floor
  
  rect(0, 0, width, height);

  // Draw the vertical divider line
  stroke(255); // White line color
  strokeWeight(2); // Line thickness
  line(width / 2, 0, width / 2, height);

  // Draw the center circle
  noFill(); // No fill for the circle
  stroke(255); // White color for the circle
  strokeWeight(2); // Circle line thickness
  ellipse(width / 2, height / 2, 100, 100); // Draw circle in the center  
}

function setup() {
  createCanvas(800, 400);
  // frameRate(30);

  // Initialize goal
  goalX = width - 40;
  goalY = height / 2 - 50;
  goalWidth = 10;
  goalHeight = 100;

}

function draw() {
  background(220);
  drawCourt();
  drawBall();
  drawGoal();

  if (velocityX || velocityY)
    updateBallPosition();
  else {
    stroke(0);
    line(mouseX, mouseY, ballX, ballY);
  }
}

function drawBall() {
  fill(255, 128, 0);
  ellipse(ballX, ballY, ballSize, ballSize);
}

function drawGoal() {
  fill(0, 0, 255);
  noStroke();
  rect(goalX, goalY, goalWidth, goalHeight);
    
  noFill();
  strokeWeight(3);
  stroke(255, 100, 0)  
  ellipse(goalX - goalWidth - 15, goalY + goalHeight/2, 50, 25);
}

function updateBallPosition() {
  ballX += velocityX * 0.1;
  ballY += velocityY * 0.1;
  
  velocityX *= 0.99;
  velocityY *= 0.99;
  
  if (abs(velocityX) < 1 && abs(velocityY) < 1) {
    velocityX = 0;
    velocityY = 0;
  }
  else
    velocityY += gravity;

  // Reset if the ball goes off the canvas
    
  if (ballX < ballSize/2 || ballX > width - ballSize/2)
    velocityX = -velocityX;
  if (ballY < ballSize/2 || ballY > height - ballSize/2)
    velocityY = -velocityY;
}

function mousePressed() {
  velocityX = mouseX - ballX;
  velocityY = mouseY - ballY;
}