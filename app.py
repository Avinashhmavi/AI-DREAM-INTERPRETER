import streamlit as st
import os
from groq import Groq
from datetime import datetime
from collections import Counter
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up the Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Set page config
st.set_page_config(page_title="Dream Interpreter AI", page_icon="🌌")

# Session state initialization
if "journal_entries" not in st.session_state:
    st.session_state.journal_entries = []

# Helper function to analyze dreams using Groq
def analyze_dream(dream_description):
    system_prompt = """You are a dream interpretation expert combining knowledge from psychology, 
    mythology, and symbolic analysis. Analyze the following dream by:
    1. Identifying key symbols and their potential meanings
    2. Emotional tone analysis
    3. Psychological interpretation
    4. Mythological/cultural connections
    5. Possible life connections
    Structure your response with clear headings in markdown using ### prefix for section titles."""

    try:
        response = client.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": dream_description}
            ],
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Error analyzing dream: {str(e)}")
        return None

# Improved function to parse AI response into sections
def parse_analysis(response):
    sections = {}
    if not response:
        return sections
    
    current_section = None
    for line in response.split('\n'):
        if line.startswith('### '):
            current_section = line.strip('# ').strip()
            sections[current_section] = []
        elif current_section and line.strip():
            sections[current_section].append(line.strip())
    return sections

# Main app interface
st.title("🌌 AI-Powered Dream Interpreter")
st.markdown("Share your dream and receive insights from psychology and mythology")

# Dream input section
with st.form("dream_form"):
    dream_text = st.text_area("Describe your dream:", height=150)
    submitted = st.form_submit_button("Interpret Dream")

if submitted and dream_text:
    with st.spinner("Analyzing your dream..."):
        analysis = analyze_dream(dream_text)
        if analysis:
            parsed_analysis = parse_analysis(analysis)
            
            if not parsed_analysis:
                st.warning("The analysis format was unexpected. Here's the raw response:")
                st.write(analysis)
            else:
                st.subheader("Dream Analysis")
                for section, content in parsed_analysis.items():
                    with st.expander(section):
                        st.write("\n".join(content))
                
                # Save to journal
                entry = {
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "dream": dream_text,
                    "analysis": parsed_analysis
                }
                st.session_state.journal_entries.append(entry)
                st.success("Analysis saved to your dream journal!")

# Dream Journal Section
st.sidebar.header("📖 Dream Journal")
if st.session_state.journal_entries:
    # Theme tracking
    all_symbols = []
    all_emotions = []
    
    for entry in st.session_state.journal_entries:
        analysis = entry['analysis']
        if 'Symbols' in analysis:
            symbols = [line.split(':')[0].strip() for line in analysis['Symbols'] if line]
            all_symbols.extend(symbols)
        if 'Emotional Tone' in analysis:
            emotions = [line.split(':')[0].strip() for line in analysis['Emotional Tone'] if line]
            all_emotions.extend(emotions)
    
    st.sidebar.subheader("Theme Tracking")
    if all_symbols:
        common_symbols = Counter(all_symbols).most_common(5)
        st.sidebar.write("**Most Common Symbols:**")
        for symbol, count in common_symbols:
            st.sidebar.write(f"- {symbol} ({count}x)")
    
    if all_emotions:
        common_emotions = Counter(all_emotions).most_common(3)
        st.sidebar.write("**Frequent Emotions:**")
        for emotion, count in common_emotions:
            st.sidebar.write(f"- {emotion} ({count}x)")

    # Journal entries
    st.sidebar.subheader("Past Entries")
    for i, entry in enumerate(reversed(st.session_state.journal_entries)):
        if st.sidebar.button(f"Entry {i+1} - {entry['date']}"):
            st.subheader(f"Journal Entry - {entry['date']}")
            st.write("**Dream:**", entry['dream'])
            st.write("**Analysis:**")
            for section, content in entry['analysis'].items():
                with st.expander(section):
                    st.write("\n".join(content))
else:
    st.sidebar.write("No entries yet - interpret some dreams to build your journal!")

# How to Run instructions in the sidebar
st.sidebar.markdown("""
**How to Use:**
1. Describe your dream in the main text area
2. Click 'Interpret Dream'
3. View analysis and save to journal
4. Track patterns over time in the sidebar

**Requirements:**
- Groq API key (in secrets.toml)
- Python packages: streamlit, groq
""")