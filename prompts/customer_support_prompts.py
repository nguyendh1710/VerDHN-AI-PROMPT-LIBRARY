from langchain.prompts import PromptTemplate

customer_summary_prompt = PromptTemplate(
    input_variables=["email_text"],
    template="""
    Bạn là nhân viên CSKH.
    Hãy tóm tắt ngắn gọn nội dung email khách hàng gửi bên dưới,
    và phân loại mức độ ưu tiên: Cao, Trung bình, Thấp.

    Email:
    {email_text}
    """
)
