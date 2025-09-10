from langchain.prompts import PromptTemplate

travel_itinerary_prompt = PromptTemplate(
    input_variables=["destination"],
    template="""
    Bạn là chuyên gia du lịch.
    Hãy gợi ý lịch trình du lịch 3 ngày tại {destination},
    bao gồm:
    - Địa điểm tham quan
    - Hoạt động chính
    - Gợi ý món ăn đặc sản
    """
)
