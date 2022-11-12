# Service that draws a stick diagram from the tracker.

def DrawStickOperation:
    def operation(golf_swing):
        result = []
        for (frame, frame_context) in golf_swing:
            stick_frame = draw(width=frame.width(), frame.height(),
                               frame_context.tracker)
            result.append(stick_frame)
        return result

    def draw(width, height, tracker):
        """Return a 2d array frame. """
        return
        