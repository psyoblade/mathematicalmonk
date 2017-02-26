## (ML 9.1) Linear regression - nonlinearity via basis functions (기저함수를 통한 비선형성)
1. 단순히 직선/평면의 방정식을 구하는 것보다 일반적인 개념이다
> 2개의 숫자 데이터 집합을 통해 상관관계 혹은 추세를 예측하기 위한 직선의 기울기를 구하는게 전부는 아니라 결과가 곡선이나 평면일 수도 있다는 의미
1. 세상에는 정말 많은 기저함수가 존재하며, 그냥 가져다 쓰면 된다
> Identity, General basis function Pi, Polinomial, Radial, Fourier, Wavelets 등 
1. 선형회귀의 경우 기저함수 자체는 선형성을 가지지 않아도 된다.
> 
1. 새로운 데이터 *x*에 대한 *y*를 예측하는 함수를 선택하는 것이 목적


## (ML 9.2) Linear regression - Definition & Motivation (정의 & 동기)
1. 기저함수를 잘 선택하면 Feature Space 상의 데이터 차원이 낮아질 수 있다
> 일반적으로 ML 에서는 학습을 위한 중요한 데이터의 종류를 특질 혹은 피쳐라 표현하는데, 같은 개념인지는 잘 모르겠다
1. identify 함수를 통해 손쉽게 w를 구할 수도 있다

(ML 9.3) Choosing f under linear regression

(ML 9.4 ~ 9.6) MLE for linear regression

(ML 9.7) Basis functions MLE

