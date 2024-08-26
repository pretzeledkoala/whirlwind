<link href="../whirlwind.css" rel="stylesheet">

<whirlheader>
    <p>Gary</p>
    <p>Massoni</p>
    <p>August 21</p>
</whirlheader>

# Introduction

Let $M^2$ be a closed, oriented, connected 3-manifold. 

Informally, a foliation $\mathcal{F}$ is made by decomposing $M$ into 2d leaves. If such a foliation is smooth, we can define $T\mathcal{F}=\text{Ker }\alpha$, where $\alpha$ is a 1-form.

<theorem>
<src>Frobenius Integrability Theorme</src>

$$
\alpha \wedge \,d\alpha=0.
$$

</theorem>

<definition>

The **minimally integrable plane field** is
$$
\xi = \text{Ker }(\alpha)
$$
where $\alpha$ is a 1-form satisfying 
$$
\alpha \wedge d\alpha \neq 0
$$

</definition>

Locally, we have the following theorem:

<theorem>
<src>Darboux</src>

$$
\alpha = \,dz+x\,dy
$$

</theorem>

<theorem>

Every homotopy class of a plane field is defined up to foliation.

</theorem>

<proof>

Follows from the $h$-principal.

</proof>

<theorem>
<src>Eliashberg</src>

The same holds for contact structures.

</theorem>


<definition>

A **taut foliation** satisfies the following properties:
- for all $p\in M$, there exists $\gamma$ cloosed loop passing through $p$, where $\gamma$ transverses $\mathcal{F}$.
- there exists $\omega$ a closed 2-form satisfying $\omega_{T\mathcal{F}}>0$.

</definition>

We present the following (badly defined) definition. 

<definition>

**Tight contact structures** is a structure that isn't over-twisted.

</definition>

<problem>

Which $M$ carry a taut foliation? Reebless foliation? Tight contact structure?

</problem>

<theorem>

If the first Betti number $b_1(H)>0$, there exists a taut foliation.

</theorem>

<theorem>
<src>Eliashberg, Thurson</src>

There exists tight contact structures.

</theorem>

<problem>

What happens for $b=1$, equivalently $QHS^3$?

</problem>

<conjecture>
<src>L-Space Conjecture</src>

Let $M$ be $QHS^3$, irreducble, The following are equivalent:

1. $M$ causes a taut foliation 
2. $M$ is not an $L$-space: $\text{HF}^{\text{red}}=0$
3. $\pi_1(M)$ is left-orderable

</conjecture>

We have the following result:

<theorem>
<src>Ozsvath, Szabo</src>

$$
(1)\implies (2)
$$

</theorem>

But in general, it's unsolved and people think it's wrong.

The punchline is taut foliations can be thought of as contact geometry objects.

# From Foliations to Contact Structures 

<theorem>
<src>Eliashberg, Thurston, 1998</src>

1. For a $\mathcal{F}$ foliation $(C^2)$ with no spherical leaf (meaning no $\mathcal{F}=S^2 \times \{\text{pt}\}$ on $S^1\times S^2$), then $T\mathcal{F}$ $t_L$ are approximately contact structures.
2. If $\mathcal{F}$ taut, then the contact structures are tight.

</theorem>

## Proof of $(2)$

Look at $[-1, 1]\times M$, choose $\omega$ closed in $M$, $w|_{T\mathcal{F}}>0$, and choose $\alpha$ a 1-form such that $T\mathcal{F}=\ker \alpha$. 

Suppose $\Omega = \omega(t\alpha)$. If $\xi_{\pm}$ weak symplectic filling of $(-M, \xi_-) \sqcup (M, \xi_+)$. If $\xi_\pm$ $C^0$-close to $T\mathcal{F}$, then $\Omega$ is symplectic and $\Omega|_{\xi_\pm}>0$.

By <src>Gromov, Eilenberg</src>, $\xi_+$ is tight.

</proof>

<definition>

A $C^0$-foliation is a topological foliation where the leaves are smoothly immersed and $T\mathcal{F}$ is $C^0$

</definition>

<theorem>
<src>Bowden, Kasez, Robert</src>

Eliashberg-Thurson holds for $C^0$-foliations.

</theorem>

We should think of Eliashberg-Thurson as a machine that turns a foliation into a postiive contact pair $(\xi_-, \xi_+)$.

# From Positive Constant Pairs to Foliations

<definition>

We say $(\xi_-, \xi_+)$ is a **positive contact pair** if $\xi_\pm$ is a $\pm$ contact structure and there exists a vector field $Z$ such that $Z$ positively transverses $\xi_\pm$.

</definition> 

Fix $(\xi_+, \xi_-)$ and $Z$.

<theorem>
<src>Massoni, 2024</src>

Assume that at least one of $\xi_\pm$ is right, or $\xi_-$ and $\xi_+$ are transverse. Then there exists a foliation $\mathcal{F}$ that transverses to $Z$.

</theorem>

<definition>

If there exists a $Z$ which is volume preserving, then we say $(\xi_-, \xi_+)$ is **strongly right**.

</definition>

A corollary of the theorem is as follows:

<corollary>

$M\neq S^1\times S^2$ admits a taut foliation if and only if it admits a strongly tight contact pair.

</corollary>

## Sketch of Proof Idea 

Consider a vector field $X\subset \xi_- \cap \xi_+$ which vanishes exactly along 
$$
\Delta = \{ p\in M| \xi_-(p) = \xi_+(p)\}
$$

Consider $\xi_\pm^t= (\phi_x^t) \times \xi_\pm$.

<proposition>

There exists $\eta$ a continuous plane field such that $\xi_\pm^t$ converges to $\eta$.

</proposition>

<proposition>

The map $(\xi_-, \xi_+)\mapsto \eta$ is continuous.

</proposition>

<proposition>

For generic $(\xi_-,\xi_+)$, $\eta$ is locally integrable.

</proposition>

Warning: $\eta$ is only $C^0$, not always uniquely integrable tangent to the foliation. 

There is also the useful notion of branching foliation, which we will not define right now.

<proposition>

Assume that there is no immersed $\overline{D}\to M$ tangent to $\eta$ such that $\partial \overline{D}^2$ tangent to $X$. Then $\eta$ is tangent to a branching foliation.

</proposition>

<proposition>

$\eta$ is approximatable by integrable plane fields.

</proposition>

# Speculation 

Here is some speculation about the future of this area.Strongly tight pairs are hard to work with, but there are a few intruiging conjectures and problems to work on.

<conjecture>
<src>Massoni</src>

If $(\xi_-, \xi_+)$ is a positive pair and both $\xi_\pm$ are tight, then there exists a Reebless foliation.

</conjecture>

We want an intrinsic result on the isotopy classes of $\xi_-$ and $\xi_+$. 

<problem>

Consider a contact pair $(\xi_-, \xi_+)$, not necessarily positive. Assume they are both tight, they are homotopic as plane fields, and $\langle c(\xi_-), c(\xi_+) \rangle=1$. Then does there exist a Reeb-less foliation on $M$?

</problem>

The third condition is motivated by the following theorem: 

<theorem>
<src>Lin</src>

If $\mathcal{F}$ is a taut foliation, $\xi_\pm$ are contact approximations, 
$$
\langle c(\xi_-), c(\xi_+) \rangle=1 
$$
where $c$ is the contact invariant in $\text{HF}$.

</theorem>

Here is an application: 

<theorem>

Take $M^2 \neq S^1 \times S^2$, with $\mathcal{F}$ a taut foliation on $M$ and $K$ a transverse and framed knot. Then there exists $s_0$ such that for every $s\in \mathbb{Q}$ with $|s|\ge s_0$, there exists a a taut foliation on $M_k(s)$ transverse to $K'$ (image of $K$).

</theorem>