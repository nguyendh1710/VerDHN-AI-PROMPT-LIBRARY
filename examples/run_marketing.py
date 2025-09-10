from prompts.marketing_prompts import ad_copy_prompt
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

final_prompt = ad_copy_prompt.format(
    product="Laptop X",
    audience="Sinh viên",
    info="Pin 12h, màn hình 14 inch, giá từ 12 triệu"
)

print("----- Prompt gửi vào model -----")
print(final_prompt)

print("\n----- Kết quả AI sinh ra -----")
print(llm.predict(final_prompt))
