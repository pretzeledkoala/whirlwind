<link href="../whirlwind.css" rel="stylesheet">

<whirlheader>
    <p>Gary</p>
    <p>Usher 3</p>
    <p>August 21</p>
</whirlheader>

# Symplectic Homology

Suppose we have $(W,\lambda)$ a Liouville domain, $\eta = \partial W$, a contact form $\alpha = \lambda_{Y}$, and $C$ a scalar of $Y$ such that $(C\lambda)\cong ((1-\epsilon, 1] \times Y, r\alpha)$. The completion is 
$$
\hat{W}:= W \bigcap_Y ([1,\infty] \times Y, r\alpha).
$$
Define
$$
\mathcal{H}_W:=\{W\text{-admissible Hamiltonians}\}
$$
where $H: \mathbb{R}/\mathbb{Z}\times \hat{W}\to \mathbb{R}$ such that $H \mid _{\mathbb{R}/\mathbb{Z}\times H} \ge 0$ and for $r\ge 1, y\in Y$, $H(t,(r,y))=-ar+b$ for $a>0, b\in \mathbb{R}$ such that $a$ is not the closed period of any Reeb orbit for $\alpha$.

Suppose $H, H \in \mathcal{H}_{W}$ and $H\ge H'$. Then for $t\in \mathbb{R}$ autonomous, we have construction maps $\text{HF}^{t}(H) \to \text{HF}^t(H')$. 

<definition>

$$
\text{SH}^t(W) = \lim_{\stackrel{\longrightarrow}{H\in \mathcal{H}_W}} \text{HF}^t(H).
$$

</definition>

A family of $H$'s approaching the limit might look like the following: take $H \mid _W$ to be a small Morse function $W\to [0,\infty)$ that is $C^2$ small in the complement of the collar, with $H \mid _{\partial W}=0$.

- On $C\cong (1-\epsilon, 1]\times Y$, we have $H(r,y)=-h(r)$, where $h'$ increases rapidly from $\delta \approx 0$ to $a \gg 0$.
- On $\hat{W}\backslash W = (1,\infty)\times Y$, we have $H(r,y)=-a(r-1)$.

Note that the Hamiltonian vector field given by $H(r,y)=-h(r)$ is $X_H=-h'(r)R_\alpha$.

Recall that for $\gamma: \mathbb{R}/\mathbb{Z}\to M$, 
$$
\mathcal{A}_H(\gamma)=-\int_{\mathbb{R}/\mathbb{Z}} \gamma^* \lambda + \int_0^1 H(t, \gamma(t))\,dt.
$$
For these $H$, $\text{Crit } \mathcal{A}_H$ consist of
- Constants at critical points of $H_{W\backslash C}$ with $\mathcal{A}_H = H(p) \approx 0$. 
- In $C=[1-\epsilon, 1]\times Y$, the critical points are given by reparameterizations of closed orbits of $R_\alpha$ with period $h'(r)$, with $\mathcal{A}_H \approx h'(r)$. 

If $t_0< \text{the minimal action of a Reeb orbit}$, 
$$
\begin{align*}
\text{SH}_*^t(W) &= H_{*+n}(\text{Morse complex of }H \mid _{W}) \\
&= H_{*+n}(W, Y).
\end{align*}
$$

Once $t$ is bigger than the minimal period of a Reeb orbit, $\text{SH}^t$ is affected by the Reeb orbits, any of which gives an $S^1$ family in $\text{Crit}(\mathcal{A}_H)$. Morse-Bott perturbation splits these into two orbits different in index by $1$, both with action approximately the period of the original orbit. 

<example>
<src>Ellipsoid</src>

Consider the ellipsoid 
$$
E(a_1,...,a_n) = \left\{ \sum_j \dfrac{\pi(x_j^2+y_j^2)}{a_j} \le 1 \right\}.
$$
with $a_1<...<a_n$. Assume that $a_j$ are linearly independent over $\mathbb{Q}$. The Reeb orbits are circles in $x_jy_j$ planes (and their $m$-fold covers) with action $ma_j$.  After Morse-Bott perturbation, there exists $1$ orbit in each index starting at $n+1$ arranged in increasing order of action. 

</example>

# Positive Symplectic Homology

The small variation on $\text{SH}^t$ is the
$$
\text{positive SH} = \text{SH}^{+,t}=\lim_{\stackrel{\longrightarrow}{H}} H_* \left( \dfrac{\text{HF}^t(H)}{\text{HF}^\epsilon (H)}\right)
$$
for $\epsilon\ll 1$. 

<example>

For $W\subset \mathbb{R}^{2n}$ star-shaped,
$$
\text{SH}_*^{+,\infty}(W) = \begin{cases} \mathbb{Q} & *=n+1 \\ 0 &\text{ otherwise }\end{cases}
$$

</example>

The larger filtration on $\text{SH}^t$ is the filtered positive $S^1$-equivariant symplectic homology. Formally, do filtered Morse theory on 
$$
\dfrac{C^\infty(S^1, \hat{W})\times S^\infty}{S^1}.
$$
With $\mathbb{Q}$ coefficients, we obtain the filtered homology of a complex with 1 generator per Reeb orbit (instead of 2).

<example>

Abbreviate $\text{CH}^t=\text{SH}_*^{S^1, +, t}$. For the ellipsoid case, 
$$
\text{CH}_*^\infty(\text{any strongly star-shaped domain in }\mathbb{R}^{2n})=\begin{cases}\mathbb{Q} & *=n-1+2k \\ 0 & \text{otherwise} \end{cases}
$$
where $k\ge 1$. 

</example>

# The Gutt-Hutchings Capacity

<definition>
<src>Gutt-Hutchings Capacity</src>

For $k\ge 1$ and $W$ strongly star-shaped $\subset \mathbb{R}^{2n}$, the **Gutt-Hutchings capacity**
$$
c_k^{\text{GH}}(W) := \inf \{t  \mid  \text{CH}_{n-1+2k}^t(W) \to \text{CH}_{n-1+2k}^\infty(W) \text{ is nonzero}\}.
$$

</definition>

<example>

$$
c_k^{\text{GH}}(E(a_1,...,a_k))= k^{\text{th}} \text{ smallest number among } ma_j
$$
for $m\ge 1, j=1,...,n$. 

</example>

<example>

$$
c_{k}^{\text{GH}}(B^2(a_1)\times ...\times B^2(a_n))= k\min a_j.
$$

</example>

# Symplectic Banach-Mazur Distances 

We quickly introduce a different problem for the remainder of the class. 

<definition>

The **symplectic Banach-Mazur distance** is given by
$$
\delta(X,Y) := \left \{\lambda \mid \exists \text{ Liouville embedding }\varphi: X\hookrightarrow \text{ such that }\lambda^{-1}(Y) \subset \varphi(X) \subset \lambda Y\right\}
$$

</definition>

A high-level overview to approach problems related to the symplectic Banach-Mazur distance is the following trick: 
$$
\text{CH}_k^t(\lambda Y) \to \text{CH}_k^t(X) \to \text{CH}_k^t \left(\lambda^{-1}Y \right)
$$
is equivalent to 
$$
\text{CH}_k^{\lambda^{-1}t}(Y) \to \text{CH}_k^t(X) \to \text{CH}_k^{\lambda t} \left(Y \right).
$$
If no such factorization exists, $\delta(X,Y) >\lambda$.