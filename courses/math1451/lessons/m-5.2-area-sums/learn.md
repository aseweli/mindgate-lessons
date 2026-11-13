Break $[a,b]$ into $n$ equal subintervals of width $\Delta x=(b-a)/n$. Each rectangle contributes height times width. The right endpoint of subinterval $i$ is $a+i\Delta x$, the left is $a+(i-1)\Delta x$, and the midpoint is $a+(i-\tfrac12)\Delta x$ for $i=1,\dots,n$.

### Finite estimates and exact limits
For an increasing function and a regular partition, the left sum is at most the true signed integral and the right sum is at least it. The order reverses for decreasing functions. A midpoint sum uses interior samples and may be above or below. For a nonnegative function, each rectangle contributes ordinary area. When negative values enter, the same sum approximates signed accumulation, covered in §5.3.

To compute an exact integral from the definition, keep $n$ symbolic. Substitute the sample point into $f$, multiply by $\Delta x$, sum using power-sum identities, simplify, and take the limit. Terms proportional to $1/n$ or $1/n^2$ disappear. For example, with $f(x)=x$ on $[0,2]$, the right sum is $(4/n^2)\sum_{i=1}^n i=2(n+1)/n\to2$.

### Reading sigma notation
The lower index is the first term and the upper index is the last. $\sum_{i=1}^n C=nC$. If a term is $A i^2+B i+C$, distribute the sum and apply each identity separately. When a problem supplies a nonuniform partition, use each rectangle’s own width $\Delta x_i=x_i-x_{i-1}$.
