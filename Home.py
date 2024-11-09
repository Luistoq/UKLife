import streamlit as st
import re


from content_values import content_values
from content_whatisuk import content_whatisuk
from content_history import content_history
from content_society import content_society
from content_law import content_law

st.title("UK Life")

# Combine the content from both modules
all_content = content_values + content_whatisuk + content_history + content_society +  content_law 

# Search input
search_term = st.text_input("Search:")

if search_term:
    # Case-insensitive search
    pattern = re.compile(re.escape(search_term), re.IGNORECASE)
    results = []

    # Search through the combined content
    for entry in all_content:
        if pattern.search(entry['content']) or pattern.search(entry['section']):
            results.append(entry)

    if results:
        st.write(f"Found {len(results)} result(s) for '{search_term}':")
        for result in results:
            st.write(f"**Page**: {result['page']}")
            st.write(f"**Section**: {result['section']}")
            
            # Highlight the search term in the content
            highlighted_content = pattern.sub(
                lambda match: f"<mark>{match.group(0)}</mark>", result['content']
            )
            st.markdown(f"**Content:** {highlighted_content}", unsafe_allow_html=True)
            st.write("---")
    else:
        st.write(f"No results found for '{search_term}'.")
