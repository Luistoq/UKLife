import streamlit as st

st.set_page_config(layout="wide")

st.title("🇬🇧 What is the UK?")

with st.expander("🗺️ Understanding the United Kingdom"):
    st.subheader("🌍 Composition of the UK")
    st.write("""
    The United Kingdom (UK) is a union of four countries:

    - **England** 🏰
    - **Scotland** 🏴󠁧󠁢󠁳󠁣󠁴󠁿
    - **Wales** 🐉
    - **Northern Ireland** 🍀

    The rest of the island of Ireland is the **Republic of Ireland**, which is an independent nation.
    """)
    st.subheader("📜 Official Name")
    st.write("""
    The full official name is **The United Kingdom of Great Britain and Northern Ireland**.

    - **Great Britain** refers only to England, Scotland, and Wales.
    - The term **Britain** or **British Isles** is often used to refer to the UK as a whole.

    💡 *Note:* Northern Ireland is part of the UK but not part of Great Britain.
    """)
    st.subheader("🏝️ Crown Dependencies and Overseas Territories")
    st.write("""
    There are islands closely associated with the UK but not part of it:

    - **Channel Islands** 🇬🇬 🇯🇪
    - **Isle of Man** 🇮🇲

    These are known as **Crown Dependencies** and have their own governments.

    The UK also has several **British Overseas Territories** around the world, such as:

    - **St. Helena** 🏝️
    - **Falkland Islands** 🐧

    These territories are linked to the UK but are not part of it.
    """)
    st.subheader("🏛️ Governance")
    st.write("""
    The UK is governed by the **Parliament at Westminster** in London.

    - **Scotland**, **Wales**, and **Northern Ireland** have their own **parliaments or assemblies** with devolved powers in certain areas.
    """)
    st.subheader("🧐 Check That You Understand")
    st.info("""
    **Make sure you know:**

    - The **four countries** that make up the UK.
    - The difference between **Great Britain** and the **United Kingdom**.
    - What the **Crown Dependencies** and **British Overseas Territories** are.
    - How **governance** works in the UK and its constituent countries.
    """)
