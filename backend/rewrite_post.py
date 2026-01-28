from backend.llm_helper import llm



# -----------------------------
# Rewrite prompt builders
# -----------------------------

def rewrite_hook_prompt(post: str) -> str:
    return f"""
Rewrite ONLY the opening 1–2 lines of the LinkedIn post below.
Make the hook more attention-grabbing.
Do NOT change the rest of the post.

Post:
{post}
"""


def rewrite_cta_prompt(post: str) -> str:
    return f"""
Rewrite ONLY the last 2–3 lines of the LinkedIn post below.
Add a clear, natural call-to-action.
Do NOT change the rest of the post.

Post:
{post}
"""


def rewrite_shorten_prompt(post: str) -> str:
    return f"""
Rewrite the LinkedIn post below to be around 30% shorter.
Preserve the core message and tone.

Post:
{post}
"""


def rewrite_bold_prompt(post: str) -> str:
    return f"""
Rewrite the LinkedIn post below to sound more confident and opinionated.
Do NOT make it aggressive or negative.

Post:
{post}
"""

# -----------------------------
# Public rewrite functions
# -----------------------------

def improve_hook(post: str) -> str:
    response = llm.invoke(rewrite_hook_prompt(post))
    return response.content


def strengthen_cta(post: str) -> str:
    response = llm.invoke(rewrite_cta_prompt(post))
    return response.content


def shorten_post(post: str) -> str:
    response = llm.invoke(rewrite_shorten_prompt(post))
    return response.content


def make_bold(post: str) -> str:
    response = llm.invoke(rewrite_bold_prompt(post))
    return response.content