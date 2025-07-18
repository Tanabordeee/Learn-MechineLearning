# แบ่งข้อมูลเพื่อทดสอบ
from sklearn.datasets import load_iris # โหลด dataset iris
from sklearn.model_selection import train_test_split # ใช้ในการแบ่งข้อมูล Training Set กับ Test Set

iris_dataset = load_iris()
# (150, 4) 150 = แถว และ 4 = หลัก
print(iris_dataset.data.shape)
# ต้องแบ่งข้อมูลเป็น 2 แบบคือ Train Set กับ Test Set
# 75% Train Set และ 25% Test Set
# แบ่ง x train สำหรับ train ในแนวแกน x และ x_test สำหรับ ทำสอบในแนวแกน x
# ทำเหมือนกันกับ ข้อมูลในแนวแกน y
# random_state = ตัวควบคุมการสุ่มแบ่งข้อมูล ถ้าเป็น 0 จะสุ่มได้เหมือนเดิมทุกครั้ง แต่ถ้าเป็น 42 หรือ เลขอื่น ข้อมูลจากการแบ่งจะหน้าตาไม่เหมือนเดิม
x_train , x_test , y_train , y_test = train_test_split(iris_dataset["data"] , iris_dataset["target"] , test_size=0.2, random_state=0) 
# X (features)	ข้อมูลนำเข้า เช่น ขนาดดอกไม้
# y (labels/target)	คำตอบที่ต้องการให้โมเดลทาย
# iris_dataset["data"] เป็นของ แกน x 
# iris_dataset["target"] เป็นของ แกน y
# ถ้าไม่ระบุในการแบ่งตัว defalut จะเป็๋น 75% กับ 25%
# ถ้าใส่ test_size=0.2 แปลว่า ตัว test จะ 20% แล้ว Train = 80%
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)