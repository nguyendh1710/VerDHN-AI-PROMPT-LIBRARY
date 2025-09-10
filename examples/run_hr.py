from prompts.hr_prompts import hr_summary_prompt
from langchain.chat_models import ChatOpenAI

# Khởi tạo model
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.3)

# Tạo prompt cuối cùng từ template
final_prompt = hr_summary_prompt.format(
    resume_text="""
    Nguyễn Văn A, 3 năm kinh nghiệm làm Data Analyst tại FPT,
    thành thạo Python, SQL, PowerBI. Tốt nghiệp loại Giỏi ngành Toán Tin,
    có chứng chỉ Google Data Analytics. Đạt giải Nhất cuộc thi phân tích dữ liệu 2022.
    """
)

print("----- Prompt gửi vào model -----")
print(final_prompt)

print("\n----- Kết quả AI sinh ra -----")
print(llm.predict(final_prompt))
