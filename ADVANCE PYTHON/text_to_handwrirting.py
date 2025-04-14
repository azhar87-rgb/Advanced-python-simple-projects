import pywhatkit as pw
txt= "Python is a very popular general-purpose interpreted, interactive,object-oriented, and high-level programming language"
pw.text_to_handwriting(txt,"demo1.png",[0,0,138])
print("END")