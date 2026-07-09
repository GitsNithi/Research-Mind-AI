import streamlit as st
from app.tools.pdf_export import create_pdf
from pathlib import Path
from app.graph.workflow import graph

st.set_page_config(
    page_title="ResearchMind AI",
    page_icon="🔎",
    layout="wide"
)

css_path = Path(__file__).parent / "styles.css"

with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown(
    """
    <h1 class="main-title">ResearchMind</h1>
    """,
    unsafe_allow_html=True
)

st.caption("AI powered Multi Agent Research Assistant")

with st.sidebar:

    st.markdown("## Research Mind")

    st.markdown("**Version:** 1.0")

    st.markdown("**Built by:** GitsNithi")

    st.markdown("---")

    st.markdown("### Powered By")

    st.markdown("""
- Python
- LangGraph
- LangChain
- Groq
- Tavily
""")

with st.form("research_form"):

    topic = st.text_input(
        "Research Topic",
        placeholder="🔍 Enter any research topic...",
        label_visibility="collapsed"
    )

    submitted = st.form_submit_button(
        "▶ Generate Report",
        use_container_width=True
    )

if submitted and topic:

    with st.spinner("Researching..."):

        result = graph.invoke(
            {
                "topic": topic
            }
        )

    st.divider()

    st.markdown(result["report"])

    pdf = create_pdf(result["report"])

    with open(pdf, "rb") as file:

        st.download_button(
            label="📄 Download PDF",
            data=file,
            file_name="Research_Report.pdf",
            mime="application/pdf"
        )

    st.divider()

st.markdown(
    """
    <div style="text-align:center; color:#D4AF37; padding:20px;">
         <b>ResearchMind</b><br>
        <span style="color:#B8B8B8;">
            Built by <b>@2026 GitsNithi</b>
        </span>
    </div>
    """,
    unsafe_allow_html=True
)