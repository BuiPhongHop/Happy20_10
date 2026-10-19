import html
import streamlit as st

# ============================================================
# CẤU HÌNH: Bạn chỉ cần sửa ảnh và link ở khu vực này
# ============================================================
LINK_KHONG = "https://tinyurl.com/OpenMeForHappy"

# Thay các giá trị None bằng đường dẫn ảnh, ví dụ: "images/loan.jpg"
# Bạn cũng có thể dùng URL ảnh công khai.

ANH = {
    "Ngô Châu Loan": "images/Loan.jpg",       # anh1
    "Lê Xuân Bích Thảo": "images/Thao.jpg",   # anh2
    "Trần Thị Thịnh": "images/Thinh.jpg",    # anh3
    "Nguyễn Thị Ý Thơ": "images/Tho.jpg",    # anh4
    "Ngô Thị Ngọc Minh": "images/Minh.jpg",  # anh5
    "Bùi Hồng Tài": "images/Tai.jpg",        # anh6
    "Huỳnh Phạm Phương Uyên": "images/Uyen.jpg", # anh7
}


LINK = {
    "Ngô Châu Loan": "https://tinyurl.com/Click4HappyT1K33",
    "Lê Xuân Bích Thảo": "https://tinyurl.com/Click4HappyT1K33",
    "Trần Thị Thịnh": "https://tinyurl.com/Click4HappyT1K33",
    "Nguyễn Thị Ý Thơ": "https://tinyurl.com/Click4HappyT1K33",
    "Ngô Thị Ngọc Minh": "https://tinyurl.com/Click4HappyT1K33",
    "Bùi Hồng Tài": "https://tinyurl.com/Click4HappyT1K33",
    "Huỳnh Phạm Phương Uyên": "https://tinyurl.com/Click4HappyT1K33",
}

# ============================================================
# CẤU HÌNH GIAO DIỆN
# ============================================================
st.set_page_config(
    page_title="20/10 | Toán 1 K33 💖",
    page_icon="💗",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700&display=swap');

    :root { --pink: #e75480; --deep: #9d3d75; --lavender: #f1e8ff; }
    html, body, [class*="css"] { font-family: 'Be Vietnam Pro', sans-serif; }
    .stApp {
        background:
          radial-gradient(circle at 8% 5%, rgba(255, 196, 220, .52), transparent 28%),
          radial-gradient(circle at 92% 22%, rgba(210, 190, 255, .45), transparent 28%),
          linear-gradient(145deg, #fff7fb 0%, #fffafd 48%, #f8f4ff 100%);
    }
    [data-testid="stHeader"] { background: rgba(255,255,255,0); }
    .block-container { max-width: 850px; padding-top: 2rem; padding-bottom: 4rem; }
    .hero {
        text-align: center; padding: 2.2rem 1.5rem 1.8rem; border-radius: 30px;
        background: linear-gradient(135deg, rgba(255,255,255,.94), rgba(255,239,247,.92));
        border: 1px solid rgba(231,84,128,.16);
        box-shadow: 0 18px 55px rgba(173, 75, 128, .12);
        position: relative; overflow: hidden; margin-bottom: 1.4rem;
    }
    .eyebrow { color: #b04a83; letter-spacing: .18em; text-transform: uppercase;
               font-size: .78rem; font-weight: 800; }
    .hero h1 {
        font-family: 'Playfair Display', Georgia, serif; color: #9d3d75;
        font-size: clamp(2rem, 5.5vw, 3.35rem); line-height: 1.18;
        margin: .8rem 0 .7rem;
    }
    .hero p { color: #76556c; font-size: 1.02rem; margin: 0; }
    .pill {
        display: inline-block; margin-top: 1.1rem; padding: .45rem .9rem;
        border-radius: 999px; background: #ffe1ed; color: #a13d70;
        font-weight: 700; font-size: .86rem;
    }
    .section-card {
        background: rgba(255,255,255,.82); border: 1px solid #f4dce9;
        border-radius: 22px; padding: 1.25rem 1.35rem;
        box-shadow: 0 8px 28px rgba(157,61,117,.07); margin: .8rem 0 1.1rem;
    }
    .welcome {
        padding: 1rem 1.15rem; border-left: 4px solid #e879a5;
        background: linear-gradient(90deg, #fff0f6, #fff9fc);
        border-radius: 12px; color: #70465f; line-height: 1.8;
    }
    .tiny-note { color: #99748b; font-size: .88rem; }
    div.stButton > button, div.stLinkButton > a {
        border-radius: 14px; font-weight: 700; border: 1px solid #efbdd4;
        min-height: 2.8rem; transition: all .2s ease;
    }
    div.stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #e75480, #b45bd4);
        color: white; border: none; box-shadow: 0 7px 18px rgba(205,75,143,.2);
    }
    div.stButton > button:hover, div.stLinkButton > a:hover {
        transform: translateY(-2px); border-color: #dc79a5;
    }
    div[data-testid="stForm"] {
        background: rgba(255,255,255,.78); border: 1px solid #f3d9e7;
        border-radius: 20px; padding: 1rem 1.1rem;
    }
    div[data-testid="stRadio"] label { color: #70465f; }
    .footer { text-align: center; color: #ad8ba0; font-size: .82rem; padding-top: 1.7rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero">
    <div class="eyebrow">A LITTLE SURPRISE, MADE WITH LOVE</div>

    <h1 class="hero-title">
        <span>Chúc mừng Ngày Phụ nữ Việt</span>
        <span>Nam</span>
        <span class="heart">💖</span>
        <span>Yêu Thương Hơn -</span>
        <span>Hạnh Phúc Hơn</span>
    </h1>
    <p>Gửi đến những cô gái tuyệt vời của Toán 1 K33 🌷</p>
    <span class="pill">20 tháng 10 · Một ngày thật đặc biệt</span>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("### 💌 Trước khi mở món quà...")
st.markdown(
    '<div class="section-card"><b>Bạn có từng là một thành viên trong gia đình Toán 1 K33 không nhỉ?</b><br>'
    '<span class="tiny-note">Chọn câu trả lời bên dưới để khám phá lời nhắn dành cho bạn nhé ✨</span></div>',
    unsafe_allow_html=True,
)

nhanh = st.radio(
    "Bạn chọn nha:",
    ["Có (Yes)", "Không (No)"],
    horizontal=True,
    key="nhanh_chinh",
)

if nhanh == "Có (Yes)":
    st.markdown(
        """
        <div class="welcome">
        🌸 <b>Chào mừng quay trở lại, hãy để những chàng trai ấm áp của Toán 1 K33
        tiếp tục mang đến nụ cười cho các bạn nhaaa!</b><br><br>
        Cô gái xinh đẹp hãy nhập một số thông tin bên dưới để chúng tôi phục vụ cho bạn thật tốt nhé!!
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("thong_tin_20_10"):
        st.markdown("#### 🎀 Một chút thông tin về bạn")
        ten_truong = st.text_input("Bạn đang học trường nào nhỉ?", key="ten_truong")
        ten_nganh = st.text_input("Cho bọn mình biết ngành luôn được không?", key="ten_nganh")
        tinh_trang = st.text_input(
            "Tình trạng kết hôn là gì? (Độc thân/Cô đơn)",
            placeholder="Ví dụ: Độc thân",
            key="tinh_trang",
        )
        ket_qua_nhap = st.text_input(
            "Bạn đã sẵn sàng nhận lấy món quà đặc biệt cho hôm nay chưa ta? "
            "(Rồi/Rất hào hứng/Các bạn nam toán 1 đẹp trai lắm)",
            key="ket_qua_nhap",
        )
        da_gui = st.form_submit_button("Lưu thông tin & tiếp tục 💗", type="primary", use_container_width=True)

    if da_gui:
        st.session_state["da_gui"] = True
        st.session_state["ten_truong_luu"] = ten_truong.strip()
        st.session_state["ten_nganh_luu"] = ten_nganh.strip()
        st.session_state["tinh_trang_luu"] = tinh_trang.strip()
        st.session_state["ket_qua_luu"] = ket_qua_nhap.strip()

    if st.session_state.get("da_gui", False):
        truong = st.session_state.get("ten_truong_luu", "") or "chưa bật mí trường"
        nganh = st.session_state.get("ten_nganh_luu", "") or "chưa bật mí ngành"
        tinh_trang_luu = st.session_state.get("tinh_trang_luu", "") or "chưa bật mí"
        cam_xuc = st.session_state.get("ket_qua_luu", "") or "rất mong chờ"
        st.markdown(
            f"""
            <div class="section-card">
              ✨ Cô gái đang học ngành <b>{html.escape(nganh)}</b> của trường <b>{html.escape(truong)}</b>,
              với tình trạng <b>{html.escape(tinh_trang_luu)}</b>, đang cảm thấy <b>{html.escape(cam_xuc)}</b>
              trước món quà to lớn sắp tới. <b>LET'S GOOOOO!</b> 🎉
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("### 🎁 Hãy cho bọn mình biết tên của bạn nha!")

        # Bảy thẻ tên/ảnh riêng. Điền đường dẫn ảnh tại ANH ở đầu file.
        ten_cac_ban = list(LINK.keys())
        for bat_dau in range(0, len(ten_cac_ban), 2):
            cot = st.columns(2)
            for j, ten_ban in enumerate(ten_cac_ban[bat_dau:bat_dau + 2]):
                with cot[j]:
                    with st.container(border=True):
                        anh_ban = ANH.get(ten_ban)
                        if anh_ban:
                            st.image(anh_ban, use_container_width=True)
                        else:
                            st.markdown(
                                '<div style="text-align:center;font-size:2.7rem;padding:.6rem">🌷💗🌷</div>',
                                unsafe_allow_html=True,
                            )
                            st.caption(f"Vị trí ảnh: anh{ten_cac_ban.index(ten_ban) + 1}")
                        st.markdown(f"**{ten_ban}**")

        ten_chon = st.radio(
            "Chọn tên của bạn trong danh sách:",
            ten_cac_ban,
            key="ten_nguoi_nhan",
        )

        link_duoc_chon = LINK[ten_chon]
        if link_duoc_chon and link_duoc_chon != f"link{list(LINK.keys()).index(ten_chon)+1}":
            st.success(f"Món quà dành cho {ten_chon} đã sẵn sàng! 💝")
            st.link_button("Mở món quà bí mật 💌", link_duoc_chon, use_container_width=True)
        else:
            st.info(
                f"🎀 Chỗ điền đường dẫn của **{ten_chon}** là `{link_duoc_chon}`. "
                "Hãy thay giá trị này trong phần LINK ở đầu file bằng URL thật để nút mở quà xuất hiện."
            )

else:
    st.markdown(
        """
        <div class="section-card" style="text-align:center">
          <h3 style="color:#9d3d75">Không sao cả!</h3>
          <p style="color:#76556c; line-height:1.9">
          Cảm ơn bạn đã đến đây - Tập thể Toán 1 K33 chúc bạn luôn khoẻ mạnh,
          hạnh phúc và thành công nha. Nhấn vào link bên dưới nèk!
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.link_button("💖 Mở món quà dành cho bạn nè!", LINK_KHONG, use_container_width=True)
    st.caption("Chúc bạn có một ngày 20/10 thật nhiều niềm vui và những điều ngọt ngào! 🌷")

st.markdown(
    '<div class="footer">Made with 💗 by the boys of Toán 1 K33 · Happy Vietnamese Women’s Day</div>',
    unsafe_allow_html=True,
)

# Pháo hoa nhẹ khi người dùng mở trang
if st.session_state.get("da_gui", False):
    st.balloons()
