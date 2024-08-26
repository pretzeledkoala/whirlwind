<link href="../whirlwind.css" rel="stylesheet">

<whirlheader>
    <p>Gary</p>
    <p>Local Structure of Holomorphic Curve Moduli Spaces</p>
    <p>August 19</p>
</whirlheader>

# The Moduli Space 

Suppose $(X^{2n}, \omega)$ is a closed symplectic manifold, $A\in H_2(X,\mathbb{Z})$ with $m \ge 0$, and $J$ is an almost complex structure $X$ tamed by $\omega$, i.e. $\omega(v,Jv)>0$ where $0\neq v \in T_X X$. Let $U$ be a $J$-holomorphic map $\mathbb{CP}^1 \to X$. Here, $du$ is linear and $u_*[\mathbb{CP}^1]=A$. This gives the moduli space $\mathcal{M}_{0,m}(X, A, J)$.

Instead of just consider $\mathbb{CP}^1$, we can also consider more complicated objects where we glue together several $\mathbb{CP}^1$ components at nodes, giving a tree of $\mathbb{CP}^1$. The curves arising from $\text{trees of }\mathbb{CP}^1 \to X$ are called **nodal genus 0 curves**.

These nodal genus 0 curves allow us to enrich our moduli space. In particular, we can now study 
$$
\overline{\mathcal{M}}_{0,m} (X,A,J) =\left\{ \left(\sum x_1,...,x_m, u: \Sigma \to X\right) | \text{condition} \right\}/\sim
$$
where the condition is that $\Sigma$ is a nodal genus 0 curve with $m$ marked points $x_1,...,x_m$, $u$ is J-holomorphic, $u_*[\Sigma]=A$ and $\# \text{Aut}(\Sigma, x_1,...,x_m,u) < \infty$. This condition is equivalent to the condition that on any component of $\Sigma$ where $u$ is constant, there are 3 special points.

We present two basic properties of this moduli space:

<theorem>
<src>Gromov Compactness Theorem</src>

$\overline{\mathcal{M}}_{0,m} (X,A,J)$ is compact and Hausdorff.

</theorem>

<theorem>

$\overline{\mathcal{M}}_{0,m} (X,A,J)$ has an expected/virtual dimension
$$
d=2(m-3+n+c_1(TX)\cdot A).
$$

</theorem>

Here is the motivating problem:

<problem>

Can we count the number of points in $\overline{\mathcal{M}}_{0,m} (X,A,J)$ after cutting down the virtual dimension to $0$?

</problem>

The issue is that in general, the moduli space is not a manifold of the expected dimension.

# The Transverse Case 

<problem>

Suppose that we are given $(\Sigma, x_1,...,x_m, u: \Sigma \to X) \in \overline{\mathcal{M}}_{0,m} (X,A,J)$? What is the local structure of $\overline{\mathcal{M}}_{0,m} (X,A,J)$ near this point?

</problem>

We have two cases: when $\Sigma$ is smooth versus nodal.

## $\Sigma$ is Smooth

Here, smooth means $\Sigma \cong \mathbb{CP}^1$. Recall that 
- $\mathcal{B}=C^\infty (\Sigma, X)_A=\left\{ v:\Sigma \to X | v \text{ is }C^\infty, v_*[\Sigma]=A \right\}$, which we should think of an infinite dimensional manifold. 
- $\mathcal{E}$ is an infinite rank vector bundle on $\mathcal{B}$ whose fiber is $\Omega^{0,1}(\Sigma, v^*TX) = \overline{\text{Hom}}_{\mathbb{C}}(T\Sigma, v^*TX)$ over any $v\in \mathcal{B}$.
- $\sigma$ is a section of $\mathcal{E}$ over $\mathcal{B}$ given by $\left(v\mapsto \overline{\partial}_J v\right)$ where $\overline{\partial}_K = \frac{1}{2} (dv+J(v)\cdot dv \cdot j_\Sigma)$

Note that $\sigma^{-1}(0)=\text{Hol}(\Sigma, X,A,J)$.

We know that $u \in \sigma^{-1}(0)$, which means $\sigma$ has a well-defined linearization of $u$, namely 
$$
D_u \sigma: T_u \mathcal{B} \to \mathcal{E}_u.
$$
More explicitly, this map is given by 
$$
D(\overline{\partial}_J)_u \sigma: \Omega^0(\Sigma, u^*TX) \to \Omega^{0,1}(\Sigma, u^* TX).
$$

In holomorphic local coordinates, $z=s+it$ on $\Sigma$, 
$$
\overline{\partial}_J u = \dfrac{1}{2} \left(\dfrac{\partial U}{\partial s} + J(u) \dfrac{\partial u}{\partial t}\right)\otimes (ds-idt).
$$

Given $\xi \in \Omega^0(\Sigma, u^*TX)$, we want to look at $\frac{d}{d\epsilon}|_{\epsilon =0}(u+\epsilon \xi)$. We have 
$$
D \left(\overline{\partial}_J\right)_u \xi = \dfrac{1}{2} \left(\dfrac{\partial \xi}{\partial s} + J(u)\dfrac{\partial \xi}{\partial t} + \left(\partial_\xi J\right)(u) \dfrac{\partial u}{\partial t}\right)\otimes (ds-idt).
$$
We can check that $\dfrac{\partial \xi}{\partial s} + J(u)\dfrac{\partial \xi}{\partial t}$ is 1st order and $\left(\partial_\xi J\right)(u) \dfrac{\partial u}{\partial t}$ is 0th order.

For notation purposes, write $D_u:= D(\overline{\partial}_J)_u$. We have $D_u$ is Fredholm, i.e. $\text{ker, coker}$ are finite dimensional, and 
$$
\text{ind}(D_u)=\dim(\ker D_u)-\dim (\text{coker} D_u)= 2(n+c_1(TX)\cdot A)
$$
where the second equality comes from Riemann-Roch. 

The implicit function theorem tells us that if $D_u$ is surjective, then $\mathcal{M}_{0,m}(X,A,J)$ is a orbifold of expected dimension near $(\Sigma, x_1,...,x_m, u)$.

We conclude that
$$
\mathcal{M}_{0,m}(X,A,J) = \text{Hol}(\mathbb{CP}^1, X,A, J)\times \left(\left(\mathbb{CP}^1\right)^m \backslash \Delta\right)/\text{PSL}_2(\mathbb{C})
$$
where $\Delta = \left\{ (x_1,...,x_m)|x_i=x_j \text{ for some }i\neq j\right\}$. 

## $\Sigma$ is Nodal

Here, nodal means $\Sigma \cong$ trees of $\mathbb{CP}^1$'s. Consider $\tilde{\Sigma}$, the normalization of $\Sigma$ where we disjoint the spheres. The map 
$$
\tilde{u}: \tilde{\Sigma} \stackrel{\text{normalization}}{\longrightarrow} \Sigma \stackrel{u}{\to} \Sigma
$$
gives 
$$
D_{\tilde{u}}: \Omega^0  \left(\tilde{\Sigma}, \tilde{u}^* TX\right)\to \Omega^{0,1}(\tilde{\Sigma}, \tilde{u}^*TX)
$$
and
$$
D_{{u}}: \Omega^0  \left({\Sigma}, {u}^* TX\right)\to \Omega^{0,1}(\tilde{\Sigma}, \tilde{u}^*TX)
$$
where $\Omega^0(\Sigma, u^*TX) \subseteq \Omega^0  \left(\tilde{\Sigma}, \tilde{u}^* TX\right)$.

<exercise>

Check that $\text{ind}(D_u)=2(n+c_1(TX)\cdot A)$

</exercise>

<theorem>
<src>Gluing Theorem</src>

If $D_u$ is surjective, then $\overline{\mathcal{M}}_{0,m}(X,A,J)$ has a local chart near $(\Sigma,x_1,...,x_m, u)$ of the form $V/\Gamma$ where $V$ is a vector space of the expected dimension and $\Gamma$ is a finite group acting linearly on the vector space.

</theorem>

# Local Kuranishi Charts

Let $\mathcal{B}$ be a Banach manifold, $\mathcal{E}$ a Banach vector bundle, and $J$ a smooth section with Fredholm linearizations. We want to study $\overline{\mathcal{M}} = \left(D \overline{\partial}\right)^{-1}(0)\subset \mathcal{B}$.

Suppose $u\in \overline{\mathcal{M}}$ is given. If $\left(D \overline{\partial}\right)_u$ is surjective, then we are done, i.e. $\overline{\mathcal{M}}$ is a manifold near $u$ and $T_u \overline{\mathcal{M}}=\ker \left(D \overline{\partial}\right)_u$.

So let's assume that $D_u: T_u \mathcal{B}\to \mathcal{E}_u$ is not surjective. Choose a finite dimensional vector space $V$ and a linear map $\lambda: E \to \mathcal{E}_u$ such that $E\twoheadrightarrow \text{coker}D_u$, i.e. $D_u \oplus \lambda: T_u \mathcal{B} \oplus E \twoheadrightarrow \mathcal{E}_u$. Choose a neighborhood $u\in \mathcal{U} \subset \mathcal{B}$ and an extension $\lambda: \mathcal{U}\times v \to \mathcal{E}_{\mathcal{U}}$.

Now, consider 
$$
\mathcal{M}_{\mathcal{U}, E, \lambda} = \left\{ v\in \mathcal{U}, e\in E | \overline{\partial}v+\lambda(v,e) =0 \right \} \hookleftarrow  \overline{\mathcal{M}}\cap \mathcal{U}.
$$
There is a projection $s: \overline{\mathcal{M}}_{\mathcal{U}, E, \lambda}\to E$. 

Let's consider the linearized operators at $(u,0) \in \overline{\mathcal{M}}_{\mathcal{U}, E, \lambda}$ given by
$$
T_u \mathcal{B} \to \mathcal{E}_u \\
(\xi, e)\mapsto D_u \xi + \lambda(u,e)
$$
which is surjective.

<definition>

Suppose $\overline{\mathcal{M}}$ is a compact Hausdorff space. Then a **local Kuranishi chart of virtual dimension $d$** for $\overline{\mathcal{M}}$ is a quintuple $(\overline{\mathcal{M}}, E_\alpha, \Gamma_\alpha, s_\alpha, \psi_\alpha)$ where we have
- A finite dimensional topological manifold $\overline{\mathcal{M}}_\alpha$
- A finite dimensional vector space $E_\alpha$ such that $\dim \overline{\mathcal{M}}_\alpha = d+ \dim E_\alpha$
- A finite group $\Gamma_\alpha$ which acts on $\overline{\mathcal{M}}_{\alpha}$ and $E_\alpha$
- A $\Gamma_\alpha$-equivariant function $s_\alpha: \mathcal{M}_\alpha \to E_\alpha$
- A homeomorphism $\psi_{\alpha}:s_\alpha^{-1}(0)/\Gamma_\alpha \stackrel{\cong}{\to} U_\alpha \subset \overline{\mathcal{M}}$ where the subset is open.

</definition>

The upshot is that $\overline{\mathcal{M}}_{0,m}(X,A,J)$ is covered by local Kuranishi charts.

A local Kuranishi chart $(\overline{\mathcal{M}}, E_\alpha, \Gamma_\alpha, s_\alpha, \psi_\alpha)$ for $\overline{\mathcal{M}}$ induces a local virtual fundamental class on $U_\alpha$ via the following map:
$$
\begin{align*}
\widecheck{H}_c^d (U_\alpha; \mathbb{Q}) &\overset{\frac{1}{|\Gamma_a|}\psi_\alpha^*}{\underset{\cong}{\longrightarrow}} \widecheck{H}_c^d \left(s_a^{-1}(0); \mathbb{Q} \right)^{\Gamma_\alpha} \\
& \overset{\text{Pardon}}{\underset{\cong}{\longrightarrow}} H_{\dim E_\alpha} \left(\overline{\mathcal{M}}_\alpha, \overline{\mathcal{M}}\backslash s_\alpha^{-1}; \mathbb{Q}\right)^{\Gamma_\alpha} \\
&\stackrel{(s_\alpha)_*}{\longrightarrow} H_{\dim E_\alpha} \left(E_\alpha, E_\alpha\backslash s_\alpha^{-1}; \mathbb{Q}\right)^{\Gamma_\alpha} \\
&\overset{\text{orientation}}{\underset{\cong}{\longrightarrow}} \mathbb{Q}
\end{align*}
$$
where Pardon is the map found in <src>Pardon, 2016, Appendix A</src>.

<definition>

The **local virtual fundamental class** is this entire map
$$
[v_\alpha]_{\text{local}}^{\text{vir}}: \widecheck{H}_c^d (U_\alpha; \mathbb{Q})\to \mathbb{Q}.
$$

</definition>

<example>

For $\overline{\mathcal{M}}_\alpha = \mathbb{C}, E_\alpha = \mathbb{C}, \Gamma_\alpha=(1), s_\alpha(z)=z^n$, then
$$
[v_\alpha]_{\text{local}}^{\text{vir}}=n[\text{pt}].
$$

</example>

