import numpy as np


#정수만 존재시 어레이에 정수형으로 구성
data_1 = [0, 1, 2, 3, 4, 5]
a1 = np.array(data_1)
a1

#정수형과 실수형이 동시에 들어가 있을 때 실수형으로 출력
data_2 = [0.1, 5, 6, 7, 8]
a2 = np.array(data_2)
a2

#데이터 타입 확인
a1.dtype #int32
a2.dtype #float64

#다차원 배열 생성
np.array([[1,2,3],[4,5,6],[7,8,9]])

#범위지정 생성 np.aragne(start, stop, step)
arr_obj = np.arange(0, 10, 3)
arr_obj
np.arange(1,10)#기본스텝은 1
np.arange(10)#기본 start는 0
np.arange(10.1)#실수형으로 리턴

#reshape as matrix
np.arange(12).reshape(4,3)
np.arange(11).reshape(4,3)#범위와 행렬 원소의 갯수가 일치해야 한다.

#배열형태 알아보기 #obj = np.aragne(x).reshape(y,z).shape
c = np.arange(12).reshape(4,3)
c.shape

#열이 없을 때
b = np.arange(5)
b
b.shape #1차원 5개의 원소 출력값 == (5,)

#Numpy 배열생성 #linspace(start, stop , n개) start부터 stop까지 n개의 Numpy배열
np.linspace(1, 10, 10)
np.linspace(1, 10, 100)#갯수/num

np.linspace(0, np.pi, 10)

#0과 1배열
np.zeros((2,5))
np.zeros(10)
np.ones(110)
np.ones((5,6))

#단위행렬 생성
np.eye(5)

#문자열 array
np.array(['1,,5', '4545', '재댜러', '343434'])
np.array(['1.5', '4545', '재댜러', 343434])#데이터 타입이 섞일 수도 있다.

#데이터 타입 변환
a= np.array(['1.5', '4545', '121', '343434'])
b= a.astype(float)
b
a= np.array(['1.5', '4545' , 343434])
c= a.astype(float)#문자열만 실수형으로 변환

a.dtype#<U6
c.dtype#float64

#난수생성
np.random.rand()#0-1까지의 난수생성
np.random.rand(2,3,4)#3차원 배열의 array생성
np.random.randint(1,10,(3,4))#3*4행렬로 1-10까지의 정수

#배열 연산
arr1 = np.random.randint(10,size=(3,4))
arr2 = np.random.randint(10,size=(3,4))
arr2
arr1 - arr2
arr2 **2#성분별로 제곱
arr1 * arr2#성분끼리 곱한다.
arr1/arr2#성분끼리 나눈다
arr2 >= 5#논리연산
a= arr2 >= 5

#통계연산
arr3 = np.arange(10)
arr3.sum()
arr4 = [arr3.sum(),arr3.max(),arr3.mean(),arr3.std(),arr3.var()]
arr4

#행렬연산
A = np.arange(4).reshape(2,2)
A
B = np.array([3, 2, 0, 1]).reshape(2,2)
B
A.dot(B) #dot-product
np.dot(A,B)

np.transpose(A)#전치행렬
np.linalg.inv(A)#역행렬
np.linalg.det(A)#역행렬 derterminant

#배열 인덱싱

#1차원 배열 인덱싱
a1= np.array([0, 10, 20, 30, 40, 50])
a1[1]
a1[[1,3,4]]
#2차원 배열의 인덱싱 #obj[행위치,열위치] ****모든 인덱스는 0부터 시작
a1= np.array([0, 10, 20, 30, 40, 50]).reshape(3,2)
a1[2,1]#성분 추출
a1[1]#행 추출
a1[:,1]#열 추출
a1
#배열의 슬라이싱
b1 = np.array([1, 2, 3, 4, 5, 6, 7])
b1[1:4]#1번째 인덱스부터 끝 위치 -1 인덱스
b1[:4]#0번쨰 인덱스 부터 끝위치-1 인덱스까지
b1[2:]#2번째 부터 배열의 끝까지

