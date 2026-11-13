An **absolute maximum** is a function value at least as large as every other value on the interval. A **local maximum** only compares nearby points. The same distinctions apply to minima. In an answer, distinguish the input where the extreme occurs from the extreme value itself.

### Why the candidate list works
The Extreme Value Theorem guarantees a maximum and a minimum when $f$ is continuous on a closed, bounded interval $[a,b]$. If an extremum occurs in the interior where $f$ is differentiable, Fermat’s theorem gives $f'(c)=0$. An extremum can also occur at a corner or cusp where $f'$ is undefined and $f$ exists. Endpoints are candidates regardless of slope.

### Closed-interval method
1. Write the domain and check continuity on $[a,b]$.
2. Find interior inputs where $f'=0$ or $f'$ fails to exist and $f$ exists.
3. Make a table with $a$, all eligible interior inputs, and $b$. Evaluate **$f$** at each input.
4. Compare values and report ties. For a local classification, use the first-derivative sign change from §4.3.

A horizontal tangent alone proves little: $x^3$ has $f'(0)=0$ and increases through zero. A missing endpoint also changes the question: $f(x)=x$ on $(0,1)$ has neither absolute extreme, even though the outputs are bounded by 0 and 1.
