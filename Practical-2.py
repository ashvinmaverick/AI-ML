import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#NUMPY
#creating an array
arr_1 = np.array( [[ 1, 2, 3],
                 [ 4, 2, 5]] )
print(arr_1)#creating array from list
arr_2= np.array([[1, 2, 4], [5, 8, 7]])
print(arr_2)

#shape,size and elements
print(arr_1.shape)
print(arr_1.size)
print(arr_1.dtype)

#creating array from tupple
arr_3=np.array((23,43,54,65))
print(arr_3)

#creating array with all zeroes
arr_4=np.zeros((3,4))
print(arr_4)

#array with constant no.
arr_5=np.full((3,3),6)
print(arr_5)

#array with random nos.
arr_7=np.random.random((2,2))
print(arr_7)

#arranging array
arr_8=np.arange(0,12,4)
print(arr_8)

#linespace in arrays
arr_9=np.linspace(0,5,3)
print(arr_9)

#adding subtracting multiplying sqauring elements
arr_11=np.array([1,2,3,4,5])
print(arr_11+1)
print(arr_11-2)
print(arr_11*2)
print(arr_11**2)


#maximum and minimum
arr_12=np.array([[1,32,43,54],
                [12,42,43,44],
                [32,87,67,98],
                [11,112,32,43]])
print(arr_12.max(axis=1))
print(arr_12.max(axis=0))

#sum and cumulative sum
print(arr_12.sum())
print(arr_12.cumsum(axis=1))
print(arr_12.cumsum(axis=0))


#adding subracting and multiplying array
arr_13=np.array([[12,42,23,54,],
                [12,54,67,98],
                [3,43,65,78],
               [10,20,30,40]])
print(arr_12 + arr_13)
print(arr_12 - arr_13)
print(arr_12 * arr_13)

#universal functions
arr_14=np.array([0,np.pi/2,np.pi])
print(np.sin(arr_14))
print(np.exp(arr_14))
print(np.sqrt(arr_14))


#sorting an array
arr_15=np.array([[1,2,4],
               [3,5,7],
               [23,43,5]])
print(np.sort(arr_15,axis=None))
print(np.sort(arr_15,axis=1))


#PANDAS
dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221]}

asd = pd.DataFrame(dict)
print(asd)

# Set the index for brics
asd.index = ["BR", "RU", "IN", "CH", "SA"]
print(asd)

#Series
Ser = pd.Series([1, 2, 3, 4, 5])
Ser = pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
print(Ser)

# Import the cars.csv data: cars
cars = pd.read_csv('cars.csv')
print(cars)

cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars['cars_per_cap'])

# Print out country column as Pandas DataFrame
print(cars[['cars_per_cap']])

# Print out DataFrame with country and drives_right columns
print(cars[['cars_per_cap', 'country']])

# Print out first 4 observations
print(cars[0:4])

# Print out fifth, sixth, and seventh observation
print(cars[4:6])
# Print out observation for Japan
print(cars.iloc[2])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']])

#checking how large is our dataframe
cars.shape

#MATPLOTLOB
plt.plot([1,2,3,4],[2,4,6,8])
plt.ylabel('numbers')
plt.show()


plt.plot([1,2,3,4],[10,15,35,70])
plt.ylabel('numbers')
plt.show()


x=np.linspace(0,100,10)
print(x)


y=x**2
print(y)

plt.scatter(x,y)

N_points = 1000
n_bins = 10

x = np.random.randn(N_points)
y = .6*x+np.random.randn(1000)+5

fig, axs = plt.subplots(1, 2, sharey=True)

axs[0].hist(x, bins=n_bins)
axs[1].hist(y, bins=n_bins)

#SEABORN
# Initialize Figure and Axes object
fig, ax = plt.subplots()

# Load in data
tips = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")

# Create violinplot
ax.violinplot(tips["total_bill"], vert=False)

# Show the plot
plt.show()

# Another example using Seaborn
# Load data
titanic = sns.load_dataset("titanic")

# Set up a factorplot
g = sns.factorplot("class", "survived", "sex", data=titanic, kind="bar", palette="muted", legend=False)

# Show plot
plt.show()
