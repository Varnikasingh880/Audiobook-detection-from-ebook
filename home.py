import streamlit as st   #use this to create the web UI.

st.markdown("<h2 style='text-align: center'>📚Audiobook Generation from eBook📚</h2>", unsafe_allow_html=True)
st.markdown("---")
st.image("assets/unnamed.webp", caption='Audiobook Generation from eBook', width=700)
st.write("Welcome to the Audiobook Generation from eBook application! This app allows you to convert your favorite eBooks into audiobooks using advanced text-to-speech technology. Simply upload your eBook file, and the app will generate an audiobook version for you to listen to on the go.")
st.write("To get started, navigate to the 'Upload eBook' section in the sidebar. You can upload eBooks in various formats such as PDF, EPUB, or TXT. Once uploaded, the app will process the text and convert it into high-quality speech.")
st.write("After the conversion is complete, you can download the generated audiobook in MP3 format. Enjoy listening to your favorite books anytime, anywhere!")
st.write("Feel free to explore the app and transform your reading experience with audiobooks!")
st.write("Developed by: Varnika Singh")


st.title("📌INTRODUCTION")
st.markdown("---")
st.write("In today's fast-paced world, finding time to sit down and read a book can be challenging. Audiobooks offer a convenient solution, allowing people to enjoy literature while commuting, exercising, or multitasking. However, not all books are available in audiobook format, which is where this application comes in.")
st.write("This application leverages advanced text-to-speech (TTS) technology to convert eBooks into audiobooks. By using state-of-the-art TTS engines, the app can produce natural-sounding speech that enhances the listening experience. Users can upload their eBooks in various formats, and the app will process the text to generate an audiobook that can be easily downloaded and enjoyed.")


st.title("📌OBJECTIVE")
st.markdown("---")
st.write("The primary objective of this application is to provide users with a simple and efficient way to convert their eBooks into audiobooks. By doing so, the app aims to make literature more accessible to a wider audience, including those who may have visual impairments or prefer listening over reading.")
st.write("Additionally, the app seeks to enhance the overall user experience by utilizing high-quality TTS technology, ensuring that the generated audiobooks are pleasant to listen to. Ultimately, the goal is to empower users to enjoy their favorite books in a format that suits their lifestyle and preferences.")


st.title("📌TECHNOLOGIES USED")
st.markdown("---")
st.write("1. Streamlit: A powerful framework for building interactive web applications in Python.")
st.write("2. Python: The primary programming language used for developing the application.")        
st.write("3. Text-to-Speech (TTS) Libraries: Libraries such as gTTS, pyttsx3, or others for converting text to speech.")
st.write("4. File Handling: Techniques for uploading and processing eBook files in various formats")
st.write("5. Audio Processing: Methods for generating and saving audio files in formats like MP3.")
st.write("6. HTML/CSS: For customizing the appearance of the web application.")


st.title("📌WORKING")
st.markdown("---")
st.write("1. User Interface: The application features a user-friendly interface built with Streamlit, allowing users to easily navigate and interact with the app.")
st.write("2. eBook Upload: Users can upload their eBook files in supported formats (e.g., PDF, EPUB, TXT) through the app's interface.")
st.write("3. Text Extraction: The app processes the uploaded eBook to extract the text content, handling different file formats appropriately.")
st.write("4. Text-to-Speech Conversion: The extracted text is then fed into a TTS engine, which converts the text into natural-sounding speech.")
st.write("5. Audio Generation: The generated speech is saved as an audio file (e.g., MP3) that users can download.")
st.write("6. Download Option: Once the audiobook is generated, users are provided with a download link to save the audio file to their device.")


st.title("📌APPLICATIONS")
st.markdown("---")
st.write("1. Accessibility: The app makes literature more accessible to individuals with visual impairments or reading difficulties by providing an alternative way to consume content.")
st.write("2. Convenience: Users can listen to audiobooks while multitasking, commuting, or exercising, making it easier to enjoy books in a busy lifestyle.")
st.write("3. Language Learning: Audiobooks can be a valuable tool for language learners, helping them improve their listening skills and pronunciation.")
st.write("4. Content Consumption: The app allows users to consume a wide range of content, including novels, educational materials, and articles, in audio format.")


st.title("📌FUTURE SCOPE")
st.markdown("---")
st.write("1. Enhanced TTS Quality: Future iterations of the app could incorporate more advanced TTS engines that offer even more natural and expressive speech synthesis.")
st.write("2. Multi-Language Support: Expanding the app's capabilities to support multiple languages and dialects would make it accessible to a broader audience.")
st.write("3. Customization Options: Allowing users to customize the voice, speed, and pitch of the generated audiobooks could enhance the user experience.")
st.write("4. Integration with eBook Platforms: Partnering with popular eBook platforms to directly convert purchased eBooks into audiobooks could streamline the process for users.")
st.write("5. Mobile Application: Developing a mobile version of the app would enable users to generate and listen to audiobooks on their smartphones and tablets.")


st.title("📌CONCLUSION")
st.markdown("---")
st.write("The Audiobook Generation from eBook application represents a significant step towards making literature more accessible and convenient for a diverse range of users. By leveraging advanced text-to-speech technology, the app provides an efficient way to convert eBooks into high-quality audiobooks, catering to the needs of individuals with varying preferences and lifestyles.")
st.write("As the app continues to evolve, there are numerous opportunities for enhancement, including improved TTS quality, multi-language support, and greater customization options. These advancements will further enrich the user experience and broaden the app's appeal.")
st.write("In conclusion, this application not only addresses the growing demand for audiobooks but also empowers users to enjoy their favorite books in a format that suits their needs. With ongoing development and innovation, the Audiobook Generation from eBook app has the potential to become a valuable resource for book lovers worldwide.")
st.markdown("---")

st.markdown("<h2 style='text-align: center'>Made with LOVE❤️</h2>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center'>Books are meant to be heard as well as read start your journey today 🎧</h3>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center'>📚Happy Listening!📚</h2>", unsafe_allow_html=True)
st.markdown("---")

st.info("📖FOR FURTHER INFORMATION GO TO ABOUT PAGE OF THIS DASHBOARD")

# button for navigation
st.markdown("<h3 style='text-align: center'>👇CLICK BELOW👇</h3>", unsafe_allow_html=True)
# st.button("About", key="about", on_click=lambda: st.experimental_set_query_params(page="about"))
# st.markdown("---")
if st.button("Go to About Page"):
    st.switch_page("pages/about.py")


    