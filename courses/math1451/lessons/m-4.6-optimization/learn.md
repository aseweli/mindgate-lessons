An optimization problem asks for the best attainable value of an **objective** under a **constraint**. The calculus is often short. The hard part is choosing variables and turning the description into the correct objective and feasible interval.

### Modeling workflow
1. Sketch and label all variable dimensions, including units.
2. Write what to maximize or minimize. In a fencing problem, the fence length may be fixed and the area is the objective. In a materials problem, volume may be fixed and surface area is the objective.
3. Use the constraint to eliminate a variable. Find the allowable inputs from nonnegative lengths, denominators, and the physical situation.
4. Differentiate the one-variable objective. Compare eligible stationary points and endpoints. For an open or unbounded domain, use derivative signs or end behavior to justify global optimality.
5. Convert the optimizing input back to the requested dimensions or value and give units.

### Common models
- **Fence along a wall:** two widths and one length use fencing, so $2w+\ell=P$ and $A=w(P-2w)$.
- **Open-top box from a sheet:** a cut of size $x$ on each corner makes height $x$ and base $(L-2x)(W-2x)$. The physical interval ends at half the shorter side.
- **Cylinder:** $V=\pi r^2h$. A closed cylinder has $S=2\pi r^2+2\pi rh$, while an open-top cylinder has one circular cap. Eliminate $h$ with the volume.
- **Closest point:** minimize the square of the distance. Square root is strictly increasing on nonnegative inputs, so the same point minimizes both.

The sign of $A'$ tells whether increasing the chosen dimension helps. At an interior stationary point that changes from positive to negative, the objective switches from rising to falling. If that holds across the whole feasible domain, it proves a global maximum.
