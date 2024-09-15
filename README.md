# Monte Carlo Simulation to Estimate the Area of a Unit Circle

This Python code uses a Monte Carlo method to estimate the area of a unit circle (a circle with radius 1). The process involves generating random points within a square that bounds a quarter of the circle and determining how many of those points fall inside the circle.

## Key Steps:
1. **Random Point Generation**: 
   - The code generates random points `(x, y)` where:
     - `x` is a random value between -1 and 1.
     - `y` is a random value between 0 and 1.

2. **Circle Boundary Check**: 
   - For each point, the code checks if it falls inside the quarter circle by comparing the `y` value to the circle's boundary at that `x`. The boundary of the quarter circle is given by the equation `y = sqrt(1 - x^2)`.

3. **Counting Points Inside the Circle**: 
   - If the point `(x, y)` is inside the quarter circle, a counter is incremented.

4. **Area Calculation**: 
   - The proportion of points inside the quarter circle is used to estimate the area of the entire circle. This is done by scaling the proportion by the area of the bounding rectangle and then doubling the result to account for the quarter-circle.

5. **Final Output**: 
   - The estimated area of the unit circle is printed, normalized by dividing by the radius squared (which is 1).

### Formulae used:
- The equation of a circle: `x^2 + y^2 = 1`
- The area of the rectangle bounding the quarter circle is `2` (width `2` and height `1`).
- The final area of the circle is estimated as:  
  `circle_area = (points_inside_circle / total_points) * rectangle_area * 2`.

This method provides an approximation of the circle's area based on the ratio of points that fall within the circle to the total points generated.
