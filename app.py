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
        "📚 Practica de sistemas de archivos",
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
    # st.subheader("Mapa Conceptual General")
    # st.image()

    st.subheader("🧾 Journaling")
    st.write(
        "El journaling es una técnica que usan los SO la cual permite registrar cambios pendientes en un registro diario antes de aplicarlos al sistema de archivos principal. Este mecanismo asegura que ante un fallo de energía, un error del sistema o apagón inesperado el sistema de archivos pueda recuperarse de manera rápida y con el menor riesgo posible de que los archivos se corrompan."
    )
    colum1, colum2 = st.columns(2)

    with colum1:
        st.markdown(
            "**Linux**  \nLinux usa ext4 journaling.  \nPuedes ver si un disco usa journaling:"
        )
        st.code("sudo tune2fs -l /dev/sdX1 | grep features")
        st.write(
            "Con este comando puedes forzar un chequeo del disco en caso de que falle"
        )
        st.code("sudo fsck /dev/sdX1")
        st.write(
            "Puedes simular un fallo (sin apagar, de forma controlada) montando y desmontando de golpe:"
        )
        st.code(
            "sudo mount /dev/sdX1 /mnt/test\nsudo umount -l /mnt/test\nsudo fsck /dev/sdX1"
        )

    with colum2:
        st.markdown(
            "**Windows**  \nWindows usa NTFS journaling.  \nPuedes verificar el disco:"
        )
        st.code("chkdsk C:")
        st.write("O repararlo:")
        st.code("chkdsk C: /f /r")

    st.subheader("🔐 Modificación de permisos")
    st.write(
        "La modificación de permisos es el proceso de gestionar y cambiar los derechos de acceso que usuarios o grupos tienen sobre archivos, carpetas o recursos del sistema."
    )
    li, wi = st.columns(2)
    with li:
        st.markdown(
            "**Linux**   \nLinux usa permisos de rwx (lectura, escritura y ejecución) para los usuarios o grupos.  \nPara ver permisos:"
        )
        st.code("ls -l")
        st.write("Crear un archivo:")
        st.code("touch archivo.txt")
        st.write("Cambiar permisos (con este damos acceso total al usuario):")
        st.code("chmod 700 archivo.txt")
        st.write("Dar permiso de lectura al grupo:")
        st.code("chmod g+r archivo.txt")
        st.write("Permisos numéricos (combinados):")
        st.code("chmod 754 archivo.txt")

    with wi:
        st.markdown(
            "**Windows**  \nWindows usa ACLs (Access Control Lists). Son más avanzadas y permiten permisos específicos a usuarios/grupos.  \nVer permisos en PowerShell:"
        )
        st.code("Get-Acl archivo.txt")
        st.write("Crear un archivo:")
        st.code("echo 'Hola' > archivo.txt")
        st.write("Asignar permisos (al usuario actual):")
        st.code("icacls archivo.txt /grant %USERNAME%:F")
        st.write("Dar solo lectura:")
        st.code("icacls archivo.txt /grant %USERNAME%:R")
        st.write("Quitar un permiso:")
        st.code("icacls archivo.txt /remove:g %USERNAME%")

    st.subheader("📁 Comprension y atributos")
    st.write(
        "Es el conjunto de métodos y estructuras que utiliza el SO para: organizar, almacenar, recuperar y gestionar los datos en dispositivos de almacenamiento como SSD o USB."
    )
    colu1, colu2 = st.columns(2)
    with colu1:
        st.markdown("**Linux**  \nVer atributos de un archivo:")
        st.code("lsattr archivo.txt")
        st.write("Comprimir un archivo:")
        st.code("gzip archivo.txt")
        st.write("Descomprimir:")
        st.code("gunzip archivo.txt.gz")
        st.write("Crear un :red[.zip]:")
        st.code("zip archivo.zip archivo.txt")

    with colu2:
        st.markdown("**Windows**  \nVer atributos de un archivo:")
        st.code("Get-Item archivo.txt | Format-List *")
        st.write("Comprimir desde PowerShell:")
        st.code("Compress-Archive archivo.txt archivo.zip")
        st.write("Descomprimir:")
        st.code("Expand-Archive archivo.zip -DestinationPath carpeta")

    st.subheader("➕ Operaciones Comunes")
    st.write("""
Crear, copiar, mover y eliminar archivos son operaciones esenciales que los sistemas
de archivos deben gestionar eficientemente.
""")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Linux:**")
        st.write(
            "Primero listamos con **ls** (usaremos mucho este comando ya que nos permite ver lo que hay en los directorios), allí con *mkdir* creamos una carpeta de prueba y con **touch** creamos un archivo **(ejecuta los comandos uno por uno)**"
        )
        st.code("ls\nmkdir prueba\ncd prueba/\ntouch pepe.txt\nls")
        st.image("linux/crear.webp")
        st.write("Para copiar un archivo a un nuevo archivo comenzamos con **cp**")
        st.code("cp pepe.txt pepe1.txt")
        st.image("linux/copiar.webp")
        st.write(
            "Para mover un archivo a otro directorio usamos **mv**, en este caso creamos con mkdir primero un subdirectorio y lo movemos"
        )
        st.code("mkdir sub_prueba")
        st.image("linux/crearmover.webp")
        st.code("mv pepe.txt sub_prueba/\ncd sub_prueba\nls")
        st.image("linux/mover.webp")
        st.write("Para eliminar un archivo lo hacemos con rm")
        st.code("rm pepe.txt\nls")
        st.image("linux/eliminar.webp")

    with col2:
        st.write("**Windows (CMD):**")
        st.write(
            "En windows a diferencia de linux mostramos directorios con **dir**, allí con *mkdir* creamos una carpeta de prueba y con **echo** creamos un archivo **(recuerda ejecutar los comandos uno por uno)**"
        )
        st.code("mkdir prueba\ncd prueba\ndir")
        st.image("windows/crearcarpeta.webp")
        st.write("Para copiar un archivo a un nuevo archivo comenzamos con **copy**")
        st.code("copy pepe.txt pepe1.txt\ndir")
        st.image("windows/copiar.webp")
        st.write(
            "Para mover un archivo a otro directorio usamos **move**, en este caso creamos con mkdir primero un subdirectorio y lo movemos"
        )
        st.code("mkdir sub_prueba\ncd sub_prueba")
        st.image("windows/crearmover.webp")
        st.code("cd ..\nmove pepe.txt pepe1.txt\ncd sub_prueba\n")
        st.image("windows/eliminar.webp")
        st.write(
            "Finalmente con **del** eliminamos un archivo, prueba con esto dentro de **sub_prueba**"
        )
        st.code("del pepe.txt\ndir")


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
