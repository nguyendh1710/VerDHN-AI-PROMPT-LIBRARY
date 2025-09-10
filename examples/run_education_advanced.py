from prompts.education_advanced_prompts import explain_simple_prompt
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.3)

final_prompt = explain_simple_prompt.format(
    concept="Trí tuệ nhân tạo (Artificial Intelligence)"
)

print("----- Prompt gửi vào model -----")
print(final_prompt)

print("\n----- Kết quả AI sinh ra -----")
print(llm.predict(final_prompt))
