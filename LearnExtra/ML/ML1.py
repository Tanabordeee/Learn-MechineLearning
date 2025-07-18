import pylab
import matplotlib.pyplot as plt
from sklearn import datasets
digit_dataset = datasets.load_digits()

# แสดงชื่อออกมา
print(digit_dataset.target[1])
# โหลด image มาใส่ สี
pylab.imshow(digit_dataset.images[1] , cmap=pylab.cm.gray_r)
# show รูป image
pylab.show()

# แบบใช้ matplot lib
plt.imshow(digit_dataset.images[1] , cmap=plt.get_cmap("gray"))
plt.show()