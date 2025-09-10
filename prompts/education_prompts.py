from langchain.prompts import PromptTemplate

quiz_generate_prompt = PromptTemplate(
    input_variables=["lesson_text"],
    template="""
    Bạn là giáo viên.
    Hãy tạo 3 câu hỏi trắc nghiệm (có 4 đáp án A-D và đáp án đúng) dựa trên nội dung sau:

    {lesson_text}
    """
)
