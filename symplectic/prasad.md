<link href="../whirlwind.css" rel="stylesheet">

<whirlheader>
    <p>Gary</p>
    <p>Cristofaro-Gardiner</p>
    <p>August 19</p>
</whirlheader>

# Basics 

Consider $(\mathbb{R}^n, \Omega = \sum_{i=1}^n \,dx_i \wedge \,dy_i)$, a Hamiltonian $H:\mathbb{R}^{2n} \to \mathbb{R}$, and the Hamiltonian vector field $X_H$.

<lemma>

The flow of $X_H$ preserves $H$.

</lemma>

<corollary>

The flow of $X_H$ preserves the level sets of $H$. 

</corollary>

<remark>

Historically, these $H$'s were called energy surfaces.

</remark>

Fix $s\in \text{Reg}(H) \implies H^{-1}(S)$ is a smooth $(2n-1)$-dimensional manifold. We call energy surfaces that arise this way **regular**.

## Invariant Sets 

<problem>
<src>Herman, 1998 ICM</src>

Fix $H:\mathbb{R}^{2n}\to \mathbb{R}$ and fix a compact regular energy surface. Does $Y$ contain a proper closed $X_H$ invariant subset?

</problem>

<theorem>
<src>Fish, Hofer, 2018</src>

Yes for $n=2$.

</theorem>

<remark>

- <src>Weinstein, Rabinowitz, Viledo</src>: When $Y$ is contact type, it contains a closed orbit 
- Examples exist where $Y$ has no closed orbits: <src>Ginzberg, Kerman, Herman</src> for $n\ge 3$, <src>Ginzburg, Gurel</src> for $n\ge 2, H$ is $C^2$

</remark>

<theorem>
<src>Prasad, 2024; Theorem A</src>

Let $H: \mathbb{R}^{n} \to \mathbb{R}$, $Y$ be a compact regular energy surface. There exists an infinite family of distinct, proper, closed invariant subsets with dense union in $Y$.

</theorem>

Notation: $\text{Reg}_C(J)=\{ s\in \text{Reg}(H)| H^{-1}(s)\text{ compact} \}$.

<theorem>
<src>Theorem A'</src>

Let $H': \mathbb{R}^{2n} \to \mathbb{R}$ for almost every $s\in \text{Reg}_c(H)$. $H'(s)$ has the following property: for any closed orbit $\Lambda \subset H^{-1}(s)$, $H^{-1}(s)/\Lambda$ is not minimal.

</theorem>

<remark>

The Le Calvez-Yoccoz property implies dense existence on invariant sets.

</remark>

## Closed Orbits 

<theorem>
<src>Hofer, Zehnder, 1987</src>

Fix $H:\mathbb{R}^{2n} \to \mathbb{R}$. For about every energy surface $s\in \text{Reg}_c(H), H^{-1}(c)$ contains a closed orbit.

</theorem>

<theorem>

Fix $H:\mathbb{R}^{2n} \to \mathbb{R}$. For almost every $s\in \text{Reg}_c H$, $H^{-1}(s)$ contains two closed orbits. This bound is sharp.

</theorem>

<proof>

Consider
$$
H=\dfrac{x_1^2+y_1^2}{a}+\dfrac{x_2^2+y_2^2}{b}
$$
where $\frac{a}{b}\notin \mathbb{Q}$. Each regular energy surface has 2 closed orbits.

</proof>

<theorem>

Fix $H:\mathbb{R}^4\to \mathbb{R}$. Under $C^\infty$-generic conditions on $H$, almost every compact regular energy surface has infinitely many closed orbits.

</theorem>

<proof>

Follows from a strictly stronger version of Theorem A' and known results about generic Hamiltonians.

</proof>

# Closed Holomorphic Curves 

Fix $H: \mathbb{CP}^2 \to \mathbb{R}$. 

<theorem>
<src>Taubes</src>

Fix base $J, J\ge 1, S\subset \mathbb{CP}^2$ such that $\# S \approx \lambda^2$. Then there exists a closed $J$-holomorphic curve $u: C\to \mathbb{CP}^2$ such that 
1. $S=u(C)$
2. $\int_C u\Omega = d$
3. $\chi(C)\sim -d^2$

</theorem>

# Theorem A 

Take 
$$
W_k=\mathbb{CP}^2 \backslash Y \cup [-k,k]\times Y.
$$

Consider the sequence $u_k: C_k \to W_k$. 

<definition>

The **stretched limit set** 
$$
\chi(u_k)\in \text{Cl}((-1,1)\times Y)\times (-1,1).
$$

We say $(\Xi, s)\in \chi(u_k)$ if there exists $\{s_k\}$ such that the following holds: 

1. $u_k(C_k) \cap (s_k^{-1}, s_k +1) \times Y \to \Xi$ after shifting 
2. $k^{-1}s_k \to s$.

</definition>

Define $u_{d,k}$ be the set of degree $d$ curves as above. The main structural result is the following:

<proposition>

1. For almost every $s$ and every $(\Xi, s) \in \chi(s_k)$, 
    $$
    \Xi = (-1,1)\times \Lambda
    $$
    where $\Lambda$ is $X_H$ invariant.
2. For all but $\sim d^2$ heights $s$, every $(\Xi, s) \in \chi(u_{d,k})$ is such that $\Xi$ is $\epsilon$-almost invariant where $\epsilon\to 0$ as $d\to \infty$.

</proposition>

