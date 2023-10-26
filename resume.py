

import streamlit as st


# st.title('This is a title')
st.title(':blue[HAFIZ ABDULLAH ASIF] ')
st.markdown('Python developer role to leverage coding proficiency and contribute to learn success in python - based software development.')
with st.expander("Contect Info"):


    phone,address,email=st.columns(3,gap="small")
    with phone:
        st.markdown(':blue[#+923202277180]')
    with address:
        st.markdown(":blue[Korangi Creek Karachi]")
    with email: 
        st.markdown(":blue[iamhafizabdullah.asif@gmail.com]")     
# st.markdown(':blue[Marital Status Single]')
# st.markdown(":blue[Religion Islam]")
col1,col2=st.columns(2)
with col1:
    st.subheader('WORK EXPERIENCE', divider='rainbow')
    st.subheader('python Developer For a Freelancer')
    st.markdown('Writing,testing and maintaining python code to meet project requirment.')
    st.markdown('Collaborating with senior developers to design and implement software solutions. ')
    st.markdown('Debugging and troubleshooting code issues.')
    st.markdown('Participating in code reviews and providing constructive feedback.')
    st.markdown('Learning and applying best practices in software deveplopment.') 
    st.markdown('Assisting in documentation and knowledge sharing ')
    st.markdown('Staying up-to-date with the latest python and software developments trends.')
    st.subheader('EDUCATION',divider='rainbow')
    st.markdown('Intermediate')
    st.markdown('Bs Data Sience (Enrolment in process)')
    st.markdown('Ilma University')
    st.markdown('Hafize Quran')


with col2:
    

    st.subheader('SKILLS',divider='rainbow')
    st.markdown('Python')       
    st.markdown('Sql')
    st.markdown('Pandas')
    st.markdown('Data Structure')
    st.markdown('Numpy')
    st.markdown('ApIs')
    st.markdown('Automations')
    st.markdown('Github')
    st.markdown('File handling')
    st.subheader('LANGUAGE',divider='rainbow')
    st.markdown('English ')
    st.markdown('Urdu')
    st.subheader('Personal Project',divider='rainbow')
    st.markdown('NOTIFICATION SYSTEM')
    st.markdown('Sending email to user on specific time and inform them any new update found in system or maintenance time')





# Bs Data Sience (Enrolment in process)')
# st.markdown('Ilma University')


# iamhafizabdullah.asif@gmail.com  Karachi Pakistan]')