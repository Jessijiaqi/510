import streamlit as st

st.set_page_config(
    page_title="Jessi Wang - UX Designer",
    page_icon="🧞",
    layout="centered",  # centered or wide
    initial_sidebar_state="auto",
)

col1, col2 = st.columns([0.3, 0.7])
with col1:
    st.markdown(
        """
    <style>
    .profile-img img {
        width: 100%;
        border-radius: 50%;
    }
    </style>

    <div class="profile-img">

    ![](https://github.com/Jessijiaqi/510/blob/main/IMG_6256%202.JPG?raw=true)
    </div>
    """,
        unsafe_allow_html=True,
    )
    # st.image('https://avatars.githubusercontent.com/u/7678108?v=4')
with col2:
    st.markdown(
        """
    # Jessi Wang (She/Her)
                
    :rainbow[**Hi,I'm Jessi. I'm an HCI/UX designer driven by a passion for creating user-centric products. I love exploring diverse fields and solving real-world problems.**]
    """
    )

st.header('Experience', divider='rainbow')

st.markdown(
    """
### Education
- M.S. in Innovation Technology at [University of Washington](https://www.washington.edu/)
- B.S. in Engineering Design at [Ulster University](https://www.ulster.ac.uk/)
- B.S. in Industrial Design at [Shaanxi University of Science & Technology](https://en.sust.edu.cn/)

### Work Experience
- Intern UX Designer in [HIKVISION](https://www.hikvision.com/us-en/)
- Product Designer in Cross-Strait Industrial Design Workshop
"""
)

st.header('Projects', divider='rainbow')

st.markdown(
    """

- [Never Fade Away](https://wangjiaqi123jessie.wixsite.com/jessi-s-portfolio/%E6%AD%BB%E4%BA%A1app)
- [Sour Amour](https://wangjiaqi123jessie.wixsite.com/jessi-s-portfolio/s-projects-side-by-side-1)
- [CareCompass](https://wangjiaqi123jessie.wixstudio.io/portfolio/blank-3)
"""
)

st.header('Hobbies and Interests', divider='rainbow')

st.markdown(
    """

- Digital painting in Procreate
"""
)




col1, col2, col3, col4, col5 = st.columns(5)


image_urls = [
    "https://github.com/Jessijiaqi/510/blob/main/%E6%9C%AA%E5%91%BD%E5%90%8D%E4%BD%9C%E5%93%81.PNG?raw=true",  
    "https://github.com/Jessijiaqi/510/blob/main/%E6%9C%AA%E5%91%BD%E5%90%8D%E4%BD%9C%E5%93%81%203.JPG?raw=true",  
    "https://github.com/Jessijiaqi/510/blob/main/IMG_6201.JPG?raw=true",  
    "https://github.com/Jessijiaqi/510/blob/main/IMG_6200.JPG?raw=true",  
    "https://github.com/Jessijiaqi/510/blob/main/IMG_5287.JPG?raw=true", 
]


for col, img_url in zip([col1, col2, col3, col4, col5], image_urls):
    col.markdown(
        f"""
        <div style="text-align: center;">
            <img src="{img_url}" style="width: 100%; max-width: 150px; height: auto; border-radius: 10%;">
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
- Reading
- Travelling
- Cats
"""
)

col1, col2 = st.columns(2)


with col1:
    st.image("https://github.com/Jessijiaqi/510/blob/main/fc8780699224b0c80b46232b7cdd4b24.jpeg?raw=true", width=300)  
    st.caption("Mily")  


with col2:
    st.image("https://github.com/Jessijiaqi/510/blob/main/IMG_0205.jpeg?raw=true", width=300)  
    st.caption("Xiaobai")  

ft = """
<style>
a:link , a:visited{
color: #BFBFBF;  /* theme's text color hex code at 75 percent brightness*/
background-color: transparent;
text-decoration: none;
}

a:hover,  a:active {
color: #0283C3; /* theme's primary color*/
background-color: transparent;
text-decoration: underline;
}

#page-container {
  position: relative;
  min-height: 10vh;
}

footer{
    visibility:hidden;
}

.footer {
position: relative;
left: 0;
top:230px;
bottom: 0;
width: 100%;
background-color: transparent;
color: #808080; /* theme's text color hex code at 50 percent brightness*/
text-align: left; /* you can replace 'left' with 'center' or 'right' if you want*/
}
</style>

<div id="page-container">

<div class="footer">
<p style='font-size: 0.875em;'>Made with <a style='display: inline; text-align: left;' href="https://streamlit.io/" target="_blank">Streamlit</a><br 'style= top:3px;'>
with <img src="https://em-content.zobj.net/source/skype/289/red-heart_2764-fe0f.png" alt="heart" height= "10"/><a style='display: inline; text-align: left;' href="https://github.com/sape94" target="_blank"> by sape94</a></p>
</div>

</div>
"""
st.write(ft, unsafe_allow_html=True)