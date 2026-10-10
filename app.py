import streamlit as st
import joblib
import re

st.set_page_config(
    page_title="FreshCart 360 | Customer Support",
    page_icon="🛒",
    layout="centered",
    initial_sidebar_state="expanded",
)

# -----------------------------
# Load trained models
# -----------------------------
@st.cache_resource
def load_models():
    category_model = joblib.load("freshcart_category_model.joblib")
    urgency_model = joblib.load("freshcart_urgency_model.joblib")
    return category_model, urgency_model

category_model, urgency_model = load_models()


# -----------------------------
# Text cleaning
# -----------------------------
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+", " ", text)
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


# -----------------------------
# Prediction: only category + urgency
# -----------------------------
def predict_ticket(message):
    cleaned = clean_text(message)
    category = category_model.predict([cleaned])[0]
    urgency = urgency_model.predict([cleaned])[0]
    return category, urgency


# -----------------------------
# Sidebar: app info + instructions
# -----------------------------
with st.sidebar:
    st.title("🛒 FreshCart 360")
    st.caption("Customer Support Assistant")
    st.divider()

    st.subheader("About the app")
    st.write(
        "FreshCart 360 helps support teams review customer messages by identifying "
        "the issue category and suggested urgency."
    )

    st.subheader("How to use")
    st.markdown(
        """
        1. Paste the customer's message in the text box.
        2. Click **Predict Ticket**.
        3. Review the **Category** and **Urgency** results.
        4. Use your team's support guidelines to decide what to do next.
        """
    )

    st.subheader("Available categories")
    st.markdown(
        """
        - Late Delivery
        - Wrong/Missing Item
        - Refund/Payment Issue
        - App/Technical Issue
        - General Feedback
        """
    )

    st.subheader("Urgency levels")
    st.markdown(
        """
        - **High** — review promptly
        - **Medium** — follow up soon
        - **Low** — normal queue
        """
    )

    st.divider()
    st.caption("Tip: Avoid entering passwords, full payment card details, or other sensitive information.")


# -----------------------------
# Main UI
# -----------------------------
st.title("Customer Support Ticket")
st.write(
    "Enter the customer's message below to predict its category and urgency."
)

message = st.text_area(
    "Customer Message",
    placeholder="Example: My order is late and I still haven't received it.",
    height=160,
)

predict_clicked = st.button(
    "Predict Ticket",
    type="primary",
    use_container_width=True,
)

if predict_clicked:
    if not message.strip():
        st.warning("Please enter a customer message first.")
    else:
        try:
            category, urgency = predict_ticket(message)

            st.subheader("Prediction Results")
            col1, col2 = st.columns(2, gap="medium")

            with col1:
                st.metric("Category", str(category))

            with col2:
                st.metric("Urgency", str(urgency))

        except FileNotFoundError:
            st.error(
                "The prediction service is unavailable. Please contact the app administrator."
            )
        except Exception:
            st.error(
                "We couldn't process this message. Please try again or review it manually."
            )
