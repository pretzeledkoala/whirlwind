<link href="../whirlwind.css" rel="stylesheet">

<whirlheader>
    <p>Gary</p>
    <p>Usher 2</p>
    <p>August 20</p>
</whirlheader>

# Symplectic Capacities 

Let $\mathcal{C}$ be some collection of $2n$-dimensional symplectic manifolds such that for all $(M, \omega) \in \mathcal{C}$ and for all $a>0$, then $(M, a\omega) \in \mathcal{C}$.

<definition>

An **symplectic capacity on $\mathcal{C}$** is a function $c: \mathcal{C}\to [0,\infty]$ such that 

1. **Monotonicity**: if there exists a symplectic embedding $(M, \omega) \hookrightarrow (M', \omega')$, then $c(M, \omega) \le c(M', \omega')$. 
2. **Comformality**: $c(M, a\omega) = ac(M, \omega)$.
3. **Nontriviality**: $c(B^{2n}(1))>0$ and $c(Z^{2n}(1))<\infty$.

</definition>

<remark>

A stronger version of $(3)$ is **normalization**: $c(B^{2n}(1))=c(Z^{2n}(1)) =1$.

</remark>

Often, we have $\mathcal{C}\subset \left\{ \text{subsets of } \mathbb{R}^{2n} \right \}$. Then, instead of scaling via $(U, \omega_0)\to (U, a\omega)$, we'll keep the same $\omega_0$, and replace $U$ by $aU := \left\{ \sqrt{a}\vec{z} \mid  \vec{z} \in U \right\} $. 

Let's look at some examples of capacities:

<example>
<src>Gromov Capacity</src>

The **Gromov capacity** is defined as
$$
c_B(M,\omega) := \sup \left\{ a\mid  \exists \text{ symplectic embedding } B^{2n}(a) \hookrightarrow (M, \omega) \right\}.
$$

</example>

One major source of symplectic capacities are Hamiltonian systems, and we can study symplectic capacities via filtered Floer homology or symplectic homology.

Here is how symplectic capacities arise from Hamiltonian systems: suppose $(M,\omega)$ is a symplectic manifold and $F:\mathbb{R}/\mathbb{Z}\times M \to \mathbb{R}$ is smooth with $(t,m) \mapsto H_t(m)$. Then the time-dependent Hamiltonian $X_{H_t}$, given by $\omega(\cdot, X_{H_t}) =dH_t$, gives a function $\varphi_H^t: M\to M$ satisfying 
$$
\dfrac{d\varphi_H^t (m)}{dt} = X_{H_t}(\varphi_H^t(m)).
$$

Here is another example of a capacity:

<example>
<src>Hofer-Zehnder Capacity</src>

The **Hofer-Zehnder capacity** is defined as

$$
c_{\text{HZ}}(M, \omega) := \sup \left\{ \max H \mid  \text{condition}\right\}
$$
where the condition is that $H:M\to \mathbb{R}$, $H=0$ on some open set compactly supported, and the only periodic orbits of $X_H$ having period $<1$ are constants. 

</example>

# (Filtered) Floer Homology

For the rest of today, assume $\omega=d\lambda$. For example, take the Euler vector field $E_X, M\subset \mathbb{R}^{2n},$ and $\lambda = \lambda_0 := \frac{1}{2}\sum_j (x_j dy_j - y_j dx_j)$.

For $H$ as above, let $\text{HF}(H)$ be the Morse homology for the action functional $\mathcal{A}_H: C^\infty (\mathbb{R}/\mathbb{Z}, M)\to \mathbb{R}$ defined by
$$
\mathcal{A}_H(\gamma)=-\int_{S^1} \gamma^* \lambda+\int_0^1 H(t, \gamma(t)) dt.
$$ 

Additionally, define
$$
\text{Crit}(\mathcal{A}_H):=\left\{ \gamma: \mathbb{R}/\mathbb{Z} \to M \mid \gamma'(t)=X_{H_t}(\gamma(t)) \right\}.
$$

There is a 1-to-1 correspondence between $\text{Crit}(\mathcal{A}_H)$ and $\text{Fix}(\varphi_H')$ given by $\gamma \mapsto \gamma(0)$. 

The negative gradient flowlines of $\mathcal{A}_H$ are described by the function $u: \mathbb{R}\to \mathbb{R}/\mathbb{Z}$ such that 
$$
\dfrac{\partial u}{\partial s}+J_t(u(s,t)) \left( \dfrac{\partial u}{\partial t}- X_{H_t} \right)=0.
$$

Additionally, we have $\text{CF} = \text{span} \left\{ \text{Crit}(\mathcal{A}_H) \right\}$, graded by $\mu_{\text{CZ}}$, with the boundary operator $\partial: \text{CF}_k(H) \to \text{CF}_{k-1}(H)$ defined by $\partial \gamma_- = \sum \# (\text{flowlines from } \gamma_- \text{ to } \gamma_+) \gamma_+$, satisfying $\text{ind}(\gamma_-) - \text{ind}(\gamma_+) = 1$.

<proposition>

Assuming the conditions at infinity guarantee spaces are compact:
- $\partial^2 =0$, which gives the homology $\text{HF}(H)$.
- If $H$ and $H'$ satisfy the same conditions at $\infty$, then there exists continuation chain maps $\text{CF}(H)\rightleftarrows \text{CF}(H')$ inducing isomorphisms on homology.

</proposition>

The filtered version can be given as follows: given $t\in \mathbb{R}$, define $\text{CF}^t(H)= \text{span} \{ \gamma \in \text{Crit}(\mathcal{A}_H) \mid  \mathcal{A}_H(\gamma)=t \}$. $\mathcal{A}_H$ decreases along its negative gradient flowlines, so $\partial(\text{CF}^t(H)) \subset \text{CF}^t(H)$. This gives a homology $\text{HF}^t(H)$ for all $t\in \mathbb{R}$, with inclusion-induced $\text{HF}^s(H)\to \text{HF}^t(H)$ for $s\le t$.

If $H\ge H'$, we have continuation chain maps $\text{CF}^t(H) \to \text{CF}^t(H')$, so for $s\le t, H\ge H'$, the following diagram commutes:
<!-- $$
\begin{tikzcd}
	{\text{HF}^s(H)} & {\text{HF}^s(H')} \\
	{\text{HF}^t(H)} & {\text{HF}^t(H'}
	\arrow[from=1-1, to=1-2]
	\arrow[from=1-1, to=2-1]
	\arrow[from=1-2, to=2-2]
	\arrow[from=2-1, to=2-2]
\end{tikzcd}
$$ -->

$$
\begin{CD}
\text{HF}^s(H) @>{}>> \text{HF}^s(H') \\
@V{}VV @V{}VV \\
\text{HF}^t(H) @>{}>> \text{HF}^t(H')
\end{CD}
$$

# Liouville Embeddings

<definition>

A **Liouville domain** $(W, \omega)$ is a compact manifold with $\partial, W$, together with a $\lambda \in \Omega^1(W)$ such that $d\lambda$ is symplectic and the Liouville vector field $V_\lambda$, defined by $d\lambda(V_\lambda, \cdot)=\lambda$, points outward along $\partial W$.

</definition>

<example>

For $\lambda_0 = \frac{1}{2} \sum (x_j \,dy_j - y_j \,dx_j)$, we have $V_{\lambda_0} = \frac{1}{2}\sum (x_j \partial{x_j}+y_j \partial_{y_j})$, so we can take $W$ to be the strongly star-shaped around the region in $\mathbb{R}^{2n}$.

In this case, $\alpha:= \lambda\mid _{\partial W}$ for $\alpha \in \Omega^1(\partial W)$ is a contact form on $\partial W$, and there exists a collar neighborhood $U$ of $\partial W$ such that $(U, \lambda) \approx ([1-\epsilon, 1]\times \partial W, r\alpha)$. From the completion, we have 
$$
\left(\hat{W}, \hat{\lambda}\right)=(W,\lambda) \bigcup_{\partial W} ([1, \infty)\times \partial W,  r\alpha).
$$
So in this case, $\hat{W}\simeq \mathbb{R}^{2n}$ is the **Liouville isomorphism**.

</example>

<definition>

Given a Liouville domain $(W,\lambda)$, a **$W$-admissible Hamiltonian** is a Hamiltonian $H: \mathbb{R}/\mathbb{Z} \times \hat{W} \to \mathbb{R}$ such that $H(t,w)\ge 0$ and for all $w\in W$, there exist 
- $a>0$ that is not the period of any closed orbit $R_\alpha$
- $b\in \mathbb{R}$ such that for $(r, y)$ where $r\in [1,\infty)$ and $y\in \partial W$
-  $H(t(r,y))=-ar+b$.

</definition>

The condition that $a$ is not the period of any closed orbit $R_\alpha$ implies that $\text{Fix}(\varphi_H^t)\subset W$. The condition that $H(t,(r,y)) = -ar+b$ implies that $X_H=-aR_\alpha$ on $(1,\infty)\times \partial W$.

Let $H_W=\left\{ W\text{-admissible Hamiltonians}\right\}$. Then we can associate $H$ with $\text{HF}^t(H)$ and if $H\ge H'$, we have a map $\text{HF}^{t}(H) \to \text{HF}^t(H')$.

<definition>

For all $t\in \mathbb{R}$, define 
$$
\text{SH}^t(W) := \lim_{\stackrel{\longrightarrow}{H\in \mathcal{H}_W}} \text{HF}^t(H)
$$
via the map we just mentioned.

</definition>

So we have $\text{SH}^s(W) \to \text{SH}^t(W)$ for all $s\le t$. 

<proposition>

$\text{SH}^\infty(W)$ depends only on the Liouville isomorphism type of $\hat{W}$. For $W\subset \mathbb{R}^{2n}$ strongly star-shaped, then $\text{SH}^\infty(W)=0$.

</proposition>

<proposition>

If $W'\subset W^0$, we get continuation maps from $W$-admissible Hamiltonians to $W'$-admissible Hamiltonians. This gives transfer maps 
$$
\text{SH}^t(W) \to \text{SH}^t(W').
$$

</proposition>

More generally:

<proposition>

For a Liouville embedding $\varphi: W' \hookrightarrow W^0$ (meaning $\varphi^*\lambda - \lambda' = d\cdot f$ for some function $f$), we get $\varphi': \text{SH}^t(W)\to \text{SH}^t(W')$.

</proposition>

# Floer-Hofer-Wysocki Capacity

Let's discuss Floer-Hofer-Wysocki Capacity for $W\subset \mathbb{R}^{2n}$ strongly star-shaped. We have the following result:

<proposition>

For $\epsilon>0$,
$$
\text{SH}_n^t(W)=\mathbb{Q}.
$$
with 
$$
\text{SH}_n^{\epsilon'}(W) \stackrel{\sim}{\to} \text{SH}^{\epsilon}(W)
$$
for all $\epsilon'< \epsilon$.

</proposition>

This motivates the following definition:

<definition>

The **Floer-Hofer-Wysocki capacity** is
$$
c_{\text{FHW}}(W):= \inf \left\{t\mid  \text{SH}_n^\epsilon(W) \to \text{SH}^t(W)=0 \text{ for small }\epsilon \right\}
$$

</definition>

<theorem>

This is a capacity.

</theorem>

<proof>

We prove the three conditions:

- Monotonicity: follows from transfer maps:

	<!-- \[\begin{tikzcd}
		{\text{SH}^\epsilon(W)} & {\text{SH}^\epsilon(W')} \\
		{\text{SH}^t(W)} & {\text{SH}^t(W')}
		\arrow["{{\varphi'}}"', from=1-1, to=1-2]
		\arrow["\cong", from=1-1, to=1-2]
		\arrow[from=1-1, to=2-1]
		\arrow[from=1-2, to=2-2]
		\arrow["{{\varphi}}"', from=2-1, to=2-2]
	\end{tikzcd}\] -->
	<USHER 2.1>

	where the left map if $0$ if $t>c_{\text{FHW}}(W)$ and the right map is $0$ if $t>c_{\text{FHW}}(W')$.
- Conformality: follows from behavior of action under scaling $\omega$.
- Nontriviality: holds by construction.

</proof>

<example> 

For $W= E(a_1,...,a_n) = \left\{ \sum \frac{\pi(x_j^2+y_j^2)}{a_j} \le 1\right\}$ with $a_1\le ...\le a_n$, we have $c_{\text{FHW}(W)}=a_1.$

 </example>