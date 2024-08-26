<link href="../whirlwind.css" rel="stylesheet">
<link rel="stylesheet" type="text/css" href="http://tikzjax.com/v1/fonts.css">
<script src="https://tikzjax.com/v1/tikzjax.js"></script>

<whirlheader>
    <p>Gary</p>
    <p>Moduli Spaces of J-holomorphic Curves and Compactness</p>
    <p>August 19</p>
</whirlheader>

# Introduction

<script type="text/tikz">
  \begin{tikzpicture}
    \draw (0,0) circle (1in);
  \end{tikzpicture}
</script>

<definition>

Let $M^{2n+1}, \xi^{2n}\subset TM$. We say $\xi$ is a **contact structure** if there exists 1-form $\alpha$ on $M$, called the **contact form**, such that
- $\xi = \ker \alpha$ 
- $\alpha \wedge (d\alpha)^n \neq 0$

</definition>

Together, these two conditions imply that $\xi$ is non-integrable.

<example>

$(\mathbb{R}^{2n+1}, \xi_{\text{std}}=\ker \alpha_{\text{std}})$ where 
$$
\alpha_{\text{std}}= dz-\sum_{i=1}^n y_i \,dx_i.
$$

When $n=1$, at the origin, we have the contact plane.

</example>

<theorem>
<src>Darboux Theorem</src>

All contact structures in $\dim 2n+1$ are locally isomorphic.

</theorem>

<theorem>
<src>Gray Stability Theorem</src>

Consider $\{\xi_t \}_{0\le t \le 1}$ contact structures on $M$. If $M$ is closed, then there exists a 1-parameter family of diffeomorphisms $\phi^t$ of $M$ such that $(\phi^t)_* \xi_t = \xi_0$ where $\phi_0 =\text{id}$.

</theorem>

# Contact Homology 

Contact homologies are some invariants of contact structures. Before we discuss further, lets look at some applications of contact homologies:

- <src>Ustilovsky, 1999</src>: $S^{4m+1}$ admits $\infty$ many contact structures in each homotopy class of **almost contact structures** $(\xi, J, \xi\to \xi, J^2 = -\text{id})$ where $\xi$ is a hyperplane.
- <src>Bourgeois, 2004</src>: $T^5$ and $T^2 \times S^3$ have $\infty$ contact structures in some homotopy class of almost contact structures. 
- <src>Giroux, 1994; Eliashberg, Hofer, Givental, 2000</src>: On $T^3$, $\alpha = \cos 2\pi n z\,dx + \sin 2\pi n z \,dy$, $\xi_n = \ker \alpha_n$, where $\xi$ are pairwise non-isomorphic.

<definition>

Given a contact form $\alpha$, $R_\alpha$ is called a **Reeb vector field** if 
- $\alpha(R_\alpha)=1$ (positively transverses to $\xi$)
- $\,d\alpha(R_\alpha, \cdot)=0$ (the flow of $R_\alpha$ preserves $\xi$)

</definition>

<definition>

Periodic orbits of $R_\alpha$ are called **Reeb orbits**.

</definition>

<conjecture>
<src>Weinstein Conjecture</src>

If $M^{2n+1}$ is closed, then for any contact form $\alpha$, there exists at least one Reeb orbit.

</conjecture>

<theorem>
<src>Taubes, 2007</src>

The Weinstein conjecture holds for $n=1$.

</theorem>

<definition>

Let $\gamma$ be a Reeb orbit of period $T$, $\varphi^t $ be a time $t$ flow of $R_\alpha$ We say $\gamma$ is non-degenerate if $\,d\varphi^T : \xi_{\gamma(0)}\to \xi_{\gamma(T)}$ does not have $1$ as an eigenvalue.

</definition>

<definition>

Trivialize $(\xi|_\gamma, \,d\alpha)$ symplectically. Then $d\varphi^t$ gives a path of symplectic matrices starting at $\text{id}$. For such a path, we can define an integer, called the **Conley-Zehnder index** of $\gamma$.

</definition>

The general definition is complicated so we will only present simple examples:

<example>

Take $n=1, \dim M=3$.
- Positive hyperbolic: If the eigenvalues of $d\varphi^T$ are positive real numbers and $d\varphi^t(v)$ winds around the origin $k$ times (where $v$ is an eigenvector), then $\mu_{\text{cz}}=2k$ are negative real numbers. 
- Negative hyperbolic: If $d\varphi^t(v)$ winds around $k+\frac{1}{2}$ times, then $\mu_{\text{cz}}(\gamma)=2k+1$.
- Elliptic: If the eigenvalues are not real, $d\varphi^t (w)$ where $w \in \xi_{\gamma(0)}$ winds between $k$ and $k+1$ times then $\mu_{\text{cz}}(\gamma)=2k+1$.

</example>

Consider the actional functional $A:C^\infty(s^t, M)\to \mathbb{R}, \gamma \mapsto \int_{S^1} \gamma^*(\alpha)$ with Reeb orbits $\text{crit }A$, with a complex structure $J:\xi$ acting on itself with $T^2=-\text{id}$ and $\langle u,v \rangle =d\alpha(u, Tv)$ for any $u,v \in \xi$. Then $\langle \cdot, \cdot \rangle$ defines an inner product which implies
- $d\alpha(u,v) = \,d\alpha(Ju, Jv)$
- $d\alpha(u, Ju) >0$ for any $u \neq 0 \in \xi$.

Take $\eta_1, \eta_2 \in T_\gamma C^\infty(S^1,M)$ with
$$
\langle \eta_1, \eta_2 \rangle=\int_{S^1} \langle \eta_1, \eta_2 \rangle + \alpha(\eta_1)\alpha(\eta_2)\,dt.
$$

Take $u: \mathbb{R}\to C^\infty(S^1, M)$ with $s\in \mathbb{R}$ and $t\in C^\infty(S^1, M)$ with $\dim u(s)$ are Reeb orbits as $s\to \pm \infty$. Then 
$$
\dfrac{du}{ds}=-\text{grad }A
$$
with $u: \mathbb{R}\times S^1 \to M$. This gives
$$
d(u^*\alpha \cdot j)=0 \\
\pi_\xi u_s + J\pi_\xi u_t =0
$$
where $j$ is a complex structure on $\mathbb{R}\times S^1$.

Let's require $u^*d\alpha \cdot j = da$ where $a: \mathbb{R}\times S^1 \to \mathbb{R}$.  Let $\tilde{u}=(a,u):\mathbb{R}\times S^1 \to \mathbb{R}\times M$. Now, we extend $J$: $T(\mathbb{R}\times M)=\mathbb{R}(\partial a) \oplus \mathbb{R}(R_\alpha)\oplus \xi$ where $a\in \mathbb{R}$, and extend $J: \mathbb{R}(\partial_a)\to \mathbb{R}(R_\alpha)$. $\tilde{u}$ is $J$-holomorphic, i.e. 
$$
\overline{\partial}\tilde{u}= \dfrac{1}{2} (d\tilde{u}+J(\tilde{u})d\tilde{u}\cdot j)=0
$$
or  
$$
\tilde{u}_s+J(\tilde{u})\tilde{u}_t = 0
$$

Next time, we will study the compactification of moduli spaces of $J$-holomorphic cylinders. 