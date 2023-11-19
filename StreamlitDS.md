---
layout: post
title: "Streamlit for Data Science"
date: 2023-11-18
tags: [streamlit, data science]
---

# Streamlit for Data Science

---

## Table of Contents
- [Streamlit for Data Science](#streamlit-for-data-science)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Getting Started](#getting-started)
    - [Streamlit Password Protection](#streamlit-password-protection)
    - [Streamlit Sidebar](#streamlit-sidebar)
    - [Streamlit Selectbox](#streamlit-selectbox)
    - [Streamlit Button](#streamlit-button)
    - [Streamlit Checkbox](#streamlit-checkbox)
    - [Streamlit Radio Button](#streamlit-radio-button)
    - [Streamlit Slider](#streamlit-slider)
    - [Streamlit Text Input](#streamlit-text-input)
  - [Integrating external ML libraries](#integrating-external-ml-libraries)
    - [Caching with Streamlit](#caching-with-streamlit)
    - [Hugging Face](#hugging-face)

## Introduction

Streamlit is a web framework tailored for data scientists and engineers, focusing on turning data scripts into easily shareable web apps. It's designed for simplicity and rapid development, making it ideal for showcasing data analysis, visualizations, and machine learning models. Unlike Flask and Django, which are more general-purpose web frameworks, Streamlit has a lower learning curve, particularly for those familiar with Python and data science libraries. Its ease of use is evident in the straightforward creation of interactive elements like sliders and plots.

While Flask and Django cater to a broader range of web applications and offer more control over web development aspects, Streamlit is particularly suited for quickly developing data-driven applications such as machine learning model demonstrations, data dashboards, and interactive reports. It's not intended for complex, database-driven web applications or those requiring extensive user authentication and authorization.

In terms of mechanics, Streamlit works by running Python scripts and handling the server and frontend communication implicitly. It reruns the script from top to bottom with each user interaction. This approach, while simplifying the development process, can have performance implications for more complex applications. In contrast, Flask and Django offer more granularity in managing the web server and the request-response cycle, following the MVC pattern.

Streamlit's customization capabilities are somewhat limited, especially when compared to the flexibility and scalability offered by Flask and Django. Django, with its comprehensive built-in features and an extensive ecosystem, is well-suited for large, feature-rich applications. Flask, being more minimalist, is often chosen for single-page applications and can be scaled with additional tools and libraries. Streamlit, while growing in popularity in the data science community, has a narrower focus and a smaller ecosystem in comparison to Django or Flask.

## Getting Started

### Streamlit Password Protection

Below snippet is a simple way to implement password protection in a Streamlit app. If the user doesn't enter the correct password, the app stops executing, thereby preventing access to whatever functionality or data might be presented in the rest of the app. This is a basic form of access control, although for more robust and secure authentication, more advanced methods should be used.

```python
password_guess = st.text_input("What is the Password?")
if password_guess != "streamlit_is_great":
    st.stop()
```

### Streamlit Sidebar

The sidebar is a useful feature for adding widgets that control the behavior of the app. It's a great way to add interactivity to the app without cluttering the main content area. The sidebar can be used to add widgets such as sliders, buttons, and checkboxes. The sidebar can also be used to display information, such as text and images.

```python
st.sidebar.header("Sidebar Header")
st.sidebar.text("Some text in the sidebar.")
```

### Streamlit Selectbox

The selectbox widget is a great way to add interactivity to the app. It allows the user to select from a list of options, which can be used to control the behavior of the app. The selectbox widget can be used to add interactivity to the app without cluttering the main content area. The selectbox widget can also be used to display information, such as text and images.

```python
option = st.sidebar.selectbox("Select a page", ["Home", "About", "Contact"])
```

### Streamlit Button

The button widget is a great way to add interactivity to the app. It allows the user to click on a button, which can be used to control the behavior of the app. The button widget can be used to add interactivity to the app without cluttering the main content area. The button widget can also be used to display information, such as text and images.

```python
if st.sidebar.button("Press me"):
    st.sidebar.write("Button pressed!")
```

### Streamlit Checkbox

The checkbox widget is a great way to add interactivity to the app. It allows the user to select from a list of options, which can be used to control the behavior of the app. The checkbox widget can be used to add interactivity to the app without cluttering the main content area. The checkbox widget can also be used to display information, such as text and images.

```python
if st.sidebar.checkbox("Check me out"):
    st.sidebar.write("Checkbox checked!")
```

### Streamlit Radio Button

The radio button widget is a great way to add interactivity to the app. It allows the user to select from a list of options, which can be used to control the behavior of the app. The radio button widget can be used to add interactivity to the app without cluttering the main content area. The radio button widget can also be used to display information, such as text and images.

```python
radio_button = st.sidebar.radio("Radio", ["Option 1", "Option 2"])
if radio_button == "Option 1":
    st.sidebar.write("Option 1 selected.")
elif radio_button == "Option 2":
    st.sidebar.write("Option 2 selected.")
```

### Streamlit Slider    

The slider widget is a great way to add interactivity to the app. It allows the user to select from a range of values, which can be used to control the behavior of the app. The slider widget can be used to add interactivity to the app without cluttering the main content area. The slider widget can also be used to display information, such as text and images.

```python
slider = st.sidebar.slider("Slide me", 0, 100)
if slider > 50:
    st.sidebar.write("Greater than 50.")
else:
    st.sidebar.write("Less than or equal to 50.")
```

### Streamlit Text Input

The text input widget is a great way to add interactivity to the app. It allows the user to enter text, which can be used to control the behavior of the app. The text input widget can be used to add interactivity to the app without cluttering the main content area. The text input widget can also be used to display information, such as text and images.

```python
text_input = st.sidebar.text_input("Enter some text")
if text_input == "Hello":
    st.sidebar.write("Hello to you too!")
else:
    st.sidebar.write("Goodbye")
```

## Integrating external ML libraries

### Caching with Streamlit

The @st.cache_resource() decorator in Streamlit is a powerful feature for caching the output of expensive computation steps in your Streamlit apps. This helps to enhance the performance of the app by not re-running certain functions every time there is a change in the user interface.

```python
@st.cache_resource()
def get_model():
    return pipeline("sentiment-analysis")
model = get_model()
```


### Hugging Face


