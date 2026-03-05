import streamlit as st
from pathlib import Path
import base64

# ===== Configuración de página =====
st.set_page_config(
    page_title="Geraldine Bertel R. | Portafolio",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ===== Función para cargar imagen como base64 =====
def get_image_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img_base64 = get_image_base64(Path(__file__).parent / "profile.jpg")

# ===== CSS personalizado =====
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');
    
    .stApp {
        font-family: 'Inter', sans-serif;
    }
    
    /* Ocultar elementos de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Hero */
    .hero-container {
        display: flex;
        align-items: center;
        gap: 3rem;
        padding: 2rem 0 3rem;
    }
    
    .hero-text h1 {
        font-family: 'Playfair Display', serif;
        font-size: 3rem;
        color: #1e293b;
        margin-bottom: 0.3rem;
        letter-spacing: -0.02em;
    }
    
    .hero-text .greeting {
        color: #2563eb;
        font-weight: 500;
        font-size: 1.1rem;
        margin-bottom: 0.5rem;
    }
    
    .hero-text .title {
        color: #2563eb;
        font-weight: 600;
        font-size: 1.4rem;
        margin-bottom: 0.3rem;
    }
    
    .hero-text .subtitle {
        color: #64748b;
        font-size: 1rem;
        margin-bottom: 1rem;
    }
    
    .badge-container {
        display: flex;
        gap: 0.5rem;
        flex-wrap: wrap;
        margin-top: 1rem;
    }
    
    .badge {
        background: rgba(37, 99, 235, 0.08);
        color: #2563eb;
        padding: 0.4rem 1rem;
        border-radius: 100px;
        font-size: 0.85rem;
        font-weight: 500;
        border: 1px solid rgba(37, 99, 235, 0.15);
    }
    
    .profile-img {
        width: 280px;
        height: 330px;
        border-radius: 20px;
        object-fit: cover;
        object-position: center top;
        box-shadow: 0 10px 15px rgba(0,0,0,0.1);
        border: 4px solid white;
    }
    
    /* Section titles */
    .section-title {
        font-family: 'Playfair Display', serif;
        font-size: 2rem;
        color: #1e293b;
        text-align: center;
        margin: 3rem 0 0.5rem;
        letter-spacing: -0.02em;
    }
    
    .section-line {
        width: 50px;
        height: 3px;
        background: #2563eb;
        margin: 0 auto 2rem;
        border-radius: 2px;
    }
    
    /* Cards */
    .card {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 1.75rem;
        transition: all 0.3s ease;
        height: 100%;
    }
    
    .card:hover {
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        border-color: rgba(37, 99, 235, 0.2);
    }
    
    .card h3 {
        font-size: 1.05rem;
        font-weight: 600;
        color: #1e293b;
        margin-bottom: 0.5rem;
    }
    
    .card p {
        font-size: 0.9rem;
        color: #64748b;
        line-height: 1.6;
    }
    
    .card-icon {
        font-size: 2rem;
        margin-bottom: 0.75rem;
    }
    
    /* Timeline */
    .timeline-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 1.75rem;
        margin-bottom: 1rem;
        border-left: 4px solid #2563eb;
    }
    
    .timeline-card h3 {
        font-size: 1.1rem;
        font-weight: 600;
        color: #1e293b;
        margin-bottom: 0.2rem;
    }
    
    .timeline-card .role {
        color: #2563eb;
        font-weight: 500;
        font-size: 0.9rem;
        margin-bottom: 0.5rem;
    }
    
    .timeline-card p {
        color: #64748b;
        font-size: 0.9rem;
        line-height: 1.6;
    }
    
    .tag-container {
        display: flex;
        gap: 0.5rem;
        flex-wrap: wrap;
        margin-top: 0.75rem;
    }
    
    .tag {
        background: rgba(37, 99, 235, 0.06);
        color: #2563eb;
        padding: 0.2rem 0.7rem;
        border-radius: 100px;
        font-size: 0.78rem;
        font-weight: 500;
    }
    
    /* Education card */
    .edu-icon {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: linear-gradient(135deg, #2563eb, #7c3aed);
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 1rem;
        color: white;
        font-size: 1.3rem;
    }
    
    .edu-status {
        display: inline-block;
        padding: 0.15rem 0.6rem;
        border-radius: 100px;
        font-size: 0.72rem;
        font-weight: 600;
        background: rgba(37, 99, 235, 0.1);
        color: #2563eb;
        margin-bottom: 0.5rem;
    }
    
    /* Skills */
    .skill-bar-bg {
        height: 6px;
        background: #e2e8f0;
        border-radius: 100px;
        overflow: hidden;
        margin-top: 0.3rem;
    }
    
    .skill-bar-fill {
        height: 100%;
        background: linear-gradient(90deg, #2563eb, #7c3aed);
        border-radius: 100px;
    }
    
    .skill-name {
        font-size: 0.85rem;
        font-weight: 500;
        color: #64748b;
    }
    
    /* Contact */
    .contact-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 2rem;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .contact-card:hover {
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        border-color: #2563eb;
    }
    
    .contact-icon {
        font-size: 2rem;
        color: #2563eb;
        margin-bottom: 0.5rem;
    }
    
    /* Cert */
    .cert-card {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        padding: 1rem 1.5rem;
        background: linear-gradient(135deg, rgba(37,99,235,0.05), rgba(124,58,237,0.05));
        border: 1px solid rgba(37,99,235,0.15);
        border-radius: 8px;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem 0;
        color: #94a3b8;
        font-size: 0.85rem;
        border-top: 1px solid #e2e8f0;
        margin-top: 3rem;
    }
</style>
""", unsafe_allow_html=True)


# ===== HERO =====
col_text, col_img = st.columns([3, 2])

with col_text:
    st.markdown("""
    <div class="hero-text">
        <p class="greeting">Hola, soy</p>
        <h1>Geraldine Bertel R.</h1>
        <p class="title">Ingeniera Industrial</p>
        <p class="subtitle">Especialista en Dirección de Operaciones · Analítica de Datos</p>
        <div class="badge-container">
            <span class="badge">Lean Six Sigma Green Belt</span>
            <span class="badge">Auditora HSEQ</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_img:
    st.markdown(f"""
    <div style="text-align: center; padding-top: 1rem;">
        <img src="data:image/jpeg;base64,{img_base64}" class="profile-img" alt="Geraldine Bertel R.">
    </div>
    """, unsafe_allow_html=True)


# ===== SOBRE MÍ =====
st.markdown('<div class="section-title">Sobre Mí</div><div class="section-line"></div>', unsafe_allow_html=True)

st.markdown("""
<div style="max-width: 800px; margin: 0 auto; text-align: center;">
    <p style="font-size: 1.05rem; color: #64748b; line-height: 1.7; margin-bottom: 1rem;">
        Ingeniera Industrial, Especialista en Dirección de Operaciones y Magíster en Analítica de Datos 
        <span style="color: #7c3aed; font-weight: 500;">(en formación)</span>, con certificación 
        <strong>Lean Six Sigma Green Belt (CSSGB)</strong> y <strong>Auditora Interna HSEQ</strong>.
    </p>
    <p style="font-size: 1.05rem; color: #64748b; line-height: 1.7;">
        Cuento con experiencia en analítica aplicada a operaciones y excelencia operacional, 
        liderando iniciativas de <strong>automatización de procesos productivos</strong>, 
        <strong>visualización de indicadores en Power BI</strong> y 
        <strong>estructuración de procesos en sistemas ERP</strong>, orientada a la optimización 
        operativa, la mejora continua y la toma de decisiones estratégicas basadas en datos.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Tarjetas de competencias
cols = st.columns(4)
competencies = [
    ("📊", "Analítica de Datos", "Toma de decisiones basadas en datos"),
    ("⚙️", "Optimización", "Mejora continua de procesos"),
    ("🤖", "Automatización", "Procesos productivos eficientes"),
    ("🏆", "Excelencia", "Six Sigma & HSEQ"),
]
for col, (icon, title, desc) in zip(cols, competencies):
    with col:
        st.markdown(f"""
        <div class="card" style="text-align: center;">
            <div class="card-icon">{icon}</div>
            <h3>{title}</h3>
            <p>{desc}</p>
        </div>
        """, unsafe_allow_html=True)


# ===== EXPERIENCIA =====
st.markdown('<div class="section-title">Experiencia Profesional</div><div class="section-line"></div>', unsafe_allow_html=True)

experiences = [
    {
        "title": "Analítica Aplicada a Operaciones",
        "role": "Líder de Proyectos de Mejora Continua",
        "desc": "Liderazgo de iniciativas de automatización de procesos productivos y visualización de indicadores clave de desempeño (KPIs) mediante Power BI.",
        "tags": ["Power BI", "Automatización", "KPIs"]
    },
    {
        "title": "Dirección de Operaciones",
        "role": "Especialista en Excelencia Operacional",
        "desc": "Estructuración de procesos en sistemas ERP, orientada a la optimización operativa y la mejora continua con enfoque en resultados.",
        "tags": ["ERP", "Lean Six Sigma", "Mejora Continua"]
    },
    {
        "title": "Gestión de Calidad",
        "role": "Auditora Interna HSEQ",
        "desc": "Implementación y auditoría de sistemas integrados de gestión en salud, seguridad, medio ambiente y calidad.",
        "tags": ["HSEQ", "Auditoría", "ISO"]
    }
]

for exp in experiences:
    tags_html = "".join([f'<span class="tag">{t}</span>' for t in exp["tags"]])
    st.markdown(f"""
    <div class="timeline-card">
        <h3>{exp["title"]}</h3>
        <p class="role">{exp["role"]}</p>
        <p>{exp["desc"]}</p>
        <div class="tag-container">{tags_html}</div>
    </div>
    """, unsafe_allow_html=True)


# ===== EDUCACIÓN =====
st.markdown('<div class="section-title">Educación</div><div class="section-line"></div>', unsafe_allow_html=True)

edu_cols = st.columns(3)
education = [
    ("🎓", "Magíster en Analítica de Datos", "En formación", "Enfoque en análisis avanzado de datos para la toma de decisiones estratégicas empresariales."),
    ("👩‍🎓", "Esp. Dirección de Operaciones", "Completado", "Formación especializada en gestión y optimización de operaciones empresariales."),
    ("🏭", "Ingeniería Industrial", "Completado", "Fundamentos sólidos en ingeniería de procesos, producción y gestión organizacional."),
]

for col, (icon, title, status, desc) in zip(edu_cols, education):
    with col:
        st.markdown(f"""
        <div class="card" style="text-align: center;">
            <div class="edu-icon">{icon}</div>
            <h3>{title}</h3>
            <span class="edu-status">{status}</span>
            <p>{desc}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Certificaciones
cert_cols = st.columns([1, 2, 2, 1])
certs = ["🏅 Lean Six Sigma Green Belt (CSSGB)", "🛡️ Auditora Interna HSEQ"]
for col, cert in zip(cert_cols[1:3], certs):
    with col:
        st.markdown(f"""
        <div class="cert-card">
            <span style="font-weight: 500; font-size: 0.9rem;">{cert}</span>
        </div>
        """, unsafe_allow_html=True)


# ===== HABILIDADES =====
st.markdown('<div class="section-title">Habilidades</div><div class="section-line"></div>', unsafe_allow_html=True)

skill_cols = st.columns(3)

skills_data = [
    {
        "category": "📊 Analítica & Datos",
        "skills": [("Power BI", 90), ("Análisis de Datos", 85), ("Visualización de Indicadores", 90), ("Python / R", 70)]
    },
    {
        "category": "⚙️ Operaciones & Procesos",
        "skills": [("Lean Six Sigma", 90), ("Sistemas ERP", 85), ("Automatización de Procesos", 85), ("Mejora Continua", 95)]
    },
    {
        "category": "✅ Gestión & Calidad",
        "skills": [("Auditoría HSEQ", 85), ("Gestión de Calidad", 85), ("Dirección de Operaciones", 90), ("Decisiones Estratégicas", 88)]
    }
]

for col, data in zip(skill_cols, skills_data):
    with col:
        skills_html = ""
        for name, pct in data["skills"]:
            skills_html += f"""
            <div style="margin-bottom: 1rem;">
                <span class="skill-name">{name}</span>
                <div class="skill-bar-bg">
                    <div class="skill-bar-fill" style="width: {pct}%"></div>
                </div>
            </div>
            """
        st.markdown(f"""
        <div class="card">
            <h3>{data["category"]}</h3>
            <br>
            {skills_html}
        </div>
        """, unsafe_allow_html=True)


# ===== CONTACTO =====
st.markdown('<div class="section-title">Contacto</div><div class="section-line"></div>', unsafe_allow_html=True)

st.markdown("""
<p style="text-align: center; font-size: 1.1rem; color: #64748b; max-width: 600px; margin: 0 auto 2rem;">
    ¿Interesado/a en colaborar o conocer más sobre mi perfil profesional? No dudes en contactarme.
</p>
""", unsafe_allow_html=True)

contact_cols = st.columns([1, 2, 2, 1])
with contact_cols[1]:
    st.markdown("""
    <a href="https://www.linkedin.com/in/geraldinebertelr/" target="_blank" style="text-decoration: none;">
        <div class="contact-card">
            <div class="contact-icon">💼</div>
            <h3 style="color: #1e293b;">LinkedIn</h3>
            <p style="color: #64748b; font-size: 0.85rem;">/in/geraldinebertelr</p>
        </div>
    </a>
    """, unsafe_allow_html=True)

with contact_cols[2]:
    st.markdown("""
    <a href="mailto:gbertel@uninorte.edu.co" style="text-decoration: none;">
        <div class="contact-card">
            <div class="contact-icon">📧</div>
            <h3 style="color: #1e293b;">Email</h3>
            <p style="color: #64748b; font-size: 0.85rem;">gbertel@uninorte.edu.co</p>
        </div>
    </a>
    """, unsafe_allow_html=True)


# ===== FOOTER =====
st.markdown("""
<div class="footer">
    <p>© 2026 Geraldine Bertel R. | Todos los derechos reservados.</p>
</div>
""", unsafe_allow_html=True)
