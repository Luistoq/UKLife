import streamlit as st

st.set_page_config(layout="wide")

st.title("A Modern, Thriving UK Society")

# The UK Today
with st.expander("🌍 The UK Today"):
    st.subheader("🌐 A Diverse and Multicultural Nation")
    st.write("""
    The United Kingdom is a diverse society with a rich cultural heritage and a mix of various ethnic groups. Approximately 10% of the population has at least one parent or grandparent born outside the UK. This multicultural fabric is especially prominent in major cities like London.
    """)
    st.subheader("🗺️ Geography")
    st.write("""
    Located in the northwest of Europe, the UK stretches about 870 miles from John O'Groats in Scotland to Land's End in England. While most people reside in urban areas, the countryside remains a cherished part of the nation's landscape, popular for activities like walking, camping, and fishing.
    """)

    st.subheader("📊 Population and Demographics")
    st.write("""
    The UK's population has grown over time due to longer life expectancy and migration. England constitutes about 84% of the total population, Scotland 8%, Wales 5%, and Northern Ireland less than 3%. The population is aging, leading to increased costs in pensions and healthcare.
    """)

    st.subheader("🗣️ Languages and Dialects")
    st.write("""
    English is the predominant language, but there are regional languages like Welsh in Wales, Gaelic in parts of Scotland, and Irish Gaelic in Northern Ireland. These languages are taught in schools and spoken in communities.
    """)

    st.subheader("💷 Currency")
    st.write("""
    The currency of the UK is the pound sterling (£), divided into 100 pence. Coins come in denominations of 1p, 2p, 5p, 10p, 20p, 50p, £1, and £2. Banknotes are available in £5, £10, £20, and £50. Scotland and Northern Ireland issue their own banknotes, which are legal currency throughout the UK.
    """)

    st.subheader("⚖️ An Equal Society")
    st.write("""
    The UK promotes equality and prohibits discrimination based on gender or marital status. Men and women have equal rights in work, property ownership, marriage, and divorce. Women make up about half of the workforce, often achieving higher educational qualifications than men.
    """)

# Religion
with st.expander("🛐 Religion in the UK"):
    st.subheader("🕊️ Religious Diversity")
    st.write("""
    Historically a Christian country, the UK now embraces a wide range of religions. According to recent surveys, 59% identify as Christian, while other religions like Islam, Hinduism, Sikhism, Judaism, and Buddhism are also practiced. About 25% of the population identifies with no religion.
    """)

    st.subheader("⛪ Christian Churches")
    st.write("""
    - **Church of England**: The official state church in England, headed by the monarch.
    - **Church of Scotland**: A Presbyterian church, independent of the state.
    - **Other Denominations**: Include Baptists, Methodists, Presbyterians, Quakers, and Roman Catholics.
    """)

    st.subheader("🎉 Patron Saints' Days")
    events = [
        ("1 March", "🏴󠁧󠁢󠁷󠁬󠁳󠁿", "St David's Day (Wales)"),
        ("17 March", "🍀", "St Patrick's Day (Northern Ireland)"),
        ("23 April", "🏴󠁧󠁢󠁥󠁮󠁧󠁿", "St George's Day (England)"),
        ("30 November", "🏴󠁧󠁢󠁳󠁣󠁴󠁿", "St Andrew's Day (Scotland)")
    ]
    st.write("Each nation in the UK has its own patron saint, celebrated on specific days:")
    for date, emoji, event in events:
        st.write(f"{emoji} **{date}**: {event}")

# Customs and Traditions
with st.expander("🎭 Customs and Traditions"):
    st.subheader("✝️ Main Christian Festivals")
    st.write("""
    - **Christmas Day (25 December)** 🎄: Celebrates the birth of Jesus Christ. Traditions include family gatherings, gift-giving, and festive meals.
    - **Easter** 🐣: Marks the resurrection of Jesus. Celebrated with church services, Easter eggs, and family activities.
    """)

    st.subheader("🕌 Other Religious Festivals")
    st.write("""
    - **Diwali** 🪔: Hindu and Sikh Festival of Lights, celebrating the victory of light over darkness.
    - **Hannukah** 🕎: Jewish festival commemorating the rededication of the Second Temple in Jerusalem.
    - **Eid al-Fitr and Eid ul Adha** 🌙: Muslim festivals marking the end of Ramadan and the willingness of Ibrahim to sacrifice his son, respectively.
    - **Vaisakhi** 🏵️: Sikh festival celebrating the founding of the Khalsa.
    """)

    st.subheader("🎈 Other Festivals and Traditions")
    st.write("""
    - **New Year's Day (1 January)** 🎆
    - **Valentine's Day (14 February)** ❤️
    - **April Fool's Day (1 April)** 🤡
    - **Mother's Day and Father's Day** 👩‍👧👨‍👧
    - **Halloween (31 October)** 🎃
    - **Bonfire Night (5 November)** 🔥: Commemorates the failure of the Gunpowder Plot in 1605.
    - **Remembrance Day (11 November)** 🌺: Honors those who died in wars.
    """)

    st.subheader("🏖️ Bank Holidays")
    st.write("""
    Additional public holidays known as bank holidays occur throughout the year, providing time off for workers and opportunities for leisure activities.
    """)

# Sport
with st.expander("🏅 Sport in the UK"):
    st.subheader("🏆 Popular Sports")
    st.write("""
    The UK is home to many popular sports, including football ⚽, cricket 🏏, rugby 🏉, tennis 🎾, golf ⛳, and horse racing 🐎. It has a rich sporting heritage and has hosted the Olympic Games in 1908, 1948, and 2012.
    """)

    st.subheader("🎖️ Notable British Sports Figures")
    sports_figures = [
        ("Sir Roger Bannister", "🏃‍♂️ First person to run a mile in under four minutes."),
        ("Sir Jackie Stewart", "🏎️ Three-time Formula One world champion."),
        ("Sir Steve Redgrave", "🚣‍♂️ Winner of gold medals in rowing at five consecutive Olympic Games."),
        ("Dame Kelly Holmes", "🏃‍♀️ Double Olympic gold medalist in middle-distance running."),
        ("Sir Mo Farah", "🏃‍♂️ Olympic gold medalist in long-distance running."),
        ("Sir Andy Murray", "🎾 Tennis champion and Wimbledon winner."),
    ]
    for name, achievement in sports_figures:
        st.write(f"- **{name}**: {achievement}")

    st.subheader("🎯 Major Sporting Events")
    st.write("""
    - **Football** ⚽: The Premier League is followed worldwide, with national teams competing in international tournaments like the FIFA World Cup.
    - **Cricket** 🏏: Home of the Ashes series against Australia.
    - **Rugby** 🏉: Both rugby union and rugby league are popular, with events like the Six Nations Championship.
    - **Tennis** 🎾: Wimbledon is one of the four Grand Slam tournaments.
    - **Horse Racing** 🐎: Events like the Grand National and Royal Ascot are key dates in the sporting calendar.
    """)

# Arts and Culture
with st.expander("🎨 Arts and Culture"):
    st.subheader("🎼 Music")
    st.write("""
    The UK has a vibrant music scene, from classical 🎻 to contemporary genres 🎸. The BBC Proms is a celebrated classical music festival, while British pop and rock bands like The Beatles and The Rolling Stones have had a global impact.
    """)

    st.subheader("🎭 Theatre")
    st.write("""
    The UK has a rich theatrical heritage, with London's West End being a hub for world-class productions. Traditional pantomimes are popular during the Christmas season.
    """)

    st.subheader("🖼️ Art and Architecture")
    st.write("""
    The UK boasts numerous galleries and architectural landmarks. Notable artists include Thomas Gainsborough, J.M.W. Turner, and David Hockney. Architectural feats range from historic castles 🏰 to modern skyscrapers 🏙️.
    """)

    st.subheader("📚 Literature")
    st.write("""
    The UK has produced many renowned authors and poets, such as William Shakespeare, Jane Austen, Charles Dickens, and J.K. Rowling. Literature continues to be a significant part of British culture.
    """)

# Leisure
with st.expander("🏖️ Leisure Activities"):
    st.subheader("🌿 Gardening")
    st.write("""
    Gardening is a popular hobby 🌱, with many people tending to their own gardens or allotments. Famous gardens include Kew Gardens and those managed by the National Trust.
    """)

    st.subheader("🛍️ Shopping")
    st.write("""
    Shopping is a common leisure activity 🛒, with various high streets, shopping centers, and markets offering a range of goods.
    """)

    st.subheader("🍽️ Cooking and Food")
    st.write("""
    The UK's culinary scene is diverse 🍲, reflecting its multicultural society. Traditional dishes vary by region, such as roast beef in England, haggis in Scotland, and Welsh cakes in Wales.
    """)

    st.subheader("🎬 Films and Cinema")
    st.write("""
    The UK has a significant film industry 🎥, producing globally recognized films and nurturing talent like Sir Alfred Hitchcock and Sir Anthony Hopkins. The British Academy Film Awards (BAFTAs) celebrate achievements in cinema.
    """)

    st.subheader("📺 Television and Radio")
    st.write("""
    The UK offers a wide range of TV channels 📺 and radio stations 📻. The BBC is a major broadcaster funded by the television licence fee.
    """)

    st.subheader("🍻 Social Activities")
    st.write("""
    - **Pubs and Nightclubs** 🍺: Central to British social life, offering places to meet and enjoy entertainment.
    - **Betting and Gambling** 🎰: A popular pastime, including national lotteries and sports betting.
    - **Pets** 🐶🐱: Many households have pets, with dogs and cats being the most common.
    """)

# Places of Interest
with st.expander("🏞️ Places of Interest"):
    st.subheader("🌄 National Parks and Countryside")
    st.write("""
    The UK has 15 national parks, offering opportunities for outdoor activities like hiking 🥾, cycling 🚴‍♀️, and wildlife watching 🦌. Notable parks include the Lake District, Snowdonia, and Loch Lomond and The Trossachs.
    """)

    st.subheader("🏛️ Famous Landmarks")
    landmarks = [
        ("Big Ben", "🕰️ The iconic clock tower located at the Houses of Parliament in London."),
        ("The Eden Project", "🌿 A complex of biomes in Cornwall housing diverse plant life."),
        ("Edinburgh Castle", "🏰 Historic fortress dominating the skyline of Scotland's capital."),
        ("The Giant's Causeway", "🌊 Unique rock formations on the coast of Northern Ireland."),
        ("London Eye", "🎡 A large Ferris wheel on the South Bank of the River Thames."),
        ("Stonehenge", "🗿 Prehistoric monument in Wiltshire, England."),
        ("The Tower of London", "🏯 Historic castle housing the Crown Jewels."),
        ("The Lake District", "⛰️ England's largest national park, known for its lakes and mountains."),
    ]
    for name, description in landmarks:
        st.write(f"- **{name}**: {description}")

# Understanding the Key Points
with st.expander("📝 Check That You Understand"):
    st.write("""
    - The capital cities of the UK and their significance.
    - Languages spoken in different regions besides English.
    - Changes in the UK's population and demographics.
    - The UK's status as an equal and ethnically diverse society.
    - The currency used in the UK.
    - The various religions practiced and the concept of religious freedom.
    - The importance of patron saints and their associated days.
    - Major festivals and public holidays.
    - Popular sports and notable athletes.
    - Contributions to arts and culture, including music, theatre, literature, and film.
    - Leisure activities and social customs.
    - Places of interest and landmarks across the UK.
    """)

