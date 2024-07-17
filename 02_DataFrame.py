import streamlit as st 
import numpy as np 
import pandas as pd 

st.title('데이터 프레임 튜토리얼')

# DataFrame 생성 
dataframe = pd.DataFrame({
    'first column' : [1,2,3,4],
    'second column' : [10,20,30,40]
})

# DataFrame 
# use_container_width 기능은 데이터프레임을 컨테이너 크기에 확장할 때 사용 (T/F)
st.dataframe(dataframe, use_container_width=False)

# 테이블(static)
# DataFrame과는 다르게 interactive 한 UI를 제공하지 않습니다. 
st.table(dataframe)

## 메트릭 
st.metric(label="온도", value="10°C", delta="1.2°C")
st.metric(label="삼성전자", value="61,000원", delta="-1,200원")

# 컬럼으로 영역을 나누어 표기한 경우 
col1, col2, col3 = st.columns(3)
col1.metric(label='달러USD', value='1,228원', delta="-12,00원")
col2.metric(label='일본JPY(100엔)', value='958,63원', delta="-7,44원")
col3.metric(label='유럽연합EUR', value='1,335.82원', delta="11.44원")

