from langchain.prompts import PromptTemplate

ticket_summary_prompt = PromptTemplate(
    input_variables=["ticket_text"],
    template="""
    Bạn là nhân viên IT Support.
    Hãy tóm tắt nội dung ticket bên dưới và gợi ý bước xử lý ban đầu.

    Ticket:
    {ticket_text}
    """
)
