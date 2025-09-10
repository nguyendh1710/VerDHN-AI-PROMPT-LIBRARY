from prompts.ecommerce_prompts import product_description_prompt
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

final_prompt = product_description_prompt.format(
    product_name="Điện thoại XPhone 12",
    features="Màn hình OLED 6.1 inch, Camera kép 48MP, Pin 4000mAh, Hỗ trợ 5G"
)

print("----- Prompt gửi vào model -----")
print(final_prompt)

print("\n----- Kết quả AI sinh ra -----")
print(llm.predict(final_prompt))
