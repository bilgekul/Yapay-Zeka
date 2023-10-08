import pandas as pd
import numpy as np
data = pd.read_csv(r'C:\Users\pegas\OneDrive\Masaüstü\Lab Uygulama I\Veriler.csv')
print("Before deleting column \n")
print(pd.DataFrame(data=data))
print("Column silinmeden önce info: ",pd.DataFrame(data=data).describe(),sep="\n")
new_data = data.drop(['Sıcaklık','Nem'],axis=1)
print("After deleting column \n")
print(pd.DataFrame(data=new_data))
print("Column silindikten sonra info: ",pd.DataFrame(data=new_data).describe(),sep="\n")

arr = np.zeros([3,4])
print("default boyutlu matris: ",arr,sep="\n")
new_arr = arr.reshape(6,2)
print("yeniden boyutlanmış matris: ",new_arr,sep="\n")

random_arr1 = np.random.randn(3,3)
random_arr2 = np.random.randn(3,3)

vertical_stack = np.vstack((random_arr1,random_arr2))
horizonal_stack = np.hstack((random_arr1,random_arr2))

print("dikey istifleme: ",vertical_stack,sep="\n")
print("yatay istifleme: ",horizonal_stack,sep="\n")