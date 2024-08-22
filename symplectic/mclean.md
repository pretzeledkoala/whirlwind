<link href="../whirlwind.css" rel="stylesheet">

<whirlheader>
    <p>Gary</p>
    <p>McLean</p>
    <p>August 19</p>
</whirlheader>

# Symplectic Orbifold GW Invariants 

The aim is to construct $\partial W$ invariants for orbifolds. Over $\mathbb{Q}$, this was done by <src>Chen, Ruan</src>. We want to use global Kuranishi charts. This is part of a larger project proving a version of the crepant resolution conjecture. There is also work by <src>Mak, Seytoddin, Smith</src> are working on the global quotient case. This talk is all joint work with <src>Ritter</src>.

An orbifold is like a manifold, but the charts look like $V/\Gamma$ where $V\subset \mathbb{R}^n$ is an open finite subset, $\Gamma \to \text{GL}_n(\mathbb{R})$. For example, $\{\text{pt}\}/\mathbb{Z}/2$ is an orbifold. 

Suppose $G$ is a compact Lie group acting on a smooth manifold $M$ with finite stabilizers. Then the quotient $[M/G]$ is naturally an orbifold.

<theorem>
<src>The Slice Theorem</src>

For each point $x\in M$, there exists a $G_X$-equivariant submanifold $S_X \subseteq M$ containing $X$ and a $G$-equivariant neighborhood $U_X\subseteq M$ of $X$ such that
$$
G\times_{G_X} S_X\to U_X
$$
is a diffeomorphism.

</theorem>

<definition>

If $S_X$ has a global $G_X$ equivariant coordinate system, then $(S_X, G_X)$ is an **orbifold chart** for $[M/G]$ centered at $X$.

</definition>

<theorem>
<src>Pardon</src>

Every compact orbifold is of the form $[M/G]$.

</theorem>

<definition>

Let $[M_1, G_1], [M_2, G_2]$ be orbifolds. A **Hilsum-Skandalis morphism** between these orbifolds is a diagram

<!-- \begin{tikzcd}
	P & {M_2} \\
	{M_1}
	\arrow["f", from=1-1, to=1-2]
	\arrow["\pi"', from=1-1, to=2-1]
\end{tikzcd} -->

where there is a $G_1\times G_2$ action on $P$, $\pi$ is a principal $G_2$-bundle that is $G_1$-equivariant, and $f$ is $G_2$-equivariant.

</definition>

We can define a symplectic orbifold, complex orbifold, etc.

<definition>

If $X=[M/G]$ is an orbifold, then $\underline{X}=M/G$ is the **underlying coarse moduli space**.

</definition>

Let's fix $(X,\omega, J)$ where $X$ is an orbifold, $\omega$ is a symplectic form, and $J$ is a $J$-taming almost complex structure. Take $\beta \in H_2(\underline{X}, \mathbb{Z})$.

<definition>

A **twisted nodal domain** $\Sigma$ is a space $\tilde{\Sigma}/\sim$ where $\tilde{\Sigma}$ is a 1d complex orbifold and the equivalence relation is identifies distinct pairs of points $p\sim q$ so that the following balancing condition holds:
- $p$ admits an orbifold chart with coordinate $z$ centered at $p$ and where the stabilizer group $\mathbb{Z}/k\mathbb{Z}$ acts by $(m,z)\to e^{2\pi i m} z$
- $q$ admits an orbifold chart with coordinate $z$ centered at $q$ and where the stabilizer group $\mathbb{Z}/k\mathbb{Z}$ acts by $(m,w)\to e^{-2\pi i m} w$

</definition>

So, near a node, $\Sigma$ looks like $\{XY=0\}/\,\mathbb{Z}/k\mathbb{Z}$ with $(g,(x,y))=(gx,g^{-1}x)$. We can extend this to $\{XY=t\}/ \, \mathbb{Z}/k\mathbb{Z}$.

<definition>

A **marking** on $\Sigma$ is a collection of distinct points $p_1,...,p_n$ disjoint from the nodes containing all smooth points with nontrivial stabilizer.

</definition>

To learn more, see <src>Abramovich, Vistoli</src>.

<definition>

A **twisted nodal curve** $U:\Sigma \to X$ is a $J$-holomorphic Hilsum-Scandalis morphism $\Sigma \to X$ such that 
- this descends to a continuous map $\Sigma \to \underline{X}$
- the induced map of stabilizer groups $G_\sigma\to G_{u(\sigma)}$ is injective for all $\sigma \in \tilde{\Sigma}$.

</definition>

<src>Abramovich, Vistoli</src> studied the example $\{\text{pt}\}/\,\mathbb{Z}/2=X$.

For smooth $g=0$ case, Sieburt considered $(u, \Sigma, F)$ where $u: \Sigma \to X$, $L\to X$, and the framing is a basis of $H^0(u^*L)$. Then, we obtain $\mathcal{E}\to \mathbb{P}^d$ where $d=\dim H^0(u^*L)-1$ and $\mathcal{F}=\mathcal{M}_{0,d}(\mathbb{P}^n)$.

There are many problems with generalizing this $g=0$ case to the smooth orbifold case:
1. For higher genus curves, there is a moduli space of line bundles in each given degree 
2. Twisted nodal curves with nontrivial stabilizer groups don't map to $\mathbb{CP}^d$

Let's deal with $(2)$, using an idea by <src>Ross, Thomas</src>. Instead of looking at curves mapping to $\mathbb{CP}^d$, we'll look at curves mapping to the weighted projective space 
$$
P(w_0,...,w_d) = \left( \mathbb{C}^{d+1}- 0\right)/\sim
$$
with 
$$
(z_0, ...,z_d)\sim (t^{w_0}z_0, ..., t^{w_d}z_d)
$$
for all $t\in \mathbb{C}^\times$. 

Let $Y$ be a compact complex orbifold with only cyclic stabilizer groups. We should think of $\tilde{\Sigma}$. 

<definition>

A line bundle $L$ is **locally ample** if for all $y\in Y$, the stabilizer group of $Y$ acts faithfully on the fiber $L|_Y$.

</definition>

<definition>

$L$ is **globally positive** if $L^N$ is a pullback of an ample line bundle from $Y$.

</definition>

<definition>

$L$ is **orbi-ample** if it is locally ample and globally positive 

</definition>

<definition>

Let $n_i = |H^0(L^i)|$ for $i$. A **$k$-framing** of $L$ is a tuple 
$$
\left(f_{ij}\right)_{i=k,...,2k, \,j=0,...,n}
$$
where $f_{ij}, J=0,...,n$ is a basis of $H^0(L^i)$.

</definition>

<theorem>

Define $\mathbb{P}_k(L)=\mathbb{P}(k,...,k, k+1,....,k+1,..., 2k, ...,2k)$ and let $n_i$ be the number of $i$'s in this expression. Take $\phi_F: Y\to \mathbb{P}_k(L)$ to be the map that sends $y$ to $[\tau f_{ij}(y)]_{i=k,..., 2k, \, j=0,...,n_i}\subset \mathbb{P}_k(L)$. Then
$$
\tau: L|_y \to \mathbb{C}
$$
is an isomorphism.

</theorem>