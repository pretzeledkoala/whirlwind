<link href="../whirlwind.css" rel="stylesheet">

<whirlheader>
<p>Gary Hu</p>
<p>Differential Geometry</p>
<p>september 6 2024</p>
</whirlheader>

# Review 

Last time, we saw some point-set concepts. 

# More Point Properties 

<proposition>

If $(X,\tau)$ is a topological space and $A\subseteq X$, then 
1. $\AA = \bigcup \{U\subseteq X: U\in \tau \text{ and } U\subseteq A \}$
2. $\overline{A}=\bigcap \{C\subseteq X: C\text{ is closed and } A\subseteq C \}$

</proposition>

<proof>

1. Obvious 
2. Take $x\in \overline{A}$. If there exists $C$ closed with $A\subseteq C$ and $x\in C$, then $X\backslash C$ is open and contains $x$. So $(X\backslash C)\cap A =\emptyset$, contradicting $A\subseteq C$. This is the $\subseteq$ direction. For the $\supseteq$ direction: FAIL.

</proof>

<corollary>

1. $(\AA)^{\circ}=\AA$
2. $\overline{\overline{A}}=\overline{A}$
3. $\AA=A \Longleftrightarrow A$ is open 
4. $\overline{A} \Longleftrightarrow A$ is closed
5. $\AA$ is the largest subset of $A$ 
6. $\overline{A}$ is the smallest closed superset of $A$

</corollary>

<proposition>

Let $(X,\tau)$ be a topological space, and take $A_1, A_2 \subseteq X$. 
1. $(A_1 \cap A_2)^\circ = \AA_1 \cap \AA_2$
2. $\AA_1 \cup \AA_2 \subseteq (A_1 \cup A_2)^\circ$
3. $\overline{A_1 \cup A_2} = \overline{A_1} \cup \overline{A_2}$
4. $\overline{A_1} \cap \overline{A_2} \subseteq \overline{A_1} \cap \overline{A_2}$

</proposition>

<proof>

1. $A_1\cap A_2 \subseteq A_1 \implies (A_1 \cap A_2)^\circ \subseteq \AA$. Same for $A_2$. So $(A_1 \cap A_2)^\circ \subseteq \AA_1 \cap \AA_2$. Next: $\AA_1 \cap \AA_2$ is open, and $\AA_1 \cap \AA_2 \subseteq A_1 \cap A_2 \implies \AA_1 \cap \AA_2 \subseteq (A_1 \cap A_2)^\circ$.

Others: left as an exercise to the reader.

</proof>

# Sequence

<definition>

A sequence $(x_n)_{n\ge 1} \subseteq (X,\tau)$ **converges** to $x\in X$ if for all $U\in \tau, x\in U$, there exists $n_0\ge 1$ such that for all $n\ge n_0$, $x_n\in U$. We write $x_n \to x$.

</definition>

<remark>

There is a generalization of sequences called **nets**; $(x_\alpha)_{\alpha \in A}$ where $A$ is a **direct set**.

</remark>

Warning: we cannot write $x=\lim_{x\to \infty}x_n$ since limits might not be unique:

<example>

Take $(X,\tau_{\text{ch}})$. If $(x_n)_{n\ge 1}$ and $x\in X$ is arbitrary, then $x_n\to x$.

</example>

<proposition>

Limits are unique in metric spaces.

</proposition>

<proof>

Assume $x_n\to x$ and $x_n\to y$. Let $\epsilon>0$. So 
- There exists $n_1 \ge 1$ such that for all $n\ge n_1, d(x_n, x) < \frac{\epsilon}{2}$
- There exists $n_2 \ge 1$ such that for all $n\ge n_2, d(x_n,y)<\frac{\epsilon}{2}$

By triangle inequality,
$$
d(x,y)\le d(x,x_n) + d(x_n,y) < \frac{\epsilon}{2} + \frac{\epsilon}{2} =\epsilon.
$$

So $0\le d(x,y)\le \epsilon$ for all $\epsilon>0$, which implies that $d(x,y) =0 \implies x=y$. 

</proof>

<definition>

We say that $(X,\tau)$ is a **Hausdorff space** if for every $x,y\in X, x\neq y$, there exists $U,V \in \tau$, disjoint, with $x\in U$ and $y\in V$.

</definition>

<proposition>

Limits are unique in Hausdorff spaces.

</proposition>

<proof>

Assume that $x_n\to x$ and $x_n\to y$. If $x\neq y$, then we fix open sets $U,V\subseteq X$ and $U\cap V=\emptyset, x\in U, y\in V$. Then 
- There exists $n_1\ge 1$ such that for all $n\ge n_1, x_n \in U$. 
- There exists $n_2\ge 1$ such that for all $n\ge n_2, x_n \in V$.

If $n\ge \max\{n_0,n_1\}$, then $x_n \in U\cap V$.

</proof>

<example>

- $(X,d)$ are always Hausdorff
- Sierpinski space $X=\{a,b\}, \tau = \{\emptyset, \{a\}, \{a,b\}\}$ is not Hausdorff 
- Sorgenfrey line is Hausdorff 
- The line with two origins is not Hausdorff
- (Finite) products of Hausdorff spaces are Hausdorff 
- Quotients of Hausdorff spaces aren't always Hausdorff

</example>

<proposition>

$(X,\tau)$ is Hausdorff $\Longleftrightarrow \Delta \subseteq X\times X$ is closed, where $\Delta = \{ (x_1,x_2)\in X\times X: x_1=x_2 \}$.

</proposition>