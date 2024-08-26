<link href="../whirlwind.css" rel="stylesheet">

<whirlheader>
    <p>Gary</p>
    <p>Cristofaro-Gardiner</p>
    <p>August 19</p>
</whirlheader>

# Introduction 

## A New Compactness Theorem 

Consider a closed oriented $2n+1$ manifold $Y$. We are interested in framed Hamiltonian structures:

<definition>

A **framed Hamiltonian structure** is a pair $(\lambda,\omega)$ where $\lambda$ is a 1-form, $\omega$ is a closed 2-form, and $\lambda \wedge \omega^n > 0$.

</definition>

<example>

- Let $\lambda$ be a contact form, $\omega =\,d\lambda$. The mapping torus is a symplectic automorphism $\phi: (M^{2n}, \omega) \to (M^{2n}, \omega)$. We have 
    $$
    Y=M^{2n}\times [0,1]/\sim
    $$
    where $(x,1) \sim (\phi(x), 0)$. The pair $(dt, \omega)$ is a framed Hamiltonian structure. 

- Suppose we have a proper Hamiltonian $H:(M^{2n}, \omega) \to R$. Suppose we have a regular value $c$. Then $H^{-1}(c)$ is a framed Hamiltonian structure.

- Non-singular volume preserving flows on a closed 3-manifold are framed Hamiltonian structures.

</example>

Let $(\lambda, \omega)$ is a Hamiltonian vector field. Suppose we have $R$ satisfying $\omega(R, \cdot)=0, \lambda(R)=1$.

<example>

In the contact case, $R$ is the Reeb vector field.

</example>

We want non-trivial (nonempty and proper) closed invariant sets of $R$.

<example>

- A periodic orbit
- The invariant tori 
- Orbit closure for $f$ proper

</example>

Consider the symplectization $X=\mathbb{R}\times Y$ with an almost complex structure: $J: TX\to TX, J^2=-1, J(\partial_S)=R$ that preserves $\text{ker}(\lambda)$ compatibly with $\omega$. We are interested in sequences of holomorphic curves 
$$
u_k: C_k \to \mathbb{R}\times Y
$$
where $u_k$ is proper and $J$-holomorphic, $C_k$ is a closed Riemann surface minus a finite number of punctures. For $u_k$, define the limit set 
$$
L(u_k) = \{ \overline{K}\subset (-1, 1)\times Y | \text{condition}\}
$$
where the condition is that $\overline{k}$ is closed and there exists a subsequence $u_k(C_k) \cap (s_k-1, s_k+1)\times Y$ converging (after shifting) to $k$. We should think of this as subsequential limits of height 2 slices.

<proposition>

$L(u_*)$ is a connected.

</proposition>

We have the following classical quantities associated to $u$:
- The action 
    $$
    \mathcal{A}(u) = \int_C u^* \omega
    $$
- The Hofer energy 
    $$
    \mathcal{E}(u)=\sup_{s\in \mathbb{R}} \int_{C\cap u^{-1}(\{s\}\times Y)} u^*\lambda
    $$

<theorem>

Let $u_k: C_k \to R\times Y$ be such that $\lim_{k\to \infty} \mathcal{A}(u_k)=0$ and $\inf_k x(C_k)>-\infty$. Then every $k\in L(u_*)$ satisfies $k=(-1,1) \times \Lambda$ for some closed non-empty invariant set $\Lambda$.

</theorem>

The upshot is that the sequence as in the theorem gives a connected family of invariant sets. 

<remark>

The main novelty is that there is no bound required on the Hofer energy $\mathcal{E}(u_k)$.

</remark>

# Dynamical Applications 

The upshot is that the theorem widely applicable in low dimensions. In higher dimensions, problems are more open. In particular, they are very important in relation to the Le Calvez-Yoccoz Theorems

<definition>
<src>Birkhoff</src>

A dynamical system $Y$ is **minimal** if every orbit is dense.

</definition>

One motivation is that if $Y$ is not minimal, we can write $Y=k \cap (Y-k)$ where $k$ is a non-trivial invariant set.

<problem>
<src>Ulam</src>

Is there a minimal homeomorphism of $\mathbb{R}^n$ or $\mathbb{R}^n - \{p\}$?

</problem>

<theorem>
<src>Le Calvez, Yocroz, 1997</src>

A homeomorphism of $S^2-\{p_1,...,p_k\}$ is never minimal.

</theorem>

<definition>

A system has the **(strong) Le Calvez-Yoccoz property** if the complement of any nontrivial invariant set is never minimal.

</definition>

<theorem>
<src>Cristofaro-Gardiner, Prasad</src>

The following have the strong Le Calvez-Yoccoz property:

1. Any Hamiltonian diffeomorphism of a closed surface
2. Any Reeb flow on a rational homology sphere 
3. Any geodesic flow on a closed surface (considered as a flow of its unit tangent bundle)

</theorem>

<remark>

There is no genericity required.

</remark>

<corollary>

$(1)-(3)$ have the property that the non-trivial invariant sets are dense 

</corollary>

<corollary>

Any geodesic flow on a surface has the property that a dense set of points have $n$ non-dense geodesic passing through them.

</corollary>

# Proof Ideas 

## Finding Low Action Curves of Controlled Topology

This part of the proof uses the embedded contact homology $\text{ECH}$. For $(Y, \lambda)$ a closed 3-manifold, $\text{ECH}(Y,\lambda)$ is a homology of a cochain complex that counts (mostly) embedded curves. 

<theorem>

$$
\text{ECH}(X, \lambda) \cong \text{HM}(Y)
$$

</theorem>

There exists a map $u: \text{ECH}\to \text{ECH}$ bounding curves through a marked point and the Weyl law allows us to use the $u$-map to produce low action curves

<problem>

How do we bound $X_\pi(C_k)?$

</problem>

There is no bound a priori on the genus.

<theorem>
<src>Cristofaro, Gardiner, Prasad</src>

$$
x_k(C_k)\ge -2.
$$

</theorem>

## Proving the Compactness Theorem

The main point is a new estimate that bounds of $C$ in a small ball if $C$ is low action in terms of $\chi(C)$.