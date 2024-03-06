text = (
    'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
    'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
)

words = text.split()
edited_list = []

for word in words:
    edited_list.append(word + 'ing')

new_text = ' '.join(edited_list)
result_text = new_text.replace(',ing', 'ing,').replace('.ing', 'ing.')
print(result_text)
