import streamlit as st
import pandas as pd
import json

if __name__ == "__main__":

    st.set_page_config(
        page_title="Happy Birthday to LSW",
        page_icon="pic.jpg",
        layout="wide",
    )

    st.markdown('<h1 style="color: #db5bcd;">LSW\'s 19th Birthday🎂🎉🎈🎁🎊🥳🕯️🍰🎇💖🎶🎀', unsafe_allow_html=True)

    tab_words, tab_music = st.tabs(["Words","Music"])

    with tab_words:
        st.header("生日快乐 Happy Birthday!")
        st.markdown('<h2 style="color: #C71585;">你好</h2>', unsafe_allow_html=True)
        st.markdown('<h2 style="color: #8A2BE2;">你好</h2>', unsafe_allow_html=True)
        st.markdown('<h2 style="color: #FF4D94;">你好</h2>', unsafe_allow_html=True)   
        st.markdown('<h2 style="color: #FF69B4;">你好</h2>', unsafe_allow_html=True)
        st.markdown('<h2 style="color: #FFC0CB;">你好</h2>', unsafe_allow_html=True)   
        st.markdown('<h2 style="color: #FFCCDE;">你好</h2>', unsafe_allow_html=True)  
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: pre;">🔥                              🔥         </h4>', unsafe_allow_html=True)
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: pre;">|                                   |         </h4>', unsafe_allow_html=True)
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: pre;">🔴🔴            🔵🔵🔵🔵🔵</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: pre;">🔴🔴            🔵                     🔵</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: pre;">🔴🔴            🔵                     🔵</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: pre;">🔴🔴            🔵🔵🔵🔵🔵</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: pre;">🔴🔴            🔵🔵🔵🔵🔵</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: pre;">🔴🔴                                     🔵</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: pre;">🔴🔴                                     🔵</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: pre;">🔴🔴            🔵🔵🔵🔵🔵</h4>', unsafe_allow_html=True)  
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: pre;">|                                   |         </h4>', unsafe_allow_html=True)
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: nowrap;">                                ⚪⚪⚪⚪⚪⚪</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: nowrap;">                     ⚪⚪⚪⚪⚪🍓🍓🍓🍓🍓⚪⚪⚪⚪⚪⚪</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: nowrap;">             ⚪⚪⚪🍓🍓🍓🍓⚪⚪⚪⚪⚪⚪⚪🍓🍓🍓🍓⚪⚪⚪⚪</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: nowrap;">        ⚪⚪🍓🍓🍓⚪⚪⚪⚪⚪🍓🍓🍓🍓🍓⚪⚪⚪⚪⚪🍓🍓🍓⚪⚪⚪</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: nowrap;">     ⚪🍓🍓⚪⚪⚪⚪⚪⚪🍓⚪⚪⚪⚪⚪⚪⚪🍓⚪⚪⚪⚪⚪⚪🍓🍓⚪⚪</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: nowrap;">   ⚪🍓🍓⚪⚪⚪⚪⚪🍓⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪🍓⚪⚪⚪⚪⚪⚪🍓🍓⚪⚪</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: nowrap;">  ⚪⚪🍓🍓⚪⚪⚪⚪⚪🍓⚪⚪⚪⚪⚪⚪⚪⚪⚪🍓⚪⚪⚪⚪⚪⚪⚪🍓🍓⚪⚪</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: nowrap;">  ⚪⚪⚪🍓🍓⚪⚪⚪⚪⚪⚪🍓⚪⚪⚪⚪⚪⚪🍓⚪⚪⚪⚪⚪⚪⚪🍓🍓⚪⚪⚪</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: nowrap;">  🟡🟡⚪⚪🍓🍓🍓⚪⚪⚪⚪⚪⚪🍓🍓🍓🍓⚪⚪⚪⚪⚪⚪⚪🍓🍓⚪⚪⚪🟡🟡</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: nowrap;">  ⚪🟡🟡⚪⚪⚪⚪🍓🍓🍓🍓⚪⚪⚪⚪⚪⚪⚪⚪⚪🍓🍓🍓🍓⚪⚪⚪⚪🟡🟡⚪</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: nowrap;">  ⚪⚪🟡🟡⚪⚪⚪⚪⚪⚪⚪🍓🍓🍓🍓🍓🍓🍓🍓🍓⚪⚪⚪⚪⚪⚪⚪🟡🟡⚪⚪</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: nowrap;">  ⚪⚪🟠🟠🟡🟡⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪🟡🟡🟠🟠⚪⚪</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: nowrap;">  ⚪⚪⚪⚪⚪⚪🟡🟡⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪🟡🟡⚪⚪⚪⚪⚪⚪</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: nowrap;">   ⚪⚪⚪⚪⚪⚪🟠🟠🟡🟡⚪⚪⚪🟠🟠🟠🟠🟠⚪⚪⚪🟡🟡🟠🟠⚪⚪⚪⚪⚪</h4>', unsafe_allow_html=True)         
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: nowrap;">       ⚪⚪⚪⚪⚪⚪⚪⚪🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡⚪⚪⚪⚪⚪⚪⚪⚪</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: nowrap;">            ⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: nowrap;">                 ⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;white-space: nowrap;">                        ⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;">你好</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;">你好</h4>', unsafe_allow_html=True) 
        st.markdown('<div style="color: #FFCCDE;text-align: center;">你好</h4>', unsafe_allow_html=True)   

    with tab_music:
        st.header("生日歌 Song for you")

        audio_file = open('Record.wav', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/wav')
        col1, col2 = st.columns(2)
        with open("Drafts.pdf", "rb") as file:
            btn = col1.download_button(
                label=f"Download drafts",
                data=file,
                file_name="19th&1st.pdf",
                mime="application/pdf"
            )
        with open("Record.mp3", "rb") as file:
            btn = col2.download_button(
                label=f"Download mp3",
                data=file,
                file_name="HBD.mp3",
                mime="audio/mp3"  # M4A文件的MIME类型
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