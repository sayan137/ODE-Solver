<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Interactive Numerical Solution of Differential Equation</h1>
    <p>
        This project visualizes the numerical solution of a first-order differential equation <code>dy/dx = 1 - y²</code> with interactive functionality. It uses <code>matplotlib</code> to plot solution curves and display vector fields.
    </p>

  <h2>Features</h2>
  <ul>
        <li><b>Interactive Click:</b> Allows users to click on the graph to select initial conditions (<code>x</code> and <code>y</code>), dynamically recalculating and plotting the solution curve.</li>
        <li><b>Numerical Integration:</b> Solves the differential equation numerically using the forward and backward Euler method.</li>
        <li><b>Vector Field:</b> Displays a vector field to provide an intuitive understanding of the differential equation.</li>
        <li><b>Annotations:</b> Shows the selected initial conditions on the graph.</li>
    </ul>

  <h2>Installation</h2>
    <ol>
        <li>Clone this repository:
            <pre><code>git clone https://github.com/yourusername/differential-equation-visualization.git
cd differential-equation-visualization
            </code></pre>
        </li>
        <li>Install the required libraries:
            <pre><code>pip install matplotlib numpy</code></pre>
        </li>
    </ol>

  <h2>Usage</h2>
    <ol>
        <li>Run the script:
            <pre><code>python interactive_differential_eq.py</code></pre>
        </li>
        <li>Click anywhere on the plot to set initial conditions and observe the updated solution curve.</li>
    </ol>

   <h2>Explanation of Components</h2>
    <ul>
        <li><b>dy_dx Function:</b> Defines the differential equation as <code>dy/dx = 1 - y²</code>.</li>
        <li><b>on_click Function:</b> Handles mouse click events to dynamically update the solution based on new initial conditions.</li>
        <li><b>Vector Field:</b> A quiver plot provides a visual representation of the slope field for the differential equation.</li>
        <li><b>Numerical Integration:</b> Uses forward Euler for positive integration and backward Euler for negative integration.</li>
        <li><b>Annotations:</b> Marks the selected initial point on the graph with coordinates.</li>
    </ul>

   <h2>Visualization Details</h2>
    <ul>
        <li><b>Vector Field:</b> Displayed using arrows to show the slope at different points in the <code>(x, y)</code> plane.</li>
        <li><b>Solution Curve:</b> A red line dynamically updated based on the selected initial conditions.</li>
        <li><b>Initial Point:</b> A blue marker shows the initial condition with coordinates annotated.</li>
      
  ![delete](https://github.com/user-attachments/assets/988aa311-d1ca-4016-bc50-5a6e42939e40)
    </ul>

   <h2>Acknowledgement</h2>
    <p>
        I got the motivation to take up this project from a slope field plotter in GeoGebra written by Dr. Adrian Jannetta. In some sense, my version is a close ripoff of that slope field plotter, but mine lacks some features like the maximum and minimum of the function.
    </p>
</body>
</html>
