#1 Tạo Dataframe
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# Dữ Liệu Khởi Tạo 10 Sinh Viên
data = {"Tên" :
               [ " Thư ",
                    "Long",
                     "Hùng",
                     " Nhung",
                     " Minh",
                     " Ronaldo",
                     " Messi",
                     " Pogba",
                     " Belgei",
                     " Kitii"],
        " Điểm chuyên cần " : [ 10,10,9,9,8,8,7,7,6,6],
        " Điểm giữa Kì " : [ 6,6,7,7,8,8,9,9,10,10],
        " Điểm cuối kì " : [ 4,5,6,7,8,9,7,6,7,9]
         }
df = pd.DataFrame(data)
print ("--- Bảng Dữ Liệu ---")
display(df)

#2 Tính Điểm Tổng Kết
df["Điểm Tổng Kết"] = (0.2 * df[" Điểm chuyên cần "] + 0.3 * df[" Điểm giữa Kì "] + 0.5 * df[" Điểm cuối kì "]).round(2)

print("--- BẢNG DỮ LIỆU CÓ ĐIỂM TỔNG KẾT ---")
display(df[["Tên", " Điểm chuyên cần ", " Điểm giữa Kì ", " Điểm cuối kì ", "Điểm Tổng Kết"]])

#3 Xếp loại sinh Viên
def classify_student(score: float) -> str:
  """Phân loại học lực dựa trên thang điểm 10."""
  if score >= 8.5:
    return "Giỏi"
  elif score >= 7.0:
    return "Khá"
  elif score >= 5.0:
    return "Trung bình"
  else:
    return "Yếu"

df["Xep_loai"] = df["Điểm Tổng Kết"].apply(classify_student)

print("--- BẢNG DỮ LIỆU HOÀN CHỈNH ---")
display(df)

#4 Thống Kê
# Điểm tổng kết trung bình của lớp
avg_score = round(df["Điểm Tổng Kết"].mean(), 2)

# Sinh viên cao điểm nhất và thấp điểm nhất sử dụng idxmax() / idxmin()
top_student = df.loc[df["Điểm Tổng Kết"].idxmax()]
lowest_student = df.loc[df["Điểm Tổng Kết"].idxmin()]

# Đếm số sinh viên đạt (Điểm tổng kết >= 5.0)
passed_count = (df["Điểm Tổng Kết"] >= 5.0).sum()
pass_ratio = (passed_count / len(df)) * 100

print("--- BẢNG THỐNG KÊ DỮ LIỆU ---")
print(f"• Điểm tổng kết trung bình cả lớp: {avg_score}")
print(
    f"• Sinh viên điểm cao nhất: {top_student['Tên']} ({top_student['Điểm Tổng Kết']} điểm)"
)
print(
    f"• Sinh viên điểm thấp nhất: {lowest_student['Tên']} ({lowest_student['Điểm Tổng Kết']} điểm)"
)
print(
    f"• Số sinh viên đạt (>= 5.0): {passed_count}/{len(df)} sinh viên ({pass_ratio:.0f}%)"
)

#5 Trực quan hóa
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10, 5))

# Vẽ biểu đồ cột
bars = plt.bar(
    df["Tên"], df["Điểm Tổng Kết"], color="#2b5c8f", edgecolor="black", width=0.55
)

# Thêm số điểm chi tiết lên đỉnh mỗi cột
for bar in bars:
  height = bar.get_height()
  plt.text(
      bar.get_x() + bar.get_width() / 2.0,
      height + 0.15,
      f"{height:.2f}",
      ha="center",
      va="bottom",
      fontsize=9,
      fontweight="bold",
  )

# Tùy chỉnh thẩm mỹ biểu đồ
plt.title(
    "BIỂU ĐỒ ĐIỂM TỔNG KẾT CỦA 10 SINH VIÊN",
    fontsize=13,
    fontweight="bold",
    pad=15,
)
plt.xlabel("Họ và tên Sinh viên", fontsize=11, labelpad=10)
plt.ylabel("Điểm tổng kết (Thang 10)", fontsize=11, labelpad=10)
plt.xticks(rotation=35, ha="right", fontsize=9)
plt.yticks(np.arange(0, 12, 1))
plt.ylim(0, 11)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()

# Hiển thị đồ thị
plt.show()