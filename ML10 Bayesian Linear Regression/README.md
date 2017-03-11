
## 베이지언 선형회귀
1. 요약
    * MLE을 왜 쓰지 않는가?
        * 과적합(overfitting) 문제가 있다.
    * MAP을 왜 쓰지 않는가?
        * 불확실성(uncertainty) 문제가 있다
    * 그러면 왜 베이지언을 쓰는가?
        * 비용함수(loss function)을 사용하여 결과 y에 대한 예측분포를 최적화 할 수 있다 == (불확실성에 대한 표현이 가능하다)
    * 베이지언 선형회귀는 하이퍼 파라메터인 mean, sigma-sqaure 값이 동적으로 변하며, 랜덤변수라는 점이 특징이다
        * 즉, p(y|d) 에 충실하여 파라메터는 몰라도 입력 데이터에 대한 출력 y값을 예측할 수 있어야 한다

2. 질문
    * 왜 분산의 역수를 precision 이라고 표현하는가?
        * 분산(표준편차)의 경우 커질 경우 데이터의 불확실성 또한 커지게 된다
        * 즉, 작아지는 경우 극값을 갖게 되어 보다 정확한 추정이 가능하며, 분산의 역수를 precision 이라고 표현한다
    * 가우시안 분포 vs. 노말 분포 ?
        * Gaussian Dist. > Normal Dist. > Standard Normal Dist. 순으로 포함관계에 있다
    * w = N(0, b-1I) 의 해석은?
        * vector w 는 서로 독립이고, b-1 많큼의 분산을 모두 가지고 있다.
        * 여기서 covariance 가 없어서 독립이다
    * MLE 구현에서 왜 P(y|wTx, sigam^2) 식에서 mean 대신 wTx 인가?
        * 일반적인 분포 mean 값이 m1 ~ m# 까지 많을 수 있는데 분산은 동일하고 mean 값이 다른 #개를 한 번에 표현하기 위함
    * y = y^ + e 에서 y 는 왜 random variable 인가?
        * y^ 은 일정한 값을 가지더라도 e(입실론) 값이 random variable 이라 가정했으므로 y 또한 random variable 이다
    * 왜 베이지언은 불확실성을 표현할 수 있다고 얘기하는가?
        * 모든 구간에 있어 데이터를 가지고 있지 않은데, MAP의 경우 모든 구간에 동일한 분산을 가정하고 있으나,
        * 베이지언의 경우 구간에 따라 분산값이 다름을 가정하고 있으므로 그 구간에 대한 불확실성을 더 잘 설명할 수 있다
    * 베이지언 방법으로 MAP이 아니라 MLE 방식으로 접근은 안되나?
        * 

## ML 10.1 Bayesian Linear Regression 

## ML 10.2~3 Posterior for linear regression

## ML 10.4~7 Predictive distribution for linear regression

