<link href="../whirlwind.css" rel="stylesheet">

<whirlheader>
    <p>Gary</p>
    <p>Pardon</p>
    <p>August 21</p>
</whirlheader>

# Introduction 

We are interested in properties and structures of moduli spaces of solutions to elliptic partial differential equations, which lead to enumerative invariants:

1. **Global topological property**: (Uhlenbeck, Gromov) compactness
2. **Local structure**: Regularity, of which there are two types:
    - Classical regularity: $\mathcal{M}$ is locally $\cong \mathbb{R}^n$ (or more generally, sometimes $\mathbb{R}\times \mathbb{R}_{\ge 0}^m$, etc.). Classical regularity requires transversality (e.g. by choosing "generic" data for the partial differential equation). 
    - Derived regularity: $\mathcal{M}$ is locally $\cong$ zero set for a smooth function on $\mathbb{R}^n$ (or more generally, sometimes $\mathbb{R}\times \mathbb{R}_{\ge 0}^m$, etc.). Derived regularity holds in wide generality, however, it becomes technical to say what the relevant structure on $\mathcal{M}$ encoding such chart actually is <src>Fukaya, Ono; Fukaya, Oh, Ohta, Ono; Li, Tian; Ruan, Seibert; etc.</src>

We want to associate with every moduli problem a moduli space, which is associated to an enumerative invariant. We will mostly focus on associating with every moduli problem a moduli space.

<problem>

Why is derived regularity complicated (in comparison to the classical case)?

</problem>

The answer is that derived regularity is a contact structure.

<example>

Consider a proper submersion $Q\to B$, let $E,F/Q$ be vector bundles, and $L:C^\infty(Q,E)\to C^\infty(Q,F)$ be a vertical elliptic operator. What is the nature of $\pi_*L$, the 2-term complex finite vector bundle on $B$ where pointwise cohomology is $\ker L_b$ and $\text{coker }L_b$, where $L_b$ is the restriction of $L$ to $Q_b$?

Given $V\stackrel{d}{\longrightarrow} W$ and $V\oplus \mathbb{R} \stackrel{d\oplus 1}{\longrightarrow} W\oplus \mathbb{R}$, $\pi_L$ is unique up to contractible choice in the 2-category of 2-term vector bundles on $B$, where contractible choice means 

\[\begin{tikzcd}
	V && W \\
	{V'} && {W'}
	\arrow["d", from=1-1, to=1-3]
	\arrow["f"', shift right=3, from=1-1, to=2-1]
	\arrow["g", shift left=3, from=1-1, to=2-1]
	\arrow["h"{description}, from=1-3, to=2-1]
	\arrow["g", shift left=3, from=1-3, to=2-3]
	\arrow["f"', shift right=3, from=1-3, to=2-3]
	\arrow["{d'}"', from=2-1, to=2-3]
\end{tikzcd}\]

where $d'h+hd=f-g$.

</example>

Let $\text{Sm}$ be the category of smooth manifolds and $\text{DSm}$ be the $\infty$-category of derived smooth manifolds. The functor $\text{Sm}\to \text{DSm}$ freely adjoints finite limits, modulo preserving finite products. 

Concretely, a derived smooth manifold is a formal symbol $\lim_K p$ for some finite degree $p: K\to \text{Sm}$, e.g.
$$
\lim\left( \begin{tikzcd}
	&& {\mathbb{R}} \\
	\\
	{*} && {\mathbb{R}}
	\arrow["{x\mapsto x^2}", from=1-3, to=3-3]
	\arrow["0", from=3-1, to=3-3]
\end{tikzcd} \right) \in \text{DSm}
$$

Additionally, we have 
$$
\text{Hom}_{\text{DSm}}(\lim_K p, \lim_L q) =\text{sheafification on }\lim_K|p| \left( \lim_L \text{colim}_{K_\Delta} \text{Hom}_{\text{Sm}}(p_\Delta, q) \right)
$$

<example>

Let 
$$
\tau:= \lim\left(\begin{tikzcd}
	&& {\mathbb{R}} \\
	\\
	{*} && {\mathbb{R}}
	\arrow["{x\mapsto x^2}", from=1-3, to=3-3]
	\arrow["0", from=3-1, to=3-3]
\end{tikzcd}\right)
$$
A map $\tau \to M \in \text{Sm}$ is a a point $p\in M$ and a vector $v\in T_pM$. 

</example>

<remark>

$D(\text{topological manifolds})$ is full subcategory of $\text{Top}$. 

</remark>

Each $X\in \text{DSm}$ has an associated $TX\in \text{Perf}^{\ge 0} (X)$. 

# Representability 

<definition>

Let $C$ be a Riemann surface, $X$ an almost complex manifold. A **family** of $\psi$-holomorphic maps $C\to X$ parameterized by $Z$ is a map $Z\times C \stackrel{u}{\longrightarrow} X$ together with an isomorphism between $0$ and the derivative 
$$
Z\times C \stackrel{(D_{C}u)^{0,1}}{\longrightarrow}TX\otimes_{\mathbb{C}} \overline{T^*C}.
$$

</definition>

<theorem>
<src>Pardon, Steffens</src>

There exists a derived smooth manifold $\text{Hol}(C,X)$ and a nontrivial bijection (for $Z\in \text{DSm}$)
$$
\left\{ \text{maps }Z\to \text{Hol}(C,X)\right\}\stackrel{\sim}{\longrightarrow} \{\text{families of }\psi\text{-holomorphic maps } C\to X \text{ parameterized by } Z\}.
$$

</theorem>

<remark>

For $u: C\to X$ a part of $\text{Hol}(C,X)$, we have a canonical isomorphism 
$$
H^*(T_n \text{Hol}(C,X))=\begin{cases} \ker D_n & *=0 \\ \text{coker }D_n & *=1 \end{cases}
$$
where 
$$
D_n :C^\infty(C, u^* TX) \to C^\infty(C, u^* TX\otimes_{\mathbb{C}} \overline{T^* C})
$$

</remark>

<example>

If $\text{coker }D_n=0$, then $T_n \text{Hol}(C,X)$ has $H^*$ support in degree $0$, which implies that $\text{Hol}(C,X)$ is smooth near $u$.

</example>

<!-- INSERT IMAGE THING HERE -->

The content in the proof is the following:

<proposition>

For $Z\in \text{DSm}$ and every map $Z\times C \to X$ (not necessarily $\psi$-holomorphic) and an isomorphism $v=v|_Z$ with $v: Q\times C\to X$. 

</proposition>

An application of the above proposition is as follows:

<theorem>
<src>Zung</src>

$X$ a smooth stack with submersive atlas and a proper diagonal, then $X$ is locally isomorphic to $M/G$ for $G$ a compact Lie group.

</theorem>

Using the proposition, we can show the same holds for any derived smooth stack.