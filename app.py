import random
import pandas as pd
import streamlit as st

st.set_page_config(page_title="経穴-LAB", page_icon="🪡", layout="centered")

@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    df = pd.read_excel(path, sheet_name=0)
    # 必要列だけ
    df = df[["要穴名", "取穴部位", "経穴名"]].copy()
    # 文字列化＆欠損整理
    for c in ["要穴名", "取穴部位", "経穴名"]:
        df[c] = df[c].astype(str).str.strip()
    df = df[(df["要穴名"] != "nan") & (df["取穴部位"] != "nan") & (df["経穴名"] != "nan")]
    return df

EXCEL_PATH = "経穴アプリ作成ファイル.xlsx"
df = load_data(EXCEL_PATH)

st.title("🪡 経穴-LAB")
st.caption("要穴を選ぶ → 取穴部位がランダム出題 → 経穴名を選んで判定")

# --- ① 要穴名をプルダウンで選ぶ ---
youketsu_list = sorted(df["要穴名"].unique().tolist())
selected = st.selectbox("① 要穴名を選んでください", youketsu_list, index=0)

subset = df[df["要穴名"] == selected].reset_index(drop=True)
st.caption(f"この要穴に含まれる問題数：{len(subset)}")

# セッション状態
if "current_idx" not in st.session_state:
    st.session_state.current_idx = None
if "answered" not in st.session_state:
    st.session_state.answered = False
if "last_selected" not in st.session_state:
    st.session_state.last_selected = selected

# 要穴名が変わったらリセット
if st.session_state.last_selected != selected:
    st.session_state.current_idx = None
    st.session_state.answered = False
    st.session_state.last_selected = selected

# --- ② ランダムに1つ問題を表示 ---
col1, col2 = st.columns(2)
with col1:
    if st.button("② 問題を出す（ランダム）", use_container_width=True):
        st.session_state.current_idx = random.randrange(len(subset))
        st.session_state.answered = False
with col2:
    if st.button("次の問題へ", use_container_width=True, disabled=(st.session_state.current_idx is None)):
        st.session_state.current_idx = random.randrange(len(subset))
        st.session_state.answered = False

if st.session_state.current_idx is None:
    st.info("上のボタンから問題を出してください。")
    st.stop()

row = subset.loc[st.session_state.current_idx]
question_text = row["取穴部位"]
correct = row["経穴名"]

st.markdown("### ② 取穴部位（問題）")
st.markdown("### ② 取穴部位（問題）")
st.info(question_text)

# --- ③ 解答欄（要穴内の経穴名をプルダウンで選んで解答） ---
options = sorted(subset["経穴名"].unique().tolist())
st.markdown("### ③ 解答（経穴名）")
answer = st.selectbox("要穴内の経穴名から選んでください", options, index=0, key="answer_select")

# --- ④ 正誤判定＆正解表示 ---
if st.button("④ 判定する", type="primary", use_container_width=True, disabled=st.session_state.answered):
    st.session_state.answered = True
    if answer == correct:
        st.success("✅ 正解！  Perfect Match")
        st.balloons()
    else:
        st.error("✖ Incorrect")
        st.markdown(f"**Correct answer： {correct}**")

with st.expander("データ確認（今の問題）", expanded=False):
    st.write({"要穴名": selected, "取穴部位": question_text, "正解の経穴名": correct})
