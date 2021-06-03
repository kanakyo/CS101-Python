la=int(input('1.English;2.中文 Please choose your language : ...'))
poi=input('Let me cheer you up! First please tell me your name ……')
times=int(input('Then pls randomly pick an Energy level from 1 to 10 / 1到1o随便选一个烈度：'))
i=0

if int(la)==1:
    while i <len(poi):
        char=poi[i]
        print('Give me a '+char+'! '+char)
        i+=1
    print('WHAT DOES THAT SPELL?')
    for i in range(times):
        print(poi,'♡'*i)
        
    ### English version above is cloned from edX [MITx: 6.00.1x Introduction to Computer Science and Programming Using Python].
    ### Chinese part below is created by me, which, though, is apparently a derivation of the one above ...
    ### will update this dull homework as long as I find new inspiration of cheering people up. 
    
else:
    while i <len(poi):
        char=poi[i]
        print(''+ ' ＼＼\۶•ᴗ•۶'+char + '۶•ᴗ•۶/／／')
        i+=1
    print(poi,'!','天下無敵！⭐')

    for i in range(times):
        print('★'*i,"You're the best！",'☆'*i)