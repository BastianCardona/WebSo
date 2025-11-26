import streamlit as st
from pandas.core.dtypes.dtypes import pa

# ======================
# Configuración de la página
# ======================
st.set_page_config(
    page_title="Articulación entre Sistemas de Archivos",
    layout="wide",
    page_icon=":computer:",
)

# ======================
# Estilos — Modo Oscuro Premium Mejorado
# ======================
dark_theme = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

body {
    background: linear-gradient(135deg, #0a0e1a 0%, #1a1f35 100%);
}

[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0a0e1a 0%, #1a1f35 100%);
    color: #e8eaed;
    font-family: 'Inter', 'Segoe UI', sans-serif;
}

[data-testid="stHeader"] {
    background: rgba(10, 14, 26, 0.95);
    backdrop-filter: blur(10px);
    border-bottom: 1px solid rgba(138, 180, 248, 0.15);
}

.block-container {
    padding-top: 2rem;
    max-width: 1400px;
}

.card {
    padding: 28px;
    border-radius: 16px;
    background: linear-gradient(135deg, rgba(26, 31, 53, 0.7) 0%, rgba(15, 20, 35, 0.7) 100%);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(138, 180, 248, 0.2);
    margin-bottom: 24px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    transition: all 0.3s ease;
}

.card:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 40px rgba(138, 180, 248, 0.15);
    border-color: rgba(138, 180, 248, 0.3);
}

h1 {
    color: #8ab4f8;
    font-weight: 700;
    font-size: 3rem !important;
    margin-bottom: 0.5rem !important;
    text-shadow: 0 2px 10px rgba(138, 180, 248, 0.3);
}

h2 {
    color: #a8c7fa;
    font-weight: 600;
    margin-top: 2rem !important;
    margin-bottom: 1rem !important;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid rgba(138, 180, 248, 0.2);
}

h3 {
    color: #c5d7f7;
    font-weight: 500;
    margin-top: 1.5rem !important;
}

.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    background: rgba(26, 31, 53, 0.5);
    padding: 8px;
    border-radius: 12px;
}

.stTabs [data-baseweb="tab"] {
    height: 50px;
    padding: 0 24px;
    background: rgba(138, 180, 248, 0.05);
    border-radius: 8px;
    color: #a8c7fa;
    font-weight: 500;
    border: 1px solid transparent;
    transition: all 0.3s ease;
}

.stTabs [data-baseweb="tab"]:hover {
    background: rgba(138, 180, 248, 0.1);
    border-color: rgba(138, 180, 248, 0.3);
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, rgba(138, 180, 248, 0.2) 0%, rgba(138, 180, 248, 0.1) 100%);
    border-color: rgba(138, 180, 248, 0.5) !important;
    color: #8ab4f8 !important;
}

.stCodeBlock {
    background: rgba(15, 20, 35, 0.8) !important;
    border: 1px solid rgba(138, 180, 248, 0.2);
    border-radius: 8px;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
}

code {
    color: #aecbfa !important;
    background: rgba(138, 180, 248, 0.1) !important;
    padding: 2px 6px !important;
    border-radius: 4px !important;
}

.stImage {
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
    border: 1px solid rgba(138, 180, 248, 0.1);
    transition: all 0.3s ease;
}

.stImage:hover {
    transform: scale(1.02);
    box-shadow: 0 12px 32px rgba(138, 180, 248, 0.2);
}

.stMarkdown a {
    color: #8ab4f8;
    text-decoration: none;
    border-bottom: 1px solid rgba(138, 180, 248, 0.3);
    transition: all 0.2s ease;
}

.stMarkdown a:hover {
    color: #aecbfa;
    border-bottom-color: #8ab4f8;
}

.stSuccess {
    background: linear-gradient(135deg, rgba(52, 168, 83, 0.15) 0%, rgba(52, 168, 83, 0.05) 100%);
    border: 1px solid rgba(52, 168, 83, 0.3);
    border-radius: 8px;
    padding: 16px;
    margin-top: 3rem;
}

table {
    border-collapse: separate;
    border-spacing: 0;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
}

thead th {
    background: linear-gradient(135deg, rgba(138, 180, 248, 0.2) 0%, rgba(138, 180, 248, 0.1) 100%);
    color: #8ab4f8;
    font-weight: 600;
    padding: 16px;
    border: 1px solid rgba(138, 180, 248, 0.2);
}

tbody td {
    background: rgba(26, 31, 53, 0.5);
    padding: 14px;
    border: 1px solid rgba(138, 180, 248, 0.1);
}

tbody tr:hover td {
    background: rgba(138, 180, 248, 0.08);
}

.element-container {
    margin-bottom: 1rem;
}

/* Animación suave al cargar */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

.block-container > div {
    animation: fadeIn 0.6s ease-out;
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
            "**Linux - ext4**  \nLinux usa ext4 journaling.  \nPuedes ver si un disco usa journaling:"
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

        st.markdown("---")
        st.markdown(
            "**Linux - Btrfs**  \nBtrfs usa copy-on-write (CoW) en lugar de journaling tradicional.  \nVer información del sistema de archivos:"
        )
        st.code("sudo btrfs filesystem show")
        st.write("Verificar integridad del sistema de archivos:")
        st.code("sudo btrfs scrub start /mnt/btrfs")
        st.write("Ver estado del scrub:")
        st.code("sudo btrfs scrub status /mnt/btrfs")

        st.markdown("---")
        st.markdown(
            "**Linux - ZFS**  \nZFS también usa CoW y tiene auto-reparación.  \nVer estado de los pools:"
        )
        st.code("sudo zpool status")
        st.write("Verificar integridad (scrub):")
        st.code("sudo zpool scrub nombre_pool")
        st.write("Ver propiedades del dataset:")
        st.code("sudo zfs get all nombre_pool/dataset")

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
    st.markdown("""
    ### 🟦 NTFS – ¿Cómo organiza los archivos?

    NTFS usa una estructura llamada **MFT (Master File Table)**.
    La MFT es como una *gran tabla de Excel* donde cada fila representa un archivo o carpeta.

    Dentro de la MFT se guarda:

    - **Nombre del archivo**
    - **Permisos**
    - **Ubicación en el disco**
    - **Fechas**
    - **Atributos especiales**

    Incluso los archivos pequeños pueden guardarse **dentro de la propia tabla**, lo que hace más rápido el acceso.

    NTFS es muy robusto: soporta **encriptación, compresión y journaling** para evitar pérdida de datos.
    """)

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
- Btrfs (moderno, con snapshots y compresión)
- ZFS (avanzado, con integridad de datos y pooling)
Estos sistemas permiten manejo eficiente de permisos y estructura jerárquica propia de Linux.
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown("""
    ### 🟩 ext4 – ¿Cómo organiza los archivos?

    En Linux, ext4 organiza la información usando **inodos**, que funcionan como pequeñas fichas donde se describe cada archivo.

    Cada inodo guarda:

    - **Tamaño del archivo**
    - **Permisos**
    - **Dueño y grupo**
    - **Ubicación de los bloques en el disco**
    - **Fechas de creación y modificación**

    Los nombres de los archivos no van en el inodo, sino en estructuras de directorio, lo que hace que ext4 sea muy eficiente buscando y gestionando archivos.

    ext4 también usa **journaling**, fragmenta muy poco y es capaz de manejar discos y archivos muy grandes, siendo uno de los sistemas más estables en Linux.
    """)

    st.markdown("""
    ### 🟧 Btrfs – Sistema de archivos moderno

    Btrfs (B-tree File System) es un sistema de archivos avanzado que usa **copy-on-write (CoW)** en lugar de journaling tradicional.

    Características principales:

    - **Snapshots instantáneos** - Crea copias de respaldo sin duplicar datos
    - **Compresión transparente** - Ahorra espacio automáticamente
    - **Checksums** - Detecta corrupción de datos
    - **RAID integrado** - Soporta múltiples discos sin software adicional
    - **Subvolúmenes** - Divide el sistema de archivos en partes independientes

    Btrfs es ideal para servidores y usuarios que necesitan funciones avanzadas de gestión de datos.
    """)

    st.markdown("""
    ### 🟦 ZFS – El sistema de archivos más avanzado

    ZFS (Zettabyte File System) es un sistema de archivos y administrador de volúmenes combinado, conocido por su robustez.

    Características principales:

    - **Integridad de datos garantizada** - Checksums en todo
    - **Pools de almacenamiento** - Combina múltiples discos como uno solo
    - **Auto-reparación** - Detecta y corrige errores automáticamente
    - **Snapshots y clones** - Instantáneos eficientes y clonación rápida
    - **Compresión y deduplicación** - Optimiza el espacio de almacenamiento
    - **ARC (Adaptive Replacement Cache)** - Caché inteligente en RAM

    ZFS es el preferido para almacenamiento empresarial, NAS y donde la integridad de datos es crítica.
    """)

    st.subheader("📝 Ver particiones desde Linux")
    st.write("Ejecuta el siguiente comando en una terminal:")
    st.code("sudo fdisk -l")
    st.write("Para ver sistemas de archivos montados:")
    st.code("df -Th")

    st.subheader("📌 Montar una partición NTFS en Linux")
    st.write("Linux permite leer/escribir NTFS usando el paquete `ntfs-3g`:")

    st.code("""
sudo apt install ntfs-3g
sudo mount -t ntfs-3g /dev/sdX1 /mnt/windows
""")

    st.subheader("📌 Montar una partición Btrfs")
    st.write("Montar un sistema de archivos Btrfs:")
    st.code("sudo mount -t btrfs /dev/sdX1 /mnt/btrfs")
    st.write("Montar un subvolumen específico:")
    st.code("sudo mount -t btrfs -o subvol=nombre_subvol /dev/sdX1 /mnt/btrfs")
    st.write("Crear un snapshot:")
    st.code("sudo btrfs subvolume snapshot /mnt/btrfs /mnt/btrfs/snapshot1")

    st.subheader("📌 Montar un pool ZFS")
    st.write("Importar un pool ZFS:")
    st.code("sudo zpool import nombre_pool")
    st.write("Ver pools disponibles:")
    st.code("sudo zpool import")
    st.write("Montar todos los datasets del pool:")
    st.code("sudo zfs mount -a")
    st.write("Crear un snapshot:")
    st.code("sudo zfs snapshot nombre_pool/dataset@snapshot1")

    st.subheader("📁 Desmontar particiones")
    st.write("Para NTFS y ext4:")
    st.code("sudo umount /mnt/windows")
    st.write("Para Btrfs:")
    st.code("sudo umount /mnt/btrfs")
    st.write("Para ZFS (exportar pool):")
    st.code("sudo zpool export nombre_pool")


# ======================
# TAB 3: COMPARACIÓN Y COMPATIBILIDAD
# ======================
with tabs[3]:
    st.subheader("Recordemos un poco")
    st.write(
        "NTFS y ext4 son sistemas de archivos, es decir, la forma en que un sistema operativo organiza y guarda los datos en un disco."
    )
    st.markdown("""
    ### 📊 Cuadro comparativo de compatibilidad (Windows vs Linux)

    | Sistema de archivos | Linux: Leer | Linux: Escribir | Windows: Leer | Windows: Escribir |
    |--------------------|:-----------:|:---------------:|:--------------:|:------------------:|
    | **NTFS (Windows)** | ✔ | ✔ | ✔ | ✔ |
    | **ext4 (Linux)** | ✔ | ✔ | ❌ | ❌ |
    | **exFAT (USB)** | ✔ | ✔ | ✔ | ✔ |
    | **FAT32** | ✔ | ✔ | ✔ | ✔ |
    | **Btrfs (Linux)** | ✔ | ✔ | ❌ | ❌ |
    | **HFS+ (macOS)** | ✔ | ❌ | ❌ | ❌ |
    """)  # Acá se ve horrible pero en la pagina sí sale bien I PROMISE.


# ======================
# FIN
# ======================
st.success("By Jhojan & Bastian")
