text = (
    'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
    'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
)

words = text.split()
edited_list = []

for word in words:
    word_without_punctuation = word.strip('.,')
    edited_list.append(word_without_punctuation + 'ing')

print(', '.join(edited_list))
