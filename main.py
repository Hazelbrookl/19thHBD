import streamlit as st
import pandas as pd
import json

if __name__ == "__main__":

    st.set_page_config(
        page_title="Happy Birthday to LSW",
        page_icon="pic.jpg",
        layout="wide",
    )

    st.markdown('<h1 style="color: #db5bcd;text-align: center;white-space: nowrap;">🎉🎂LSW\'s 19th Birthday🎂🎉', unsafe_allow_html=True)

    tab_words, tab_music = st.tabs(["Words","Music"])

    with tab_words:
        st.markdown('<h1 style="text-align: center;white-space: nowrap;">🎈🎊🎈🎊🎈🎊🎈🎊🎈🎊🎈🎊🎈🎊🎈', unsafe_allow_html=True)
        st.markdown('<h2 style="text-align: center;white-space: pre;">生日快乐 Happy Birthday!', unsafe_allow_html=True)
        st.markdown('<div style="color: #FFCCDE;text-align: center">因为知道你过生日的时候就回家去了，所以琢磨了一下，想到可以稍微用上一点专业技能，\
                    弄个可以远程给你的小惊喜。于是草草写了这个网页，很潦草很简陋，但是能在网络上永久地留下一小片空间，也算有些意思</div>', unsafe_allow_html=True)
        st.markdown('<h1 style="text-align: center;">', unsafe_allow_html=True)
        st.markdown('<div style="color: #FFC0CB;text-align: center">前几天恰巧看了一下日历，发现今年你的阳历和阴历生日是同一天。阴历虽然19年就轮一圈，但是大部分时候都会偏差一两天，\
                    我翻了一下只有06年你前后这几个月出生的人正好日子能赶到一起，而且38、57岁的时候也都赶上了，还挺幸运的，我好像要76岁才能赶上，所以要好好庆祝啊</div>', unsafe_allow_html=True)
        st.markdown('<h1 style="text-align: center;">', unsafe_allow_html=True)
        st.markdown('<div style="color: #FF69B4;text-align: center">期末周的时间是够赶的，刚回去这两天肯定还累得慌吧。这个学期下来感觉你整个就是很辛苦，不停在忙各种事情，真得好好歇歇。\
                    在学校就是这样，每天累呼呼的，精神状态很不稳定的同时心情又忽上忽下的哈哈哈哈哈，不过后面会好起来的，累和烦在所难免，但学会把它们甩开之后就很爽很开心😁</div>', unsafe_allow_html=True)   
        st.markdown('<h1 style="text-align: center;">', unsafe_allow_html=True)
        st.markdown('<div style="color: #FF4D94;text-align: center">之前好几次已经感觉到你归心似箭了，确实回去有家人和好多朋友的感觉好幸福😿我现在很多朋友都出国了，想找都找不到什么人，\
                    以前成天一起玩的时候从来没想到有天会这样，所以家人也好朋友也好，趁着现在一定要好好珍惜，多见多玩😭😭😭</div>', unsafe_allow_html=True)
        st.markdown('<h1 style="text-align: center;">', unsafe_allow_html=True)
        st.markdown('<div style="color: #8A2BE2;text-align: center">点开上面的<span style="color: #db5bcd;font-size: 28px;font-weight: bold;">Music</span>去听一下里面的歌！最近正好有一丝丝灵感，就胡乱写了个曲子出来，\
                    结果这两天又感冒，降好多key还是够呛，就凑合听吧！写完感觉好像比较幼稚，最后一点是单独加上的，不知道你会不会喜欢哈哈哈</div>', unsafe_allow_html=True)   
        st.markdown('<h1 style="text-align: center;">', unsafe_allow_html=True)
        st.markdown('<div style="color: #C71585;text-align: center">最后，祝你生日快乐，19岁的每天都有开心的事发生！</div>', unsafe_allow_html=True)  
        st.markdown('<h1>🥳🕯️🍰🎁', unsafe_allow_html=True)
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: pre;font-size: 6pt">🔥                              🔥         </h4>', unsafe_allow_html=True)
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: pre;font-size: 6pt">|                                   |         </h4>', unsafe_allow_html=True)
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: pre;font-size: 6pt">🔴🔴            🔵🔵🔵🔵🔵</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: pre;font-size: 6pt">🔴🔴            🔵                     🔵</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: pre;font-size: 6pt">🔴🔴            🔵                     🔵</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: pre;font-size: 6pt">🔴🔴            🔵🔵🔵🔵🔵</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: pre;font-size: 6pt">🔴🔴                                     🔵</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: pre;font-size: 6pt">🔴🔴                                     🔵</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: pre;font-size: 6pt">🔴🔴            🔵🔵🔵🔵🔵</h4>', unsafe_allow_html=True)  
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: pre;font-size: 6pt">|                                   |         </h4>', unsafe_allow_html=True)
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: nowrap;font-size: 6pt">                                ⚪⚪⚪⚪⚪⚪</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: nowrap;font-size: 6pt">                     ⚪⚪⚪⚪⚪🍓🍓🍓🍓🍓⚪⚪⚪⚪⚪⚪</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: nowrap;font-size: 6pt">             ⚪⚪⚪🍓🍓🍓🍓⚪⚪⚪⚪⚪⚪⚪🍓🍓🍓🍓⚪⚪⚪⚪</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: nowrap;font-size: 6pt">        ⚪⚪🍓🍓🍓⚪⚪⚪⚪⚪🍓🍓🍓🍓🍓⚪⚪⚪⚪⚪🍓🍓🍓⚪⚪⚪</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: nowrap;font-size: 6pt">     ⚪🍓🍓⚪⚪⚪⚪⚪⚪🍓⚪⚪⚪⚪⚪⚪⚪🍓⚪⚪⚪⚪⚪⚪🍓🍓⚪⚪</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: nowrap;font-size: 6pt">   ⚪🍓🍓⚪⚪⚪⚪⚪🍓⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪🍓⚪⚪⚪⚪⚪⚪🍓🍓⚪⚪</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: nowrap;font-size: 6pt">  ⚪⚪🍓🍓⚪⚪⚪⚪⚪🍓⚪⚪⚪⚪⚪⚪⚪⚪⚪🍓⚪⚪⚪⚪⚪⚪⚪🍓🍓⚪⚪</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: nowrap;font-size: 6pt">  ⚪⚪⚪🍓🍓⚪⚪⚪⚪⚪⚪🍓⚪⚪⚪⚪⚪⚪🍓⚪⚪⚪⚪⚪⚪⚪🍓🍓⚪⚪⚪</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: nowrap;font-size: 6pt">  🟡🟡⚪⚪🍓🍓🍓⚪⚪⚪⚪⚪⚪🍓🍓🍓🍓⚪⚪⚪⚪⚪⚪⚪🍓🍓⚪⚪⚪🟡🟡</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: nowrap;font-size: 6pt">  ⚪🟡🟡⚪⚪⚪⚪🍓🍓🍓🍓⚪⚪⚪⚪⚪⚪⚪⚪⚪🍓🍓🍓🍓⚪⚪⚪⚪🟡🟡⚪</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: nowrap;font-size: 6pt">  ⚪⚪🟡🟡⚪⚪⚪⚪⚪⚪⚪🍓🍓🍓🍓🍓🍓🍓🍓🍓⚪⚪⚪⚪⚪⚪⚪🟡🟡⚪⚪</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: nowrap;font-size: 6pt">  ⚪⚪🟠🟠🟡🟡⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪🟡🟡🟠🟠⚪⚪</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: nowrap;font-size: 6pt">  ⚪⚪⚪⚪⚪⚪🟡🟡⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪🟡🟡⚪⚪⚪⚪⚪⚪</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: nowrap;font-size: 6pt">   ⚪⚪⚪⚪⚪⚪🟠🟠🟡🟡⚪⚪⚪🟠🟠🟠🟠🟠⚪⚪⚪🟡🟡🟠🟠⚪⚪⚪⚪⚪</h4>', unsafe_allow_html=True)         
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: nowrap;font-size: 6pt">       ⚪⚪⚪⚪⚪⚪⚪⚪🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡⚪⚪⚪⚪⚪⚪⚪⚪</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: nowrap;font-size: 6pt">            ⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: nowrap;font-size: 6pt">                 ⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: nowrap;font-size: 6pt">                        ⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪</h4>', unsafe_allow_html=True) 
        st.image("pic.jpg", width=200)
        st.markdown('<div>（。真的一眼相中这只兔子）</div>', unsafe_allow_html=True)

    with tab_music:
        st.markdown('<h1 style="color: #db5bcd;text-align: center;white-space: nowrap;">🎶🎇🎶🎇🎶🎇🎶🎇🎶🎇🎶🎇🎶🎇🎶', unsafe_allow_html=True)
        st.markdown('<h2 style="text-align: center;white-space: pre;">生日歌 Song for you', unsafe_allow_html=True)
        st.markdown('<h4 style="text-align: center;white-space: pre;">Light Shines Wind Blows', unsafe_allow_html=True)

        audio_file = open('Record.wav', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/wav')
        col1, col2 = st.columns(2)
        with open("Drafts.pdf", "rb") as file:
            btn = col1.download_button(
                label=f"Download drafts",
                data=file,
                file_name="19th&1stHBD.pdf",
                mime="application/pdf"
            )
        with open("Record.mp3", "rb") as file:
            btn = col2.download_button(
                label=f"Download mp3",
                data=file,
                file_name="Light_Shines_Wind_Blows.mp3",
                mime="audio/mp3"
            )

        st.markdown('<div style=\'text-align: center;\'>夜只是保护色 仍期盼光 几秒钟</div>', unsafe_allow_html=True)
        st.markdown('<div style=\'text-align: center;\'>花在等待结果 请仔细听 每阵风</div>', unsafe_allow_html=True)
        st.markdown('<div style=\'text-align: center;\'></div>', unsafe_allow_html=True)
        st.markdown('<div style=\'text-align: center;\'>青春生命就像那心灵唱歌</div>', unsafe_allow_html=True)
        st.markdown('<div style=\'text-align: center;\'>空气安静时不妨呼吸片刻</div>', unsafe_allow_html=True)
        st.markdown('<div style=\'text-align: center;\'>伴月的金星 身影也难以捕捉</div>', unsafe_allow_html=True)
        st.markdown('<div style=\'text-align: center;\'>它在这</div>', unsafe_allow_html=True)
        st.markdown('<div style=\'text-align: center;\'></div>', unsafe_allow_html=True)
        st.markdown('<div style=\'text-align: center;\'>其实不止漆黑 有好多颜色</div>', unsafe_allow_html=True)
        st.markdown('<div style=\'text-align: center;\'>走遍花田 最美的芬芳永远开在角落</div>', unsafe_allow_html=True)
        st.markdown('<div style=\'text-align: center;\'></div>', unsafe_allow_html=True)
        st.markdown('<div style=\'text-align: center;\'>不见的 不舍的 留在回忆中忐忑</div>', unsafe_allow_html=True)
        st.markdown('<div style=\'text-align: center;\'>不怕了 不哭了 看所有的故事曲折</div>', unsafe_allow_html=True)
        st.markdown('<div style=\'text-align: center;\'>把剧本里过多猜测都烧成一把火</div>', unsafe_allow_html=True)
        st.markdown('<div style=\'text-align: center;\'>照亮了心窝</div>', unsafe_allow_html=True)
        st.markdown('<div style=\'text-align: center;\'></div>', unsafe_allow_html=True)
        st.markdown('<div style=\'text-align: center;\'>打开窗帘才发现 今天傍晚光线很美</div>', unsafe_allow_html=True)
        st.markdown('<div style=\'text-align: center;\'>来不及去道别 就奔向旷野肆意飞跑追着风儿吹</div>', unsafe_allow_html=True)
        st.markdown('<div style=\'text-align: center;\'></div>', unsafe_allow_html=True)
        st.markdown('<div style=\'text-align: center;\'>不安的 不可的 我宁愿就都算了</div>', unsafe_allow_html=True)
        st.markdown('<div style=\'text-align: center;\'>伤心原因 可惜忘了 没有什么瞬间再让我停格</div>', unsafe_allow_html=True)
        st.markdown('<div style=\'text-align: center;\'>不管了 不要了 种种顾虑缠着路途坎坷</div>', unsafe_allow_html=True)
        st.markdown('<div style=\'text-align: center;\'>一直相信 无知的无畏了 没烦恼地活着就足够了</div>', unsafe_allow_html=True)
        st.markdown('<div style=\'text-align: center;\'>请记得答应过</div>', unsafe_allow_html=True)
        st.markdown('<div style=\'text-align: center;\'></div>', unsafe_allow_html=True)
        st.markdown('<div style=\'text-align: center;\'>雨空中流的河 织成了网 裹着风</div>', unsafe_allow_html=True)
        st.markdown('<div style=\'text-align: center;\'>光透过你的手 握不住的 在心中</div>', unsafe_allow_html=True)
        st.markdown('<div style=\'text-align: center;\'></div>', unsafe_allow_html=True)
        st.markdown('<div style=\'text-align: center;\'>午夜之后写了一首肤浅的歌</div>', unsafe_allow_html=True)
        st.markdown('<div style=\'text-align: center;\'>还要多说一句祝你生日快乐</div>', unsafe_allow_html=True)
        st.markdown('<div style=\'text-align: center;\'>回首的风景 向往都值得诉说</div>', unsafe_allow_html=True)
        st.markdown('<div style=\'text-align: center;\'>愿你心 常温热</div>', unsafe_allow_html=True)