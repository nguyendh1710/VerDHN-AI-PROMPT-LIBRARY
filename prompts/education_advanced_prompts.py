from langchain.prompts import PromptTemplate

explain_simple_prompt = PromptTemplate(
    input_variables=["concept"],
    template="""
    Bạn là giáo viên.
    Hãy giải thích khái niệm "{concept}" bằng ngôn ngữ đơn giản,
    dễ hiểu cho học sinh lớp 10.
    """
)
