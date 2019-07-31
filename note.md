# _belief rule-based system_

rule-based mode: $R=<U,A,D,F>$

antecedent attributes: $U=\{U_i,i=1,\cdots,T\}$  

referential values: $A=\{A_1,A_2,\cdots,A_T\},A_i=\{A_{ij},j=1,\cdots,J_i=|A_i|\}$

consequents: $D=\{D_n,n=1,\cdots,N\}$

logic function: $F$

the k-th rule in BRB system can be written as:

$R_k:if\{(A_1^k,\alpha_1^k) \wedge (A_2^k,\alpha_2^k) \wedge \cdots \wedge (A_{T_k}^k,\alpha_{T_k}^k)\}then\{(D_1,\overline{\beta}_{1k}),(D_2,\overline{\beta}_{2k}),\cdots,(D_N,\overline{\beta}_{Nk})\}$

with a rule weight $\theta_k$
and attribute weights $\delta_{k1},\delta_{k2},\cdots,\delta_{kT_k}$

$\alpha_i^k$ and $\overline{\beta}_{ik}$ are belief degree

aggregation function to calculate the toltal rule belief degree:

$\alpha_k=\varphi((\delta_{k1},\alpha_1^k),(\delta_{k2},\alpha_2^k),\cdots,(\delta_{kT_k},\alpha_{T_k}^k))$
$\{ex:\alpha_k=\prod_{i=1}^{T_k}(\alpha_i^k)^{\overline{\delta}_{ki}},\overline{\delta}_{ki}=\frac{\delta_{ki}}{\max_{j=1,\cdots,T_k}\delta_{kj}}\}$

generating and normalizing the activation weight of $R_k$:

$w_k=\frac{\theta_k\alpha_k}{\sum_{i=1}^L\theta_i\alpha_i}$

distribution on the referential values are $S(A_i^*,\varepsilon_i)=\{(A_{ij},\alpha_{ij});j=1,\cdots,J_i\}$,the input $A_i^*$
i is assessed to the referential value
$A_{ij}$ with the degree of belief of $\alpha_{ij}$

updating $\overline{\beta}_{ik}$ in consquent $D_i$:

$\beta_{ik}=\overline{\beta}_{ik}\frac{\sum_{t=1}^{T_k}(\tau(t,k))\sum_{j=1}^{J_i}\alpha_{tj}}{\sum_{t=1}^{T_k}\tau(t,k)},\tau(t,k)=\begin{cases}1,U_t\in R_k\\0,otherwise\end{cases}$

belief rule expression matrinx for a rule base

$
\begin{array}{c|}
O|I & A^1(w_1) & \cdots & A^L(w_L) \\
\hline
D_1 & \beta_{11} & \cdots & \beta_{1L} \\
\vdots & \vdots & \ddots & \vdots \\
D_N & \beta_{N1} & \cdots & \beta_{NL}
\end{array}
$

evidential reasoning approach

transform belief degrees into probability masses:

$m_{j,k}=w_k\beta_{j,k},j=1,\cdots,N$

$m_{D,k}=1-\sum_{j=1}^Nm_{j,k}=1-w_k\sum_{j=1}^{N}\beta_{j,k}$

$\overline{m}_{D,k}=1-w_k$

$\widetilde{m}_{D,k}=w_k(1-\sum_{j=1}^N\beta_{j,k})$

$m_{D,k}=\overline{m}_{D,k}+\widetilde{m}_{D,k}$

the remaining degree of belief of unassigned to any consequent $m_{D,k}$ is split into two parts:$\overline{m}_{D,k}$ caused by the relative importance $w_k$ and $\widetilde{m}_{D,k}$ caused by the incompleteness

suppose $m_{j,I(k)}$ is the combined degree of belief in $D_j$ by aggregating first $k$ rules,$m_{D,I(k)}$ is the remaining degress, let $m_{j,I(1)}=m_{j,1}$ and $m_{D,I(1)}=m_{D,1}$

the combined degree of first $k+1$ rules can be generated as:

$m_{j,I(k+1)}=K_{I(k+1)}[m_{j,I(k)}m_{j,k+1}+m_{j,I(k)}m_{D,k+1}+m_{D,I(k)}m_{j,k+1}]$

$\overline{m}_{D,I(k+1)}=K_{I(k+1)}[\overline{m}_{D,I(k)}\overline{m}_{D,k+1}]$

$\widetilde{m}_{D,I(k+1)}=K_{I(k+1)}[\widetilde{m}_{D,I(k)}\widetilde{m}_{D,k+1}+\widetilde{m}_{D,I(k)}\overline{m}_{D,k+1}+\overline{m}_{D,I(k)}\widetilde{m}_{D,k+1}]$

$K_{I(k+1)}=[1-\sum_{j=1}^N\sum_{t=1,t \neq j}^Nm_{j,I(k)}m_{t,k+1}]^{-1}$

$\beta_j=\frac{m_{j,I(L)}}{1-\overline{m}_{D,I(L)}},\beta_D=\frac{\widetilde{m}{D,I(L)}}{1-\overline{m}_{D,I(L)}},\sum_{j=1}^N\beta_j+\beta_D=1$

an analytical ER algorithm is developed:

$m_j=k[\prod_{i=1}^L(m_{j,i}+m_{D,i})-\prod_{i=1}^Lm_{D,i}]$

$\overline{m}_D=k[\prod_{i=1}^L\overline{m}_{D,i}]$

$\widetilde{m}_D=k[\prod_{i=1}^Lm_{D,i}-\prod_{i=1}^L\overline{m}_{H,i}]$

$k=[\sum_{j=1}^N\prod_{i=1}^L(m_{j,i}+m_{D,i})-(N-1)\prod_{i=1}^Lm_{D,i}]^{-1}$

$\beta_j=\frac{m_j}{1-\overline{m}_D}=\frac{\prod_{i=1}^L(m_{j,i}+m_{D,i})-\prod_{i=1}^Lm_{D,i}}{\sum_{j=1}^N\prod_{i=1}^L(m_{j,i}+m_{D,i})-(N-1)\prod_{i=1}^Lm_{D,i}-\prod_{i=1}^L\overline{m}_{D,i}}$

$\beta_D=\frac{\widetilde{m}_D}{1-\overline{m}_D}=\frac{\prod_{i=1}^Lm_{D,i}-\prod_{i=1}^L\overline{m}_{D,i}}{\sum_{j=1}^N\prod_{i=1}^L(m_{j,i}+m_{D,i})-(N-1)\prod_{i=1}^Lm_{D,i}-\prod_{i=1}^L\overline{m}_{D,i}}$