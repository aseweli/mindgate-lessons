A secant measures average change across $[a,b]$. The Mean Value Theorem (MVT) guarantees an interior tangent parallel to that secant when $f$ is continuous on $[a,b]$ and differentiable on $(a,b)$. It places no differentiability requirement at the endpoints. There may be multiple eligible points. Rolle’s theorem is the case $f(a)=f(b)$, so the tangent is horizontal somewhere inside.

### Written solution template
1. State why $f$ is continuous on the closed interval and differentiable on the open interval.
2. Compute the secant slope $\big(f(b)-f(a)\big)/(b-a)$.
3. Solve $f'(c)$ equal to that slope and retain all solutions strictly inside $(a,b)$.

### Why the hypotheses matter
For $f(x)=|x|$ on $[-1,1]$, the endpoint values match, but the only possible horizontal-tangent candidate would be at the corner. It has slopes $-1$ and $1$ on either side. A discontinuity anywhere on the closed interval also prevents using the guarantee.

### Use the theorem to bound change
If $m\le f'(x)\le M$ between $a$ and $b$, then $m(b-a)\le f(b)-f(a)\le M(b-a)$. If $f'=0$ everywhere on an interval, apply MVT to any two inputs to show their outputs are equal. If $f'>0$ throughout, any two ordered inputs have positive change, establishing strict increase. Rolle’s theorem can rule out two roots when $f'$ is never zero.
