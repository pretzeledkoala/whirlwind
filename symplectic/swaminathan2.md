<link href="../whirlwind.css" rel="stylesheet">

<whirlheader>
    <p>Gary</p>
    <p>Cylindrical Contact Homology in Dimension Three via Obstruction Bundle Gluing</p>
    <p>August 20</p>
</whirlheader>

# Global Kuranishi Charts and Equivalence

<definition>

Given $\overline{\mathcal{M}}$ a compact Hausdorff space, a **global Kuranishi chart of virtual dimension $d$** for $\overline{\mathcal{M}}$ consists of 
- A finite dimensional topological manifold $\mathcal{T}$, called the **thickening**
- A finite rank vector bundle on $\mathcal{E}\to \mathcal{T}$, called the **obstruction bundle**
- A section $S: \mathcal{T}\to \mathcal{E}$, called the **obstruction section**
- A compact Lie group $G$ which acts on $s^{-1}: \mathcal{E}\to \mathcal{T}$ such that the action of $G$ on $\mathcal{T}$ has finite stabilizers (and these stabilizers act linearly in suitable local coordinates), satisfying $\dim \mathcal{T}= d+ \text{rank} \mathcal{E} - \dim G$, called the **symmetry group**
- A homeomorphism $s^{-1}(0)/G \stackrel{\sim}{\longrightarrow} \overline{\mathcal{M}}$, called the **footprint map**

</definition>

Why do we allow infinite $G$? It turns out allowing finite groups is not flexible enough. For example, if we take $\mathbb{CP}^1$ and consider a disk $\mathbb{D}$ at the origin with a $\mathbb{Z}/2$ action, we need infinite $G$. 

On the other hand, our current condition is sufficient: Every effective orbifold is a global quotient $\mathcal{M}/G$ for some orbifold $M$ quotiented by a Lie group $G$.

We want to study orientations on 
- $\mathcal{T}, \mathcal{E}$ preserved by $G$
- $\mathfrak{g}=\text{Lie}(G)$

which together induce a virtual fundamental class for $\overline{\mathcal{M}}$:

$$
\begin{align*}
\widecheck{H}^*(\overline{\mathcal{M}}, \mathbb{Q}) &\stackrel{\text{Poincaré Duality}}{\longrightarrow}H_{\text{rank } \mathcal{E}} (\mathcal{T}/G, \mathcal{T}/g - \overline{\mathcal{M}}, \mathbb{Q}) = H_{\text{rank } \mathcal{E}}^G (\mathcal{T}- \mathcal{T}-s^{-1}(0), \mathbb{Q}) \\
&\stackrel{s_*}{\longrightarrow} H_{\text{rank }\mathcal{E}}^G (\mathcal{E}, \mathcal{E}- 0_{\mathcal{E}}, \mathbb{Q}) \\
&\stackrel{\tau_{\mathcal{E}}^G}{\longrightarrow} H_0^G(\text{pt}, \mathbb{Q})\cong \mathbb{Q}
\end{align*}
$$

<problem>

When are two global Kuranishi charts equivalent?

</problem>

<proposition>

Two global Kuranishi charts are equivalent if we can reach one from the other using a sequence consisting of the following moves:
1. Germ equivalence: choose a $G$-invariant neighborhood $s^{-1}(0) \subset \mathcal{U}\subset \mathcal{T}$ where the second subset is open, and take $(G, \mathcal{U}, \mathcal{E}|_{\mathcal{U}}, s|_{\mathcal{U}})$.
2. Group enlargement: choose another compact Lie group $H$ and a $G$-equivariant principle $H$-bundle $p:P\to \mathcal{T}$ and take $(G\times H, P, p^* \mathcal{E}, p^* s)$
3. Stabilization: choose a $G$-equivariant vector bundle $\pi: \mathcal{W}\to \mathcal{T}$ and take $(G, \mathcal{W}, \pi^*(\mathcal{E}\oplus \mathcal{W}), \pi^* s \oplus \Delta_{\mathcal{W}})$. 

</proposition>

This should be thought of as an analog of the Reidemeister moves. 

# Complex Geometry Background 

On $\mathbb{CP}^1$, we have the tautological line bundle $\mathcal{O}(-1)\hookrightarrow \mathbb{CP}^n \times \mathbb{C}^{n+1}$, which has a dual $\mathcal{O}(1)$, and we define $\mathcal{O}(k) = \mathcal{O}(1)^{\otimes k}$. 

## Holomorphic Line Bundles on Curves (Riemann Surfaces)

<lemma>

Suppose $\Sigma$ is a Riemann surface, $L\to \Sigma$ is a $C^\infty$ complex line bundle, and $\nabla$ is a $\mathbb{C}$-linear connection on it. Then $\nabla^{0,1}$ defines an unique holomorphic structure on $L$.

</lemma>

<proof>

Given $p\in \Sigma$. Choose a $C^\infty$ section $\tau$ of $L$ defined near $p$ such that $\tau(p)\neq 0$. 
<center>

$$
\nabla^{0,1}(\tau) = g\otimes \tau
$$

</center>

where $g\in \Omega^{0,1}(\Sigma)$.

The $\overline{\partial}$-Poincaré lemma states that we can find a $C^\infty$-function such that $g=\overline{\partial}f$ near $p$. Define $\sigma = e^{-f}\tau$, and we have 
<center>

$$
\begin{align*}
\Delta^{0,1} \sigma &= e^{-f}\nabla^{0,1} \tau + \overline{\partial}(e^{-f})\otimes \tau \\
&= e^{-f}(g\otimes \tau - \overline{\partial}f \otimes \tau)\\
&= 0.
\end{align*}
$$

</center>

</proof>

<lemma>

Suppose $\Sigma$ is a nodal genus $0$ curve. Then the isomorphism class of a holomorphic line bundle $L$ on $\Sigma$ is determined by the degree of $L$ on each component of $\Sigma$.

</lemma>

<corollary>

Consider $L\to \Sigma$ as above. Suppose $L$ has total degree $d$ and has degree $\ge 0$ on each component. Then $\dim H^0(\Sigma, L) = d+1$ and $\dim_{\mathbb{C}} H^1(\Sigma, L)=0$.

</corollary>

## Genus 0 Curves in $\mathbb{CP}^n$

Suppose $X$ is a complex manifold with 
1. a holomorphic map $f: X\to \mathbb{CP}^n$ 
2. a holomorphic line bundle $\mathcal{L}\to X$ and holomorphic sections $s_0,...,s_n$ such that they have no common zero in $X$. 

To go between these two, we can do the following:
$$
(X\stackrel{f}{\longrightarrow} \mathbb{P}^n_{[x_0:...:x_n]})\mapsto (f^* \mathcal{O}(1), f^*x_0,...,f^*x_n) \\
(\mathcal{L}, s_0,...,s_n) \mapsto (X\stackrel{[s_0:...:s_n]}{\longrightarrow} \mathbb{CP}^n ).
$$

Consider $\overline{\mathcal{M}}_{0,m}(\mathbb{CP}^n, d)$ for some $n, d\ge 1, m\ge 0$. 

<lemma>

This space is a complex orbifold of the expected dimension.

</lemma>

<proof>

Take $f:\Sigma \to \mathbb{P}^n$ where $\Sigma$ is a genus $0$ nodal curve. Recall $D_f: \Omega^0(\Sigma, f^*T \mathbb{CP}^n)\to \Omega^{0,1}(\Sigma)$. We want to show that this is surjective, which is equivalent to $\text{coker}D_f = H^1(\Sigma, f^* T \mathbb{CP}^n )$. We have the Euler exact sequence: 
<center>

$$
0 \longrightarrow \mathcal{O} \longrightarrow \mathcal{O}(1)^{\oplus n+1}\longrightarrow T \mathbb{CP}^n \longrightarrow
$$

</center>

If we pullback along $f:\Sigma \to \mathbb{CP}^n$ and take long exact sequence
<center>

$$
\longrightarrow H^1(\Sigma, f^* \mathcal{O})^{\oplus n+1}\longrightarrow H^1(\Sigma, f^*T \mathbb{CP}^n) \to 0
$$

</center>

and we are done.

</proof>