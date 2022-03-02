import streamlit as st
import pandas as pd

df = pd.read_csv("df.csv",dtype='str')

st.title("f1分数解析🤡")
st.write("能源大数据子赛道——虚拟货币“挖矿”行为识别 专用")
st.write("比赛地址: https://www.dcic-china.com/competitions/10025/")

score = st.text_input('输入排行榜得分', '0.75883586')
try:
    score = "{:.8f}".format(float(score))
    result = df[df.score==score[:10]].iloc[0]
    st.write("*************")
    st.write(f"你预测了{result['pred_num']}个异常用户")
    st.write(f"其中预测对了{result['pred_true_num']}个用户")
    dif = 37-int(result['pred_true_num'])
    if dif != 0:
        st.write(f"还差{dif}个异常用户没找到")
    else:
        st.write("居然全找到了！🐂🍺")
    st.write("*************")
except:
    st.write("输入有误请重试！")
st.write("预祝各位都能拿满分🎉！DF平台越办越棒！")
st.write("by lmy")
