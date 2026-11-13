Substitution reverses the chain rule. If part of the integrand is a composition $f(g(x))$, look for a factor proportional to $g'(x)\,dx$. Set $u=g(x)$ and write $du=g'(x)\,dx$. Rewrite the entire integrand and differential in $u$ before integrating.

### How the constant appears
In $\int x(1+x^2)^4\,dx$, choose $u=1+x^2$. Then $du=2x\,dx$, so the **combined factor** $x\,dx$ is $\tfrac12\,du$. The integral becomes $\tfrac12\int u^4\,du$, giving $(1+x^2)^5/10+C$. The variable $x$ itself does not become $1/2$; the one-half adjusts the differential factor.

### Decide what to substitute
- For $\int g'(x)[g(x)]^n dx$, choose the expression being raised to a power.
- For $\int g'(x)/g(x)\,dx$, choose the denominator and get $\ln|g(x)|+C$ on an interval avoiding its zeros.
- For $\int e^{g(x)}g'(x)\,dx$ or $\int\cos(g(x))g'(x)\,dx$, choose the exponent or trig argument.
- Sometimes you can replace a leftover factor algebraically. With $u=x+1$, $x=u-1$. If an unmatched variable remains, reconsider the choice or simplify.

### Bounds for definite integrals
Either convert both limits to $u(a),u(b)$ and finish entirely in $u$, or integrate in $u$, back-substitute, and evaluate the original $x$-bounds. If the new bounds are decreasing, retain their order and the sign. Use a final derivative check for indefinite integrals.
