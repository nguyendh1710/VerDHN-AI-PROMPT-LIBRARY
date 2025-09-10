from prompts.it_support_prompts import ticket_summary_prompt
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

final_prompt = ticket_summary_prompt.format(
    ticket_text="""
    Người dùng báo lỗi: Không thể đăng nhập vào hệ thống CRM.
    Thông báo lỗi: 'Invalid credentials'.
    Người dùng xác nhận đã nhập đúng mật khẩu nhiều lần.
    """
)

print("----- Prompt gửi vào model -----")
print(final_prompt)

print("\n----- Kết quả AI sinh ra -----")
print(llm.predict(final_prompt))
