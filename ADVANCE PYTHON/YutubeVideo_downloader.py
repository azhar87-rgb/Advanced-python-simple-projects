from pytube import YouTube
Link="https://www.youtube.com/watch?v=Sdgag7RG2l4"
vid=YouTube(Link)
# video=vid.streams.filter(only_audio=True)
video=vid.streams.all()
task=list(enumerate(video))
for i in task:
    print(i)
print()
str=int(input("enter: "))
video[str].download()
print("Succesfully Downloaded..")