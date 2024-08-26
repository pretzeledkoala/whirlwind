<link href="../whirlwind.css" rel="stylesheet">

<whirlheader>
    <p>Gary</p>
    <p>Massoni</p>
    <p>August 21</p>
</whirlheader>

# (Symplectic) Khovanov Homology

Khovanov homology takes a link $L\subseteq S^3$ and gives back $\text{Kh}(L)$, a bigraded vector space over some field with $\chi$ the Jones polynomial. 

<theorem>
<src>Ozswatch, Szabé</src>

There exists a spectral sequence 
$$
\widehat{\text{Kh}}(L; \mathbb{F}_2)\rightrightarrows \widehat{\text{HF}}(\Sigma(\overline{L}))
$$

</theorem>

Here is the Floer theory analogy:
- $(M,\omega)$ are exact, $\omega = d\lambda$, and convex at $\infty$
- $L_0, L_1$ are exact compact Lagrangians satisfying $\lambda|_{L_i}=df_i$
- $(M, L_0,L_1)\rightsquigarrow \text{CF}(M, L_0,L_1) = (\mathbb{F} \langle L_1 \text{ transverses }L_1 \rangle, \partial)$.

Let's briefly discuss symplectic Khovanov homology. 

Take $p = \prod_{i=1}^n (z - k_i)$ and consider:
$$
\left\{ u^2 + v^2 + p(z) = 0 : (u, v, z) \in \mathbb{C}^3 \right\}.
$$

Define $\Sigma_{\beta_L}$ as:
$$
\left\{ (u, v, z) : z \in B_i, u, v \in \sqrt{-p(z)} \mathbb{R} \right\}.
$$

Let $\mathcal{Y}_n \subseteq \text{Hilb}^n(S) \xrightarrow{\text{Hilbert-Chow}} \text{Sym}^n(S)$ be 1-to-1 away from the diagonal.

Define $\Sigma_A = \Sigma_{A_1} + \cdots + \Sigma_{A_n}$ and $\Sigma_B = \Sigma_{B_1} + \cdots + \Sigma_{B_n} \subseteq \text{Sym}^n(S) \setminus \Delta \subseteq \mathcal{Y}_n \subseteq \text{Hilb}^n(S)$, where
$$
\mathcal{Y}_n = \text{HC}^{-1}\left\{ (u_1, v_1, z_1), \ldots, (u_n, v_n, z_n) : z_i = z_j \implies (u_i, v_i) = (u_j, v_j) \right\}.
$$

Then, we have the following definition:

<definition>

$$
\text{Kh}_{\text{symp}}(L) = \text{HF}(\Sigma_A, \Sigma_B).
$$

</definition>

<theorem>
<src>Abouzaid, Smith</src>

Over characteristic 0, $\text{Kh}(K)=\text{Kh}_{\text{symp}}(K)$.

</theorem>

Since $O(2)$ acts on $(u,v)$, we have an action on $S$ and thus a symplectic action on $(\mathcal{Y}_n, \Sigma_A, \Sigma_B)$.

Let's briefly digress to discuss $\mathbb{F}_2$-actions:

<example>
<src>Smith, Borel</src>

Consider $\tau$ acting on $X$ satisfying $\tau^2 = \text{Id}$, a fixed set $X^{\text{Fix}}$. Then there is a spectral sequence 
$$
\begin{align*}
H^*(x; \mathbb{F}_2)\otimes \mathbb{F}_2 \left[\theta, \theta^{-1}\right] &\rightrightarrows \theta^{-1} H_{\mathbb{Z}/2\mathbb{Z}}(X; \mathbb{F}_2) \\
& \simeq H^* (X^{\text{fix}}; \mathbb{F}_2)\otimes \mathbb{F}\left[\theta, \theta^{-1}\right]
\end{align*}
$$
where 
$$\mathbb{F}_2\left[\theta, \theta^{-1}\right] = \theta^{-1}H^*(\theta \mathbb{Z}_2; \mathbb{F}_2)
$$
and 
$$
\theta^{-1} H_{\mathbb{Z}/2\mathbb{Z}}(X; \mathbb{F}_2) = \text{Ext}_{\mathbb{F}_2\left[\mathbb{Z}_2 \right]}(C_*(X), \mathbb{F}_2)
$$

</example>

<example>
<src>Seidel, Smith, 2010</src>

Given $\tau$ acting on $(M,L_0, L_1)$ with $\tau^2 = \text{Id}, \tau^*\omega = \omega, \tau(L_i)=L_i$. Take $(M^{\text{Fix}},L_0^{\text{Fix}}, L_1^{\text{Fix}})$. Then
$$
\text{HF}(M, L_0, L_1)\otimes F_2[\theta, \theta^{-1}]\rightrightarrows \text{HF}(M^{\text{Fix}},L_0^{\text{Fix}}, L_1^{\text{Fix}})\otimes \mathbb{F}_2 [\theta, \theta^{-1}]
$$

</example>

The intrinsic symmetry is $(u,v,z)\to (u, -v,z)$.

<theorem>
<src>Manelescu</src>

Consider 

$$
\mathcal{Y}_n^{\text{Fix}}=\text{Sym}^n(\Sigma-\{ \vec{z} \})\backslash \nabla \\

\Sigma_A^{\text{Fix}}=\alpha_1\times ....\times \alpha_n\\

\Sigma_B^{\text{Fix}}=\beta_1\times ....\times \beta_n
$$

Then 
$$
\text{Kh}_{\text{symp}}(L)\otimes \mathbb{F}_2[\theta, \theta^{-1}]\rightrightarrows g\widehat{\text{HF}}(\Sigma (\overline{L})\otimes H_*(S^1))\otimes \mathbb{F}_2[\theta, \theta^{-1}]
$$

$$
\widehat{\text{HF}}(\Sigma(\overline{L}))\times H_*(S^1)\otimes \mathbb{F}_2[\theta, \theta^{-1}]
$$

</theorem>

## Extrinsic Symmetries 

For a link $L$, we have $\mathcal{S}, \mathcal{Y}_n$. Do the same for $\overline{L}$. $\tau: (u,v,z)\mapsto (u,v,-z)$. $S/\tau =\overline{S}, z\mapsto z^2$.

Let $\text{Hilb}$ be the Hilbert scheme.

<theorem>

The following commutative diagram commutes:
\[\begin{tikzcd}
	{\text{Hilb}^{n/2}\left(\overline{S}\right)} && {\text{Hilb}^n(S)} \\
	\\
	{\text{Sym}^{n/2}\left(\overline{S}\right)} && {\text{Sym}^n(S)} \\
	{(u,v,z)} && {\left\{ (u,v,-\sqrt{z}), (u,v,-\sqrt{z})\right\}}
	\arrow[hook, from=1-1, to=1-3]
	\arrow["{\text{HC}}"', from=1-1, to=3-1]
	\arrow["{\text{HC}}", from=1-3, to=3-3]
	\arrow[hook, from=3-1, to=3-3]
	\arrow[maps to, from=4-1, to=4-3]
\end{tikzcd}\]

where $\tau$ acts on $\text{Hilb}^n(S)$ and $\text{Sym}^n(S)$.

</theorem>

<theorem>
<src>Seidel, Smith</src>

$$
\text{Kh}_{\text{symp}}(L)\otimes \mathbb{F}_2[\theta, \theta^{-1}]\rightrightarrows \text{Kh}_{\text{symp}}(\overline{L})\otimes \mathbb{F}_2[\theta, \theta^{-1}]
$$

</theorem>

<theorem>
<src>Stoffregen, Zhang, 2018; Borodzik, Politarcyzk, Silvero</src>

$$
\text{Kh}(L)\otimes \mathbb{F}_2[\theta, \theta^{-1}]\rightrightarrows \text{AKh}(\overline{L})\otimes \mathbb{F}[\theta, \theta^{-1}].
$$

</theorem>

# Annular (Symplectic) Khovanov Homology 

Following the works of <src>Asaeda; Przytycki, Sikora; Roberts</src>. $\text{AKh}$ is an associated graded ring of an annular filtration.

<theorem>
<src>Mak, Smith, 2019</src>

Over characteristic $0$,
$$
\text{AKh}_{\text{symp}}^{HH}(L)\simeq \text{AKh}(L)
$$
where $HH$ is the Hochschild homology.

</theorem>

Now, we present a new $\text{AKh}_{\text{symp}}$. Replace $\text{Hilb}^n(S)$ with $\text{Hilb}^n(S\backslash \pi^{-1}(0))$, deleting a divisor over $0$.

<theorem>
<src>Hendricks, Mak, Raghunath</src>

$\text{AKh}_{\text{symp}}(L)$ is a link invariant.

</theorem>

<conjecture>

Over characteristic 0, it is the same as $\text{AKh}_{\text{symp}}^{HH}(L)$.

</conjecture>

## Intrinsic 

We have the following intrisic cases: 
- $(u,v,z)\mapsto (u,-v,z)$
$$
\begin{align*}
\text{AKh}_{\text{symp}}(L)\otimes \mathbb{F}_2[\theta, \theta^{-1}] & \rightrightarrows g\widehat{CFK}(\Sigma(mL), \tilde{A})\otimes H_*(S^1) \otimes \mathbb{F}_2[\theta, \theta^{-1}]  \\
& \rightrightarrows \widehat{CFK}(\Sigma(mL), \tilde{A})\otimes H_*(S^1) \otimes \mathbb{F}_2[\theta, \theta^{-1}]
\end{align*}
$$
- $(u,v,z)\mapsto (u,v,-z)$
$$
\text{AKh}_{\text{symp}}(L)\otimes \mathbb{F}_2[\theta, \theta^{-1}]\rightrightarrows \text{AKh}_{\text{symp}}(\overline{L})\otimes \mathbb{F}_2[\theta, \theta^{-1}]
$$
- $(u,v,z)\mapsto (-u,-v, -z)$: start with the original theory and do not delete a divisor. 
- $\{ (u,v,z), (-u, -v, -z)\}$:
$$
\text{Kh}_{\text{symp}}(L)\otimes \mathbb{F}_2[\theta, \theta^{-1}]\rightrightarrows \text{AKh}_{\text{symp}}(\overline{L})\otimes \mathbb{F}_2[\theta, \theta^{-1}].
$$

# The Table 

