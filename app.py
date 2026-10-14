import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

# Cấu hình trang Web
st.set_page_config(
    page_title="QUẢN LÝ ĐIỂM SINH VIÊN-", page_icon="🎓", layout="wide"
)

# Yêu cầu 1: Hiển thị tiêu đề
st.title("QUẢN LÝ ĐIỂM SINH VIÊN-")
st.write("---")

# #1 Tạo Dataframe
data = {
    "Tên": [
        " Thư ",
        "Long",
        "Hùng",
        " Nhung",
        " Minh",
        " Ronaldo",
        " Messi",
        " Pogba",
        " Belgei",
        " Kitii",
    ],
    " Điểm chuyên cần ": [10, 10, 9, 9, 8, 8, 7, 7, 6, 6],
    " Điểm giữa Kì ": [6, 6, 7, 7, 8, 8, 9, 9, 10, 10],
    " Điểm cuối kì ": [4, 5, 6, 7, 8, 9, 7, 6, 7, 9],
}
df = pd.DataFrame(data)

# #2 Tính Điểm Tổng Kết
df["Điểm Tổng Kết"] = (
    0.2 * df[" Điểm chuyên cần "]
    + 0.3 * df[" Điểm giữa Kì "]
    + 0.5 * df[" Điểm cuối kì "]
).round(2)


# #3 Xếp loại sinh Viên
def classify_student(score: float) -> str:
  if score >= 8.5:
    return "Giỏi"
  elif score >= 7.0:
    return "Khá"
  elif score >= 5.0:
    return "Trung bình"
  else:
    return "Yếu"


df["Xep_loai"] = df["Điểm Tổng Kết"].apply(classify_student)

# Yêu cầu 2: Hiển thị bảng điểm hoàn chỉnh của 10 sinh viên
st.subheader("📋 Bảng điểm sinh viên")
st.dataframe(df, use_container_width=True)

st.write("---")

# #4 Thống Kê
avg_score = round(df["Điểm Tổng Kết"].mean(), 2)
top_student = df.loc[df["Điểm Tổng Kết"].idxmax()]
lowest_student = df.loc[df["Điểm Tổng Kết"].idxmin()]
passed_count = (df["Điểm Tổng Kết"] >= 5.0).sum()
pass_ratio = (passed_count / len(df)) * 100

# Yêu cầu 3, 4, 5: Hiển thị điểm TB, Cao nhất, Thấp nhất, Số SV đạt
st.subheader("📊 Thống kê kết quả")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Điểm trung bình lớp", f"{avg_score}")
col2.metric("Điểm cao nhất", f"{top_student['Điểm Tổng Kết']}", f"{top_student['Tên'].strip()}")
col3.metric("Điểm thấp nhất", f"{lowest_student['Điểm Tổng Kết']}", f"{lowest_student['Tên'].strip()}")
col4.metric("Số sinh viên đạt (>=5)", f"{passed_count}/{len(df)} ({pass_ratio:.0f}%)")

st.write("---")

# Yêu cầu 6 & 7: Selectbox chọn sinh viên và hiển thị chi tiết
st.subheader("🔍 Tra cứu chi tiết từng sinh viên")
selected_student = st.selectbox("Chọn sinh viên:", df["Tên"])

if selected_student:
  sv_info = df[df["Tên"] == selected_student].iloc[0]

  c1, c2, c3, c4, c5 = st.columns(5)
  c1.info(f"**Chuyên cần:**\n\n### {sv_info[' Điểm chuyên cần ']}")
  c2.info(f"**Giữa kỳ:**\n\n### {sv_info[' Điểm giữa Kì ']}")
  c3.info(f"**Cuối kỳ:**\n\n### {sv_info[' Điểm cuối kì ']}")
  c4.success(f"**Tổng kết:**\n\n### {sv_info['Điểm Tổng Kết']}")
  c5.warning(f"**Xếp loại:**\n\n### {sv_info['Xep_loai']}")

st.write("---")

# #5 Trực quan hóa
st.subheader("📈 Biểu đồ điểm tổng kết của 10 sinh viên")

fig, ax = plt.subplots(figsize=(10, 5))

bars = ax.bar(
    df["Tên"], df["Điểm Tổng Kết"], color="#2b5c8f", edgecolor="black", width=0.55
)

for bar in bars:
  height = bar.get_height()
  ax.text(
      bar.get_x() + bar.get_width() / 2.0,
      height + 0.15,
      f"{height:.2f}",
      ha="center",
      va="bottom",
      fontsize=9,
      fontweight="bold",
  )

ax.set_title(
    "BIỂU ĐỒ ĐIỂM TỔNG KẾT CỦA 10 SINH VIÊN", fontsize=13, fontweight="bold", pad=15
)
ax.set_xlabel("Họ và tên Sinh viên", fontsize=11, labelpad=10)
ax.set_ylabel("Điểm tổng kết (Thang 10)", fontsize=11, labelpad=10)
plt.xticks(rotation=35, ha="right", fontsize=9)
plt.yticks(np.arange(0, 12, 1))
plt.ylim(0, 11)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()

# Yêu cầu 8: Hiển thị biểu đồ bằng lệnh của Streamlit
st.pyplot(fig)

st.write("---")

# Yêu cầu 9: Hiển thị họ tên và MSSV ở cuối trang với chữ nhỏ
st.caption("Người tạo ứng dụng: **Nguyễn Văn A** | MSSV: **12345678**")
