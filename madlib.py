import re

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

    new_string = re.sub(r"(?<={).*?(?=})", '', str)
    new_prompts = re.findall(r"(?<={).*?(?=})", str)

    return pieces(new_string, tuple(new_prompts))

# merge the string with the given prompts
def merge(str, prompts):
    return str.format(*prompts)

# run game
if __name__ == '__main__':
    print("""
    ** Welcome! I'm glad you're here!
    ** I've got a fun game for you today...
    ** Madlibs!
    ** In this game, all you need to do is reply with a word that matches my prompts and I'll give you back a fun scenario!
    ** Are you ready?
    ** Let's start!
    """)

    text = read_template("assets/make_me_a_video_game.txt")
    parsed_text, prompts = parse_template(text)

    responses = []
    for prompt in prompts:
        responses.append(input(prompt + ' > '))

    final = merge(parsed_text, tuple(responses))
    print(final)

    with open('assets/madlib_response.txt', 'w') as file:
        file.writelines(final)