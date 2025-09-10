from langchain.prompts import PromptTemplate

legal_extract_prompt = PromptTemplate(
    input_variables=["contract_text"],
    template="""
    Bạn là chuyên viên pháp chế.
    Hãy trích xuất các điều khoản quan trọng trong hợp đồng dưới đây:
    - Thời hạn hợp đồng
    - Quyền & nghĩa vụ các bên
    - Điều khoản thanh toán
    - Điều khoản chấm dứt

    Hợp đồng:
    {contract_text}
    """
)
