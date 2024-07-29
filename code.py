# Check for collision with the border
if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"

    # Hide the segments
    for segment in segments:
        segment.goto(1000, 1000)

    # Clear the segments list
    segments.clear()

# Check for collision with food
if head.distance(food) < 20:
    # Move the food to a random location
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    food.goto(x, y)

    # Add a segment to the snake
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("green")
    new_segment.penup()
    segments.append(new_segment)

# Move the snake segments in reverse order
for i in range(len(segments) - 1, 0, -1):
    x = segments[i - 1].xcor()
    y = segments[i - 1].ycor()
    segments[i].goto(x, y)

# Move the first segment to where the head is
if len(segments) > 0:
    x = head.xcor()
    y = head.ycor()
    segments[0].goto(x, y)

move()

# Check for collision with the tail
for segment in segments:
    if segment.distance(head) < 20:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

time.sleep(0.1)
