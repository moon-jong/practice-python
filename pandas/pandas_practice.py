import pandas as pd
s= pd.Series([10, 20, 30, 40, 50])
s

#인덱스와 값
s.index #start 부터 stop-1 까지
s.values #array구조로 값을 출력

#다른 자료형도 포함 가능
s2 = pd.Series(['a', 'b', 'c', 1, 2, 3,])
s2 #dtype이 object로 출력

import numpy as np

s3 = pd.Series([np.nan, 10 ,30])
s3 #0번 index에 결측치 (데이터 없음)

#Series에 인덱스 추가
index_date = pd.Series(['2018-10-07', '2018-10-08', '2018-10-09', '2018-10-10'])
s4 =pd.Series([200, 195, np.nan, 205],index=index_date)
s4 #index에 지정한 값이 들어감

s5 = pd.Series({'국어':100, '영어':95, '수학':90})
s5

#날짜 자동생성
pd.date_range('2018-10-09', '2018-11-1')#10월 9일부터 11월 1일 까지의 날짜 생성
pd.date_range('2019-10-1',periods=7)#끝날짜 정하지 않고 생성
pd.date_range('2019-10-12', periods= 11, freq='2D')

#DataFrame을 이용한 데이터
pd.DataFrame([[1,2,3],[1,2,3],[1,2,3]])

data_list = np.array([[1,2,3],[4,5,6,],[7,8,9]])
data_list
pd.DataFrame(data_list)

#인덱스와 컬럼 지정
data = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
index_date = pd.date_range('2019-10-12',periods=4)
column_list = ['A','B','C']
pd.DataFrame(data,index_date,column_list)

#dictionary를 이용하여 입력
table_data = {'날짜':pd.date_range('2019-09-2',periods=5),
              '지사':['한','미','한','미','한'],
              '고객수':[200,250,400,500,200]}

pd.DataFrame(table_data)
df= pd.DataFrame(table_data,columns=['지사','고객수','날짜'])
df.index
df.values
df.columns


#pandas의 연산

a= pd.Series([1,2,3,4,5,6,7])
b= pd.Series([10,20,30,40,50,60,70])
a + b

a1 = pd.Series([1,2,3,4,5,6,7])
a2 = pd.Series([1,2,3,4,5,6])
a1 + a2 #배열의 크기가 다르더라도 연산이 가능하다 #!마지막 인덱스에 결측치 생성

#DataFrame의 연산
table_data1 = {'A':[1,2,3,4,5], 'B':[10,20,30,40,50],'C':[100, 200, 300, 400, 500]}

table_data1

df1 = pd.DataFrame(table_data1)
df1

table_data2 = {'A':[1,2,3], 'B':[4,5,6], 'C':[7,8,9]}
table_data2

df2 = pd.DataFrame(table_data2)
df2

df1 + df2 #연산 불가능한 곳은 결측치로 남는다.



table_data3 = {'s':[1,2,3], 'B':[4,5,6], 'C':[7,8,9]}

df3 = pd.DataFrame(table_data3)
df2 + df3 #컬럼 이름이 같지 않을 때는 새로운 컬럼을 추가 후 결측치로 생성

#pandas methods로 데이터 분석 예제
table_data4 = {'봄':[256.5, 264.3, 215.9, 223.2, 312.8],
               '여름':[770,567.5,599,387,446],
               '가을':[363,231.2,293,247,281],
               '겨울':[139,59.9,109,108,109]}
column_list1 = ['봄', '여름', '가을', '겨울']
index_list1 = ['2012', '2013', '2014', '2015','2016']
df4 =pd.DataFrame(table_data4, columns=column_list1, index=index_list1)
df4.mean(axis=1)#axis가 1이면 행별로 연산
df4.sum()#axis가 0이면 열별로 연산 default = 0
df4.describe()#DataFrame에 대한 전반적인 정보를  보여준다.


#KTX_Data를 이용한 분석 (이용자 수)
KTX_Data = {'경부선':[39060, 39896, 42005, 43621, 41702, 41266, 32427],
            '호남선':[7313, 6967, 6873, 6626, 8675, 1062, 9228],
            '경전선':[3627, 4168, 4088, 4424, 4606, 4984, 5570],
            '전라선':[309, 1771, 1954, 2244, 3146, 3945, 5766],
            '동해선':[np.nan,np.nan,np.nan,np.nan,2395,3786,6667]}
col_list = ['경부선', '호남선', '경전선', '전라선', '동해선']
idx_list = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
df_KTX = pd.DataFrame(KTX_Data,index=idx_list, columns= col_list)
df_KTX.head()#첫 5개
df_KTX.tail()#뒤어서 5개
df_KTX.head(3)#숫자를 지정하면 원하는 만큼 볼 수 있다.
df_KTX.T#전치행렬
df_KTX.loc['2016','호남선']

#데이터 통합하기 append join merge

#세로방향 append
df1 = pd.DataFrame({'class1':[95,92,98,100], 'class2':[91,93,97,99]})
df1
df2 = pd.DataFrame({'class1':[88,98], 'class2':[99,92]})#두명의 학생이 전학
df1.append(df2)#같은 컬럼에 학생 추가 그러나 기존의 인덱스를 가져옴
df1.append(df2,ignore_index=True)#기존의 인덱스 삭제 후 순차적으로 인덱스 생성
df2 = pd.DataFrame({'class1':[88,99]})
df1.append(df2)#2반에 추가되지 않은 2명은 결측치로 나타남

#가로방향 join
df4= pd.DataFrame({'class3':[93,91,95,98]})#3반 추가
df1.join(df4)#3반이 가로로 추가
df5= pd.DataFrame({'class3':[93,91,95,96,97]})
df1.join(df5)#행의 갯수가 맞지 않으면 추가되는 데이터의 행 버림

#특정 열을 기준으로 통합하기 merge
df_A_B = pd.DataFrame({'판매월':['1월', '2월', '3월', '4월'],'제품A':[100,150,200,130],'제품B':[90,110,140,170]})
df_A_B
df_C_D = pd.DataFrame({'판매월':['1월','2월','3월','4월'], '제품C':[112, 141, 203, 134],'제품D':[90,110,140,170]})
df_A_B.merge(df_C_D)

#how 선택인자
df_left = pd.DataFrame({'key':['A', 'B', 'C'], 'left':[1,2,3]})
df_right = pd.DataFrame({'key':['A','B','D'], 'right':[4,5,7]})
df_left.merge(df_right,how='left')# 왼쪽 데이터는 모두 선택되고 오른쪽 데이터는 공통 key를 갖고 있는 인자만 선택
df_left.merge(df_right,how='right')#오른쪽 데이터 모두 선택, 왼쪽의 데이터는 오른쪽 데이터와 공통 key를 갖고있는 인자만 선택
df_left.merge(df_right,how='inner')#선택된 데이터중 공통 항목만 선택
df_left.merge(df_right,how='outer')#모든 데이터 선택 빈곳은 결측치로 채워짐

######파일 쓰기
f = open('sea_data.csv','w')
f.write('연도,동해,남해,서해,전체\n')
f.write('1996,17.4629,17.2288,14.436,15.9067\n')
f.write('1997,17.4116,17.4092,14.8248,16.6044\n')
f.write('1998,17.5944,18.011,15.2512,16.6044\n')
f.write('1999,18.1495,18.3175,14.8979,16.6284\n')
f.write('2000,17.9288,18.1766,15.0504,16.6178\n')
f.close()

pd.read_csv('sea_data.csv')

pd.read_csv('sea_data.csv',index_col='연도')#index열이 연도로 변경됨

#표형식의 데이터를 파일로 쓰기
df_WH = pd.DataFrame({'Weight':[62, 67, 55, 74],
                      'Height':[165, 177, 160, 180]},
                      index = ['ID_1', 'ID_2', 'ID_3', 'ID_4'])
df_WH.index.name = 'User'
df_WH
bmi = df_WH['Weight']/(df_WH['Height']/100)**2
bmi
#dataFrame에 추가
df_WH['BMI'] =bmi
df_WH

df_WH.to_csv('save_DataFrame.csv')#csv파일 workingdirectory에 저장

#저장시 옵션지정
df_pr = pd.DataFrame({'판매가격': [2000, 3000, 5000, 10000],
                      '판매량': [32, 53, 40, 25]},
                     index=['P1001', 'P1002', 'P1003', 'P1004'])
df_pr.index.name = '제품번호'
df_pr
#txt파일로 저장 및 인코딩 형식, 데이터 필드 변경
df_pr.to_csv('save_Data2.txt', sep=" ", encoding='cp949')
