let rectangles = [];
let rect_width = 100;
let rect_height = 500;

function setup() {
  createCanvas(300, 500);
  rectangles.push({x: 0, color: '#ff0000'});
  rectangles.push({x: rect_width, color: '#00ff00'});
  rectangles.push({x: rect_width*2, color: '#ff00ff'});
  rectangles.push({x: rect_width*3, color: '#0000ff'});
  rectangles.push({x: rect_width*4, color: '#ff8800'});
}
function draw_rect(r) {
  fill(r.color);
  rect(r.x, 0, rect_width, rect_height);
}
function update_rect(r) {
  r.x -= 3;
  if (r.x < -rect_width) {
    r.x = 500;
    moving = false;
  }
}
let moving = true;
let counter = 0;
function draw() {
  background(220);
  if (moving == true)
    rectangles.forEach(r => update_rect(r));
  else {
    counter ++;
    if (counter == 20) {
      moving = true;
      counter = 0;
    }
  }
  rectangles.forEach(r => draw_rect(r));
}