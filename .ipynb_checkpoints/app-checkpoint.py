import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime, timedelta

# Configuración de la página
st.set_page_config(
    page_title="Ecosistema Digital Sostenible - Dashboard",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1A365D;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #2E86C1;
    }
    .section-header {
        color: #2E86C1;
        font-size: 1.5rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Título principal
st.markdown('<h1 class="main-header">🏦 Ecosistema Digital Sostenible</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #666;">Dashboard de Transformación Digital - Banco Tradicional Colombiano</p>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #2E86C1; font-weight: bold;">DataSphere Consulting</p>', unsafe_allow_html=True)

# Sidebar
st.sidebar.title("📊 Navegación")
page = st.sidebar.selectbox(
    "Selecciona una sección:",
    ["Resumen Ejecutivo", "Análisis Financiero", "Transformación Digital", 
     "Sostenibilidad", "Gestión de Riesgos", "Experiencia del Cliente", "Automatización"]
)

# Datos del proyecto
@st.cache_data
def load_data():
    # KPIs principales
    kpis = {
        'roi_3_anos': 180,
        'reduccion_costos': 26,
        'reduccion_carbono': 65,
        'mejora_nps': 25,
        'ahorro_anual': 8.5,
        'ingresos_adicionales': 12.3,
        'inversion_inicial': 15.0
    }
    
    # Datos del sector bancario
    sector_data = pd.DataFrame({
        'Tipo_Entidad': ['Bancos Tradicionales', 'Compañías de Financiamiento', 'Cooperativas Financieras', 'Fintechs'],
        'Con_Perdidas': [9, 10, 2, 0],
        'Con_Ganancias': [16, 5, 8, 12]
    })
    
    # Problemáticas (radar chart)
    problematicas = pd.DataFrame({
        'Dimension': ['Impacto Financiero', 'Competitividad', 'Experiencia Cliente', 
                     'Sostenibilidad', 'Eficiencia Operativa', 'Cumplimiento Regulatorio'],
        'Baja_Integracion': [70, 65, 80, 40, 90, 50],
        'Falta_Innovacion': [60, 85, 75, 50, 65, 40],
        'Impacto_Ambiental': [50, 40, 30, 90, 45, 75],
        'Desconexion_Datos': [75, 70, 65, 45, 80, 60],
        'Debilidades_Competitivas': [85, 90, 85, 55, 70, 65]
    })
    
    # Proyección financiera
    proyeccion = pd.DataFrame({
        'Año': ['Año 1', 'Año 2', 'Año 3'],
        'Inversión': [15, 3, 2],
        'Reducción_Costos': [4.5, 8.5, 8.5],
        'Incremento_Ingresos': [3.2, 12.3, 15.5]
    })
    
    # Riesgos
    riesgos = pd.DataFrame({
        'Riesgo': ['Resistencia al Cambio', 'Sobrecostos', 'Fallas Técnicas', 'Amenazas Seguridad', 'Dependencia Proveedores'],
        'Probabilidad': [60, 45, 25, 20, 10],
        'Impacto': [70, 85, 65, 75, 90],
        'Categoria': ['Alto', 'Alto', 'Medio', 'Medio', 'Bajo']
    })
    
    # Sostenibilidad
    sostenibilidad = pd.DataFrame({
        'Métrica': ['Emisiones CO2', 'Consumo Energético', 'Uso de Papel', 'Huella Hídrica'],
        'Antes': [100, 100, 100, 100],
        'Después': [35, 70, 20, 60]
    })
    
    # Timeline de implementación
    timeline = pd.DataFrame({
        'Mes': list(range(1, 37)),
        'Reducción_Costos': [0] * 6 + [10] * 6 + [20] * 6 + [26] * 18,
        'Incremento_Ingresos': [0] * 6 + [3] * 6 + [8] * 6 + [12] * 6 + [15] * 6 + [18] * 6,
        'ROI_Acumulado': [-100] * 6 + [-60] * 6 + [-10] * 6 + [50] * 6 + [120] * 6 + [180] * 6
    })
    
    return kpis, sector_data, problematicas, proyeccion, riesgos, sostenibilidad, timeline

kpis, sector_data, problematicas, proyeccion, riesgos, sostenibilidad, timeline = load_data()

# PÁGINA: RESUMEN EJECUTIVO
if page == "Resumen Ejecutivo":
    st.markdown('<h2 class="section-header">📈 KPIs Principales</h2>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="ROI Proyectado (3 años)",
            value=f"{kpis['roi_3_anos']}%",
            delta="Punto de equilibrio: Mes 18"
        )
    
    with col2:
        st.metric(
            label="Reducción de Costos",
            value=f"{kpis['reduccion_costos']}%",
            delta="En 18 meses"
        )
    
    with col3:
        st.metric(
            label="Reducción Huella Carbono",
            value=f"{kpis['reduccion_carbono']}%",
            delta="1,200 ton CO2/año"
        )
    
    with col4:
        st.metric(
            label="Mejora en NPS",
            value=f"+{kpis['mejora_nps']} puntos",
            delta="De 35 a 60"
        )
    
    st.markdown('<h2 class="section-header">🏦 Contexto del Sector Bancario Colombiano</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        fig = px.bar(
            sector_data, 
            x='Tipo_Entidad', 
            y=['Con_Perdidas', 'Con_Ganancias'],
            title="Desempeño Financiero por Tipo de Entidad (2023)",
            color_discrete_map={'Con_Perdidas': '#E74C3C', 'Con_Ganancias': '#2E86C1'},
            labels={'value': 'Número de Entidades', 'variable': 'Estado Financiero'}
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("""
        **Datos Clave del Sector:**
        - 📉 Descenso del 53.4% en ganancias (2023)
        - 🏛️ 21 de 62 entidades con pérdidas
        - 📱 75% población usa servicios digitales
        - 🚀 Presión competitiva de fintechs
        - 🌱 Regulaciones ASG emergentes
        """)
    
    st.markdown('<h2 class="section-header">🎯 Propuesta: Ecosistema Digital Sostenible</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **🔧 Componentes Tecnológicos:**
        - Migración Cloud Inteligente
        - Plataforma de BI en Tiempo Real
        - Automatización RPA
        """)
    
    with col2:
        st.markdown("""
        **🌱 Sostenibilidad:**
        - Finanzas Verdes
        - Eficiencia Energética
        - Productos Sostenibles
        """)
    
    with col3:
        st.markdown("""
        **🚀 Innovación:**
        - Laboratorio Digital
        - Metodologías Ágiles
        - Cultura Data-Driven
        """)

# PÁGINA: ANÁLISIS FINANCIERO
elif page == "Análisis Financiero":
    st.markdown('<h2 class="section-header">💰 Impacto Financiero Proyectado</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Inversión Inicial", f"${kpis['inversion_inicial']}M", "Presupuesto total")
    with col2:
        st.metric("Ahorro Anual", f"${kpis['ahorro_anual']}M", "A partir del año 2")
    with col3:
        st.metric("Ingresos Adicionales", f"${kpis['ingresos_adicionales']}M", "Nuevos productos")
    
    # Gráfico de proyección financiera
    fig = px.bar(
        proyeccion, 
        x='Año', 
        y=['Inversión', 'Reducción_Costos', 'Incremento_Ingresos'],
        title="Proyección Financiera por Año (Millones USD)",
        color_discrete_map={
            'Inversión': '#E74C3C',
            'Reducción_Costos': '#2E86C1',
            'Incremento_Ingresos': '#27AE60'
        }
    )
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)
    
    # Timeline detallado
    st.markdown('<h3 class="section-header">📅 Timeline de Beneficios</h3>', unsafe_allow_html=True)
    
    fig_timeline = px.line(
        timeline, 
        x='Mes', 
        y=['Reducción_Costos', 'Incremento_Ingresos', 'ROI_Acumulado'],
        title="Evolución de Beneficios en el Tiempo (%)",
        color_discrete_map={
            'Reducción_Costos': '#2E86C1',
            'Incremento_Ingresos': '#27AE60',
            'ROI_Acumulado': '#F39C12'
        }
    )
    fig_timeline.update_layout(height=400)
    st.plotly_chart(fig_timeline, use_container_width=True)

# PÁGINA: TRANSFORMACIÓN DIGITAL
elif page == "Transformación Digital":
    st.markdown('<h2 class="section-header">🔄 Matriz de Problemáticas</h2>', unsafe_allow_html=True)
    
    # Radar chart de problemáticas
    fig_radar = go.Figure()
    
    colors = ['#2E86C1', '#F39C12', '#27AE60', '#E74C3C', '#9B59B6']
    problemas = ['Baja_Integracion', 'Falta_Innovacion', 'Impacto_Ambiental', 'Desconexion_Datos', 'Debilidades_Competitivas']
    nombres = ['Baja Integración Tecnológica', 'Falta de Cultura de Innovación', 'Impacto Ambiental Elevado', 
               'Desconexión Estrategia-Datos', 'Debilidades Competitivas']
    
    for i, problema in enumerate(problemas):
        fig_radar.add_trace(go.Scatterpolar(
            r=problematicas[problema],
            theta=problematicas['Dimension'],
            fill='toself',
            name=nombres[i],
            line_color=colors[i]
        ))
    
    fig_radar.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        showlegend=True,
        title="Severidad de Problemáticas por Dimensión",
        height=600
    )
    
    st.plotly_chart(fig_radar, use_container_width=True)
    
    # Herramientas tecnológicas
    st.markdown('<h3 class="section-header">🛠️ Herramientas Tecnológicas</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **📊 BI y Análisis de Datos:**
        - Power BI Enterprise
        - Tableau para análisis ejecutivo
        - Azure Synapse Analytics
        
        **☁️ Infraestructura Cloud:**
        - Amazon Web Services (AWS)
        - Google Cloud Platform
        - Arquitectura multi-zona
        """)
    
    with col2:
        st.markdown("""
        **🤖 Automatización:**
        - UiPath Enterprise Platform
        - Automation Anywhere IQ Bot
        - Bots cognitivos para atención
        
        **📡 IoT y Monitoreo:**
        - Sensores de eficiencia energética
        - AWS IoT Core
        - Amazon Timestream
        """)

# PÁGINA: SOSTENIBILIDAD
elif page == "Sostenibilidad":
    st.markdown('<h2 class="section-header">🌱 Impacto Ambiental</h2>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Reducción CO2", "65%", "1,200 ton/año")
    with col2:
        st.metric("Ahorro Energético", "2.4 GWh", "30% menos consumo")
    with col3:
        st.metric("Papel Eliminado", "2.5M hojas", "300 árboles/año")
    with col4:
        st.metric("Nuevos Clientes", "50,000", "Inclusión financiera")
    
    # Gráfico de reducción de impacto
    fig_sost = px.bar(
        sostenibilidad, 
        x='Métrica', 
        y=['Antes', 'Después'],
        title="Reducción de Impacto Ambiental (%)",
        color_discrete_map={'Antes': '#E74C3C', 'Después': '#2E86C1'},
        labels={'value': 'Porcentaje (%)', 'variable': 'Estado'}
    )
    fig_sost.update_layout(height=400)
    st.plotly_chart(fig_sost, use_container_width=True)
    
    # Productos financieros verdes
    st.markdown('<h3 class="section-header">💚 Productos Financieros Sostenibles</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🏗️ Créditos Verdes:**
        - Proyectos de energía renovable
        - Construcción sostenible
        - Eficiencia energética
        - Transporte limpio
        """)
    
    with col2:
        st.markdown("""
        **📈 Inversiones Sostenibles:**
        - Bonos verdes corporativos
        - Fondos ASG
        - Cuentas de ahorro con impacto
        - Seguros para proyectos sostenibles
        """)

# PÁGINA: GESTIÓN DE RIESGOS
elif page == "Gestión de Riesgos":
    st.markdown('<h2 class="section-header">⚠️ Matriz de Riesgos</h2>', unsafe_allow_html=True)
    
    # Gráfico de dispersión para matriz de riesgos
    color_map = {'Alto': '#E74C3C', 'Medio': '#F39C12', 'Bajo': '#27AE60'}
    
    fig_riesgos = px.scatter(
        riesgos, 
        x='Probabilidad', 
        y='Impacto',
        color='Categoria',
        size=[15]*len(riesgos),
        hover_data=['Riesgo'],
        title="Matriz de Probabilidad e Impacto de Riesgos",
        color_discrete_map=color_map,
        labels={'Probabilidad': 'Probabilidad (%)', 'Impacto': 'Impacto (%)'}
    )
    
    fig_riesgos.update_layout(height=500)
    fig_riesgos.update_traces(textposition="middle center")
    st.plotly_chart(fig_riesgos, use_container_width=True)
    
    # Tabla de riesgos
    st.markdown('<h3 class="section-header">📋 Detalle de Riesgos</h3>', unsafe_allow_html=True)
    
    riesgos_display = riesgos.copy()
    riesgos_display['Probabilidad'] = riesgos_display['Probabilidad'].astype(str) + '%'
    riesgos_display['Impacto'] = riesgos_display['Impacto'].astype(str) + '%'
    
    st.dataframe(riesgos_display, use_container_width=True)
    
    # VaR
    st.markdown('<h3 class="section-header">📊 Valor en Riesgo (VaR)</h3>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("VaR (95% confianza)", "$6.8M", "Pérdida máxima esperada")
    with col2:
        st.metric("Valor Esperado", "$2.1M", "14% del presupuesto")
    with col3:
        st.metric("Período de Análisis", "18 meses", "Implementación completa")

# PÁGINA: EXPERIENCIA DEL CLIENTE
elif page == "Experiencia del Cliente":
    st.markdown('<h2 class="section-header">👥 Métricas de Experiencia</h2>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("NPS Actual", "35", "Baseline")
    with col2:
        st.metric("NPS Proyectado", "60", "+25 puntos")
    with col3:
        st.metric("Tiempo Créditos", "2 horas", "vs 120h actuales")
    with col4:
        st.metric("Resolución Reclamos", "24 horas", "vs 5 días actuales")
    
    # Gráfico de mejora en tiempos
    tiempos_data = pd.DataFrame({
        'Proceso': ['Solicitudes de Crédito', 'Consultas Rutinarias', 'Resolución de Reclamos', 'Apertura de Cuentas'],
        'Antes (horas)': [120, 0.08, 120, 24],
        'Después (horas)': [2, 0.008, 24, 0.1]
    })
    
    fig_tiempos = px.bar(
        tiempos_data, 
        x='Proceso', 
        y=['Antes (horas)', 'Después (horas)'],
        title="Reducción en Tiempos de Procesamiento",
        color_discrete_map={'Antes (horas)': '#E74C3C', 'Después (horas)': '#2E86C1'},
        log_y=True
    )
    fig_tiempos.update_layout(height=400)
    st.plotly_chart(fig_tiempos, use_container_width=True)
    
    # Beneficios para el cliente
    st.markdown('<h3 class="section-header">✨ Beneficios para el Cliente</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🚀 Servicios Mejorados:**
        - Respuesta instantánea 24/7
        - Personalización basada en datos
        - Productos financieros sostenibles
        - Experiencia omnicanal
        """)
    
    with col2:
        st.markdown("""
        **📱 Canales Digitales:**
        - App móvil optimizada
        - Chatbots inteligentes
        - Servicios de autogestión
        - Notificaciones proactivas
        """)

# PÁGINA: AUTOMATIZACIÓN
elif page == "Automatización":
    st.markdown('<h2 class="section-header">🤖 Procesos Automatizados</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Horas Ahorradas/Mes", "4,200", "Procesamiento automático")
    with col2:
        st.metric("Precisión Mejorada", "99.5%", "vs 95% manual")
    with col3:
        st.metric("Procesos Automatizados", "15", "Críticos identificados")
    
    # Gráfico de ahorros por proceso
    ahorros_data = pd.DataFrame({
        'Proceso': ['Solicitudes Crédito', 'Conciliación Cuentas', 'Reportes Regulatorios', 
                   'Gestión Reclamos', 'Apertura Cuentas'],
        'Horas_Ahorradas_Mes': [2400, 1800, 600, 300, 100],
        'Empleados_Equivalentes': [15, 11, 4, 2, 1]
    })
    
    fig_ahorros = px.bar(
        ahorros_data, 
        x='Proceso', 
        y='Horas_Ahorradas_Mes',
        title="Ahorros Mensuales por Proceso Automatizado",
        color='Horas_Ahorradas_Mes',
        color_continuous_scale='Blues'
    )
    fig_ahorros.update_layout(height=400)
    st.plotly_chart(fig_ahorros, use_container_width=True)
    
    # Tecnologías de automatización
    st.markdown('<h3 class="section-header">⚙️ Tecnologías Implementadas</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🔧 UiPath Enterprise:**
        - Automatización de procesos estructurados
        - Orchestrator para gestión centralizada
        - Studio para desarrollo de bots
        - Robots para ejecución distribuida
        """)
    
    with col2:
        st.markdown("""
        **🧠 Automation Anywhere:**
        - IQ Bot para documentos no estructurados
        - OCR avanzado con IA
        - Procesamiento de lenguaje natural
        - Bots cognitivos para atención al cliente
        """)

# Footer
st.markdown("---")
st.markdown(
    '<p style="text-align: center; color: #666;">Dashboard desarrollado por DataSphere Consulting | '
    'Datos basados en análisis estratégico para transformación digital bancaria</p>', 
    unsafe_allow_html=True
)

