from langchain.prompts import PromptTemplate

invoice_extract_prompt = PromptTemplate(
    input_variables=["invoice_text"],
    template="""
    Bạn là kế toán viên.
    Hãy trích xuất thông tin từ hóa đơn sau và trả về JSON:
    {{
      "invoice_number": "",
      "supplier": "",
      "date": "",
      "total_amount": "",
      "items": []
    }}

    Hóa đơn:
    {invoice_text}
    """
)

