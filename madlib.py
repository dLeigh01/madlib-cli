import re

print("""
** Welcome! I'm glad you're here!
** I've got a fun game for you today...
** Madlibs!
** In this game, all you need to do is answer my prompts and I'll give you back a fun scenario!
** Are you ready?
** Let's start!
""")

# strip text from template
def read_template(f):
    with open(f) as file:
        text = file.read()

    return text.strip()

# Parse out prompts and promptless string
def parse_template(str):
    # tuple to return both pieces of requested data
    def pieces(text, prompts):
        stripped = text
        parts = prompts
        return stripped, parts

    new_string = re.sub(r'\{\w+\}', '{}', str)
    new_prompts = re.findall(r'\{\w+\}', str)
    remove_curly_bracers(new_prompts)

    return pieces(new_string, tuple(new_prompts))

# merge the string with the given prompts
def merge(str, prompts):
    return str.format(*prompts)

# removes extra characters from prompts
def remove_curly_bracers(prompts):
    i = 0
    for item in prompts:
        prompts[i] = item.replace('{', '')
        prompts[i] = prompts[i].replace('}', '')
        i += 1

