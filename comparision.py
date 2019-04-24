# importing the required module 
import matplotlib.pyplot as plt 
  
# x axis values 
x = [1,2,3,4,5,6,7,8,9,10] 
# corresponding y axis values 
y = [35,32,20,14,3,30,6,20,2,30] 
  
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('busiest places in descending-order') 
# naming the y axis 
plt.ylabel('# of important customers') 
  
# giving a title to my graph 
plt.title('important_customers') 
  
# function to show the plot 
plt.show() 