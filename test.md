<link href="whirlwind.css" rel="stylesheet">

<whirlheader>
    <p>pretzeledkoala</p>
    <p>whirlwind example</p>
    <p>june 29, 2024</p>
</whirlheader>

The goal is to survey some mathematical outcomes of the influential proposal of
Kapustin and Witten, and propose a stringy perspective.

It consists of two parts:
- Quantum Field Theory and Geometric Representation Theory
- String Theory and Geometric Representation Theory

We will mostly suppress technical aspects which involve derived algebraic geometry and BV formalism.

# What is QFT?

Quantum Field Theory (QFT) is, at its first approximation, the study of integrals, called **correlation functions**, of the form
$$
\int_{\phi \in \mathcal{\mathcal{E}}} e^{-S(\phi)} O_1(\phi) \cdots O_n(\phi) \, D\phi
$$
where $\mathcal{E}$ is a space, $D\phi$ is a volume element on $\mathcal{E}$, and $S, O_i : \mathcal{E} \to \mathbb{R}$ are functions.

The simplest example is as follows:

<example>

Consider $E = \mathbb{R}$ with Lebesgue measure $dx$ and a polynomial function
$S = f : \mathbb{R} \to \mathbb{R}$, for instance,
$$
\int_{\mathbb{R}} e^{-x^2 - x^4} x^n \, dx.
$$

</example>

Of course, this is not the ending, but rather the beginning. In fact, the input data should be realized in terms of 
1. (spacetime) a manifold $M$.
2. (space of fields) a space $\mathcal{E}=\mathcal{E}(M)$ of sections of a fiber bundle over $M$.
3. (actional functional) $S:\mathcal{E}\to \mathbb{R}$ a functional.

A **$d$-dimensional QFT** refers to this setting where $M$ is $d$-dimensional.

Let's see some examples of correlation functions:

<example>

1. The 2d $\mathcal{N}=(2,2)$ $\sigma$-modlel with target $X$, where $X$ is a Calabi Yau manifold: $M=\Sigma^2, \mathcal{E}\approx \{\text{maps }\Sigma \to X\}, S$ complicated.
2. The 3d CS theory with gauge group $G$, where $G$ is a simple lie group: $M=M^3, \mathcal{E}\approx \Omega^1(M;\mathcal{g})$, $S(A)=\int_{M^3} \text{Tr}(A\wedge \,dA + \frac{2}{3}A\wedge A \wedge A)$.
3. The 4d $\mathcal{N}=2$ theory with gauge group $G$: $M=M^4$, $\mathcal{E}\approx \{ G\text{-connections on }M^4\}, S$ complicated.

</example>

These correlation functions are very important in mathematics:
1. Leads to enumerative geometry and then mirror symmetry.
2. Leads to knot theory and then quantum topology 
3. Leads to 4-manifold theory and eventually (enriched) 4-manifold theory

<remark>

These theories depend only on (smooth) topology of $M$ and hence are called **topological QFT** (TQFT). A more general QFT has a lot more information but is too complicated to give nicely structured mathematical results as above.

</remark>

# QFT and GRT

As part of Geometric Langlands Theory amounts to the study of various objects where one can attach to a pair $(C,G)$, where $C$ is a Riemann surface and $G$ is a complex reductive Lie group, like $\text{GL}_n$. In particular, the Geometric Langlands Correspondence (GLC) is an equivalence of tow categories. We will discuss it soon.

<src>Kapustin, Witten, 2007</src> found a physical context for a version of GLC, again in terms of 4d TQFT on spacetime $M=\Sigma \times C$. Note that $C$ is a Riemann surface in Geometric Langlands Theory, which depends on the complex/algebraic structure of $C$. Hence, TQFT cannot possible capture the subtlety of Geometric Langlands Theory.

Let's discuss GLC. From now on, everything is over $\mathbb{C}$ unless otherwise specified. We need two inputs:
- a compact Riemann surface $C$
- a reductive group $G$ (e.g. $text{GL}_n$ or $\text{SL}_n$) and its Langlands dual group $\widecheck{G}$ (e.g. $\text{GL}_n$ or $\text{PGL}_n$).

The (global, unramified, de Rham, categorical) Geometric Langlands Correspondence <src>Beilinson, Drinfeld, 1990s</src> asserts an equivalence between two categories one can associate to $C$ and $G$. More precisely,

<conjecture>
<src>The Best Hope</src>

There is an equivalence of categories
$$
\text{D-mod}(\text{Bun}_G(C)) \simeq \text{QCoh}(\text{Flat}_{\widecheck{G}}(C)),
$$
where $\text{Bun}_G(C)$ is the moduli space of $G$-bundles on $C$ and $\text{Flat}_{\widecheck{G}}(C)$ is the moduli space of flat $\widecheck{G}$-bundles on $C$. D-mod stands for D-modules and QCoh stands for quasi-coherent sheaves.

</conjecture>

<remark>

1. Useful mnemonic: “category of bundles with flat connections on space of bundles” $\approx$ “category of bundles on space of bundles with flat connections”
2. The moduli spaces $\text{Loc}_{\widecheck{G}}(C)$ of local systems and $\text{Flat}_{\widecheck{G}}(C)$ of flat connections are NOT isomorphic as algebraic objects. This is very important to us: there is no intrinsic way to tell them apart in the current framework of physics!
3. As stated, the conjecture is known to be false as soon as $G$ is non-abelian. There is a modified version due to <src>Arinkin, Gaitsgory, 2015</src>

</remark>

## Survey of Results:

<src>Elliot, Yoo, 2015</src> develops a framework of (classical) field theory using derived algebreaic geometry (DAG). DAG is useful because it captures both topology and algebraic geometry in a single framework. In the original definition of a topological twist, translations $\frac{\partial}{\partial x_i}$ act trivially on a flat space $\mathbb{R}^4$, which is captured by having a **de Rham stack** $\chi_{dR}$.

1.  The mnemonic translates into having the derives stacks $\underline{\text{Map}}(C_B,G)_{dR}$ and $\underline{Map}(C_{dR}, \widecheck{G})$
2. We distinguish $\text{Loc}_{\widecheck{G}}:= \underline{\text{Map}}(C_B, \widecheck{G})$ and $\text{Flat}_G(C):=\underline{\text{Map}}(C_{dR}, \widecheck{G})$.

<src>Elliot, Yoo, 2017</src> discusses moduli of vacua and quantization in this framework. Remark 3 recovers the modified version of Arinkin and Gaitsgory. This paper obtains interesting new conjectures and prove special cases. It also has a major application in physics: this work has an interpretation in terms of D-brane configurations of string theory.

We can compare this to 4-manifold theory as an analogy:

|                         | 4-manifold                   | Geometric Langlands          |
|-------------------------|------------------------------|------------------------------|
| pioneering work         | <src>Donaldson, 1983</src>              | <src>Beilinson, Drinfelt, 1990s</src>    |
| physical context        | <src>Witten, 1988</src>                 | <src>Kapustin, Witten, 2007; Elliot, Yoo, 2015</src>             |
| physical development    | <src>Seiberg, Witten, 1994</src>         | <src>Kapustin, Witten, 2007; Elliot, Yoo, 2017</src>             |
| application to math     | <src>Witten, 1994</src>                 | <src>Elliot, Yoo, 2017</src>                     |

There are some further developments: 
- <src>Yoo</src> found a physical interpretation of other forms of Langlands duality including Feigin-Frenkel duality of $\mathcal{W}$-algebras, the Fundamental Local Equivalence, two geometric realizations of an affine Hecke category... These were used by <src>Frenkel, Gaiotto, 2020</src>, extending quantum geometric Langlands correspondence in terms of vertex algebras, and also used to formulate the Gaiotto Conjectures.
- <src>Gaiotto</src> developed a vertex algebra approach for better understanding various aspects of GLC.
- <src>Ben, Zvi, Nadler, 2018</src> developed Betti Geometric Langlands, taking the original TQFT perspective much more seriously.

The new framework can be applied to various other field theories. For instance, in the context of symplectic duality and 3d mirror symmetry:

<Image 1 />

This gives a categorification of the <src>Braverman-Finkelberg-Nakajima</src> construction, a new relationship between Langlands and symplectic duality, and <src>Hilburn, Raskin</src> proved the simple nontrivial case.

<remark>

An independent work of <src>Ben, Zvi, Sakellaridis, Venkatesh</src> applied <src>Gromov, Witten</src> to a more arithmetic setting to introduce Relative Langlands Program.

</remark>

# String Theory and GRT

## Towards S-duality
Based on <src>Raghavendran, Yoo</src>. In order to understand the physical context of GRT better, it is crucial to understand S-duality mathematically. What is S-duality?

A fundamental context to understand a physical duality is string theory. 

<definition>

S-duality is an action of $S\in \text{SL}_2(\mathbb{Z})$ on type IIB string theory compatible with
$$
\text{M}[S_M^1 \times S_r^1 \times M^9] \overset{\text{red}_M}{\underset{\simeq}{\longrightarrow}} \text{IIA}[S_r^1\times M^9] \overset{\textbf{T}}{\underset{\simeq}{\longrightarrow}} \text{IIB}[S_{1/r}^1\times M^9]
$$
where  $M$ stands for M-theory, IIA stands for type IIA superstring theory, and $\text{red}_M$ is an equivalence from the "fact" that a circle reduction of M-theory is equivalent to type IIA theory, T-duality $\textbf{T}$ is an equivalence between type II string theories, the $\text{SL}_2(\mathbb{Z})$ action on M-theory is on $S_M^1 \times S_r^1$, and $\text{SL}_2(\mathbb{Z})$-action on IIB string theory is transferred from the $\text{SL}_2(\mathbb{Z})$-action on M-theory through the equivalences.

</definition>

## Type IIB Superstring Theory

Let's briefly discuss Type IIB Superstring theory, which is usually done on a 10-manifold $M^{10}$. **D-brane gauge theory** for $D_{2k-1}$-branes wrapping on $N^{2k}\subset M^{10}$ is a $2k$-dimensional field theory, e.g. D3 branches on $\mathbb{R}^4 \subset \mathbb{R}^{10}$ yield 4d $\mathcal{N}=4$ SYM theory or D5 branes on $\mathbb{R}^6\subset \mathbb{R}^{10}$ yield 6d $\mathcal{N}=(1,1)$ SYM theory. **Closed string field theory** on $M^{10}$ is a field theory on $M^{10}$ describing string theory. In **open-closed coupling**, closed string state yields a deformation of D-brane gauge theory. The existence of $\text{SL}_2(\mathbb{Z})$ symmetry or $S$-duality is very important in all of these cases.

<problem>

How much can we capture mathematically?

</problem>

Answer: Most of it, for **twisted string theory**.

## (Extended) TQFT
Let's digress to TQFT:

<definition>

A $d$-dimensional TQFT is a symmetric monoidal functor 
$$
Z:(\underline{\text{Bord}}_d, \coprod)\to \left(\text{Vect}_{\mathbb{C}}, \otimes \right).
$$

Here, $(\text{Vec}_{\mathbb{C}}, \otimes)$ is a symmetric monoidal category of $\mathbb{C}$-vector spaces and $\underline{\text{Bord}}_d$ is a category where 
- an object is a closed $(d-1)$-manifold;
- a morphism is a cobordism up to diffeomorphism;
- the composition is a gluing of cobordisms 
- the monoidal structure is a disjoint union $\coprod$

</definition>

<theorem>

A 2d TQFT $Z$ is determined by a commutative Frobenius algebra $Z(S^1)=A$.

</theorem>

| morphism in $\text{Bord}_2$ | morphism in $\text{Vect}_{\mathbb{C}}$ |
|-----------------------------|----------------------------------------|
| $\varnothing \to S^1$       | $u: \mathbb{C} \to A$                  |
| $S^1 \to \varnothing$       | $\text{Tr}: A \to \mathbb{C}$          |
| $S^1 \sqcup S^1 \to S^1$    | $m: A \otimes A \to A$                 |
| $S^1 \to S^1 \sqcup S^1$    | $\Delta: A \to A \otimes A$            |

This is a (baby) (topological) string theory, where 
$$
Z(S^1)=A=(\text{the space of closed string states}).
$$

<problem>

Can we see an open string (interval) as well?

</problem>

We need to introduce an extended 2d QFT by going a little deeper:

<definition>

An **extended 2d TQFT** is a symmetric monoidal functor 
$$
Z:(\text{Bord}_2, \coprod)\to (\text{DGCat}_{\mathbb{C}}, \otimes).
$$

</definition>

For example,

| $\text{Bord}_2$                 | $\text{DGCat}_{\mathbb{C}}$          |
|---------------------------------|--------------------------------------|
| closed 2-manifold               | complex number                       |
| closed 1-manifold               | $\mathbb{C}$-vector space            |
| cobordism of 1-manifolds        | $\mathbb{C}$-linear map              |
| closed 0-manifold               | $\mathbb{C}$-linear category         |
| cobordism of 0-manifolds        | $\mathbb{C}$-linear functor          |

<theorem>
<src>Costello, Hopkins, Lurie</src>

An extended 2d TQFT $Z$ is determined by a Calabi-Yau category $Z(\text{pt})=\mathcal{C}$.

</theorem>

Once we have this, we have an answer to the question:
- $Z(\text{pt})=\mathcal{C}$ is the category of boundary conditions and $\text{Hom}_{\mathcal{C}}(\mathcal{B}_1, \mathcal{B}_2)$ is the space of open string states from $\mathcal{B}_1$ to $\mathcal{B}_2$.

By topological string theory, we mean such a 2d extended TQFT determined by a Calabi-Yau 5-category.

<example>

Let $X$ be a CY 5-fold with a non-vanishing holomorphic volume form $\Omega_X$.

$$
        \begin{array}{c|cc}
        & \text{A-model} & \text{B-model} \\
        \hline
        Z(\text{pt}) = \mathbb{C} & \text{Fuk}(X) & \text{Coh}(X) \\
        Z(S^1) = \text{HH}(\mathbb{C}) & \text{QH}(X) & \text{PV}(X)
        \end{array}
$$

Here $\text{PV}(X) = \bigoplus \text{PV}^{i,j}(X)$ where $\text{PV}^{i,j}(X) = \Omega^{0,j}(X, \wedge^i T_X)$ with a differential $\bar{\partial}: \text{PV}^{i,j} \to \text{PV}^{i,j+1}$. For future reference, note that using the isomorphism $(-) \vee \Omega_X: \text{PV}^{i,j}(X) \cong \Omega^{d-i,j}(X)$, one has $\bar{\partial}: \text{PV}^{i,j} \to \text{PV}^{i-1,j}$.

</example>

So when a physicist says type IIB string theory on $M^{10}$, a mathematician can think of the Calabi-Yau 5-category $\mathcal{C}$.

<example>

- $\mathcal{C}=\text{Coh}(X^5)$ for a CY 5-fold $X$.
- $\mathcal{C}=\text{Fuk}(T^*N)\otimes \text{Coh}(X^3)$ for a smooth 2-manifold $N$.

</example>

## D-brane Gauge Theory of String Theory
$\mathcal{C}$ is fixed. Physicists care about how open strings ending on branes $\mathcal{B}$ yield $D$-brane gauge theory.

When a physicist says D-brange gauge theory on $N^{2k} \subset M^{10}$, a mathematician should think of $\mathcal{E}=\mathbb{R}\text{End}_{\mathbb{C}}(\mathcal{B})[1]$. To do this, a DG category $\mathcal{C}$ is associative and hence a Lie structure on $\mathbb{R}\text{End}_{\mathbb{C}}(\mathcal{B})$, and a CY category $\mathcal{C}$ is a shifted symplectic structure on $\mathbb{R}\text{End}_{\mathcal{C}}(\mathcal{B})[1]$.

<example>

| $\mathcal{C}$                                    | $\text{Coh}(C^5)$                                            | $\text{Fuk}(\mathbb{R}^4) \otimes \text{Coh}(C^3)$                            |
|--------------------------------------|-------------------------------------------------------|---------------------------------------------------------------------|
| branes | D3's on $C^2 \subset C^5$                             | D3's on $\mathbb{R}^2 \times C \subset \mathbb{R}^4 \times C^3$    |
| $\mathcal{E}$                    | $\mathcal{E}_{D3}^{\text{Hol}}(C^2) := \Omega^{0,\bullet}(C^2)[-1,\varepsilon_2,\varepsilon_3][1]$ | $\mathcal{E}_{D3}^{\text{HT}}(\mathbb{R}^2 \times C) := \Omega^{\bullet}(\mathbb{R}^2) \otimes \Omega^{0,\bullet}(C)[-1,\varepsilon_2][1]$ |
| name                             | holomorphic twist of 4d $\mathcal{N} = 4$ theory     | holomorphic-topological twist of 4d $\mathcal{N} = 4$ theory        |

</example>

## Closed String Field Theory of String Theory 
Again, $\mathcal{C}$ is fixed. Recall that $Z(S^1)$ is the space of closed string states, but note that: 
- Physics: The worldsheet theory, being coupled with gravity theory, should be invariant under $\text{Diff}(S^1)$. This motivates $Z(S^1)^{S^1}$.
- Mathematics: $Z(S^1)=\text{HH}(\mathcal{C})$ admits an $S^1$-action which corresponds to so-called Connes' $B$ operator, so $Z(S^1)^{S_1} = \text{Cyc}(\mathcal{C})$.

When a physicist says closed string field theory on $M^{10}$, a mathematician can think of $\mathcal{E}=\text{Cyc}^{\bullet}(\mathcal{C})[2]$.

<example>

<src>Bershadsky, Cecotti, Ooguri, Vafa; Costello, Li</src>

If $\mathcal{C}=\text{Coh}(X^5)$, then $Z(S^1)\cong \text{PV}(X)$ and $B=\partial$. Hence the corresponding closed string field theory is given by $(\ker \partial \subset \text{PV}(X)[2], \overline{\partial})$ or $\mathcal{E}_{\text{BCOV}}(X)=(\text{PV}(X) \llbracket t \rrbracket [2], \overline{\partial}+t\partial )$.

</example>

## Coupling of Open and Closed Sectors

The last ingredient we mention is that when a physicist says coupling of closed string field theory and D-brane gauge theory, a mathematician can think of a closed-open map $\text{CO}:\text{Cyc}^{\bullet}(\mathcal{C})[1] \to \text{Cyc}^{\bullet}(\mathbb{R}\text{End}(\mathcal{B}))[1]$. Physically, a closed string state $\alpha \in \text{Cyc}^\bullet(\mathcal{C})$ gives a deformation of D-brane gauge theory given by $\mathbb{R}\text{End}_\mathcal{C}(\mathcal{B})$.

<example>

| $\mathcal{C}$ | $\text{Coh}(C^5)$ | $\text{Fuk}(\mathbb{R}^4) \otimes \text{Coh}(C^3)$ |
|---------------|-------------------|--------------------------------------------------|
| $\mathcal{B}$ | $C^2_z \subset C^5_{z_i,w_j}$ | $\mathbb{R}^2 \times C_z \subset \mathbb{R}^4 \times C^3_{z,w_j}$ |
| $\mathcal{E}$ | $\mathcal{E}_{D3}^{\text{Hol}}(C^2_z) = \Omega^{0,\bullet}(C^2_z)[-1,\varepsilon_2,\varepsilon_3][1] \simeq \mathcal{O}(C^2_z)[-1,\varepsilon_2,\varepsilon_3][1]$ | $\mathcal{E}_{D3}^{\text{HT}}(\mathbb{R}^2 \times C_z) = \Omega^{\bullet}(\mathbb{R}^2) \otimes \Omega^{0,\bullet}(C_z)[-1,\varepsilon_2][1] \simeq \mathcal{O}(C_z)[-1,\varepsilon_2][1]$ |
| CO | $\text{PV}(C^5_{z_i,w_j}) \to \text{HH}(\mathcal{O}(C^2_z)[-\varepsilon_j])$ | $\text{PV}(C^3_{z,w_j}) \to \text{HH}(\mathcal{O}(C_z)[-\varepsilon_j])$ |
|    | $z_i, \partial_{z_i}, w_j, \partial_{w_j} \mapsto z_i, \partial_{z_i}, \partial_{\varepsilon_j}, \varepsilon_j$ | $z, \partial_z, w_j, \partial_{w_j} \mapsto z, \partial_z, \partial_{\varepsilon_j}, \varepsilon_j$ |

</example>

## S-Duality
Recall
$$
\text{SL}_2(\mathbb{Z})=\langle S=\begin{pmatrix}
0 & -1 \\ 1 & 0
\end{pmatrix}, T=\begin{pmatrix}
1 & 1 \\ 0 ^ 1
\end{pmatrix} \mid S^4=1, (ST)^3=S^2
 \rangle
$$

<theorem>
<src>Raghavendran, Yoo</src>

Let $(X, \Omega_X)$ be a CY 3-fold. There exists an action of $SL_2(\mathbb{Z})$ on $\mathcal{E}_m(X) = \text{PV}^{0,\bullet}(X)[2] \oplus (\text{PV}^{1,\bullet}(X)[1] \to t \text{PV}^{0,\bullet}(X)) \oplus \text{PV}^{3,\bullet}(X)$ that is compatible with the physics expectations.

</theorem>

At the level of cohomology, it is
$$
S \mapsto \begin{pmatrix}
 & -(-) \vee \Omega_X & \\
 & \text{Id} & \\
(-) \wedge \Omega_X^{-1} & & 
\end{pmatrix}, \quad
T \mapsto \begin{pmatrix}
\text{Id} & (-) \vee \Omega_X & \\
 & \text{Id} & \\
 & & \text{Id}
\end{pmatrix}.
$$

For instance,
$$
\begin{align*}
\alpha \in \text{PV}^0_{\text{hol}}(X) &\rightsquigarrow S(\alpha) = \alpha \wedge \Omega_X^{-1} \in \text{PV}^3_{\text{hol}}(X) \\
\gamma \in \text{PV}^3_{\text{hol}}(X) &\rightsquigarrow S(\gamma) = -\gamma \vee \Omega_X \in \text{PV}^0_{\text{hol}}(X)
\end{align*}
$$

## Twisted String Theory
To summarize twisted string theory, S-duality is a duality of type IIB string theory, and we construct the S-duality operation on a sector of string theory. Our interest in duality between D-brane gauge theories, or more precisely, deformations of D-brane gauge theory. Closed-open map yields S-duality of deformations of D-brane gauge theories.

From now on, we let $\mathcal{C}=\text{Fuk}(\mathbb{R}^4) \otimes \text{Coh}(\mathbb{C}^3)$ and consider $N$ D3 branes on $\mathbb{R}^2 \times \mathbb{C}_z \subset \mathbb{R}^4 \times \mathbb{C}_{z,w_1,w_2}^3$ to get $\mathcal{E}_{\text{D3}}^{\text{HT}}(\mathbb{R}^2\times \mathbb{C}_z)=\Omega^\bullet(\mathbb{R}^2)\otimes \Omega^{0,\bullet}(\mathbb{C})[\varepsilon_1, \varepsilon_2]\otimes \mathfrak{gl}_N[1]$. Then for 
<Image 2>
we compare deformations of HT twist by $F\in \tilde{\mathcal{E}}_m$ and its S-dual element $S(F)$.

## Applications of S-duality

### Geometric Langlands
$F=w_1$. S-duality gives a duality between two deformations $\partial_{\varepsilon_1}\leftrightarrow \varepsilon_2 \partial_z$, precisely the deformations $(\text{B}, \text{Higgs}_G(C)) \overset{\partial \varepsilon_1}{\to} (\text{B}, \text{Bun}_G(C)_{\text{dR}})$ and $(\text{B}, \text{Higgs}_G(C)) \overset{\varepsilon_2 \partial_z}{\to} (\text{B}, \text{Flat}_G(C))$. S-duality would yield $\text{D}(\text{Bun}_G(C))\simeq \text{QCoh}(\text{Flat}_G(C))$ for $G=\text{GL}_n$. Moreover, one also obtains Quantum Geometric Langlands Correspondence in a simpler way.

### S-Duality Between Superconformal Deformations $F=zw_2$

|   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|
|   |   $u$   |   $v$   |   $z$   |   $w_1$  |   $w_2$  |
| K D5 |   | $\times$ | $\times$ |   | $\times$ | $\times$ | $\times$ | $\times$ |   |   |
| N D3 | $\times$ | $\times$ |   |   | $\times$ | $\times$ |   |   |   |   |

S-duality gives a duality between two deformations

$(1)\ z\partial_{e_2} \leftrightarrow (2)\ \partial_{w_1}(w_2\partial_{w_2} - z\partial_z)$.

1. The deformation $z\partial_{e_2}$ turns HT twist of 6d $\mathcal{N} = (1,1)$ theory to 4d CS theory on $\mathbb{R}^2 \times \mathbb{C}_{w_1}$ <src>Costello, Yagi</src>: it follows from

   $\Omega^{0,\bullet}(\mathbb{C}_{w_1}) \otimes (\Omega^{0,\bullet}(\mathbb{C}_z)_{e_2} \xrightarrow{z\partial_{e_2}} \Omega^{0,\bullet}(\mathbb{C}_z)) \cong \Omega^{0,\bullet}(\mathbb{C}_{w_1})$

   One has (truncated) Yangian of $\mathfrak{gl}(K)$ on the 1d defect.

2. The deformation $S(zw_2) = \partial_{w_1}(w_2\partial_{w_2} - z\partial_z)$ can be understood as 3d $\mathcal{N} = 4$ theory configuration, where the Yangian is expected to arise as the quantized Coulomb branch algebra.

### New Examples of S-dual Theories: $F=w_1w_2$

S-duality gives a duality between two deformations

$$
\partial_{\varepsilon_1}\partial_{\varepsilon_2} \leftrightarrow \pi = \partial_{\varepsilon_1}\partial_z\varepsilon_1 - \partial_{\varepsilon_2}\partial_z\varepsilon_2. 
$$

1. As $(C[\varepsilon_1, \varepsilon_2], \partial_{\varepsilon_1}\partial_{\varepsilon_2})$ is Clifford algebra $Cl(C^2) \cong \text{End}(C^{1|1})$, the element $\partial_{\varepsilon_1}\partial_{\varepsilon_2}$ deforms

   $\Omega^\bullet(\mathbb{R}^2) \otimes \Omega^{0,\bullet}(C)[\varepsilon_1, \varepsilon_2] \otimes \mathfrak{gl}_N[1] \rightsquigarrow \Omega^\bullet(\mathbb{R}^2) \otimes \Omega^{0,\bullet}(C) \otimes \mathfrak{gl}_{N|N}[1]$,

   yielding 4d CS theory with $GL_{N|N}$. The category $\mathcal{L}_{GL(N|N)}$ of line defects of 4d CS theory is known, in terms of modules over Yangian, quantum affine algebra, and elliptic quantum group for $C = \mathbb{C}, \mathbb{C}^\times$, and $E$, respectively.

2. The element $\pi$ gives a particular deformation

   $\text{Coh}(\text{Higgs}_G(C)) \rightsquigarrow \text{Coh}(\text{Higgs}_G(C), \pi)$

   where $\text{Coh}(\text{Higgs}_G(C), \pi)$ is expected to be expressed in terms of certain difference modules.

<conjecture>
<src>The Meta Conjecture</src>

The monoidal category $\mathcal{L}_{GL(N|N)}$ acts on $\text{Coh}(\text{Higgs}_{GL_N}(C), \pi)$.

</conjecture>

# Summary 
Quantum Field Theory has been incredibly useful in discovering new mathematical conjectures and results in several fields of mathematics. Kapustin and Witten made a pioneering proposal, suggesting a profound relationship between Quantum Field Theory and Geometric Langlands Theory. A new mathematical framework of physics, which can capture the algebraic structure of spacetime, was developed. This framework has been used to discover many new mathematical conjectures and results. A new framework for aspects of string theory and duality is currently being developed, and this framework is expected to be used to discover many new mathematical conjectures and results.