from langchain.prompts import PromptTemplate

product_description_prompt = PromptTemplate(
    input_variables=["product_name", "features"],
    template="""
    Bạn là content writer cho website thương mại điện tử.
    Hãy viết mô tả hấp dẫn cho sản phẩm {product_name},
    dựa trên các đặc điểm sau: {features}.
    Văn phong ngắn gọn, thu hút, khuyến khích mua hàng.
    """
)
