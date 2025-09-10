from langchain.prompts import PromptTemplate

ad_copy_prompt = PromptTemplate(
    input_variables=["product", "audience", "info"],
    template="""
    Bạn là copywriter marketing.
    Viết nội dung quảng cáo cho sản phẩm {product} dành cho nhóm {audience}.
    Yêu cầu:
    - Ngắn gọn, hấp dẫn (dưới 100 từ).
    - Có CTA (Call To Action).
    - Văn phong trẻ trung, thân thiện.

    Thông tin sản phẩm:
    {info}
    """
)
