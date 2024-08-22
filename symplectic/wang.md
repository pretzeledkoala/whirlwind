<link href="../whirlwind.css" rel="stylesheet">

<whirlheader>
    <p>Gary</p>
    <p>Wang</p>
    <p>August 19</p>
</whirlheader>

# ASDASD 

<definition>

$(X_1, \omega_1)$ and $(X_2, \omega_2)$ are **deformation equivalent** if there exists a diffeomorphism $\varphi: X_1\to X_2$ such that $\varphi^* \omega_2 \rightsquigarrow \omega_1$.

</definition>

<problem>
<src>Donaldson</src>

Given two closed simply-connected homeomorphic $(X_1^4, \omega_1)$ and $(X_2^4, \omega_2)$. Is $X_1$ diffeomorphic to $X_2$ equivalent to 
$$
(X_1\times S^2 \omega_1 \oplus \omega_{\text{std}}) \simeq (X_s \times S^2, \omega_2 \oplus \omega_{\text{std}}).
$$

</problem>

<theorem>
<src>Wall, 1964</src>

Two closed simply-connected homeomorphic 4-manifold are $h$-cobordant. 

</theorem>

<theorem>
<src>Smale, 1962</src>

Let $n\ge 5$. Then two closed simply connected $n$-manifolds are $h$-cobordant implies they are diffeomorphic.

</theorem>

Some history:
- <src>Ruan, 1994</src>: Homeomorphic but not diffeomorphic Kähler surfaces $\mathbb{C}^2 \# \overline{\mathbb{CP}}^2$ and Barlow surface.
- <src>Ruan, Tian, 1997</src>: Stabilizing conjecture. For simply connected elliptic surfaces.
- <src>Ionel, Parker, 1999</src> $E(n)$ using knot surgery.
- <src>Smith, 2000</src> Given $n\ge 2$. Constructs $n$ symplecitc structures on a fixed simply-connected $Z^4$ such that $c,s$ are different, which implies the 4-6 question cannot be replaced by $\pi^2$.


## Theorem A
<theorem>
<src>Hirschi, Wang, 2023</src>

There exists infinitely many pairs $(X_1, \omega_1), (X_2, \omega_2)$ such that $X_1, X_2$ are diffeomorphic, but 
$$
(X_1 \times S^2, \omega_1 \oplus \omega_{\text{std}}) \not\simeq (X_2 \times S^2, \omega_2 \oplus \omega_{\text{std}}).
$$

</theorem>

## Theorem B

<theorem>
<src>Hirschi, Wang, 2023</src>

Let $(X_1, \omega_1)$ and $(X_2, \omega_2)$ be closed simply-connected 4-manifolds such that 
$$
(X_1 \times S^2, \omega_1 \oplus \omega_{\text{std}}) \simeq (X_2 \times S^2, \omega_2 \oplus \omega_{\text{std}}).
$$

Then $\text{GW}(X_1)=\text{GW}(X_2)$.

</theorem>

# ASDAS 

<corollary>

If $(X_1, \omega_1)$ and $(X_2, \omega_2)$ satisfy hypothesis of Theorem B, and $b_2^+ \ge 2$, then $\text{SW}(X_1)=\text{SW}(X_2)$.

</corollary>

The invariant is orbits under diffeomorphisms of $c_1$: given symplectic form $\omega$, we can take a tame $J$ and it's first chern class $c_1(TX,J)$.

The goal is to show that $c_1(X\times S^2, \omega_1 \oplus \text{std})$.

<definition>

Given $X,Y$ let $G_{X,Y}$ be the set of cohomology equivalences $\psi$ of $X\times Y$ such that $\psi^*$ are maps $H^2(X, \mathbb{Z})\to H^2(X, \mathbb{Z})$ and $\text{pr}_G\psi(\cdot, Y)$ is cohomology equivalent.

</definition>

Steps:

0. Find a smooth manifold $X^4$ with symplectic forms $\omega_1$ and $\omega_2$ such that $c_1(\omega_1)$ and $c_1(\omega_2)$ lie in different orbits of cohomology equivalences. 
1. Show that if $c_1(\omega_1)$ and $c_2(\omega_2)$ lie in different orbits of cohomology equivalence, then $c_1(\omega_1 \oplus \omega_{\text{std}})$ and $c_1(\omega_2 \oplus \omega_{\text{std}})$ lie in different orbits of $G_{X, S^2}$.
2. Show that any diffeomorphism of $X\times S^2$ lies in $G_{X,S^2}$.

# Step 1 Proof
Let's prove step 1: 

Suppose there exists $\psi \in G_{X,S^2}$ such that $\psi^* c_1(\omega_2 \oplus \omega_{\text{std}})=c_1(\omega_1 \oplus \omega_{\text{std}})$. Then $\psi^* h = h+\alpha$, where $\alpha \in H^2(x)$. Also, $\psi^*(h^2)=0$ implies that $(h+\alpha)^2 = h^2 + 2\alpha h + \alpha^2 =0$, which implies $2a=0$ in $H^*(X\times \mathbb{CP}^1)\cong H^*(x)[h]/h^2$. Now we get 
$$
\begin{align*}
c_1(\omega_1) + 2h &= \psi^* c_1(\omega_2) + 2\psi^* h \\
&= \psi^* c_1(\omega_2)+2h+2\alpha
\end{align*}
$$

<proposition>

$\hat{\psi}$ is a cohomology equivalence on $X$.

</proposition>

## Counter Example for 0/2

Let $Z:= \mathbb{T}^4\# 5E(1)$ where $\#$ is the fiber sum. Then we have $\langle x,t \rangle = T_X, T_Y, T_Z, 2T_W$ where $[T_W] = [T_x+T_y+T_Z]$. Then we have $T_X, 2T_W$ are symplectic and $T_Y, T_Z$ are Lagrangian. 

<theorem>
<src>Smith</src>

$\xi \mid c_1(TZ, \omega)$ and $c_1(TZ, \omega)$ is prime.

</theorem>

# Theorem B Proof

Consider $(X_0, \omega_0)$ and $(X_1, \omega_1)$ simply connected. Suppose 
$$
(X_0\times S^2, \omega_0 \oplus \omega_{\text{std}})\simeq (X_1\times S^2, \omega \oplus \omega_{\text{std}}).
$$
Then there exists a homeomorphism $\varphi: X_0\to X_1$ such that for all $g,n \ge 0$ and $A\in H_2(X_0)$, we have 
$$
\text{GW}_{g,n,A}^{X_0, \omega_0}(\varphi^* \alpha_1, ..., \varphi^* \alpha_n)= \text{GW}_{g,n,\varphi^* A}^{X_0, \omega_0}(\alpha_1, ..., \alpha_n)
$$
for any $\alpha \in H^*(X, \mathbb{Q})$. 

<theorem>
<src>Hirschi-Swaminathan Product Formula</src>

For $(X_0, \omega_0)$ and $(X_1, \omega_1)$ with torsion free $H_1(X; \mathbb{Z})$, we have
$$
\text{GW}_{g,n,(B_X, B_Y)}^{X\times Y, \omega_X \oplus \omega_Y}(\alpha_1\times \beta_1,...,\alpha_n \times \beta_n) = \text{GW}_{g,n,B_X}^{X, \omega}(\alpha_1,...,\alpha_n)\text{GW}_{g,n B_Y}^{Y, \omega Y}(\beta_1,...,\beta_n)
$$
in $H^*(\overline{\mathcal{M}}\text{gin???}; \mathbb{Q})$.

</theorem>

The goal is to find some ????????????????

<lemma>

This is possible 
?????

Now assume $\exists$ homeomorphism $\phi: X_0 \to X_1$ such that $\tilde{\phi}^*$ on $X_1\times S^2 \to X_0 \times S^2$ agree with $\phi^* \otimes \text{id}$.

</lemma>


??????????WRITE THE REST LATER