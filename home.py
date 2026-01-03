import streamlit as st

def render(debug=False):
    st.title("🏏 Cricbuzz LiveStats")
    st.subheader("Live Match & Today’s Matches")

    # ---------- MAIN LAYOUT ----------
    left_col, right_col = st.columns([1, 2])

    # ---------- LEFT SIDE : TODAY MATCHES DROPDOWN ----------
    with left_col:
        match_options = [
            "Today’s Matches",
            "India vs Australia — 🟢 In progress",
            "Pakistan vs England — ⏳ Will begin in 10 mins (Toss: Pakistan, Bat first)",
            "South Africa vs Sri Lanka — ❌ Cancelled due to rain",
            "New Zealand vs Bangladesh — 🌙 Delayed (Low light, starts in 40 mins)",
            "West Indies vs Afghanistan — 🚫 Abandoned (Bad weather)",
            "Nepal vs Ireland — 🕗 Today 8:00 PM"
        ]

        selected_match = st.selectbox("", match_options, index=0)

        if selected_match != "Today’s Matches":
            if "🟢 In progress" in selected_match:
                st.info("India vs Australia is currently in progress.")
            elif "⏳ Will begin in 10 mins" in selected_match:
                st.info("Pakistan vs England — Toss won by Pakistan, chose to bat first. Match will begin in 10 mins.")
            elif "❌ Cancelled" in selected_match:
                st.info("The scheduled match between South Africa vs Sri Lanka was cancelled due to heavy rain.")
            elif "🌙 Delayed" in selected_match:
                st.info("The scheduled match between New Zealand vs Bangladesh is delayed due to low light. Next update in 20 mins.")
            elif "🚫 Abandoned" in selected_match:
                st.info("The scheduled match between West Indies vs Afghanistan was abandoned due to bad weather.")
            elif "🕗 Today 8:00 PM" in selected_match:
                st.info("Nepal vs Ireland match will start at 7:30 PM (toss).")

    # ---------- RIGHT SIDE : LIVE MATCH CARD ----------
    with right_col:
        with st.container(border=True):
            st.markdown(
                """
                <div style="display:flex; justify-content:space-between;">
                    <b>Gavaskar - Border Series 2025 • Match 4</b>
                    <span style="color:green;"><b>🟢 LIVE • T20</b></span>
                </div>
                <hr/>
                <div style="font-size:16px;">
                    🏏 <b>India</b> — 167/3 (20 overs)<br/>
                    🏏 <b>Australia</b> — 110/6 (14.5 overs)
                </div>
                <div style="margin-top:12px; font-size:14px;">
                    Australia batting
                </div>
                """,
                unsafe_allow_html=True
            )

            show_details = st.button("📊 View Live Match Details")

    # ---------- MATCH REPORT TABS ----------
    if show_details:
        st.divider()
        tab1, tab2, tab3 = st.tabs(["📋 Summary of Match", "📑 Scorecard", "ℹ️ Match Info"])

        # ---------- SUMMARY ----------
        with tab1:
            st.subheader("📋 Summary of Match")
            st.write("India — 167/3 (20 overs)")
            st.write("Australia — 110/6 (14.5 overs)")
            st.write("• Current Run Rate: 8.35")
            st.write("• Required Run Rate: 11.20")
            st.write("• Partnership: Maxwell & Green — 45 runs (28 balls)")
            st.write("• Current Bowler: Bumrah — 3.1 overs, 20 runs, 2 wickets, 10 dot balls")

        # ---------- SCORECARD ----------
        with tab2:
            st.subheader("📑 Scorecard")
            left_col2, right_col2 = st.columns(2)

            # India Innings
            with left_col2:
                st.markdown("### 🏏 India Innings")
                st.markdown(
                    """
                    <style>.small-font {font-size:13px;}</style>
                    <table class="small-font" border="1" cellspacing="0" cellpadding="4">
                        <tr><td>👤 Rohit Sharma</td><td>65 (42) • 6️⃣×4 • 2️⃣×6</td><td>OUT (Warner(C)/Starc(B))</td></tr>
                        <tr><td>👤 Virat Kohli</td><td>32 (21) • 4️⃣×4 • 0️⃣×6</td><td>OUT (Maxwell(C)/Zampa(B))</td></tr>
                        <tr><td>👤 KL Rahul</td><td>20 (15) • 2️⃣×4 • 0️⃣×6</td><td>OUT (Hazlewood(B))</td></tr>
                        <tr><td>👤 Suryakumar Yadav</td><td>28 (18) • 3️⃣×4 • 1️⃣×6</td><td>NOT OUT</td></tr>
                        <tr><td>👤 Ravindra Jadeja</td><td>22 (15) • 2️⃣×4 • 0️⃣×6</td><td>NOT OUT</td></tr>
                        <tr><td><b>Total</b></td><td colspan="2">167/3 (20 overs)</td></tr>
                    </table>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown("#### 🎯 Bowling — Australia (all 4 overs)")
                st.markdown(
                    """
                    <table class="small-font" border="1" cellspacing="0" cellpadding="4">
                        <tr><td>🎳 Starc</td><td>4.0 overs</td><td>35 runs</td><td>1 wicket</td><td>6 dot balls</td></tr>
                        <tr><td>🎳 Zampa</td><td>4.0 overs</td><td>28 runs</td><td>1 wicket</td><td>7 dot balls</td></tr>
                        <tr><td>🎳 Cummins</td><td>4.0 overs</td><td>32 runs</td><td>1 wicket</td><td>8 dot balls</td></tr>
                        <tr><td>🎳 Hazlewood</td><td>4.0 overs</td><td>30 runs</td><td>1 wicket</td><td>5 dot balls</td></tr>
                        <tr><td>🎳 Maxwell</td><td>4.0 overs</td><td>42 runs</td><td>0 wickets</td><td>4 dot balls</td></tr>
                    </table>
                    """,
                    unsafe_allow_html=True
                )

            # Australia Innings
            with right_col2:
                st.markdown("### 🏏 Australia Innings")
                st.markdown(
                    """
                    <table class="small-font" border="1" cellspacing="0" cellpadding="4">
                        <tr><td>👤 David Warner</td><td>40 (25) • 5️⃣×4 • 1️⃣×6</td><td>OUT (Jadeja(C)/Bumrah(B))</td></tr>
                        <tr><td>👤 Steve Smith</td><td>22 (18) • 3️⃣×4 • 0️⃣×6</td><td>OUT (Kohli(C)/Kuldeep(B))</td></tr>
                        <tr><td>👤 Labuschagne</td><td>15 (12) • 2️⃣×4 • 0️⃣×6</td><td>OUT (Jadeja(B))</td></tr>
                        <tr><td>👤 Carey</td><td>8 (10) • 1️⃣×4 • 0️⃣×6</td><td>OUT (Rahul(C)/Siraj(B))</td></tr>
                        <tr><td>👤 Stoinis</td><td>5 (7) • 0️⃣×4 • 0️⃣×6</td><td>OUT (Kuldeep(B))</td></tr>
                        <tr><td>👤 Head</td><td>7 (9) • 1️⃣×4 • 0️⃣×6</td><td>OUT (Bumrah(B))</td></tr>
                        <tr><td>👤 Maxwell</td><td>18 (12) • 2️⃣×4 • 1️⃣×6</td><td>NOT OUT</td></tr>
                        <tr><td>👤 Green</td><td>10 (8) • 1️⃣×4 • 0️⃣×6</td><td>NOT OUT</td></tr>
                        <tr><td><b>Total</b></td><td colspan="2">110/6 (14.5 overs)</td></tr>
                    </table>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown("#### 🎯 Bowling — India (14.5 overs so far)")
                st.markdown(
                    """
                    <table class="small-font" border="1" cellspacing="0" cellpadding="4">
                        <tr><td>🎳 Bumrah</td><td>3.1 overs</td><td>20 runs</td><td>2 wickets</td><td>10 dot balls</td></tr>
                        <tr><td>🎳 Kuldeep</td><td>4.0 overs</td><td>25 runs</td><td>2 wickets</td><td>7 dot balls</td></tr>
                        <tr><td>🎳 Jadeja</td><td>4.0 overs</td><td>28 runs</td><td>1 wicket</td><td>6 dot balls</td></tr>
                        <tr><td>🎳 Siraj</td><td>3.0 overs</td><td>22 runs</td><td>1 wicket</td><td>5 dot balls</td></tr>
                    </table>
                    """,
                    unsafe_allow_html=True
                )

        # ---------- MATCH INFO ----------
        with tab3:
            st.subheader("ℹ️ Match Info")
            st.write("Venue: Chennai")
            st.write("Series: Gavaskar - Border Series 2025")
            st.write("Match Type: T20")

    # ---------- QUICK ACCESS ----------
    st.divider()
    st.subheader("⚡ Quick Access")

    c1, c2, c3, c4 = st.columns(4)
    if c1.button("🏏 Player Stats →"):
        st.session_state.page = "Player Stats"
        st.rerun()
    if c2.button("📊 SQL Analysis →"):
        st.session_state.page = "SQL Analysis"
        st.rerun()
    if c3.button("🏆 Rankings →"):
        st.session_state.page = "Rankings"
        st.rerun()
    if c4.button("🛠 CRUD Operations →"):
        st.session_state.page = "CRUD Operations"
        st.rerun()

    if debug:
        st.info("Debug mode enabled")