---
theme: apple-basic
layout: intro
title: Portfolio Optimization
---

# Portfolio Optimization

Using quantum computing

<div class="absolute bottom-10">
  <span class="font-700">
    José Ossorio - March 28th 2023
  </span>
</div>


---
layout: image-right
image: '/stocks.png'
---

# Understanding the problem
## What's portfolio optimization?

Finding the best distribution of assets to maximize or minimize a desired metric

<br>

<div v-click="1">
  Examples:
  <ul>
    <li>Maximizing the return while limiting the risk</li>
    <li>Minimizing the risk while maintaining a minimum return</li>
  </ul>
</div>

<!-- <div class="page-num">
  <SlideCurrentNo /> / <SlidesTotal />
</div> -->

<style>
  .page-num {
    position: absolute;
    bottom: 12px;
    left: 443px;
  }
</style>

---

<div class="container">
  <div>
    <h1>Classical Approaches</h1>
    <ul>
      <li v-click="">Linear Programming</li>
      <li v-click="">Quadratic Programming</li>
      <li v-click="">Genetic Algorithms</li>
    </ul>
    <h2 v-click>In general, heuristic methods</h2>
  </div>
</div>

<!-- <div class="page-num">
  <SlideCurrentNo /> / <SlidesTotal />
</div> -->

<style>
  li {
    font-size: 23px;
  }
  .container {
    display: flex;
  }
  img {
    position: absolute;
    left: 550px;
    top: 200px;
  }
  .page-num {
    position: absolute;
    bottom: 12px;
    left: 443px;
  }
</style>

---

# Why take a hybrid approach?

<div>
  <ul>
    <li v-click="1">Limited quantum resources</li>
    <li v-click="2">Suboptimal results in classical methods</li>
    <li v-click="3">Long runtimes in classical methods</li>
    <li v-click="4">Using the best of both worlds</li>
  </ul>
</div>

<!-- <div class="page-num">
  <SlideCurrentNo /> / <SlidesTotal />
</div> -->

<style>
  li {
    font-size: 23px;
  }
  .page-num {
    position: absolute;
    bottom: 12px;
    left: 47.7%;
  }
</style>

---

# Current Quantum Solutions

<div>
  <ul>
    <li v-click="1">VQE</li>
    <li v-click="2">QAOA</li>
    <li v-click="3">Quantum Annealing <span v-click="4">👈</span></li>
  </ul>
</div>
<!-- <div class="page-num">
  <SlideCurrentNo /> / <SlidesTotal />
</div> -->

<style>
  li {
    font-size: 23px;
  }
  .page-num {
    position: absolute;
    bottom: 12px;
    left: 47.7%;
  }
  .d-wave-img {
    height: 320px;
    width: 300px;
    position: absolute;
    left: 500px;
    bottom: 120px;
  }
</style>

---

<img src="hybrid-solvers.png" />
<p>Source: D-Wave</p>
<!-- <div class="page-num">
  <SlideCurrentNo /> / <SlidesTotal />
</div> -->

<style>
  .page-num {
    position: absolute;
    bottom: 12px;
    left: 47.7%;
  }
  p{
    font-size: 12px;
  }
</style>

---

<img src="hybrid-solver-workflow.png" />
<p>Source: <i>Hybrid Solver for Constrained Quadratic Models - D-Wave White Paper</i></p>
<!-- <div class="page-num">
  <SlideCurrentNo /> / <SlidesTotal />
</div> -->

<style>
  .page-num {
    position: absolute;
    bottom: 12px;
    left: 47.7%;
  }
  p{
    font-size: 12px;
  }
</style>

---
layout: section
---

# Modeling the problem

<!-- <div class="page-num">
  <SlideCurrentNo /> / <SlidesTotal />
</div>

<style>
  .page-num {
    position: absolute;
    bottom: 12px;
    left: 47.7%;
  }
</style> -->

<!-- Notes: -->

---

# Things to consider

<div>
  <ul>
    <li v-click="1">The expected return</li>
    <li v-click="2">Cost of the portfolio</li>
    <li v-click="3">The interactions between stocks</li>
  </ul>
</div>

<!-- <div class="page-num">
  <SlideCurrentNo /> / <SlidesTotal />
</div> -->

<style>
  li {
    font-size: 23px;
  }
  .page-num {
    position: absolute;
    bottom: 12px;
    left: 47.7%;
  }
</style>

---

# The expected return
## Our linear terms and objective function

$$Obj = \sum_{i=1}^{n}{r_ip_ix_i}$$

$r_i$ is the expected monthly return

$p_i$ is the price per share

$x_i$ how many shares to buy

<!-- <div class="page-num">
  <SlideCurrentNo /> / <SlidesTotal />
</div> -->

<style>
  .katex { font-size: 40px; }
  .page-num {
    position: absolute;
    bottom: 12px;
    left: 47.7%;
  }
</style>

---

# The cost of the portfolio
## First constraint

$$C \le B$$

<div class="legend">

  $C$ is the total cost

  $B$ is the maximum budget

</div>

<!-- <div class="page-num">
  <SlideCurrentNo /> / <SlidesTotal />
</div> -->

<style>
  .katex { font-size: 40px; }
  .legend .katex {
    font-size: 28px;
  }
  .page-num {
    position: absolute;
    bottom: 12px;
    left: 47.7%;
  }
</style>

---

# The cost of the portfolio
## First constraint

$$C \le B$$

$$\sum_{i=1}^n{p_ix_i} \le B$$

$p_i$ is the price per share

$x_i$ how many shares to buy

<!-- <div class="page-num">
  <SlideCurrentNo /> / <SlidesTotal />
</div> -->

<style>
  .katex { font-size: 40px; }
  .page-num {
    position: absolute;
    bottom: 12px;
    left: 47.7%;
  }
</style>

---

# The interactions between stocks (Risk)
## Second constraint

$$R \le M$$

<div class="legend">

  $R$ is the risk

  $M$ is the maximum risk

</div>

<!-- <div class="page-num">
  <SlideCurrentNo /> / <SlidesTotal />
</div> -->

<style>
  .katex { font-size: 40px; }
  .legend .katex {
    font-size: 28px;
  }
  .page-num {
    position: absolute;
    bottom: 12px;
    left: 47.7%;
  }
</style>

---

# The interactions between stocks (Risk)
## Second constraint

$$R \le M$$

$$\sum_{i=1}^{n}\sum_{j=1}^{n}{\sigma_{ij}p_ix_ip_jx_j} \le M$$

<div class="legend">

  $\sigma_{ij}$ is the covariance between stocks

  $p_i$ is the price per share

  $x_i$ how many shares to buy

</div>

<!-- <div class="page-num">
  <SlideCurrentNo /> / <SlidesTotal />
</div> -->

<style>
  .katex { font-size: 40px; }
  .legend .katex {
    font-size: 28px;
  }
  .page-num {
    position: absolute;
    bottom: 12px;
    left: 47.7%;
  }
</style>

---
layout: section
---

# Implementing the solution
## Using QPLEX

---

# Creating the model

<div>

```python 
from qplex.library.qmodel import QModel

portfolio_model = QModel('portfolio')
```

</div>

---

# Creating the model
<div>

```python 
from qplex.library.qmodel import QModel

portfolio_model = QModel('portfolio')

stocks = ['AAL', 'AAPL', 'AAP', 'ABBV', 'ABC', 'ABT', ...]
x = portfolio_model.integer_var_list(n, name=lambda index: stocks[index])
```

</div>

---

<div>

## Computing the cost

```python
cost = sum(price[s] * x[index] for index, s in enumerate(stocks))
```

<p>Where <i>price</i> is a dictionary storing the price of each stock</p>

</div>

<div v-click>

## Computing the risk

```python 
risk = 0
for i, s1 in enumerate(stocks):
    for j, s2 in enumerate(stocks):
        coefficient = covariance_matrix[s1][s2] * price[s1] * price[s2]
        risk = risk + coefficient * x[i] * x[j]
```

<p>Where <i>covariance_matrix</i> is a matrix storing the covariance between stocks <i>i,j</i></p>

</div>

<div v-click>

## Computing the returns (the objective function)

```python
returns = 0
for index, stock in enumerate(stocks):
    returns = returns + avg_monthly_returns[stock] * x[index] * price[stock]
```

<p>Where <i>avg_monthly_returns</i> is a dictionary containing the average monthly return of eacth stock</p>

</div>

<style>
  p {
    font-size: 13px;
  }
</style>

---
layout: statement
---
# Demo
