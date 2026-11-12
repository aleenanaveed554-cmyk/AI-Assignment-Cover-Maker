    d.polygon([(0, H), (340, H), (0, H-340)], fill=accent)

    d.polygon([(W, H), (W-470, H), (W, H-470)], fill=dark)
    d.polygon([(W, H), (W-300, H), (W, H-300)], fill=accent)

    # decorative bottom lines
    for i in range(5):
        y = H - 275 - i * 28
        d.line((95, y, 430, y+90), fill=accent, width=5)
    for i in range(5):
        y = H - 275 - i * 28
        d.line((W-95, y, W-430, y+90), fill=accent, width=5)

    # footer
    center_text(
        d,
        (W//2, H-95),
        "ACADEMIC ASSIGNMENT • PROFESSIONAL COVER",
        get_font(22, True),
        "#6A7787"
    )

    return img

# ---------- Sidebar ----------
with st.sidebar:
    st.markdown("## ⚙️ Cover Settings")
    theme = st.selectbox("🎨 Theme", list(THEMES.keys()), index=1)

    st.markdown("---")
    st.markdown("### 🏫 Institution")
    institution = st.text_input("University / School", "Imran Public School and College")
    department = st.text_input("Department", "Department of Computer Science")

    st.markdown("### 📚 Assignment")
    assignment_title = st.text_input(
        "Assignment Title",
        "Artificial Intelligence and Generative AI"
    )
    subject = st.text_input("Subject", "Introduction to Artificial Intelligence")

    st.markdown("### 👩‍🎓 Student")
    student_name = st.text_input("Student Name", "Aleena Naveed")
    roll_no = st.text_input("Roll No.", "CS-102")
    course = st.text_input("Course / Class", "DIT / Computer Science")
    semester = st.text_input("Semester", "1st Semester")
    session = st.text_input("Session", "2026-27")

    st.markdown("### 👨‍🏫 Submitted To")
    faculty = st.text_input("Teacher / Faculty", "Muhammad Sir")
    submission_date = st.date_input("Submission Date", date.today())

    st.markdown("### 🖼️ Images")
    logo_file = st.file_uploader("University Logo (optional)", type=["png", "jpg", "jpeg"])
    photo_file = st.file_uploader("Student Photo (optional)", type=["png", "jpg", "jpeg"])

# ---------- Data ----------
data = {
    "institution": institution,
    "department": department,
    "assignment_title": assignment_title,
    "subject": subject,
    "student_name": student_name,
    "roll_no": roll_no,
    "course": course,
    "semester": semester,
    "session": session,
    "faculty": faculty,
    "submission_date": submission_date.strftime("%d %B %Y"),
}

logo = Image.open(logo_file) if logo_file else None
student_photo = Image.open(photo_file) if photo_file else None

# ---------- Generate ----------
if st.button("✨ Generate Professional Cover", use_container_width=True, type="primary"):
    st.session_state["cover"] = make_cover(data, theme, logo, student_photo)

if "cover" not in st.session_state:
    st.info("👈 Fill the details and click **Generate Professional Cover**.")

else:
    cover = st.session_state["cover"]

    st.markdown("### 🖼️ Your Assignment Cover")
    st.image(cover, width=700)

    # PNG
    png_buffer = BytesIO()
    cover.save(png_buffer, format="PNG")
    png_buffer.seek(0)

    # PDF
    pdf_buffer = BytesIO()
    cover.convert("RGB").save(pdf_buffer, format="PDF", resolution=150.0)
    pdf_buffer.seek(0)

    c1, c2 = st.columns(2)

    with c1:
        st.download_button(
            "⬇️ Download PNG",
            data=png_buffer,
            file_name="assignment_cover.png",
            mime="image/png",
            use_container_width=True
        )

    with c2:
        st.download_button(
            "📄 Download PDF",
            data=pdf_buffer,
            file_name="assignment_cover.pdf",
            mime="application/pdf",
            use_container_width=True
        )

    st.success("✅ Cover generated successfully!")
