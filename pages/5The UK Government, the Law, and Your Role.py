import streamlit as st

st.set_page_config(layout="wide")

st.title("🇬🇧 The UK Government, the Law, and Your Role")

# The Development of British Democracy
with st.expander("🏛️ The Development of British Democracy"):
    st.subheader("📜 Evolution of Democracy")
    st.write("""
    Democracy, a system where the entire adult population has a say in governance, either directly or through elected representatives, has evolved significantly in the UK.

    At the start of the 19th century, the UK was far from the democracy we know today. Although elections existed, only a small fraction of the population—men over 21 who owned a certain amount of property—could vote.

    Throughout the 19th century, the right to vote expanded, and political parties began involving ordinary citizens as members.
    """)
    st.subheader("✊ The Chartists Movement")
    st.write("""
    In the 1830s and 1840s, a group called the Chartists campaigned for reforms, demanding:

    - Universal male suffrage 🗳️
    - Annual parliamentary elections 🗓️
    - Equal electoral districts ⚖️
    - Secret ballots 🕵️
    - No property qualifications for MPs 🏛️
    - Salaries for MPs 💷

    While initially unsuccessful, by 1918 most of these reforms were implemented. Women over 30 gained the right to vote in 1918, and by 1928, both men and women over 21 could vote. The voting age was lowered to 18 in 1969.
    """)

# The British Constitution
with st.expander("📖 The British Constitution"):
    st.subheader("📝 An Unwritten Constitution")
    st.write("""
    A constitution outlines the principles by which a country is governed, including the institutions responsible and how their powers are checked. The UK's constitution isn't written in a single document, earning it the description of "unwritten."

    This unwritten nature stems from the UK's gradual development without a revolutionary change that overhauled the system entirely. Some argue this allows for flexibility and effective governance, while others advocate for a single written document.
    """)
    st.subheader("🏢 Constitutional Institutions")
    st.write("""
    Key parts of the UK's government include:

    - The Monarchy 👑
    - Parliament (House of Commons and House of Lords) 🏛️
    - The Prime Minister and Cabinet 👥
    - The Judiciary ⚖️
    - The Police 🚓
    - The Civil Service 🏢
    - Local Government 🏘️

    Additionally, devolved governments in Scotland, Wales, and Northern Ireland have legislative powers on certain issues.
    """)

# The Monarchy
with st.expander("👑 The Monarchy"):
    st.subheader("👑 King Charles III")
    st.write("""
    King Charles III is the UK's head of state and also serves as the monarch for several Commonwealth countries. The UK operates as a constitutional monarchy, meaning the monarch doesn't govern the country but plays a ceremonial role.

    The monarch invites the leader of the majority party in Parliament to become the Prime Minister. While the monarch meets regularly with the Prime Minister to offer advice and encouragement, government policies are determined by the Prime Minister and the Cabinet.

    The King has important ceremonial duties, such as opening the new parliamentary session each year and representing the UK internationally.
    """)
    st.subheader("🎶 The National Anthem")
    st.write("""
    The UK's national anthem is "God Save the King." It is performed at significant national events and occasions involving the monarch or the Royal Family.

    **First Verse:**

    *"God save our gracious King!  
    Long live our noble King!  
    God save the King!  
    Send him victorious,  
    Happy and glorious,  
    Long to reign over us,  
    God save the King!"*

    New citizens swear or affirm loyalty to the King during the citizenship ceremony.
    """)

# System of Government
with st.expander("🏛️ System of Government"):
    st.subheader("🗳️ Parliamentary Democracy")
    st.write("""
    The UK operates as a parliamentary democracy, divided into constituencies that elect Members of Parliament (MPs) during General Elections. The party with the majority of MPs forms the government.

    - **House of Commons**: The primary legislative body with elected MPs representing constituencies.
    - **House of Lords**: Members are not elected but appointed, including life peers, bishops, and hereditary peers (limited number).
    """)
    st.subheader("🔨 The Speaker")
    st.write("""
    Debates in the House of Commons are chaired by the Speaker, who is an MP elected by other MPs. The Speaker remains neutral and ensures that debates are conducted fairly, following the rules of the House.
    """)
    st.subheader("🗳️ Elections")
    st.write("""
    - **General Elections**: Held at least every five years to elect MPs.
    - **By-elections**: Occur if an MP resigns or passes away.
    - **Voting System**: 'First past the post'—the candidate with the most votes in a constituency wins.
    """)

# Check That You Understand
with st.expander("🧐 Check That You Understand"):
    st.info("""
    **It's crucial to understand the following topics:**

    - **Development of Democracy in the UK**: How democratic rights have evolved over time.
    - **The UK's Constitution**: The nature of the unwritten constitution and how it differs from others.
    - **Role of the Monarch**: The ceremonial duties and constitutional role of the King.
    - **Functions of the House of Commons and House of Lords**: Their composition and responsibilities.
    - **Role of the Speaker**: How the Speaker ensures fair debates in Parliament.
    - **Election of MPs**: The electoral process and the 'first past the post' system.
    """)

# The Government
with st.expander("👥 The Government"):
    st.subheader("👔 The Prime Minister")
    st.write("""
    The Prime Minister is the leader of the party with the most seats in the House of Commons. Responsibilities include:

    - Appointing Cabinet members.
    - Overseeing the operation of the government.
    - Representing the UK domestically and internationally.

    The official residence is at 10 Downing Street in London.
    """)
    st.subheader("👥 The Cabinet")
    st.write("""
    The Cabinet consists of senior government ministers appointed by the Prime Minister. Key positions include:

    - **Chancellor of the Exchequer**: Manages the economy.
    - **Home Secretary**: Oversees crime, policing, and immigration.
    - **Foreign Secretary**: Manages relations with other countries.

    The Cabinet meets regularly to make important policy decisions.
    """)
    st.subheader("🧑‍💼 The Opposition and Shadow Cabinet")
    st.write("""
    The second-largest party forms the Opposition, led by the Leader of the Opposition. Responsibilities include:

    - Challenging government policies.
    - Offering alternative proposals.
    - Appointing a Shadow Cabinet to mirror government positions.

    **Prime Minister's Questions**: A weekly session where the Opposition questions the Prime Minister.
    """)
    st.subheader("🏛️ Political Parties")
    st.write("""
    The main political parties in the UK are:

    - **Conservative Party** 🟦
    - **Labour Party** 🟥
    - **Liberal Democrats** 🟨
    - Parties representing Scottish, Welsh, and Northern Irish interests.

    Citizens can join political parties to participate in political debates, contribute to campaigns, and stand for public office.
    """)
    st.subheader("🏢 The Civil Service")
    st.write("""
    Civil servants are employed to implement government policies and deliver public services. Key characteristics:

    - Politically neutral.
    - Selected based on merit.
    - Serve ministers of any government.

    Core values include integrity, honesty, objectivity, and impartiality.
    """)
    st.subheader("🏘️ Local Government")
    st.write("""
    Local authorities govern towns, cities, and rural areas, providing services like:

    - Education 🎓
    - Housing 🏠
    - Planning 🗺️
    - Social Services ❤️

    They are funded by central government grants and local taxes.
    """)
    st.subheader("🏴󠁧󠁢󠁳󠁣󠁴󠁿 Devolved Administrations")
    st.write("""
    Since 1997, powers have been devolved to:

    - **Scottish Parliament** in Edinburgh.
    - **Senedd Cymru** (Welsh Parliament) in Cardiff.
    - **Northern Ireland Assembly** in Belfast.

    They have authority over areas like education, health, and transportation.
    """)
    st.subheader("📰 Media and Government")
    st.write("""
    Parliamentary proceedings are broadcasted and published in official reports called Hansard. The UK has a free press, meaning newspapers and other media can publish without government interference. However, they are expected to provide balanced coverage, especially in broadcasting.
    """)

# Check That You Understand (Government)
with st.expander("🧐 Check That You Understand"):
    st.info("""
    **Key topics to understand:**

    - **Roles of the Prime Minister, Cabinet, Opposition, and Shadow Cabinet**.
    - **Function of Political Parties**: How they influence the UK government system.
    - **Main Political Parties**: Recognize the major parties and their symbols.
    - **Pressure and Lobby Groups**: Their role in influencing policies.
    - **Civil Service**: Understand its neutrality and function.
    - **Local Government Responsibilities**: Services provided at the local level.
    - **Devolved Governments**: Powers held by Scotland, Wales, and Northern Ireland.
    - **Media's Role**: How proceedings are reported and the importance of a free press.
    """)

# Voting
with st.expander("🗳️ Voting and Elections"):
    st.subheader("🗳️ Who Can Vote?")
    st.write("""
    The UK has a democratic voting system since 1928. You can vote if you are:

    - Aged 18 or over.
    - A UK citizen, or a qualifying Commonwealth or Irish citizen resident in the UK.

    """)
    st.subheader("📝 The Electoral Register")
    st.write("""
    To vote, you must be registered on the electoral register. You can register online or by contacting your local council's electoral registration office.

    The register is updated annually, but you can register at any time.
    """)
    st.subheader("🏫 Where to Vote")
    st.write("""
    Voting takes place at local polling stations, open from 7 AM to 10 PM on election day. You'll receive a poll card informing you of your designated polling station.

    If you cannot attend in person, you can apply for a postal vote.
    """)
    st.subheader("🧑‍💼 Standing for Office")
    st.write("""
    Most citizens aged 18 or over can stand for public office, except:

    - Members of the armed forces.
    - Civil servants.
    - People convicted of certain criminal offenses.

    Members of the House of Lords cannot stand for the House of Commons but can hold other public offices.
    """)
    st.subheader("🏛️ Visiting Parliament and Devolved Administrations")
    st.write("""
    **UK Parliament**: The public can watch debates from the galleries in the Houses of Parliament.

    **Scottish Parliament, Senedd Cymru, and Northern Ireland Assembly**: Visitors can watch proceedings and participate in tours. Check their official websites for details.
    """)

# Check That You Understand (Voting)
with st.expander("🧐 Check That You Understand"):
    st.info("""
    **Essential points:**

    - **Eligibility to Vote**: Who can vote in the UK.
    - **How to Register**: The process of getting on the electoral register.
    - **Voting Process**: How and where to vote.
    - **Standing for Public Office**: Requirements to become a candidate.
    - **Visiting Government Institutions**: How to visit Parliament and devolved administrations.
    """)

# The UK and International Institutions
with st.expander("🌐 The UK and International Institutions"):
    st.subheader("🌍 The Commonwealth")
    st.write("""
    An association of 54 countries, mostly former British colonies, that work together towards shared goals in democracy and development. Membership is voluntary.
    """)
    st.subheader("🏛️ The Council of Europe")
    st.write("""
    An organization with 47 member countries promoting human rights, democracy, and the rule of law. Responsible for the European Convention on Human Rights.
    """)
    st.subheader("🇺🇳 The United Nations (UN)")
    st.write("""
    An international organization with over 190 member countries aimed at maintaining international peace and security. The UK is one of the five permanent members of the UN Security Council.
    """)
    st.subheader("🛡️ The North Atlantic Treaty Organization (NATO)")
    st.write("""
    A military alliance of European and North American countries committed to mutual defense in response to an attack by any external party.
    """)

# Check That You Understand (International Institutions)
with st.expander("🧐 Check That You Understand"):
    st.info("""
    **Key topics:**

    - **Role of the Commonwealth**.
    - **International Organizations**: The UK's membership in bodies like the UN, NATO, and the Council of Europe.
    """)

# Respecting the Law
with st.expander("⚖️ Respecting the Law"):
    st.subheader("⚖️ The Law in the UK")
    st.write("""
    The UK legal system treats everyone equally. Laws are divided into:

    - **Criminal Law**: Offenses against society, prosecuted by the state.
    - **Civil Law**: Disputes between individuals or organizations.

    Examples of criminal offenses include carrying weapons, drug offenses, racial crimes, selling tobacco or alcohol to minors, and smoking in prohibited areas.

    Civil laws cover areas like housing disputes, consumer rights, employment law, and debt.
    """)
    st.subheader("👮 The Police and Their Duties")
    st.write("""
    The police are responsible for:

    - Protecting life and property.
    - Maintaining public order.
    - Preventing and detecting crime.

    Police officers are expected to act with integrity and can be held accountable if they misuse their authority.
    """)
    st.subheader("🛡️ Terrorism and Extremism")
    st.write("""
    The UK faces various terrorist threats. Citizens should be vigilant and report any suspicious activities to the authorities. Extremism and radicalization are taken seriously to ensure everyone's safety.
    """)

# Check That You Understand (Law)
with st.expander("🧐 Check That You Understand"):
    st.info("""
    **Important points:**

    - **Difference Between Civil and Criminal Law**.
    - **Duties of the Police**.
    - **Current Terrorist Threats**: Awareness of potential risks.
    """)

# The Role of the Courts
with st.expander("⚖️ The Role of the Courts"):
    st.subheader("👨‍⚖️ The Judiciary")
    st.write("""
    Judges interpret the law, ensure fair trials, and are independent of the government. They can challenge government actions and settle disputes between individuals.
    """)
    st.subheader("🏛️ Criminal Courts")
    st.write("""
    - **Magistrates' and Justice of the Peace Courts**: Handle minor offenses. Magistrates are community members who volunteer.
    - **Crown Courts and Sheriff Courts**: Deal with serious offenses with a judge and jury.
    - **Youth Courts**: Handle cases involving individuals aged 10 to 17.
    """)
    st.subheader("🏛️ Civil Courts")
    st.write("""
    - **County Courts**: Handle disputes like personal injury, family matters, and breaches of contract.
    - **Small Claims Procedure**: Simplifies resolving minor disputes without significant legal costs.
    """)
    st.subheader("📝 Legal Advice")
    st.write("""
    **Solicitors** are trained lawyers who provide legal advice and representation. They can be found locally, and it's important to choose one specializing in the relevant area of law.
    """)

# Check That You Understand (Courts)
with st.expander("🧐 Check That You Understand"):
    st.info("""
    **Key topics:**

    - **Role of the Judiciary**: Independence and responsibilities.
    - **Different Criminal Courts**: Functions and structures.
    - **Different Civil Courts**: How they handle disputes.
    - **Small Claims**: How to resolve minor legal issues.
    """)

# Fundamental Principles
with st.expander("⚖️ Fundamental Principles"):
    st.subheader("🗽 Human Rights")
    st.write("""
    The UK has a long history of protecting individual rights, rooted in documents like Magna Carta and the Bill of Rights of 1689. The Human Rights Act 1998 incorporates the European Convention on Human Rights into UK law, covering rights such as:

    - Right to life.
    - Prohibition of torture.
    - Freedom of thought, conscience, and religion.
    - Freedom of expression.
    """)
    st.subheader("⚖️ Equal Opportunities")
    st.write("""
    UK laws prohibit unfair treatment based on age, disability, sex, pregnancy, race, religion, sexuality, or marital status. Organizations like the Equality and Human Rights Commission provide support and information.
    """)
    st.subheader("🚫 Domestic Violence")
    st.write("""
    Domestic violence is a serious crime. Anyone experiencing or aware of domestic violence should seek help immediately. There are helplines, shelters, and legal protections available.
    """)
    st.subheader("🚫 Female Genital Mutilation (FGM)")
    st.write("""
    FGM is illegal in the UK. It's a criminal offense to perform FGM or assist in arranging it.
    """)
    st.subheader("🚫 Forced Marriage")
    st.write("""
    Forced marriage is illegal. Everyone has the right to choose whom they marry. Protection orders can be issued to prevent forced marriages.
    """)
    st.subheader("💰 Taxation")
    st.write("""
    - **Income Tax**: Paid on earnings, pensions, and other income.
    - **National Insurance**: Contributions fund state benefits like the NHS and pensions.

    You need a National Insurance number to work and pay taxes in the UK.
    """)
    st.subheader("🚗 Driving")
    st.write("""
    To drive in the UK, you must:

    - Be at least 17 years old (16 for mopeds).
    - Have a valid driving license.
    - Have insurance, pay vehicle tax, and ensure the vehicle has a valid MOT if over three years old.
    """)

# Check That You Understand (Principles)
with st.expander("🧐 Check That You Understand"):
    st.info("""
    **Essential points:**

    - **Fundamental Principles of UK Law**: Including human rights and equal opportunities.
    - **Illegality of Domestic Violence, FGM, and Forced Marriage**.
    - **Income Tax and National Insurance**: Understanding taxation responsibilities.
    - **Driving Requirements**: Legal obligations for drivers.
    """)

# Your Role in the Community
with st.expander("🤝 Your Role in the Community"):
    st.subheader("🤲 Values and Responsibilities")
    st.write("""
    Becoming a British citizen or resident comes with responsibilities:

    - Obeying the law.
    - Respecting others' rights.
    - Treating others with fairness.
    - Looking after yourself and your family.
    - Protecting the environment.
    - Participating in community life.
    """)
    st.subheader("🏡 Being a Good Neighbor")
    st.write("""
    - Introduce yourself to neighbors.
    - Respect privacy and keep noise levels reasonable.
    - Maintain your property and dispose of rubbish properly.
    """)
    st.subheader("🎗️ Getting Involved in Local Activities")
    st.write("""
    Volunteering and community participation enrich both you and your community. Opportunities include:

    - **Jury Service**: Serving on a jury if called.
    - **Helping in Schools**: Assisting with activities or joining the PTA.
    - **Becoming a School Governor**: Contributing to school management.
    - **Supporting Political Parties**: Joining a party and participating in political processes.
    - **Volunteering with Local Services**: Such as police, health services, or charities.
    - **Blood and Organ Donation**: Registering to donate can save lives.
    """)
    st.subheader("🌳 Looking After the Environment")
    st.write("""
    - **Recycle**: Reduce waste by recycling materials.
    - **Support Local Businesses**: Shop locally to reduce your carbon footprint.
    - **Use Public Transport**: Walk, cycle, or use public transport when possible.
    """)

# Check That You Understand (Community)
with st.expander("🧐 Check That You Understand"):
    st.info("""
    **Key areas:**

    - **Ways to Help at Your Child's School**.
    - **Role of School Governors**: How to become one.
    - **Political Participation**: Roles within political parties.
    - **Volunteering Opportunities**: How to support local services.
    - **Blood and Organ Donation**: Importance and how to register.
    - **Benefits of Volunteering**: For you and the community.
    - **Environmental Responsibility**: Actions to protect the environment.
    """)

