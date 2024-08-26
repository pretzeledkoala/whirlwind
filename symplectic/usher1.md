<link href="../whirlwind.css" rel="stylesheet">

<whirlheader>
    <p>Gary</p>
    <p>Symplectic Embedding Obstructions and Constructions</p>
    <p>August 19</p>
</whirlheader>

# Introduction

Here are some examples of questions that symplectic geometers care about:
1. Suppose $X(\vec{r})$ and $Y(\vec{s})$ are symplectic manifolds depending on parameters $\vec{r}$ and $\vec{s}$. For what values of $\vec{r}$ and $\vec{s}$ do there exist symplectic embeddings $X(\vec{r})\hookrightarrow Y(\vec{s})$?  For example, do there exist symplectic embeddings $X(\vec{r})\hookrightarrow Y(\vec{s})$ where 
    $$
    X(\vec{r}) = X(a)=B^{2n}(a)=\left\{ (\vec{x}, \vec{y})\in \mathbb{R}^{2n} \mid  \pi \sum(x_j^2+y_j^2) \le a \right\} \\
    Y(\vec{s}) = E^{2n}(s_1,...,s_n) = \left\{ (\vec{x}, \vec{y}) \in \mathbb{R}^{2n} \mid  \pi \sum \dfrac{(x_j^2+y_j^2)}{s_j}\le 1 \right\}
    $$
    with $a>0$?
2. If $X\subset \mathbb{R}^{2n}$ is a domain with contact type boundary, what can be said about the action of closed characteristics on $\partial X$? What is the connection between this question and the previous one? 
3. For $\phi: M\to M$ a Hamiltonian diffeomorphism, what happens to the actions of fixed points of $\phi^k$, denoted $\# \text{Fix}\left(\phi^k\right)$, and the Hofer norm $\mid \mid \phi^k\mid \mid _{\text{Hofer}}$ as $k\to \infty$?

For the rest of this talk, we will mostly focus on the first question, partially because the first result that got mathematicians interested in studying quantitative symplectic geometry arose from this problem.

<theorem>
<src>Gromov's Non-Squeezing Theorem, 1985</src>

Let
$$
B^{2n}(a) = \left\{ (\vec{x}, \vec{y}) \in \mathbb{R}^{2n} \mid  \pi \sum (x_j^2+y_j^2) \le a\right\}
$$
and 
$$
Z^{2n}(A) = \left\{ (\vec{x}, \vec{y}) \in \mathbb{R}^{2n} \mid  \pi(x_j^2+y_j^2) \le A \right\}=B^2(A) \times \mathbb{R}^{2n-2}.
$$
Then there exists a symplectic embedding $B^{2n}(a) \hookrightarrow Z^{2n}(A)$ only if $a\le A$.

</theorem>

Basically, this result tells us that we cannot squeeze a ball into a cylinder of smaller radius while preserving the symplectic structure.

# Proof of Gromov's Non-Squeezing Theorem

We present a proof sketch.

Suppose there exists a symplectic embedding $\phi: B^{2n}(a) \hookrightarrow Z^{2n}(A)$. Let $\epsilon >0$. We want to show that $a\le A$, so it suffices to show that $a-\epsilon < A+\epsilon$. 

Choose $L$ such that $\text{Im}(\phi) \subset B^2(A)\times (-L,L)^{2n-2}$. Regard $B^2(A)$ as a subset of $S^2(A+\epsilon)$, the 2-sphere with area $A+\epsilon$. Then $\phi$ can be regarded as having image in $(M, \omega)=(S^2(A+\epsilon)\times \mathbb{R}^{2n}/2L\mathbb{Z}^{2n-2})$ with symplectic form $\omega_{\text{std}}\oplus \omega_{\text{std}}$.

There are 2 key facts:

1. For any $\omega$-compatible almost complex structure $J$ on $M$, there exists a $J$-holomorphic map $u:S^2 \to M$ such that $\phi\left(\vec{0}\right)\subset \text{Im}(u)$ and $u_*[S^2]=[S^2\times \{\text{pts}\}] \in H_c(M)$. In particular, this applies to $J$'s agreeing on $\phi(B^{2n}(a-\frac{\epsilon}{2}))$ with $\phi_*J_0$, where $J_0$ is the standard complex structure on $B^{2n}(u-\frac{\epsilon}{2})$.
2. For a $J_0$-holomorphic map $v: \sum \to B^{2n}(c)$ where $\sum$ is a compact surface with boundary and $c \in (a - \epsilon, a - \frac{\epsilon}{2})$ such that $v(\partial \sum) \subset \partial B^{2n}(c)$ and $\vec{0} \subset \text{Im}(v)$, then $\text{Area}(v) \ge c$.

Together, these two facts prove the desired claim: assuming we have both key facts, for generic $c \in (a-\frac{\epsilon}{2}, a-\epsilon)$, take $\sum u^{-1}(\phi(B^{2n}(c)))$ and take $v:\sum \to B^{2n}(c)$ with $v= \phi^{-1} \cdot u\mid _\Sigma$. Then

$$
\begin{align*}
c&\le a-\dfrac{\epsilon}{2} \\
&\le \text{Area}(v) = \int_\Sigma v^*\omega_0= \int_\Sigma u^*\omega=\text{Area}(u\mid _\Sigma) \\
& \le \text{Area}(u) = A+\epsilon \\
\end{align*}
$$

The idea of the proof of $(1)$ is as follows:

<proof>

For any $\omega$-compatible $J$, consider 
$$
M_J = \left\{ u:S^2 \to M \mid  u_*[S^2]=S^2 \times \{ \text{pt}\}, U(0,0,1) = \phi\left(u\left(\vec{0}\right)\right)\right\}.
$$.

If $J$ is the standard complex structure $J_0$, $M_{J_0}$ has one element. For contradiction, suppose $M_{J_1} = \phi$. For a generic path $\{J_t\}_{0\le t \le 1}$, 
$$
\bigcup_{t\in [0,1]} \{t\}\times M_{J_t}
$$
would be a compact 1-manifold with boundary equal to $M_{J_0}$. But compact 1-manifolds have an even number of boundary points, contradiction.

</proof>

We will not prove $(2)$.

# 4-Dimensional Packing Problem 

<problem>
<src>4-Dimensional Packing Problem</src>

Given $k\in \mathbb{N}, a>0$, does there exist a symplectic embedding $\amalg_k B^4(a) \hookrightarrow B^4(1)$?

</problem>

But we have the following relation:

<proposition>
<src>McDuff-Polterovich</src>

$$
B^4(1) = \mathbb{CP}^1
$$

</proposition>

So we can also study symplectic embeddings $\amalg_k B^4(a) \hookrightarrow \mathbb{CP}^1$ instead.

We have $\text{Vol}(\amalg_k B^4(a))=k \frac{a^2}{2}$ and $\text{Vol}(B^4(1)) = \frac{1}{2}$ so the fraction of volume filled is $ka^2$ - can this $a$ be close to $1$?

<theorem>
<src>2-Ball Theorem</src>

If $k=2$, this embedding exists only if $a\le \frac{1}{2}$.

</theorem>

We present two proofs: 

<proof>

1. If $\varphi_1, \varphi_2: B^{4}(a)\hookrightarrow \mathbb{CP}^{2}(1)$ are symplectic embeddings with disjoint images, find a holomorphic curve for a $J$ agreeing with $\phi_{1*}J_0, \phi_{2*} J_0$ on images, passing through $\phi_j(\vec{0})$ and representing $\mathbb{CP}^1$ in $H_2$. Then
$$
1=\text{Area}(u) \ge a+a \implies a \le \frac{1}{2}.
$$

2. Blowup the images from the balls, giving a symplectic form on $\mathbb{CP}^2 \# 2 \overline{\mathbb{CP}^2}$ such that $[\mathbb{CP}^1]$ has area $1$ and $\# 2 \overline{\mathbb{CP}^2}$ are exceptional divisors on $E_1,E_2$, and $E_1, E_2$ have area $a$. But $[\mathbb{CP}^1]-E_1-E_2$ is represented by holomorphic spheres which have area $\ge 0$, which implies $1-2a\ge 0\implies a\le \frac{1}{2}$.

</proof>