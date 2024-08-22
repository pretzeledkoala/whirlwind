<link href="../whirlwind.css" rel="stylesheet">

<whirlheader>
    <p>Gary</p>
    <p>Pieloch</p>
    <p>August 19</p>
</whirlheader>

# Spectral Equivalence of Nearby Lagrangians 

Joint work with Johan Asplund and Yash Deshmukh.

<theorem>
<src>Abouzaid</src>

Let $L\subset T^* Q$ be exact, equipped with a choice of rank 1 local system $L$ equivalent in the wrapped Fukaya category $W(T^* Q, \mathbb{Z})$ to the zero section, with some choice of rank 1 local system.

</theorem>

Notation: Let $R$ be a commutative ring spectrum. 

<remark>

A spectrum is morally something that functions like a space. It's a bit more complicated, but this complication allows us to do more algebraic operations. There spectrum also allow us to define more homology theories. An each one of these, can be realized using the language of spectrum. For example, we can take 
$$
\pi_*(M\wedge R) = H_*(M, \mathbb{R}).
$$
If welet $R=HK$, then we have $H_*(M;K)$. If we let $R=\text{MO}$, then we get $\Omega_*^{\text{MO}}(M)$

</remark>

<theorem>

Let $L\subset T^*Q$ be a nearby Lagrangian with an $R$-brane. In $W(T^*Q, \mathbb{R})$, $L$ is equivalent to an $R$-brane on the zero section.

</theorem>

Here is one application of this theorem:

<theorem>

Let $X$ be a subcritical Weinstein domain with $c_1(X)=0=c_2(X)$. Let $\Lambda \subseteq \partial X$ be a Legendrian unknot, with standard filling $C$. Fix a Lagrangian $L\subseteq X$ that is an exact filling of $\Lambda$. $L$ is homotopic to $C$ with $\Lambda$ fixed in $X/X_{n-2} = \bigvee S^{n-1}$. 

</theorem>

<definition>

1. Consider $W(X, \mathbb{Q})$ where objects are the exact canonical Maslaw Lagrangians with rank 1 local systems and the morphisms are chain complexes built from $M(\between)$.
2. $W(X, \mathbb{R})$ are where objects are the exact canonical Maslaw Lagrangians with rank 1 local systems R-branes. And morphisms are $R$-module spectra built from $M(\between)$. 

</definition>

<definition>

A vector bundle $\mathcal{E}\to \mathcal{B}$ is **$R$-orientable** if 
$$
\mathcal{B}\stackrel{\mathcal{E}}{\longrightarrow} \text{BO} \longrightarrow \text{BGL}()\longrightarrow \text{BGL}(\mathbb{R})
$$
is null.

</definition>

<example>

Let $\mathbb{R}= H \mathbb{Z}$, 
$$
B\to \text{BO} \to \text{BGL}(H \mathbb{Z}) = B\text{Aut}(\mathbb{Z})=B\mathbb{Z}/2
$$
and $W_1$ is this entire map.

</example>

Assume that $X$ be a symplectically trivializable space, meaning $TX=\mathbb{C}\otimes \mathbb{R}^n$. 

<definition>

Given $L\subset X$ a Lagrangian, $GL : L\to \mathcal{U}/O$ to be the Lagrangian Grassmannian

</definition>

<definition>

An $R$-brane is a choice of null-homotopy of
$$
L\stackrel{\text{GL}}{\longrightarrow} \mathcal{U}/O \stackrel{\text{Bott}}{\longrightarrow} B^2(0) \longrightarrow B^2 \text{GL}_1(R).
$$

</definition>

<remark>

1. $R$-branes correspond to $[L, B \text{GL}_1(R)]$ which are rank 1 local systems. 
2. $R=H\mathbb{Z}, [L, B\text{GL}_1(H\mathbb{Z})] = [L, B\mathbb{Z}/2 ]$ are rank 1 local systems. 
3. Let $M_L=\{(D, \partial D) \to (X,L)| \overline{\partial} u=0, \text{ based} \}$. We want 
$$
\text{add this diagram later}
$$
<!-- \[\begin{tikzcd}
	{\mathcal{M}_L} & BO & {BGL_1(R)} \\
	{\Omega L} & {\Omega \mathcal{U}/O}
	\arrow["{T\mathcal{M}_L}", from=1-1, to=1-2]
	\arrow[from=1-1, to=2-1]
	\arrow[from=1-2, to=1-3]
	\arrow["{*}"', shift right, curve={height=30pt}, from=2-1, to=1-3]
	\arrow["{\Omega G_L}"', from=2-1, to=2-2]
	\arrow["{\text{Bott Periodicity}}"', from=2-2, to=1-2]
\end{tikzcd}\] -->

</remark>

<proposition>

1. We have
$$
\text{Mor}(L, L)=\text{HW}(L, L, \mathbb{R})= L \wedge R
$$
2. For $L$ compact, we have
$$
\pi_*(\text{HW}(L, K, R)) \in \text{Ab} \\
\pi_*(\text{HW}(L, L, R)) = H_*(L, R)
$$
3. Change of coefficients: consider $S$ a module over $R$. Then we have 
    $$
    W(X, S) = W(X,R) \wedge_R S
    $$

</proposition>

Notation:
1. $R$ is connective 
2. $\pi_0(R)=K$ is discrete 
3. The Hurwitz map $\text{Hw}: R\to \text{HK}$ that is $\mathbb{1}$ on $\pi_0$. 

<proposition>

Let $M, M'$ be connected $R$-module spectra. 
1. Let 
    $$\pi_*(M\wedge_R \text{HK}) = \begin{cases} K & *=0 \\ 0 & \text{else} \end{cases}
    $$
    Then $M=R$.
2. If 
INSERT THIS LATER
    <!-- \[\begin{tikzcd}
	M && {M'} \\
	\\
	{M\wedge_R \text{HK}} && {M' \wedge_R \text{HK}}
	\arrow["f", from=1-1, to=1-3]
	\arrow["{\text{H}_W}", from=1-1, to=3-1]
	\arrow["{\text{H}_W}", from=1-3, to=3-3]
	\arrow["{H_n(f)}"', from=3-1, to=3-3]
    \end{tikzcd}\] -->
    then $\text{Hw}(f)$ are equiv implies $f$ is an equiv.

</proposition>

<proof>

We have 
1. $\text{HW}(\text{Fib}=F, F, R)=\Omega Q \wedge R$.
2. $\text{HW}(F,L, R) =R$.
3. FIX THIS LATER
    <!-- \[\begin{tikzcd}
        {\text{HW}(F, F)\wedge_R \text{HW}(F, L)} && {\text{HW}(F,L)} \\
        \\
        {\Omega Q \wedge R} && R
        \arrow["{\mu^2}", from=1-1, to=1-3]
        \arrow[from=1-1, to=3-1]
        \arrow[from=1-3, to=3-3]
        \arrow[from=3-1, to=3-3]
    \end{tikzcd}\] -->
    which implies that $\text{HW}(F,L) \leftrightarrow Q \to \text{BGL}_1(R) \leftrightarrow $ rank 1 local system on $Q$.

4. Every such local system is realized by $\text{HW}(G, Q^\#)$ where $Q^{\#}$ is some $R$-brane.

5. FIX THIS DIAGRAM LATER
    <!-- \[\begin{tikzcd}
	{\text{HW}(L, Q^\#)} & {} && {F_{\Omega Q \wedge R}(R, R)} \\
	\\
	{\text{HW}(L, Q)\wedge_R \text{HK}} \\
	{\text{HW}(L,Q,K)} & {} && {F_{\Omega Q \wedge HK}(\text{HK}, \text{HK})}
	\arrow[from=1-1, to=1-4]
	\arrow["{\text{H}_W}"', from=1-1, to=3-1]
	\arrow["{\text{H}_W}", from=1-4, to=4-4]
	\arrow["{=}"{description}, draw=none, from=3-1, to=4-1]
	\arrow["\cong"', from=4-1, to=4-4]
	\arrow[from=4-2, to=1-2]
    \end{tikzcd}\] -->

</proof>

Recall that $X$ is a subcritical Weinstein $c_1(X)=0=a(X)$, $\dim_{\mathbb{C}}X\ge 4$, $\Lambda \subset \partial X$ the unknown with standard filling $C$, $L\subset X$ an exact filling of $L$ (where $L=\mathbb{D}^n$).

<proposition>

It suffices to show that $[L \cup_\Lambda C] =0 \in \tilde{\Omega}^{\text{spin}}_n (X) = \tilde{H}_X(X, \mathcal{M}\text{Spin})$ 

</proposition>

<proof>

1. It suffices to show that $L\cup_\Lambda C \cong S^n \implies X/X_{n-?} \simeq V$ where $S^{n-1}$ is based null.
2. $\mathbb{Z}/2 \cong \pi_n(S^{n-1}) \to \tilde{\Omega}_n^{\text{spin}} (S^{n-1}) \stackrel{\cong}{\longrightarrow} \Omega_1^{\text{spin}}(\text{pt})\subset \Omega_1^{\text{spin}} \mathbb{Z}/2$
    which is an isomorphism by Pontryagin-Thorn.
3. If $X/X_{n-2} \simeq S^{n-1}$, then the claim holds.
4. If $X/X_{n-2} = \vee S^{n-2}$, then the claim holds by the Milnor-Hilton argument.

</proof>

INSERT DIAGRAM HERE LATER

where $\hat{X}=X\cup_\Lambda H^n, \hat{L}=L, \hat{C}= c \subset U_n$ (the core of $H^n$) 
<!-- IDK WHATS GOING ON HERE FIX THIS LATER -->

<proposition>

We want to show that $[\hat{L}]=[\hat{C}]\in \tilde{\Omega}^{\text{spin}}(\hat{X})$. 

</proposition>

<proof>

$f:\hat{X}\to X$ such that $\hat{f}(\hat{L}) = [L\cup_\Lambda C]$. We have $0=f(\hat{C})\in \text{Im}(B^{2n})$.

</proof>

<proof>

1. The obstruction to $M\text{Spin}$-brane is cohomology. But we can take $\pi_1(L)=0, w_2(L)=0, H_3(L, \mathbb{Z}/2)=0$

2. $\hat{X}=\text{subcritical handles} \cup T^*S^n \implies W(\hat{X}, R) \cong W(T^*S^n, R)$.
3. Similarly, $\hat{L}\cong \hat{C}$ in $W(\hat{W}, R)$.
4. $\text{HW}(L, L, R)\to H_n(\hat{X}, R) =\Omega_n^{\text{spin}}(\hat{X})$.

</proof>