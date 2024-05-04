import streamlit as st

st.title('Hello Python Students!!!!')

st.header("this is a header!!!")

st.subheader("this is a subheader!!!")

st.text('I am AMITAVA')

st.markdown("### This is a markdown")

st.success('congratulation!!!')

st.info('this is important')

st.warning('Be Alert!!!')

st.error('This is wrong')

e=ZeroDivisionError("Trying 2 divide by 0")

st.exception(e)

st.write('I am learming python')

st.write(range(10))

from PIL import Image

i=Image.open('hero.jpg')

st.image(i,width=200)

if st.checkbox("Show/Hide"):
    st.text('showing it...')

status=st.radio('Select gender: ',('Male','Female'))

if (status=='Male'):
    st.success('U are a Male')
else:
    st.success('U are a female!!!')


hobby=st.selectbox("Hobbies: ",['cricket','dancing','drawing','sleeping'])

st.write("Sruti's hobby is ",hobby )


hobbies=st.multiselect("Hobbies: ",['cricket','sports','drawing','sleeping'])

st.write("Dhruva's hobby are ",len(hobbies),hobbies)

st.button('click me')
if st.button('About'):
    st.text('Welcome to Streamlit!!!!')


x=int(st.text_input('enter 1st no','type here'))

y=int(st.text_input('enter second no','type here'))

if st.button('ADD TWO NUMBERS'):
    result=x+y
    st.success(result)


age=st.slider('please enter your age',min_value=0,max_value=100,value=10)

st.write('your age is ',age)











