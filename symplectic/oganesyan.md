<link href="../whirlwind.css" rel="stylesheet">

<whirlheader>
    <p>Gary</p>
    <p>Oganesyan</p>
    <p>August 21</p>
</whirlheader>

# Introduction

Let $(X,e)$ where $e\in X$. Consider 
$$
\text{SP}^n(X) = X^n/S_n
$$

We have an embedding $\text{SP}^n(X) \hookrightarrow \text{SP}^{n+1}(X)$ through $\{p_1,...,p_n\}\to \{p_1,...,p_n, e\}$. So we have $\text{SP}^0(X) \hookrightarrow \text{SP}^1(X) \hookrightarrow ...$

Define 
$$
\text{SP}(X) =\bigcup \text{SP}^n(X)
$$
This consists of elements $p=\{ e, p_1,...,p_n, e\}$. It turns out $\text{SP}(X)$ is a semigroup under the following operation:
$$
\{ p_1,...,p_n, e\} + \{q_1,...,q_k, e\} = \{p_1,...,p_n, q_1,...,q_k, e\}
$$

Let $\Delta^n$ be an $n$-simplex. We consider
$$
\text{Map}(\Delta^n, \text{SP(X)})^+
$$
which is also a semigroup. We can turn this into a gorup by considering the Grothendieck group
$$
\text{Map}(\Delta^n, \text{SP(X)})^+=C_n(X)
$$
by adding $-f, -g$ satisfying $-(f+g)=-f-g$ and taking the restriction $\partial_K:C_n(X) \to C_{n-1}\to X$ with $d=\sum_{k=0}^n (-1)^k \partial_X$ satisfying $d^2=0$. 

# Dold-Thom Theorems

<theorem>
<src>Dold, Thom, 1968</src>

$$
H(C_*(X), d)= H_*^{\text{sing}}(X, \mathbb{Z}).
$$
where $H(C_*(X), d)=\pi_*(\text{SP}(X))$

</theorem>

<theorem>
<src>Dold, Thom, 1988-2000</src>

Let $X$ be a variety, $\text{SP}^n(X)$, $\Delta_{\text{alg}}^n=\{ z\in \mathbb{C}^{n-1} \mid z_1+...+z_{n+1} =1\}$, Consider $C_n^{\text{alg}}=\text{Map}_{\text{alg}}(\Delta_{\text{alg}}^n, \text{SP}(X))^+$. 

Define 
$$
H(C_*^{\text{alg}, d} )=H_*^{\text{sus}}(X)
$$
where $\text{sus}$ means the Suslin homology.

We have 
$$
H_0^{\text{sus}}(T^2) = \mathbb{Z}\times T^2 \\
H_0^{\text{sus}}(\Sigma_g)=\mathbb{Z}\times \text{Jac}(\Sigma_g)
$$

</theorem>

# Categories

Let $Y$ be a variety, $\mathcal{U}\subset Y$ be open. We can define 
$$
C_n(\mathcal{U}, X)=\text{Maps}_{\text{alg}} (\Delta_{\text{alg}}^n, \text{SP}(X))
$$
and $\mathcal{U}\to C_*(\mathcal{U}, X)$ is a sheaf on $Y$.

We can define the following categories:
1. Map are symplectic embeddings 
2. Map are generalized Lagrangians corr
3. $J$-holomorphic maps 

The second one is the most important but also the hardest.

<problem>

What is $\Delta^n$? What is $\text{Map}(Y, \text{SP}(X))$? $\text{Map}(Y, \text{SP}(X))$?

</problem>

Consider $\mathcal{U} \stackrel{\text{symplectic}}{\hookrightarrow} X^n/S_n$. We are interested in $U\longrightarrow$ unordered maps $f_1,...,f_n: U\to X$ such that $f_1^* w_X + ... +f_n^* w_X= w_Y$ which is a presheaf. When we perform sheafification, we obtain a global section $\int \text{SCor}_n(Y,X)$. This is an analogue of maps $Y\to \text{SP}^n(X)$. 

We need to define a map $Y\to \text{SP}(X)$. Consider $\text{ICor}(Y,X)$ in the same way: $\mathcal{U}\stackrel{\text{isotropic}}{\longrightarrow} X^n$ where if $G\in \text{ICor}_k(Y,X), F\in \text{SCor}_n(T, X)$, then $F+G\in \text{SCor}_{n+k}(T,X)$.

<definition>

We say $F_1\in \text{SCor}_n(Y,X), F_2 \in \text{Scor}_{n+k}(Y,X)$, then $F_1\sim F_2$ if there exists $G\in \text{ICor}(T,X)$ such that $F_2=F_1+G$.

</definition>

We want to define $\text{SCor}(Y,X)= \left(\bigsqcup \text{SCor}_n(Y,X) \right)/\sim$ an analogue of $Y\to \text{SP}(X)$. Fix a segment $M=(M, w_M, p_0, p_1)$. 

Now, we define $\text{SC}_n(Y,X) = \text{Map}(Y\times M^n, X)$. We have an embedding $i_k^\epsilon: M^n \hookrightarrow M^{n+1}$ where $M^n \to M^k\times p_\epsilon \times M^{n-k}$ where $\epsilon =0,1$. We have 
$$
\partial_k: \text{SC}_n(T,X) \to \text{SC}_{n-1}(Y,X)\\
d=\sum_{\epsilon=0}^1 \sum_{k=0}^n \partial_k
$$
where $d^2=0$.

We obtain
$$
H(\text{SC}_*(Y,X), d)=\text{EH}_*(Y,X).
$$

All standard symplectic embeddings belong to $\text{SCor}(Y,X)$. If $Y$ is contractible, then $\text{SCor}(Y,X)\neq 0$. 

# Homotopy and Triangulated Persistence Categories

<definition>

Let $F_0, F_1 \in \text{SCor}(Y,X)$. $F_0$ is **$M$-homotopic** to $F_1$ if there exists $H\in \text{SCor}(Y\times M, X)$ such that
$$
H|_{Y\times p_0}=F_0, \qquad H|_{Y\times p_2}=F_2.
$$

</definition>

<proposition>

1. Homotopy equivalences defines equivalence relation $\text{SCor}(Y,X)$.
2. If $\varphi_t: Y\to X$ is a symplectic isotopy, then $\varphi_0$ is homotopic to $\varphi_1$.
3. Define $H(\text{SC}_*(Y,X), d) = \text{EH}_*(Y,X)$. Groups $\text{EH}_*(Y,X)$ are functorial in all nice ways.
4. These groups are homotopy invariant.
5. These groups have all of the required exact sequences.

</proposition>

<src>Biran, Corea, Zhang</src> defined triangulated persistence category on $\mathcal{A}$, where $\text{ob}(\mathcal{A})$ are symplectic manifolds and $\text{Mor}(T,X)=\text{SCor}(T,X)$. This category is additive, and we can consider a category of chain complexes to get a triangulated persistence category with metric $\text{dist}(Y_1, Y_2)=\text{dist}_*(Y_1,X) \cdot \text{SC}_*(Y_2,X)$.

We can define $\text{JH}_*(T,X)$. Let $M=\mathbb{CP}^*$. If $X$ is Kähler and $\text{JH}_0(\text{pt}, X)=0$, then $X$ is algebraic.