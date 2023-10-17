# SF1692 Numerical Project 

## 2. Language: Python

All numerical code should be written in Python.

## 3. 2 "Random Number" $N$

Let $N$ be the last two digits of your personal number.

## 4. 3 Existence but not uniqueness

Consider the BVP

$$ y' = \sqrt{|y|}, \quad y(0)=0 $$

- Start by solving it analytically.
- Solve the problem numerically. Any comments?
- For how long can you numerically get a solution to "stick" to $y=0$ given that $y(-1)=-1$? (I.e., let $y(-1)=-1+\epsilon$ with $\epsilon$ "very small", and we say that $y$ "sticks" as long as $|y| \le 10^{-4}$.)

## 5. BANG!

Consider the BVP

$$ y' = y^2, \quad y(0)=N/100 $$

- Solve the problem analytically. When does it burst?
- Try solving the problem numerically. Can you "numerically show" that it bursts? Can you estimate the time to singularity?
- Convince yourself (prove!?) that if $y(0) < 0$, then $y(t) < 0$ for all $t > 0$. (Hint: Picard.)
- Can you find numerical examples where $y(0) = \epsilon < 0$, but $y(t) > 0$ for some $t > 0$? (You might need to slightly modify the equation and take $y' = Cy^2$ for a large $C > 0$.) Philosophical question: if you were to create an "automatic solver", how should it avoid/detect deeply incorrect solutions of this kind?

## 6. Not BANG

Consider the BVP

$$ y' = y, \quad y(0) = N $$

Solve the problem numerically and find $y(2^k)$ to two correct decimals, for $k=1,2,3, ...$.

## 7. 6 What is $\pi$?

Start by reading the beginning of Chapter 4.24. Consider the BVP

$$ y'' + y = 0, \quad y(0) = 1, \quad y'(0) = 0 $$

- Solve analytically.
- Define $\pi/2$ as the first value on $t > 0$ such that $y(t) = 0$. Estimate $\pi$ by solving the BVP numerically (and estimate the first zero). Warm-up: how many correct digits can you get before your computer melts? (Try using Euler and better methods.) After the warm-up: find 20 correct decimals. Hint: you can ask for a hint.
- If we choose to estimate $\pi$ by finding the root closest to $10^3$, how much harder does the problem become?

## 8. Newton!

Read Chapter 3.21. Place the sun at the origin (assume the sun doesn't move). Take a planet $P$ moving in the $x, y$-plane, and let $(x(t), y(t))$ be the planet's position at time $t$.

- Derive a second-order system of differential equations describing the planet's motion. (Do not switch to polar coordinates.) You can choose masses so the equations are as simple as possible.
- Simulate the system for a short time by solving numerically with different initial values. (Plot the results!)
- Simulate the system for a long time by solving numerically with different initial values. Can you notice anything strange? (You can ask for a hint.)

Hint: in our universe and in this course, energy is conserved.

- Can you find ways to restore order in our simulation? You can ask for a hint.

Hint: search for semi-implicit Euler (or symplectic Euler).

## 9. Newton revisited (something for nothing)

Consider a solar system with the sun, Jupiter (i.e., heavy planet), and Earth (point-like). Given a spaceship near Earth with a "delta-v" so small that the ship can't leave the solar system (hint: "escape velocity"), design a trajectory near Jupiter that works as a "gravitational slingshot" so the ship can leave the solar system.

- Explore numerically and find masses, planetary orbits, etc., so that the above works. Hints: use astronomical units (the Earth is about 1 AU from the sun). If you have trouble hitting Jupiter: use software to search for initial conditions. You can ask for hints.
  
- How do you know for sure that the ship really leaves the solar system?