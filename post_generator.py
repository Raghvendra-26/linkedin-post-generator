from llm_helper import llm
from few_shot import FewShotPosts

few_shot = FewShotPosts()


def get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"
    elif length == "Medium":
        return "6 to 10 lines"
    elif length == "Long":
        return "11 to 15 lines"
    
    
def get_prompt(length,language,tag):
    length_str = get_length_str(length)
    
    prompt = f'''
    Generate a LinkedIn post using the below information. No preamble.
    1. Topic : {tag}
    2. Language : {language}
    3. Length : {length_str}
    If language is Hinglish then it means it is a mix of Hindi and English.
    The script for the generated post should always be in English
    '''
    
    examples = few_shot.get_filtered_posts(length,language,tag)
    
    if len(examples) > 0:
        prompt += "4. Use the writing style as per the following examples."
        for i,post in enumerate(examples):
            post_text = post['text']
            prompt += f"\n\n Example {i+1}: \n\n {post_text}"
            
            if i==1:
                break
    
    return prompt


def audience_modifier(audience):
    audience_context = {
        "Student": "use simple language and a learning mindset",
        "Fresher": "be growth-oriented and opportunity-seeking",
        "Professional": "share experience-backed insights",
        "Founder": "focus on leadership, vision, and execution",
        "Recruiter": "emphasize talent, hiring, and culture"
    }
    context = audience_context.get(
        audience,
        "maintain a professional and neutral tone"
    )
    return (
        f"5. Target audience: {audience}. "
        f"6. Writing guidelines: {context}."
    )
    

def goal_modifier(goal):
    goal_context = {
        "Job Search": "highlight skills, intent, and openness to opportunities",
        "Personal Branding": "build credibility and long-term consistency",
        "Thought Leadership": "share clear opinions and original insights",
        "Hiring": "communicate clarity, trust, and expectations",
        "Networking": "encourage meaningful professional connections"
    }

    context = goal_context.get(
        goal,
        "focus on delivering value to the reader"
    )

    return (
        f"7. Post objective: {goal}. "
        f"8. Content focus: {context}."
    )


def style_modifier(style):
    style_prompts = {
        'Conversational' : '''
            Guidelines:
                - Use simple, natural language.
                - Keep sentences short and punchy.
                - Write as if speaking to a colleague.
                - Use rhetorical questions where appropriate.
                - Avoid jargon and formal phrasing.x    
                - Maintain a friendly and approachable tone.''',
        'Corporate' : '''
            Guidelines:
                - Use formal and professional language.
                - Maintain a clear and structured flow.
                - Avoid slang, emojis, or casual expressions.
                - Focus on clarity, credibility, and precision.
                - Write with an executive or enterprise audience in mind.''',
        'Storytelling' : '''
            Guidelines:
                - Start with a relatable situation or experience.
                - Build a clear narrative flow (context → insight → takeaway).
                - Use first-person perspective where appropriate.
                - Keep the story realistic and concise.
                - End with a reflective or actionable takeaway.''',
        'Data-driven' : '''
            Guidelines:
                - Structure content using clear points or sections.
                - Reference trends, observations, or patterns.
                - Use numbers or facts when relevant (avoid fabricating statistics).
                - Maintain an objective and analytical tone.
                - Minimize emotional or subjective language.''',
        'Bold' : '''
            Guidelines:
                - Open with a strong or unconventional statement.
                - Challenge common assumptions respectfully.
                - Take a clear stance or opinion.
                - Keep the tone confident, not aggressive.
                - Support claims with reasoning or experience.'''
    }

    context = style_prompts.get(
        style,
        "Use a clear, professional, and engaging writing style."
    )
    
    return (
        f"9. {context}"
    )
    
 
def add_emoji():
    return '''
        Emoji usage:
        - Add a small number of relevant emojis to highlight key ideas.
        - Emojis should enhance readability, not distract.
        - Prefer insight-focused emojis (💡📌🚀📊).
        - Limit emoji usage to important lines only.
        - If writing style is Corporate, minimize emoji usage further.
        '''
       
       
def add_hashtags():
    return '''
        Hashtag instructions:
        - Generate 3–6 relevant hashtags based on the topic, audience, and goal.
        - Include at least one niche or role-specific hashtag.
        - Avoid vague hashtags like #Success or #Motivation unless clearly relevant.
        - Place all hashtags at the end of the post.
        - Use professional LinkedIn-style hashtags only.
        '''
       
              
def generate_post(length,language,tag,audience,goal,style,emoji,hashtags):
    prompt = get_prompt(length,language,tag)
    
    prompt += audience_modifier(audience)
    prompt += goal_modifier(goal)
    prompt += style_modifier(style)
    
    if emoji:
        prompt += add_emoji()
    
    if hashtags:
        prompt += add_hashtags()
    
    # return prompt

    response = llm.invoke(prompt)
    return response.content
    
    
if __name__ == "__main__":
    post = generate_post("Medium","English","Skills",'Student','Personal Branding','Corporate',True,True)
    print(post)