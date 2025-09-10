from prompts.healthcare_prompts import medical_summary_prompt
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

final_prompt = medical_summary_prompt.format(
    patient_record="""
    Bệnh nhân: Trần Văn B, 45 tuổi.
    Chẩn đoán: Tiểu đường type 2.
    Thuốc: Metformin 500mg ngày 2 lần.
    Hẹn tái khám: 20/09/2023.
    """
)

print("----- Prompt gửi vào model -----")
print(final_prompt)

print("\n----- Kết quả AI sinh ra -----")
print(llm.predict(final_prompt))
