import streamlit as st

st.set_page_config(layout="wide")

st.title("Timeline of Key Dates and Events in British History")

# CSS style for year labels
st.markdown("""
    <style>
    .year-label {
        font-size: 1.3em;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Function to display events with styled labels
def display_events(events):
    for label, emoji, description in events:
        st.markdown(f'<span class="year-label">{label}</span> {emoji} {description}', unsafe_allow_html=True)

# Prehistoric Britain
with st.expander("Prehistoric Britain"):
    events = [
        ("c. 10,000 years ago", "🌍", "Britain becomes an island separated from the continent due to rising sea levels."),
        ("c. 6,000 years ago", "🪨", "First farmers arrive from south-east Europe; build monuments like Stonehenge (Wiltshire) and Skara Brae (Orkney)."),
        ("c. 4,000 years ago", "🏺", "Bronze Age begins; people make bronze tools and gold ornaments; live in roundhouses."),
        ("Iron Age", "⚒️", "Iron tools and weapons are developed; Celtic languages are spoken; hill forts like Maiden Castle are built; first coins minted in Britain.")
    ]
    display_events(events)

# The Romans
with st.expander("The Romans"):
    events = [
        ("55 BC", "⚔️", "Julius Caesar leads first Roman invasion; unsuccessful."),
        ("AD 43", "⚔️", "Emperor Claudius successfully invades Britain; begins Roman occupation."),
        ("AD 60–61", "👑", "Boudicca, queen of the Iceni, leads rebellion against Romans; remembered as a national heroine."),
        ("AD 122", "🏰", "Emperor Hadrian orders construction of Hadrian's Wall to keep out the Picts."),
        ("3rd–4th centuries AD", "✝️", "First Christian communities appear in Britain."),
        ("AD 410", "🏳️", "Roman army leaves Britain to defend Rome; end of Roman rule.")
    ]
    display_events(events)

# The Anglo-Saxons
with st.expander("The Anglo-Saxons"):
    events = [
        ("5th–6th centuries AD", "⚔️", "Angles, Saxons, and Jutes invade from northern Europe; languages they spoke form basis of modern English."),
        ("By AD 600", "🏰", "Anglo-Saxon kingdoms established in England; Sutton Hoo burial shows sophisticated culture."),
        ("7th century", "✝️", "Christian missionaries like St Augustine (first Archbishop of Canterbury) and St Columba spread Christianity."),
        ("Sutton Hoo", "🛡️", "Anglo-Saxon royal burial site in Suffolk; provides insight into early medieval culture.")
    ]
    display_events(events)

# The Vikings
with st.expander("The Vikings"):
    events = [
        ("AD 789", "⚔️", "Vikings from Scandinavia begin raiding coastal towns; take goods and slaves."),
        ("9th century", "👑", "King Alfred the Great unites Anglo-Saxon kingdoms; defeats Vikings; establishes Danelaw in the east."),
        ("Danelaw", "⚔️", "Area of England under Viking control; Viking influence seen in place names."),
        ("Early 11th century", "👑", "Danish kings like King Cnut (Canute) rule England."),
        ("Scotland", "🏰", "Kenneth MacAlpin unites the Scots; term 'Scotland' begins to be used.")
    ]
    display_events(events)

# The Norman Conquest
with st.expander("The Norman Conquest"):
    events = [
        ("1066", "⚔️", "Battle of Hastings; William the Conqueror defeats King Harold II; last successful foreign invasion of England."),
        ("1086", "📜", "Domesday Book compiled by order of William I; detailed survey of land and property ownership.")
    ]
    display_events(events)

# The Middle Ages
with st.expander("The Middle Ages"):
    events = [
        ("1215", "📜", "Magna Carta signed by King John; establishes principle that everyone, including the king, is subject to the law."),
        ("1284", "⚖️", "Statute of Rhuddlan integrates Wales into the Kingdom of England; introduces English law."),
        ("1314", "⚔️", "Battle of Bannockburn; Robert the Bruce leads Scots to victory over English; Scotland remains independent."),
        ("1348", "☣️", "Black Death arrives; one-third of population dies; leads to social and economic changes."),
        ("1387–1400", "📖", "Geoffrey Chaucer writes 'The Canterbury Tales'; significant work in development of English literature."),
        ("1455–1485", "⚔️", "Wars of the Roses between Houses of Lancaster and York for the English throne."),
        ("1485", "👑", "Battle of Bosworth Field; Henry Tudor defeats Richard III; becomes Henry VII; starts Tudor dynasty.")
    ]
    display_events(events)

# The Tudors and Stuarts
with st.expander("The Tudors and Stuarts"):
    events = [
        ("1509–1547", "👑", "Reign of Henry VIII; breaks from Catholic Church; establishes Church of England via Act of Supremacy (1534); marries six times."),
        ("1536", "⚖️", "Act of Union with Wales; incorporates Wales under English legal system."),
        ("1547–1553", "👑", "Reign of Edward VI; Protestant reforms continue; Book of Common Prayer introduced."),
        ("1553–1558", "👑", "Reign of Mary I ('Bloody Mary'); restores Catholicism; persecutes Protestants."),
        ("1558–1603", "👑", "Reign of Elizabeth I; re-establishes Protestant Church; defeats Spanish Armada in 1588; era of exploration and cultural growth."),
        ("1603", "👑", "James VI of Scotland becomes James I of England; first Stuart king; unites crowns but not parliaments."),
        ("1642–1651", "⚔️", "English Civil War between Royalists (Cavaliers) and Parliamentarians (Roundheads); struggle over governance and religion."),
        ("1649", "⚔️", "Execution of Charles I; England declared a republic (Commonwealth) under Oliver Cromwell."),
        ("1660", "👑", "Restoration of the monarchy; Charles II becomes king."),
        ("1685", "👑", "James II becomes king; favors Catholics; tension with Protestant Parliament."),
        ("1688", "⚖️", "Glorious Revolution; William III and Mary II invited to rule; Bill of Rights 1689 establishes constitutional monarchy.")
    ]
    display_events(events)

# A Global Power
with st.expander("A Global Power"):
    events = [
        ("1707", "⚖️", "Act of Union unites England and Scotland into Kingdom of Great Britain; creates unified Parliament."),
        ("1721–1742", "👔", "Sir Robert Walpole serves as first de facto Prime Minister; establishes role of Cabinet government."),
        ("1745–1746", "⚔️", "Jacobite Rebellion led by Bonnie Prince Charlie; defeated at Battle of Culloden; end of major Jacobite attempts."),
        ("1760s onwards", "⚙️", "The Enlightenment spreads; Industrial Revolution begins; advancements in science, technology, and philosophy."),
        ("1807", "⚖️", "Slave Trade Act abolishes slave trade in British Empire; result of abolitionist movement led by figures like William Wilberforce."),
        ("1833", "⚖️", "Slavery Abolition Act abolishes slavery throughout most of the British Empire.")
    ]
    display_events(events)

# 19th Century and the Victorian Age
with st.expander("19th Century and the Victorian Age"):
    events = [
        ("1837–1901", "👑", "Reign of Queen Victoria; era marked by industrial expansion and empire building."),
        ("1851", "🎪", "Great Exhibition held in Crystal Palace, London; showcases Britain's industrial achievements."),
        ("1853–1856", "⚔️", "Crimean War; Florence Nightingale revolutionizes nursing practices."),
        ("1867", "🗳️", "Second Reform Act extends voting rights to urban working men; part of democratic reforms."),
        ("Late 19th century", "♀️", "Women's suffrage movement grows; leaders like Emmeline Pankhurst advocate for voting rights."),
        ("1918", "🗳️", "Representation of the People Act grants voting rights to women over 30."),
        ("1928", "🗳️", "Equal Franchise Act grants equal voting rights to women at age 21.")
    ]
    display_events(events)

# The 20th Century
with st.expander("The 20th Century"):
    events = [
        ("1914–1918", "⚔️", "First World War; Britain fights with Allies; significant loss of life; Battle of the Somme."),
        ("1916", "💣", "Easter Rising in Dublin; leads to increased support for Irish independence."),
        ("1921", "⚖️", "Anglo-Irish Treaty partitions Ireland; creation of Irish Free State and Northern Ireland."),
        ("1939–1945", "⚔️", "Second World War; Britain stands against Nazi Germany; Winston Churchill becomes Prime Minister."),
        ("1940", "✈️", "Battle of Britain; RAF defends UK against German Luftwaffe."),
        ("1944", "⚔️", "D-Day landings in Normandy; begin liberation of Western Europe."),
        ("1945", "🏳️", "End of WWII; founding of United Nations; UK faces economic challenges.")
    ]
    display_events(events)

# Post-War Britain
with st.expander("Post-War Britain"):
    events = [
        ("1945", "⚖️", "Labour government under Clement Attlee elected; begins establishment of welfare state."),
        ("1948", "⚕️", "National Health Service (NHS) established by Aneurin Bevan; provides free healthcare."),
        ("1950s", "🚢", "Immigration from Commonwealth countries to aid reconstruction; arrival of SS Empire Windrush."),
        ("1960s", "🎸", "Social and cultural revolution; rise of British music, fashion, and liberalization of laws."),
        ("1973", "🇪🇺", "UK joins European Economic Community (EEC); begins closer economic ties with Europe."),
        ("1979–1990", "👩‍💼", "Margaret Thatcher serves as Prime Minister; implements economic reforms; privatization and deregulation."),
        ("1982", "⚔️", "Falklands War; UK defends Falkland Islands from Argentine invasion."),
        ("1998", "⚖️", "Good Friday Agreement signed; significant step in Northern Ireland peace process.")
    ]
    display_events(events)

# Contemporary Britain
with st.expander("Contemporary Britain"):
    events = [
        ("1997", "⚖️", "Tony Blair's Labour government introduces devolution; Scottish Parliament and Welsh Assembly established."),
        ("2010", "👔", "Coalition government formed; David Cameron becomes Prime Minister."),
        ("2016", "🇪🇺", "Brexit referendum; UK votes to leave European Union."),
        ("2020", "🏳️", "UK formally leaves the European Union on January 31st.")
    ]
    display_events(events)

# Key British Inventions of the 20th Century
with st.expander("Key British Inventions of the 20th Century"):
    events = [
        ("1928", "💊", "Penicillin discovered by Sir Alexander Fleming; revolutionizes medicine."),
        ("1930s", "✈️", "Jet engine developed by Sir Frank Whittle; advances aviation."),
        ("1935", "📡", "Radar technology developed by Sir Robert Watson-Watt; crucial in WWII."),
        ("1953", "🧬", "Structure of DNA discovered by Francis Crick and James Watson at Cambridge."),
        ("1967", "🏧", "First cash-dispensing ATM installed; invented by James Goodfellow."),
        ("1989", "🌐", "World Wide Web invented by Sir Tim Berners-Lee; transforms global communication."),
        ("1996", "🐑", "Dolly the sheep cloned by Sir Ian Wilmut and Keith Campbell; first mammal cloned from adult cell.")
    ]
    display_events(events)

# Understanding the Key Themes
with st.expander("Understanding the Key Themes"):
    themes = [
        ("Development of Parliament", "🏛️", "From Magna Carta to Bill of Rights 1689; establishes constitutional monarchy and parliamentary democracy."),
        ("Impact of Invasions", "⚔️", "Roman, Anglo-Saxon, Viking, and Norman invasions shape culture, language, and society."),
        ("Religious Changes", "✝️", "Shift from paganism to Christianity; Reformation under Henry VIII; religious conflicts and settlements."),
        ("Wars and Conflicts", "💣", "Crucial battles like Hastings, Bannockburn, Civil Wars, and World Wars shape national identity."),
        ("Expansion and Empire", "🌍", "Growth of British Empire; colonization; impact on global trade and politics."),
        ("Industrial Revolution", "⚙️", "Technological advancements transform industry; Britain becomes 'workshop of the world.'"),
        ("Social Reforms", "📜", "Democratic progress through Reform Acts; women's suffrage movement achieves voting rights."),
        ("20th Century Events", "🕰️", "World Wars, establishment of welfare state, decolonization, social changes, and Brexit.")
    ]
    display_events(themes)
