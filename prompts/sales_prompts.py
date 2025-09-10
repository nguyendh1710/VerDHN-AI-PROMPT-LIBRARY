from langchain.prompts import PromptTemplate

sales_email_prompt = PromptTemplate(
    input_variables=["product", "audience"],
    template="""
    Bạn là nhân viên Sales.
    Hãy viết một email chào hàng ngắn gọn cho sản phẩm {product},
    hướng đến nhóm khách hàng {audience}.
    Email cần:
    - Giới thiệu sản phẩm
    - Lợi ích chính
    - CTA khuyến khích phản hồi
    """
)
