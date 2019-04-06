import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ctx = 'C:/Users/ezen/PycharmProjects/ezen_day1_03/titanic/data/'

train = pd.read_csv(ctx +'train.csv')
test = pd.read_csv(ctx + 'test.csv')

# df = pd.DataFrame(train)
#   컬럼 구하는 코딩
# print(df.columns)


f, ax = plt.subplots(1, 2, figsize=(18, 8))
train['Survived'].value_counts().plot.pie(explode=[0, 0.1],
                                          autopct="%1.1f%%", ax=ax[0], shadow=True)
ax[0].set_title('Survived')
ax[0].set_ylabel('')

sns.countplot('Survived', data=train, ax=ax[1])
ax[1].set_title('Survived')


"""
['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
       'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']    
      
PassengerId 고객아이디
Survived 생존여부    Survival    0 = No, 1 = Yesp
Pclass   생존권 클래스  Ticket class    1 = 1st, 2 = 2nd, 3 = 3rd
Name  이름
Sex    성별 Sex    
Age    나이 Age in years    
SibSp    동반한 형제자매 , 배우자수 # of siblings / spouses aboard the Titanic    
Parch    # of parents / children aboard the Titanic    
Ticket    Ticket number    
Fare    Passenger fare    
Cabin    Cabin number    
Embarked    Port of Embarkation    
C = Cherbourg, Q = Queenstown, S = Southampton\


f , ax = plt.subplots(1,2 , figsize=(18 , 8))
train ['Survived'][train["sex"] == 'male'].value_counts().plot.pie(explode = [0,0,1] ,
                                       autopct="%1.1f%" , ax = ax[0] , shadow = True)
train ['Survived'][train["sex"] == 'Female'].value_counts().plot.pie(explode = [0,0,1] ,
                                       autopct="%1.1f%" , ax = ax[1] , shadow = True)
ax[0].set_title('Survived(male)')
ax[1].set_ylabel('Survived(Female)')

plt.show()


데이터는 훈련데이터 (train.csv) , 테스트 데이터(test.csv) 두가지로 제공됩니다
목적데이터에는 위 항목에서는 survived 정보가 빠져있습니다 
그것은 답 이기 때문입니다 
"""

df_1 = [train['Sex'],train['Survived']]
df_2 = train['Pclass']
df = pd.crosstab(df_1, df_2 , margins=True )
# print(df.head())

"""
Pclass             1    2    3  All
Sex    Survived                    
female 0           3    6   72   81
       1          91   70   72  233
male   0          77   91  300  468
       1          45   17   47  109
All              216  184  491  891
"""
"""
f, ax = plt.sublots(2,2 , figsize=(20 , 15))
sns.countplot('Embarked' , data=train , ax=ax[0,0])
ax=ax[0,0].set_title('No of Passengers Pclass')

sns.countplot('Embarked' , hue='Sex',  data=train , ax=ax[0,1])
ax=ax[0,1].set_title('Male - female for Embarked')

sns.countplot('Embarked' , hue='Survived' , data=train , ax=ax[1,0])
ax=ax[1,0].set_title('Embarked vs survided')

sns.countplot('Pclass' , data=train , ax=ax[1,1])
ax=ax[1,1].set_title('Embarked vs Pclass')

plt.show()

"""
"""
RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
PassengerId    891 non-null int64
Survived       891 non-null int64
Pclass         891 non-null int64
Name           891 non-null object
Sex            891 non-null object
Age            714 non-null float64
SibSp          891 non-null int64
Parch          891 non-null int64
Ticket         891 non-null object
Fare           891 non-null float64
Cabin          204 non-null object
Embarked       889 non-null object
dtypes: float64(2), int64(5), object(5)

PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64

print(train.isnull().sum())
"""

def bar_chart(feature) :
    survived = train[train['Survived'] ==  1 ][feature].value_counts()
    dead = train[train['Survived'] == 0][feature].value_counts()
    df = pd.DataFrame([survived , dead])
    df.index = ['survived' , 'dead']
    df.plot(kind='bar' , stacked=True , figsize=(10,5))
    plt.show()

bar_chart('Sex')
bar_chart('Pclass')
bar_chart('SibSp')
bar_chart('Parch')
bar_chart('Embarked')
