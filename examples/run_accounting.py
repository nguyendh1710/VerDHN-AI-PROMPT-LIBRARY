from prompts.accounting_prompts import invoice_extract_prompt
from langchain.chat_models import ChatOpenAI

# Khởi tạo model
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Tạo prompt cuối cùng từ template
final_prompt = invoice_extract_prompt.format(
    invoice_text="""
    HÓA ĐƠN GTGT
    Số: 000123
    Nhà cung cấp: Công ty TNHH ABC
    Ngày: 05/09/2023
    Tổng cộng: 15.000.000 VND
    Sản phẩm: Laptop Dell XPS 13 - SL: 1 - Giá: 15.000.000 VND
    """
)

print("----- Prompt gửi vào model -----")
print(final_prompt)

print("\n----- Kết quả AI sinh ra -----")
print(llm.predict(final_prompt))
