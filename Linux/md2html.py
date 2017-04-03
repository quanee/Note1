import markdown
import codecs

input_file = codecs.open('UNIXmd.md', mode="r", encoding="utf-8")
text = input_file.read()
html = markdown.markdown(text)

f = open('UNIX.html', 'w', encoding="utf-8")
f.write(html)
f.close()