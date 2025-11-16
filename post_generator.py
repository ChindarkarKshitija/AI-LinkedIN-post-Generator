from http.client import responses

from llm_helper import llm
from few_shot import FewShotPosts


few_shot = FewShotPosts()
few_shot.load_posts("data/processed_posts.json")

def get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"
    if length == "Medium":
        return "6 to 10 lines"
    if length == "Long":
        return "11 to 15 lines"
    return ""

def get_prompt(length, language, tag):

    length_str = get_length_str(length)
    prompt = f'''
    Generate a LinkedIn post using the below information. No preamble.
    
    1. Topic: {tag}
    2. Length: {length}
    3. Language: {language}
    If language is Hinglish then it means it is a mix of Hindi and English. 
    The script for the generated post should always be English.
    '''

    examples = few_shot.get_filtered_posts(length, language, tag)

    if len(examples) > 0:
        prompt += "\n4. Use the writing style as per the following examples."
        for i, post in enumerate(examples):
            prompt += f"\n\nExample {i+1}:\n{post['text']}"
            if i == 1:
                break

    return prompt.strip()


def generate_post(length, language, tag):
    prompt = get_prompt(length, language, tag)
    response = llm.invoke(prompt)
    return response.content

if __name__ == "__main__":
    test_post = generate_post("Short", "English", "Mental Health")
    print(test_post)
