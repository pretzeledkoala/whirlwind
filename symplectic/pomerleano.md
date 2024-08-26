<link href="../whirlwind.css" rel="stylesheet">

<whirlheader>
    <p>Gary</p>
    <p>Oganesyan</p>
    <p>August 21</p>
</whirlheader>

- Let $K$ be a field.
- Fix a lattice $M\cong Z^n$ a lattice, assume $n\ge 4$.
- Let $M_R = M\otimes_{\mathbb{Z}} \mathbb{R}$, $M_{\mathbb{C}^\times}=M\otimes_{\mathbb{Z}} \mathbb{C}^\times$.
- Fix $\Delta$ a reflexive polytope in $M_{\mathbb{R}}$, and let $\Delta_* \subset M_{\mathbb{R}}^*$ be the dual polytope. 
- Let $\overline{\Sigma} \subset M_{\mathbb{R}}^*$ be the fan dual to $\Delta$ (rays of the fan point along the vertices of $\Delta^*$)

Assumption: 
- $\Sigma^*$ the fan dual to $\Delta^*$ is a smooth fan.
- $\overline{\Sigma} \rightsquigarrow \overline{Y}$ a toric variety, $\Sigma^* \rightsquigarrow Y^*$ smooth. 
- Let $P$ denote the integer lattice points $\Delta^* \cap M^*$ and let $P\subset P^0$ be the subset of lattice points which lie on a face of codimension $\ge 2$. 

# B-Side 
Consider $\mathcal{L}_{\Delta^*} \to Y^*$ and let 
$$
W_r = - z^0 + \sum_{p\in P} r_pz^p
$$

$(r_p) \in \wedge_K^P$ where $\wedge_K:= \sum_{i=0}^\infty a_iT^{b_i}$, where $\lim_{i\to \infty} b_i = \infty, a_i \in K$ is the Novikov ring. We have 
$$
X_r^* = \{ W_r =0\}\subset Y.
$$

# A-Side 

- Assume $\overline{Y}$ is not assumed to be smooth, $A=\Delta\cap M$, $z^\alpha \in \Gamma(\overline{Y}, \mathcal{L}_\Delta)$. 
- Let $\Sigma$ be a refinement of $\overline{\Sigma}$, where $\Sigma(1)=P$.
- Assume $Y=Y_\Sigma$ is smooth away from dimension 
    $$
        \overline{X}_t = \{ -tz^0 + \sum_{\alpha \in A\backslash 0} z^\alpha =0 \}\subset \overline{Y}
    $$
    The proper transform $X_t$ is a smooth Calabi-Yau in $Y$.

Consider a Kähler class on $Y$ of the form 
$$
[w]=\sum_{p\in P} \ell_p \text{PD}([D_P^Y]), \qquad \ell_p \in \mathbb{R}^{>0}.
$$
and restrict it to $X_t$.

On the A-side, we consider a variant of the Fukaya category 
$$
\text{Fut}(X_t, D; \wedge)
$$

where 
- objects of this category are compact exact Lagrangian submanifolds in $X_t \backslash D$.
- holomorphic curves $u$ are weighted by $T^{\Sigma \ell_p u \cdot D_p}$.

<theorem>

Suppose that $D_p$ are connected. Away from finitely many bad characteristics, there exist $b(\wedge)=(b(\wedge))
_{p\in P} \in \wedge^P$ with $\text{val}(b(\wedge)_p)=\ell_p$
and an equivalence 
$$
\text{Fuk}(X_t, D; A)\cong D^b\text{Coh}(X_{b(\wedge)})^*
$$

</theorem>

<remark>

In characteristic 0, homological mirror symmetry implies Givental's Hodge theoretic mirror symmetry.

</remark>

This motivates the following problem:

<problem>

Is there some kind of Gromov-Witten implication of homological mirror symmetry in a positive characteristic?

</problem>

# Strategy of Proof 

Follows from the groundbreaking worth of Seidel (in the case of quartic surface in $\mathbb{P}^3$). 

1. Step 1: $\text{Fuk}(X_t\backslash D) \cong D^b\text{Coh}(\partial Y^*)$ where $\partial Y^*$ is the toric divisor which is cut out by $z^0$. For $\mathcal{A}_0 \subset \text{Fuk}(X_t\backslash D)$, $\mathcal{B}_\gamma:= \{\theta(i)\}_{i\in \mathbb{Z}}$
2. Step 2: Employ a deformation theory argument

## Step 1: Open HMS 

Let $H=X_t\backslash D \subset (\mathbb{C}^\times)^n$.
- We can consider $W(H)$, where we allow certain non-compact Lagrangians 
- $W((\mathbb{C}^\times)^n, H)$.

where $\cup$ is the Orlov functor.

<theorem>
<src>Gammage, Shende</src>

<!-- \[\begin{tikzcd}
	{W(H)} && {D^b\text{Coh}(} \\
	{W((\mathbb{C}^\times)^n, H)} && {D^b\text{Coh}(Y^*)}
	\arrow["\cong"{description}, draw=none, from=1-1, to=1-3]
	\arrow["\cup", from=1-1, to=2-1]
	\arrow["\cong"{description}, draw=none, from=2-1, to=2-3]
\end{tikzcd}\] -->

</theorem>

Abouzaid considered a different form of homological mirror symmetry for toric varieties where he considers certain Lagrangian actions with boundary on this hypersurface $H$ 
$$
\mathcal{F}_{\text{trop}}((\mathbb{C}^\times)^n, H) \simeq \text{Pic}^{dg}{Y^*}
$$

<theorem>

INSERT DIAGRAM

</theorem>

One thing that gets used that wasn't available to Seidel/Sheridan is that 
$$
\text{CO}: \text{SH}^*(X_t\backslash D) \longrightarrow \text{HH}^*(W(X_t\backslash D))\longrightarrow \text{HH}^*(\text{Fut}(X_t\backslash D))
$$
are isomorphisms and $\text{SH}^*(X_t\backslash D)$ can be computed in terms of the topology of the pair $(X_t,D)$.