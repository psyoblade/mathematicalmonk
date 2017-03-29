## 추정량의 이해
1. 요약
    * 추정량 및 그 성질 및 관련용어에 대한 이해
    * 추정을 위한 2가지 접근법 (베이지언 vs. 빈도론)


## ML1. Estimators (추정량)
1. 용어의 정의 및 표기법
    * 통계량(statistic)은 데이터에 대한 함수의 결과를 나타내는 확률변수(random variable)다
    * 추정량(estimator)은 데이터를 분포를 나타내는(governing) 파라메터를 근사(approximate) 하기위한 통계량(statistic = r.v.)
        * 추정한 파라메터 theta hat 을 theta 의 추정량(estimator)라 표현한다
    * 표본추출(sampling)에 대한 통계량
        * 평균(mean)은 불편(unbiased)
        * 분산(variance)는 편향(biased) 이지만 아래의 S^2은 비편향(unbiased)이다
        * ![Equation](https://latex.codecogs.com/gif.latex?s%5E%7B2%7D%3D%5Cfrac%7B1%7D%7Bn-1%7D%5Csum_%7Bn%7D%5E%7Bi%3D1%7D%28%7BX%7D_i-%5Cbar%7BX%7D%29%5E2)


## ML 11.2. Decision Theory Terminology (결정 이론 용어)
1. 개요
    * 우리가 공부한 추정량(estimator)과 회귀/분류(regression/classification)에서 논의했던 개념들이 유사한데,
    * 여기서 일반적인 결정이론에서의 용어와의 비교를 통해서 정리할 수 있다
1. 결정이론(general)
    * decision rule delta: 추정량/회귀분석의 개념을 아우르는 일반적인 결정규칙을 말함
    * state s
    * data D
    * action a = delta(D)
    * loss L(s, a)
1. 추정량(estimators)
    * estimator function g
    * param theta
    * data D
    * estimator/estimate theta = g(D): 여기서 추정량(estimator)는 확률변수(random variable), 추정치(estimate)는 정해진 값을 말한다
    * loss L(theta, theta\_hat)
1. 회귀/분류(regression/classification)
    * prediction function f
    * target Y
    * point X
    * prediction y\_hat = f(X)
    * loss L(Y, Y\_hat)


## ML 11.3. Loss & Risk (비용 & 위험 - Bayes Risk)
1. Loss
    * Loss = L(theta, g(D))
    * 일반적인 비용함수는 실제비용(theta) 대비 데이터(D)를 입력으로하는 추정 비용함수(g(D))와의 차이를 말한다
    * 결국 우리는 어떠한 현상을 예측하기 위한 모델링을 하는데 2가지 관점에서 비용함수를 선택할 수 있다
    * 베이지언 관점에서의 손실(Loss)과 빈도론 관점에서의 위험(Risk)이 그것이다
1. Bayesian Expected Loss (베이지언 예측 손실)
    * "We know Data": "데이터를 안다" 라는 말을 "우리는 충분히 많은 데이터가 있고, 이를 알고 있어 prior에 대한 정보가 있다"
    * BayesianExpectedLoss(pi, g(D)) = E(L(theta, g(D))|D): prior 값과 likelihood 함수를 통해서 posterior 를 추정하고 이를 반복하여 예측하는 접근법
        * 여기에서 theta 값은 구해야할 고정된 최종 값이 아니라 추정 과정에서 발생하는 확률변수라고 본다
        * prior 값을 알고 있다고 생각하므로, theta 값을 추정할 수 있다
    * prior를 가정하고, 파라메터 theta 값에 대한 average 값을 추정하는 과정이다
1. Frequentist Risk (빈도론 위험)
    * "We don't know True Pi": "우리는 진정한 prior pi 값을 모른다"는 말은 "데이터가 많건 작건 간에 데이터가 있지만, prior에 대한 정보가 부족하다"
    * FrequentistRisk(theta, g) = E(L(theta, g(D))|theta): theta 값과 likelihood 함수를 통해서 결과를 예측하는 접근법
        * prior 값을 모른다고 생각하므로, 적절한 예측함수 g를 가정하고, theta 값을 추정해야만 한다
        * 여기서 파라메터 theta가 확률변수라고 보지는 않는다
    * 예측함수 g를 가정하고, 데이터 D에 대한 average 값을 추정하는 과정이다
1. Bayes Risk (베이즈 위험)
    * 결국, 베이지언 접근과 빈도론적 접근을 통해서 우리가 원하는 것은 위험을 추정하는 것이고, 이를 통해 예측을 할 수 있다는 것이다
    * BayesRisk(pi, g)
        * Bayes world 를 통해서 averaging over theta 를 
        * Risk world 를 통해서 averaging over data 를 구할 수 있었다
    * 이 두 가지 접근법을 "베이즈 리스크" 정도의 용어로 말할 수 있을 것이다
        * 필요에 따라 어느 쪽을 선택하여 "베이즈 리스크"를 통해 예측을 하는 것이다


## ML 11.4. Choosing a decision rule - Bayesian and frequentist
1. 개요
    * 베이지언과 빈도론자 입장에서의 결정규칙을 선택하는 방법
1. 베이지언 관점
    * Case #1. 데이터를 알고 있을때, 베이지언 추정 비용을 최소화 하기 위한 함수 f(D)를 선택
    * Case #2. a.k.a Conditional Bayes: 데이터를 모를 때, "Bayes Risk"를 최소화 하기 위한 함수 f를 선택하는 것
        * average over D - minimizing expected loss under those average over D and Pi
        * 여기서 베이지언 접근임에도 불구하고, 데이터를 모르는 경우 베이즈 함수를 최소화 하도록 선택해야 한다
1. 빈도주의 관점
    * 선택을 위한 원칙을 가이드해야 한다
        * Unbiaseness
        * Admissibility: 위험 함수간에 전체 theta 데이터의 모든 구간에서 위험함수의 결과가 나은 경우에 위험이 큰 것을 선택할 이유가 없는 것
        * Minimax
        * Invariance


## ML 11.5. Bias-Variance decomposition
1. 개요
    * MSE(mean square error) = bias^2 + var
    * 증명을 통해서 평균 제곱 오류는 bias 제곱과 variance 합으로 분해될 수 있다


## ML 11.6 ~ 7. Inadmissibility
1. 개요
    * 적절하지 않은 추정량을 제외하는 방법 (reject certain estimators)
    * 이상적인 상황(var=1)과 특수한 상황(var=0)을 비교하여 허용성(admissibility)를 설명할 수 있다
        * delta 를 dominate 하는 또 다른 decision rule delta 가 존재한다면, 결정규칙 delta 는 inadmissible 하다 즉, 허용할 수 없다고 말한다
            * 그렇지 않으면 (일부만 inadmissible 한 경우 포함) 모두 admissible 한다 즉, 허용가능하다


## ML 11.8 Bayesian decision theory
1. 개요
    * 



