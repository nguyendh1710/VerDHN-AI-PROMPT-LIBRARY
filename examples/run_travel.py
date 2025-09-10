from prompts.travel_prompts import travel_itinerary_prompt
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.6)

final_prompt = travel_itinerary_prompt.format(
    destination="Đà Nẵng"
)

print("----- Prompt gửi vào model -----")
print(final_prompt)

print("\n----- Kết quả AI sinh ra -----")
print(llm.predict(final_prompt))
