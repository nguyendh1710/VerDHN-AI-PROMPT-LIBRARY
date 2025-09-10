from langchain.prompts import PromptTemplate

medical_summary_prompt = PromptTemplate(
    input_variables=["patient_record"],
    template="""
    Bạn là bác sĩ.
    Hãy tóm tắt hồ sơ bệnh án bên dưới thành:
    - Thông tin cơ bản
    - Chẩn đoán chính
    - Thuốc đã kê
    - Lịch hẹn tiếp theo

    Hồ sơ bệnh án:
    {patient_record}
    """
)
