A limit describes nearby values. Approach $a$ along inputs on each side; a two-sided finite limit exists when both sides approach the same number. The plotted solid dot tells you $f(a)$ and may differ from the limit. An infinite limit describes unbounded growth with a particular sign. A table can suggest a limit; algebra or a theorem justifies it.

### Pick the first legal method
1. Try substitution for a continuous expression at a valid input. The quotient law requires a nonzero denominator limit.
2. If substitution gives $0/0$, look for a common factor, a conjugate, a common denominator, or a trig identity. Cancellation holds for nearby $x\ne a$ even when the original formula is undefined at $a$.
3. If the denominator approaches zero and the numerator is nonzero, determine the sign on each side. An even power keeps the same sign; an odd power switches.
4. When a bounded factor oscillates, bound the entire expression above and below. For example, $-x^2\le x^2\sin(1/x)\le x^2$, so the middle tends to zero.
5. For a trig limit, use radians and arrange an exact $\sin u/u$ pair. The limit of $(1-\cos x)/x$ is zero by multiplying by $1+\cos x$.

The precise meaning of $\lim_{x\to a}f(x)=L$ is that every output tolerance $\varepsilon>0$ can be met by a small enough input radius $\delta>0$ with $0<|x-a|<\delta$. For $3x+1$ at $a=2$, choosing $\delta=\varepsilon/3$ works.
