import streamlit as st
import pickle

# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="ReviewCheck | AI Review Detector",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- LOAD MODEL ----------------

@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)

    with open("vectorizer.pkl", "rb") as file:
        vectorizer = pickle.load(file)

    return model, vectorizer


model, tfidf = load_model()


# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

/* Main Background */
.stApp {
    background: #f5f3fc;
}

/* Page Layout */
.block-container {
    max-width: 1100px;
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

/* Navigation */
.navbar {
    background: white;
    padding: 18px 25px;
    border-radius: 14px;
    border: 1px solid #e5def5;
    margin-bottom: 30px;
    box-shadow: 0 3px 12px rgba(35,11,133,0.06);
}

.brand {
    color: #230b85;
    font-size: 27px;
    font-weight: 800;
}

/* Hero Section */
.hero {
    background: linear-gradient(120deg, #230b85, #6845c6);
    padding: 65px 25px;
    border-radius: 22px;
    text-align: center;
    margin-bottom: 35px;
    box-shadow: 0 10px 25px rgba(35,11,133,0.20);
    transition: transform 0.3s ease;
}

.hero:hover {
    transform: translateY(-4px);
}

.hero h1 {
    color: white !important;
    font-size: 42px !important;
    font-weight: 800 !important;
}

.hero p {
    color: #f0eaff !important;
    font-size: 18px !important;
}

/* Headings */
.section-heading {
    color: #230b85;
    font-size: 28px;
    font-weight: 800;
    margin-bottom: 8px;
}

.description {
    color: #393449;
    font-size: 16px;
    line-height: 1.7;
}

/* Input */
.stTextArea label,
.stTextArea label p {
    color: #230b85 !important;
    font-size: 17px !important;
    font-weight: 700 !important;
}

.stTextArea textarea {
    background-color: white !important;
    color: #222222 !important;
    border: 2px solid #d6ccef !important;
    border-radius: 13px !important;
    font-size: 16px !important;
    transition: border 0.3s ease, box-shadow 0.3s ease;
}

.stTextArea textarea:focus {
    border: 2px solid #6845c6 !important;
    box-shadow: 0 0 10px rgba(104,69,198,0.20);
}

.stTextArea textarea::placeholder {
    color: #777777 !important;
    opacity: 1;
}

/* Analyze Button */
.stButton button {
    background: linear-gradient(120deg, #230b85, #6845c6);
    color: white !important;
    border: none;
    border-radius: 12px;
    height: 54px;
    font-size: 18px;
    font-weight: 700;
    transition: all 0.3s ease;
    box-shadow: 0 5px 12px rgba(35,11,133,0.18);
}

.stButton button:hover {
    background: linear-gradient(120deg, #18065e, #4d2ba7);
    transform: translateY(-3px);
    box-shadow: 0 9px 18px rgba(35,11,133,0.30);
    color: white !important;
}

.stButton button:active {
    transform: scale(0.98);
}

/* Result Cards */
.result-card {
    padding: 30px 20px;
    border-radius: 17px;
    text-align: center;
    margin-top: 20px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.result-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 22px rgba(0,0,0,0.10);
}

.genuine-card {
    background: #e5f8ed;
    border: 2px solid #16834a;
}

.fake-card {
    background: #fff0f0;
    border: 2px solid #d62828;
}

.result-card h2 {
    font-size: 30px;
    font-weight: 800;
    margin-bottom: 10px;
}

.result-card p {
    font-size: 17px;
    font-weight: 600;
}

.genuine-card h2,
.genuine-card p {
    color: #126b3b !important;
}

.fake-card h2,
.fake-card p {
    color: #b71c1c !important;
}

/* Information Cards */
.info-card {
    background: white;
    border: 1px solid #e5def5;
    border-radius: 15px;
    padding: 25px;
    min-height: 155px;
    margin-bottom: 15px;
    transition: all 0.3s ease;
    box-shadow: 0 3px 10px rgba(35,11,133,0.05);
}

.info-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 10px 22px rgba(35,11,133,0.13);
    border-color: #9276d6;
}

.info-card h3 {
    color: #230b85 !important;
    font-size: 20px;
}

.info-card p {
    color: #393449 !important;
    font-size: 15px;
    line-height: 1.6;
}

/* Footer */
.footer {
    text-align: center;
    color: #454052;
    padding: 25px;
    border-top: 1px solid #ded8ed;
    margin-top: 40px;
    font-size: 14px;
}

/* Divider */
hr {
    border-color: #ded8ed !important;
}

</style>
""", unsafe_allow_html=True)


# ---------------- NAVIGATION ----------------

st.markdown("""
<div class="navbar">
    <span class="brand">🔍 ReviewCheck</span>
</div>
""", unsafe_allow_html=True)


# ---------------- HERO SECTION ----------------

st.markdown("""
<div class="hero">
    <h1>Detect Fake Product Reviews</h1>
    <p>
        Make Smarter Decisions with Machine Learning
        <br>
        Analyze product reviews and identify suspicious feedback.
    </p>
</div>
""", unsafe_allow_html=True)


# ---------------- REVIEW ANALYZER ----------------

st.markdown("""
<div class="section-heading">Analyze Your Review</div>
<div class="description">
    Enter or paste a product review below to check its predicted authenticity.
</div>
""", unsafe_allow_html=True)

st.write("")

review = st.text_area(
    "Product Review",
    placeholder="Example: This product has excellent quality. I really love its performance...",
    height=170
)

st.caption("Enter a product review and click the button below to analyze it.")

st.write("")

# ---------------- ANALYZE BUTTON ----------------

if st.button("🔍  Analyze Review", use_container_width=True):

    if review.strip():

        review_tfidf = tfidf.transform([review])
        prediction = model.predict(review_tfidf)[0]

        st.divider()

        st.markdown("""
        <div class="section-heading">Analysis Result</div>
        """, unsafe_allow_html=True)

        # Genuine Result
        if prediction == "CG":

            st.markdown("""
            <div class="result-card genuine-card">
                <h2>✓ GENUINE REVIEW</h2>
                <p>Our Machine Learning model predicts this review as Genuine.</p>
            </div>
            """, unsafe_allow_html=True)

        # Fake Result
        elif prediction == "OR":

            st.markdown("""
            <div class="result-card fake-card">
                <h2>✕ FAKE REVIEW</h2>
                <p>Our Machine Learning model predicts this review as Fake.</p>
            </div>
            """, unsafe_allow_html=True)

        else:

            st.warning(f"Predicted Label: {prediction}")

        st.caption(
            "Note: This is a machine learning prediction and does not "
            "guarantee the actual authenticity of a review."
        )

    else:

        st.warning("Please enter a product review first.")


# ---------------- ABOUT PROJECT ----------------

st.write("")
st.divider()

st.markdown("""
<div class="section-heading">About This Project</div>

<div class="description">
ReviewCheck is a Machine Learning based web application
that classifies product reviews as Fake or Genuine.

It uses Natural Language Processing techniques to convert
text into numerical features and applies a trained
classification model to make predictions.
</div>
""", unsafe_allow_html=True)


# ---------------- TECHNOLOGIES ----------------

st.write("")
st.markdown("""
<div class="section-heading">Technologies Used</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="info-card">
        <h3>🐍 Python</h3>
        <p>Used for data processing and machine learning development.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <h3>🧠 Machine Learning</h3>
        <p>TF-IDF and Logistic Regression for review classification.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="info-card">
        <h3>🌐 Streamlit</h3>
        <p>Used to build the interactive web application.</p>
    </div>
    """, unsafe_allow_html=True)


# ---------------- FOOTER ----------------

st.markdown("""
<div class="footer">
    <b>ReviewCheck</b>
    <br>
    Fake Review Detection using Machine Learning
    <br><br>
    Built with Python | Streamlit | Scikit-learn
</div>
""", unsafe_allow_html=True)
