import streamlit as st

# ======================
# Configuración de la página
# ======================
st.set_page_config(page_title="Articulación entre Sistemas de Archivos", layout="wide")

# ======================
# Estilos — Modo Oscuro Premium -> Esto me lo dió chatgpt
# ======================
dark_theme = """
<style>

body {
    background-color: #0d0f14;
}

[data-testid="stAppViewContainer"] {
    background-color: #0d0f14;
    color: #e5e5e5;
    font-family: 'Segoe UI', sans-serif;
}

[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
    border-bottom: 1px solid rgba(255,255,255,0.08);
}

.block-container {
    padding-top: 2rem;
}

.card {
    padding: 20px;
    border-radius: 14px;
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(5px);
    border: 1px solid rgba(255,255,255,0.1);
    margin-bottom: 20px;
}

h1, h2, h3 {
    color: #8ab4f8;
}

.tabs-container {
    color: white !important;
}

</style>
"""

st.markdown(dark_theme, unsafe_allow_html=True)

# ======================
# Título principal
# ======================
st.title("Articulación entre Sistemas de Archivos en Windows y Linux")
st.write(
    "En esta página encontrarás una explicación sencilla y visual de cómo interactúan ambos sistemas, cómo montar particiones y cómo compartir archivos."
)
st.subheader("Pero, ¿Qué es un Sistema de archivos?")
st.markdown(
    "Es la estructura lógica que se crea encima de una partición para poder organizar los ficheros,   \nun ejemplo sencillo es un campo que está sin tratar así no podremos plantar nada porque no se puede regar ni utilizar.  \nEste se comunica con el SO para decir donde están los archivos, quiero guardar un archivo nuevo, etc."
)


# ======================
# Pestañas principales
# ======================
tabs = st.tabs(
    [
        "📚 Conceptos Básicos",
        "🪟 Windows",
        "🐧 Linux",
        "🔀 Comparación y Compatibilidad",
    ]
)

# ======================
# TAB 0: CONCEPTOS BÁSICOS
# ======================
with tabs[0]:
    st.header("📚 Conceptos Básicos de Sistemas de Archivos")

    st.markdown(
        """
<div class="card">
Los sistemas de archivos incluyen varias características importantes para garantizar
la integridad, seguridad y organización de los datos. Aquí se explican las más importantes:
</div>
""",
        unsafe_allow_html=True,
    )

    # Imagen del mapa conceptual
    st.subheader("Mapa Conceptual General")
    # st.image()

    st.subheader("🧾 Journaling")
    st.write("""
El journaling permite registrar las operaciones antes de aplicarlas.
Esto evita corrupción de datos en caso de apagados inesperados.
""")
    st.code("Ejemplo: NTFS, ext4 usan journaling")

    st.subheader("🔐 Encriptación")
    st.write("""
Muchos sistemas de archivos permiten cifrar datos para protegerlos.
Esto evita que usuarios no autorizados accedan a la información.
""")
    st.code("Ejemplo: Windows EFS, Linux LUKS")

    st.subheader("📁 Propiedades de Archivos y Directorios")
    st.write("""
Incluyen permisos, atributos especiales, dueño, grupo y modos de acceso.
Linux usa permisos (rwx) y Windows usa ACLs con más granularidad.
""")
    colu1, colu2 = st.columns(2)
    with colu1:
        st.write("**Linux**")
        st.code("chmod 755 archivo")

    with colu2:
        st.write("**Windows**")
        st.code("icacls archivo /grant Usuario:F")

    st.subheader("➕ Operaciones Comunes")
    st.write("""
Crear, copiar, mover y eliminar archivos son operaciones esenciales que los sistemas
de archivos deben gestionar eficientemente.
""")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Linux:**")
        st.write("Para copiar un archivo a un nuevo archivo:")
        st.code("cp archivo1 archivo2")
        st.write("Para mover un archivo a otro directorio:")
        st.code("mv archivo carpeta/")
        st.write("Para eliminar un archivo:")
        st.code("rm archivo")

    with col2:
        st.write("**Windows (CMD):**")
        st.write("Para copiar un archivo a un nuevo archivo:")
        st.code("copy archivo1 archivo2")
        st.write("Para mover un archivo a otro directorio:")
        st.code("move archivo carpeta")
        st.write("Para eliminar un archivo:")
        st.code("del archivo")

# ======================
# TAB 1: WINDOWS
# ======================
with tabs[1]:
    st.header("🪟 Sistemas de Archivos usados en Windows")
    st.markdown(
        """
<div class="card">
<b>Windows utiliza principalmente:</b>
- NTFS (moderno, seguro, permisos avanzados)
- FAT32 (antiguo, limitado a 4GB por archivo)
- exFAT (ideal para USBs y tarjetas SD)

Estos sistemas determinan cómo se almacenan y gestionan los datos en un disco.
</div>
""",
        unsafe_allow_html=True,
    )
    # To do imagen de estructura windows
    st.subheader("Estructura del NTFS")
    st.info("To do")
    # st.image()

    st.subheader("¿Cómo puedes ver los discos desde Windows?")
    st.write("Puedes usar el Administrador de discos o ejecutar:")

    st.code("diskpart\nlist volume")

    st.subheader("💾 ¿Puede Windows leer particiones de Linux?")
    st.write(
        "Windows por defecto **NO** puede leer particiones ext4/ext3/ext2. :rainbow[:(((]"
    )
    st.write("Pero puedes instalar un programa externo:")

    st.code("Linux Reader (software de terceros)")

# ======================
# TAB 2: LINUX
# ======================
with tabs[2]:
    st.header("🐧 Sistemas de Archivos usados en Linux")
    st.markdown(
        """
<div class="card">
<b>Linux utiliza principalmente:</b>
- ext4 (actual y estable)
- ext3
- ext2
Estos sistemas permiten manejo eficiente de permisos y estructura jerárquica propia de Linux.
</div>
""",
        unsafe_allow_html=True,
    )

    st.subheader("Estructura EXT4")
    st.info("To do")
    # st.image("")

    st.subheader("📝 Ver particiones desde Linux")
    st.write("Ejecuta el siguiente comando en una terminal:")
    st.code("sudo fdisk -l")

    st.subheader("📌 Montar una partición NTFS en Linux")
    st.write("Linux permite leer/escribir NTFS usando el paquete `ntfs-3g`:")

    st.code("""
sudo apt install ntfs-3g
sudo mount -t ntfs-3g /dev/sdX1 /mnt/windows
""")

    st.subheader("📁 Desmontar la partición")
    st.code("sudo umount /mnt/windows")


# ======================
# TAB 3: COMPARACIÓN Y COMPATIBILIDAD
# ======================
with tabs[3]:
    st.header("🔀 Compatibilidad entre ambos sistemas")
    st.markdown(
        """
<div class="card">
<b>¿Linux puede leer NTFS?</b> ✔ Sí (con ntfs-3g)
<b>¿Windows puede leer ext4?</b> ❌ No nativamente
<b>¿Qué sistema usar para USB?</b> ✔ exFAT (compatible con ambos)
</div>
""",
        unsafe_allow_html=True,
    )

    st.subheader("Imagen..")
    st.info("To do")
    # st.image("")

    st.subheader("🧪 Ejemplo: Preparar un USB compatible con ambos")
    st.write("Puedes formatearlo en exFAT:")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**En Windows:**")
        st.code("formato → seleccionar exFAT")

    with col2:
        st.write("**En Linux:**")
        st.code("sudo mkfs.exfat /dev/sdX1")


# ======================
# FIN
# ======================
st.success("By Jhojan & Bastian")
