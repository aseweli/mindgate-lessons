The Fundamental Theorems connect slopes with accumulation. For continuous $f$ on $[a,b]$ and an antiderivative $F$, the definite integral equals $F(b)-F(a)$. The same result can be viewed as net change: an integral of a rate gives final amount minus initial amount.

### Evaluate with the antiderivative
Find $F$, then compute the **upper value minus the lower value**. Write brackets and keep parentheses around the lower expression. Adding a constant to $F$ would cancel, so a definite integral answer is a number with no $+C$. If a discontinuity lies in the interval, check that the ordinary definite-integral setup applies before using endpoint evaluation. In particular, substituting endpoints into $\ln|x|$ does not evaluate an integral of $1/x$ across zero.

### Differentiate with variable endpoints
For $A(x)=\int_a^x f(t)\,dt$, the derivative is $f(x)$ at points where $f$ is continuous. A small increment in $x$ adds a narrow strip whose height approaches $f(x)$. For upper bound $g(x)$, apply the chain rule to get $f(g(x))g'(x)$. A moving lower bound contributes with a minus sign. If both move, keep both terms. The integrand’s $t$ is a dummy variable, while $x$ controls the bounds.

### Read an accumulation graph
For $A(x)=\int_a^x f(t)\,dt$, $A(a)=0$, the sign of $f$ gives the sign of $A'$, and the slope of $f$ gives $A''$ where it exists. A negative value of $A$ reflects net accumulated area since $a$; whether $A$ is currently decreasing depends on $f(x)$.
