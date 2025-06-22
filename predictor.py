import pandas as pd
import streamlit as st
from pathlib import Path

# ─── Load CSV ─────────────────────────────
def load_data(path: Path) -> pd.DataFrame:
    required_cols = ["College Name", "Branch", "Category", "Rank", "Percentile"]
    if not path.exists():
        st.error(f"❌ CSV file '{path}' not found.")
        st.stop()
    df = pd.read_csv(path)
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        st.error(f"CSV is missing columns: {', '.join(missing)}")
        st.stop()
    return df

# ─── Filter Logic with ± Buffer ───────────
def filter_df(df: pd.DataFrame, percentile: float, category: str,
              branch_filter: str | None = None,
              college_filter: str | None = None,
              buffer: float = 2.0,
              lower_limit: float = 5.0) -> pd.DataFrame:

    df = df[df["Category"].str.upper() == category.upper()].copy()

    def get_status(p):
        if percentile - lower_limit <= p <= percentile + buffer:
            if p < percentile:
                return "Safe 🎯"
            elif p == percentile:
                return "Exact Match ✅"
            else:
                return "Near Miss ⚠️"
        return None

    df["Status"] = df["Percentile"].apply(get_status)
    df = df[df["Status"].notna()]

    if branch_filter:
        df = df[df["Branch"].str.contains(branch_filter, case=False, na=False)]
    if college_filter:
        df = df[df["College Name"].str.contains(college_filter, case=False, na=False)]

    return df.sort_values(["Status", "College Name", "Percentile"], ascending=[True, True, False])

# ─── Streamlit App ────────────────────────
def run_app():
    st.set_page_config(page_title="MHT CET College Predictor", layout="wide")
    st.markdown("""
    <h1 style='text-align: center;'>🎓 MHT CET College Predictor 2023–24</h1>
    <h4 style='text-align: center; color: grey;'>Made by Zainul Aabdeen (🔧 Developer)</h4>
    """, unsafe_allow_html=True)

    df = load_data(Path("final_structured_cutoffs.csv"))

    percentile = st.sidebar.number_input("🎯 Your Percentile", 0.0, 100.0, 90.0, 0.1)
    category = st.sidebar.selectbox("📂 Your Category", sorted(df["Category"].unique()))
    branch = st.sidebar.multiselect("🔧 Filter by Branch", sorted(df["Branch"].unique()))
    college = st.sidebar.text_input("🏫 College name contains")
    buffer = st.sidebar.slider("Upper Range: Show near misses within +X%", 0.0, 10.0, 2.0, 0.1)
    lower_limit = 5.0  # fixed lower range

    branch_pattern = "|".join(branch) if branch else None
    filtered = filter_df(df, percentile, category, branch_pattern, college, buffer, lower_limit)

    st.subheader(f"🎯 {len(filtered)} options found (within +{buffer} / -{lower_limit} range)")
    st.markdown("✅ **Exact Match** = college cutoff exactly at your percentile  ")
    st.markdown("🎯 **Safe** = cutoff below your score but within 5%  ")
    st.markdown("⚠️ **Near Miss** = cutoff slightly above your score")

    # Add horizontal separators between colleges
    if not filtered.empty:
        current_college = None
        for _, row in filtered.iterrows():
            if row["College Name"] != current_college:
                st.markdown("---")
                st.markdown(f"### 🏫 {row['College Name']}")
                current_college = row["College Name"]
            st.markdown(f"- **{row['Branch']}** ({row['Category']}): Rank {int(row['Rank'])}, Percentile {row['Percentile']:.2f} → {row['Status']}")
    else:
        st.info("No colleges found in this range.")

    st.markdown("---")
    st.markdown("Made with ❤️ for MHT CET aspirants | Data: CAP Round 1")

if __name__ == "__main__":
    run_app()