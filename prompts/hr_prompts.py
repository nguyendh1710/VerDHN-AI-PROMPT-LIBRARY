from langchain.prompts import PromptTemplate

hr_summary_prompt = PromptTemplate(
    input_variables=["resume_text"],
    template="""
    Bạn là chuyên viên tuyển dụng.
    Hãy tóm tắt CV sau thành 5 gạch đầu dòng, tập trung vào:
    - Kinh nghiệm
    - Kỹ năng
    - Học vấn
    - Thành tích nổi bật

    CV:
    {resume_text}
    """
)
