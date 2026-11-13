L’Hôpital’s rule can replace the limit of a quotient by the limit of the quotient of derivatives when the original form is $0/0$ or $\infty/\infty$, with the needed differentiability near the approach point and $g'(x)\ne0$ there. If the derivative quotient has a finite or signed infinite limit, the original quotient has that limit. If the new limit fails, try another method. The derivatives are taken separately, so this is different from differentiating the whole quotient.

### Match the form to a rewrite
| Form | First move |
| --- | --- |
| $0/0$, $\infty/\infty$ | Differentiate numerator and denominator separately, then recheck the new form. |
| $0\cdot\infty$ | Move one factor downstairs as a reciprocal. |
| $\infty-\infty$ | Combine fractions, rationalize, or factor the dominant term. |
| $1^\infty$, $0^0$, $\infty^0$ | For a positive base, set $y=f^g$, take $\ln y=g\ln f$, find its limit, then exponentiate. |

### Decide when to stop
$\lim_{x\to0}(e^x-1)/x$ gives $0/0$. The derivative quotient is $e^x/1$, which directly gives 1. Stop there. For $\lim_{x\to0^+}1/x$, the numerator tends to 1, so analyze the sign of the denominator instead. For a rational function at infinity, leading powers are usually faster. For repeated applications write the form before each arrow.
