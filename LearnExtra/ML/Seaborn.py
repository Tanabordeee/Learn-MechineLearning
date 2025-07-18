import seaborn as sb 
# seaborn คือ ไลบรารีสำหรับ การวิเคราะห์ข้อมูลเชิงภาพ  ที่ใช้ข้อมูลในรูปแบบ DataFrame (จาก pandas)
# ทำงานอยู่ บนพื้นฐานของ matplotlib (คือใช้ matplotlib อยู่เบื้องหลัง)
import matplotlib.pylab as plt
# โหลดข้อมูลเข้ามา
iris_dataset = sb.load_dataset("iris")
'''
ดึง dataset ดอกไม้ Iris ที่มีอยู่ใน seaborn มาใช้ ซึ่งมี 150 แถว 5 คอลัมน์ :
- sepal_length
- sepal_width
- petal_length
- petal_width
- species → ชื่อพันธุ์ (target label)
'''
# ตั้งค่าธีมกราฟให้สวยงามขึ้น (ใช้ default style ของ seaborn)
sb.set()
# pairplot(...) → แสดงกราฟ scatter plot สำหรับ ทุกคู่ของ features (เช่น sepal_length vs sepal_width, petal_length vs petal_width ฯลฯ)
# hue="species" → ใช้สีแยกประเภทของดอกไม้ (Setosa, Versicolor, Virginica)
# height=2 → กำหนดขนาดของกราฟแต่ละช่อง (เล็กหน่อย)
sb.pairplot(iris_dataset , hue="species" , height=2)
plt.show() # เพราะ ด้านหลัง seaborn ก็คือ matplot lib เลย .show ได้