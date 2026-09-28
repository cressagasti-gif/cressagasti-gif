"""Genera assets SVG para el perfil de GitHub de cressagasti-gif.
Todo original, sin dependencias externas. Salida: ./assets/*.svg
"""
import os
import random

random.seed(98)  # 98 -> GastiSnake98

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
os.makedirs(OUT, exist_ok=True)

RED = "#FF2D2D"
RED_HI = "#FFD9D9"
BG = "#0D0D0D"


# ---------------------------------------------------------------- matrix rain
def matrix_rain():
    W, H, COL, FS = 1200, 220, 24, 16
    # Katakana + ASCII imprimibles. OJO: nada de & < > " ' sin escapar:
    # en XML rompen el documento. Se escapan abajo con _esc().
    CHARS = ("ｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝ0123456789"
             "ABCDEFGHJKLMNPQRSTUVWXYZ<>/\\|=+-*#$%&@")
    ESC = {"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&apos;"}

    def esc(s):
        return "".join(ESC.get(c, c) for c in s)

    p = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="{W}" height="{H}" role="img" aria-label="Matrix rain">',
        "<style>.g{filter:drop-shadow(0 0 5px rgba(255,45,45,.5))}"
        "text{font-family:ui-monospace,'Cascadia Mono','Consolas',monospace}</style>",
        '<defs><linearGradient id="f" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0%" stop-color="{RED}" stop-opacity="0"/>'
        f'<stop offset="45%" stop-color="{RED}" stop-opacity=".55"/>'
        f'<stop offset="100%" stop-color="{RED}" stop-opacity="1"/>'
        "</linearGradient></defs>",
        f'<rect width="{W}" height="{H}" fill="{BG}"/>',
    ]

    ROWS = int(H / (FS * 1.15))          # caracteres visibles por columna
    TRAIL = ROWS + 6                      # largo de la estela
    STEP = FS * 1.15

    for i in range(W // COL):
        x = COL // 2 + i * COL
        dur = round(random.uniform(2.2, 6.5), 2)
        beg = -round(random.uniform(0, dur), 2)
        s = "".join(random.choice(CHARS) for _ in range(TRAIL))
        anim = (f'<animateTransform attributeName="transform" type="translate" '
                f'from="0 {-TRAIL * STEP}" to="0 {H + 40}" dur="{dur}s" '
                f'begin="{beg}s" repeatCount="indefinite"/>')

        p.append(f'<g class="g" text-anchor="middle" font-size="{FS}">{anim}')
        # un tspan por caracter: en SVG el salto de linea no existe
        for j, c in enumerate(s):
            head = (j == 0)
            fill = RED_HI if head else "url(#f)"
            op = "" if head else ' opacity=".9"'
            p.append(f'<text x="{x}" y="{j * STEP}" fill="{fill}"{op}>{esc(c)}</text>')
        p.append("</g>")

    p.append("</svg>")
    with open(os.path.join(OUT, "matrix-rain.svg"), "w", encoding="utf-8") as f:
        f.write("".join(p))
    return len("".join(p))


# ---------------------------------------------------------------- emblemas
def badge(name, body, label):
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 96 96" width="96" '
        f'height="96" role="img" aria-label="{label}">'
        f'<g fill="none" stroke="{RED}" stroke-width="3" stroke-linecap="round" '
        f'stroke-linejoin="round" filter="drop-shadow(0 0 4px rgba(255,45,45,.45))">'
        f"{body}</g></svg>"
    )
    with open(os.path.join(OUT, f"{name}.svg"), "w", encoding="utf-8") as f:
        f.write(svg)


# estrella de ninja (4 puntas cóncavas) dentro de un aro
badge(
    "emblem-shuriken",
    '<circle cx="48" cy="48" r="45" stroke-width="2" opacity=".55"/>'
    '<path d="M90 48 L57.2 57.2 L48 90 L38.8 57.2 L6 48 L38.8 38.8 L48 6 '
    'L57.2 38.8 Z" fill="rgba(255,45,45,.14)"/>'
    '<circle cx="48" cy="48" r="7" fill="none"/>',
    "Ninja star",
)

# Sharingan Eterno (Mangekyou) — diseño original, 3 tomoe en pinwheel ANIMADO
def mangekyo():
    """Aro exterior igual que el shuriken y el ojo, para que los tres
    emblemas de la fila queden simetricos. El iris gira, el aro no."""
    tomoe = (
        '<path d="M60.5 40.4 a7.2 7.2 0 1 0 0 15.2 '
        'c0-4.4-3.2-6.6-6.4-7.6 3.2-1 6.4-3.2 6.4-7.6 Z" '
        f'fill="{RED}" fill-opacity=".95" stroke="none"/>'
    )
    ray = (f'<path d="M55 48 H51.5" stroke="{RED}" stroke-width="2.4" '
           'stroke-linecap="round"/>')

    p = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 96 96" width="96" '
        'height="96" role="img" aria-label="Eternal Mangekyo Sharingan">',
        '<style>.e{filter:drop-shadow(0 0 5px rgba(255,45,45,.55))}</style>',
        # ---- aro exterior: identico al del shuriken y al del ojo ----
        f'<g class="e" fill="none" stroke="{RED}" stroke-width="2" '
        'stroke-linecap="round" opacity=".55">',
        '<circle cx="48" cy="48" r="45"/>',
        "</g>",
        # almendra del ojo (fija)
        '<g class="e" fill="none" stroke="#FF2D2D" stroke-width="3" '
        'stroke-linecap="round" stroke-linejoin="round">',
        '<path d="M16 48 C32 31 64 31 80 48 C64 65 32 65 16 48 Z" '
        'fill="rgba(255,45,45,.10)"/>',
        '<circle cx="48" cy="48" r="19" fill="rgba(255,45,45,.18)"/>',
        "</g>",
        # ---- grupo GIRATORIO: 3 tomoe en pinwheel, 120 grados entre si ----
        '<g class="e" stroke-linejoin="round">',
        '<g>',
        '<animateTransform attributeName="transform" type="rotate" '
        'from="0 48 48" to="360 48 48" dur="9s" repeatCount="indefinite"/>',
    ]
    for a in (0, 120, 240):
        p.append(f'<g transform="rotate({a} 48 48)">')
        p.append(tomoe)
        p.append(ray)
        p.append("</g>")
    p += [
        "</g>",
        # nucleo fijo (no gira) + reflejo del cristal
        '<circle cx="48" cy="48" r="4.2" fill="#FFD9D9"/>',
        '<circle cx="48" cy="48" r="6.4" fill="none" stroke="#FF2D2D" stroke-width="2"/>',
        '<path d="M34 36 a17 17 0 0 1 11-7" fill="none" stroke="#FFD9D9" '
        'stroke-width="1.8" stroke-linecap="round" opacity=".75"/>',
        "</g></svg>",
    ]
    with open(os.path.join(OUT, "emblem-mangekyo.svg"), "w", encoding="utf-8") as f:
        f.write("".join(p))


# ojo / energia maldita
badge(
    "emblem-eye",
    '<circle cx="48" cy="48" r="45" stroke-width="2" opacity=".55"/>'
    '<path d="M12 48 C28 26 68 26 84 48 C68 70 28 70 12 48 Z" '
    'fill="rgba(255,45,45,.14)"/>'
    '<circle cx="48" cy="48" r="13"/>'
    '<circle cx="48" cy="48" r="5" fill="none" stroke-width="2"/>'
    '<path d="M40 26 C44 18 52 18 56 26" stroke-width="2" opacity=".8"/>',
    "Cursed eye",
)


# ------------------------------------- anillos concentricos (franja terminal)
def concentric_mark(cx, cy, r, color):
    """Serie de circulos concentricos que se achican hacia adentro,
    con un punto solido al centro como pupila. Mismo radio exterior que
    usaba el emblema anterior, asi la franja no cambia de alto."""
    g = [
        f'<g fill="none" stroke="{color}" stroke-width="1.7">',
    ]
    # anillos de radio decreciente
    for k, (f, op) in enumerate(
        ((1.00, "1"), (0.78, ".75"), (0.58, ".58"), (0.40, ".45"), (0.24, ".35"))
    ):
        g.append(
            f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r * f:.1f}" '
            f'opacity="{op}"/>'
        )
    g.append("</g>")
    # pupila
    g.append(
        f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r * 0.11:.1f}" '
        f'fill="{color}"/>'
    )
    return "".join(g)


def to_binary(text):
    """Codifica el texto a binario ASCII, 8 bits por caracter."""
    return " ".join(
        f"{ord(c):08b}" if c != " " else "00100000" for c in text
    )


def typewriter():
    """Terminal propia en SVG.

    Por que no readme-typing-svg: ese servicio fuerza height=50 en el
    viewBox siempre, asi que recorta las lineas 2..N. Verificado con
    1, 2, 3, 5 y 8 lineas -> siempre "0 0 720 50".

    Comportamiento: las lineas se van escribiendo y ACUMULAN (no se
    borran una por una). Cuando aparecen todas queda todo fijo unos
    segundos y recien ahi se borra todo junto y arranca de nuevo.
    """
    W, FS, LH, PAD = 780, 20, 33, 24
    TYPING = 46          # ms por caracter
    PAUSE = 620          # ms de respiro entre lineas
    FIXED = 5200         # ms que queda todo fijo antes de borrar

    # Frase que codifica el binario de la franja superior.
    # "Sekai ni itami o" = "ahora el mundo conocera el dolor" (JJK)
    PHRASE = "Sekai ni itami o"

    lines = [
        "❯ whoami",
        "Gastón Cressa",
        "❯ cat ~/about.json",
        "IT Technician / Programmer @ Syscom Computers",
        "Córdoba, Argentina · 7 years in tech",
        "❯ ls ~/stack",
        "python · C · SQL · power bi · excel · git · power query",
        "❯ _",
    ]
    n = len(lines)
    BAR = 34                          # alto de la franja del clan
    CT = PAD + BAR / 2 + 4            # cy del emblema
    TOP = PAD + BAR + 20              # donde arranca la 1ra linea
    # OJO: el alto tiene que cubrir DESDE el origen la ULTIMA linea,
    # no solo PAD*2 + LH*n, o las ultimas quedan fuera del viewBox.
    H = TOP + (n - 1) * LH + FS + PAD * 1.6

    def esc(s):
        return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    # tiempos: escritura de cada linea, y despues todo queda fijo
    write = [(len(ln) * TYPING) / 1000.0 for ln in lines]
    gap = PAUSE / 1000.0
    t_write = sum(write) + gap * (n - 1)
    total = t_write + FIXED / 1000.0

    p = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="{W}" height="{H}" role="img" aria-label="Terminal intro">',
        "<style>"
        'text{font-family:ui-monospace,"Cascadia Mono",Consolas,monospace;'
        f'font-size:{FS}px;font-weight:600;fill:{RED}}}'
        '.t2{font-family:ui-monospace,Consolas,monospace;font-size:15px;'
        f'fill:{RED};letter-spacing:3px;opacity:.75}}'
        '.g{filter:drop-shadow(0 0 5px rgba(255,45,45,.45))}'
        "</style>",
        f'<rect width="{W}" height="{H}" fill="{BG}"/>',
    ]

    # ---- franja superior: anillos + binario con significado ----
    # "Sekai ni itami ore" = "ahora el mundo conocera el dolor" (Jujutsu Kaisen)
    bits = to_binary(PHRASE)
    x0 = 76
    lane = W - x0 - PAD                          # ancho visible del marquee
    # textLength fija el ancho exacto -> el loop del marquee no da saltos
    one = lane * 2                               # ancho de una copia
    p.append(concentric_mark(48, CT, 15, RED))
    p.append(
        f'<defs><clipPath id="mq">'
        f'<rect x="{x0}" y="{CT - 13}" width="{lane}" height="26"/>'
        f"</clipPath></defs>"
    )
    p.append(
        f'<g clip-path="url(#mq)">'
        f'<g><animateTransform attributeName="transform" type="translate" '
        f'from="0 0" to="{-one:.1f} 0" dur="26s" repeatCount="indefinite"/>'
        f'<text class="t2" x="{x0}" y="{CT + 5}" '
        f'textLength="{one:.0f}" lengthAdjust="spacing">{esc(bits)}</text>'
        f'<text class="t2" x="{x0 + one:.0f}" y="{CT + 5}" '
        f'textLength="{one:.0f}" lengthAdjust="spacing">{esc(bits)}</text>'
        f"</g></g>"
    )
    p.append(f'<path d="M{PAD} {CT + 24} h{W - PAD * 2}" stroke="#3D0A0A" '
             'stroke-width="1.5"/>')

    top = TOP
    # ---- lineas de la terminal: se revelan y se QUEDAN ----
    t0 = 0.0
    for i, ln in enumerate(lines):
        y = top + i * LH + FS
        k_open = t0 / total
        k_done = (t0 + write[i]) / total
        k_clear = 0.985                      # todas se borran juntas al final
        p.append(
            f'<clipPath id="k{i}"><rect x="0" y="0" width="0" height="{H}">'
            f'<animate attributeName="width" values="0;0;{W};{W};0" '
            f'keyTimes="0;{k_open:.5f};{k_done:.5f};{k_clear};1" '
            f'dur="{total}s" repeatCount="indefinite"/></rect></clipPath>'
        )
        p.append(
            f'<text x="{PAD}" y="{y:.0f}" clip-path="url(#k{i})">{esc(ln)}</text>'
        )
        # cursor blinking al final de la linea
        cx = PAD + len(ln) * FS * 0.6
        p.append(
            f'<rect x="{cx:.0f}" y="{y - FS * 0.80:.0f}" width="{FS * 0.5:.0f}" '
            f'height="{FS * 0.84:.0f}" fill="{RED}" clip-path="url(#k{i})">'
            f'<animate attributeName="opacity" values="1;1;0;0" dur="1s" '
            f'repeatCount="indefinite"/></rect>'
        )
        t0 += write[i] + gap

    p += ["</svg>"]
    svg = "".join(p)
    with open(os.path.join(OUT, "terminal.svg"), "w", encoding="utf-8") as f:
        f.write(svg)
    return len(svg)


def profile_card():
    """Simula la columna izquierda del perfil de GitHub, pero en rojo.

    GitHub NO permite custom CSS en el perfil (sanitiza <style>, <script>
    y CSS inline), asi que la columna real no se puede pintar. Esto es
    una tarjeta que va dentro del README, al lado del contenido.
    """
    W, H = 300, 386
    CARD = "#1A0505"                  # rojo muy oscuro, casi negro
    EDGE = "#3D0A0A"
    TXT = "#FF5A5A"
    DIM = "#C43B3B"

    p = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="{W}" height="{H}" role="img" aria-label="Perfil de Gaston Cressa">',
        '<style>'
        'text{font-family:-apple-system,"Segoe UI",Helvetica,Arial,sans-serif}'
        f'.t{{fill:{TXT}}}.d{{fill:{DIM}}}'
        '.g{filter:drop-shadow(0 0 10px rgba(255,45,45,.22))}'
        '</style>',
        # tarjeta
        f'<g class="g">',
        f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="8" '
        f'fill="{CARD}" stroke="{EDGE}" stroke-width="2"/>',
        # franja superior tipo "cover"
        f'<path d="M9 1 h{W - 18} a8 8 0 0 1 8 8 v34 h-{W - 2} v-34 '
        f'a8 8 0 0 1 8 -8 z" fill="#2A0707"/>',
        # avatar: circulo con iniciales (GitHub ya pone la foto real al lado)
        '<circle cx="150" cy="96" r="34" fill="none" stroke="#FF2D2D" '
        'stroke-width="2" opacity=".9"/>',
        '<text x="150" y="105" text-anchor="middle" font-size="28" '
        'font-weight="700" class="t">GC</text>',
        # nombre y usuario
        '<text x="150" y="164" text-anchor="middle" font-size="19" '
        'font-weight="700" class="t">Gastón Cressa</text>',
        '<text x="150" y="185" text-anchor="middle" font-size="13" '
        'class="d">cressagasti-gif</text>',
        # bio
        '<text x="24" y="216" font-size="12.5" class="d">'
        '<tspan x="24" dy="0">IT Technician &amp; Programmer.</tspan>'
        '<tspan x="24" dy="17">Support, hardware, networks</tspan>'
        '<tspan x="24" dy="17">and CCTV · Learning AI/ML.</tspan></text>',
        # separador
        f'<path d="M24 278 h{W - 48}" stroke="{EDGE}" stroke-width="1.5"/>',
        # datos
        '<g font-size="13">',
        '<circle cx="31" cy="302" r="6" fill="none" stroke="#FF2D2D" '
        'stroke-width="1.8"/>',
        '<text x="48" y="307" class="d">Córdoba, Argentina</text>',
        '<rect x="25" y="322" width="12" height="12" fill="none" '
        'stroke="#FF2D2D" stroke-width="1.8"/>',
        '<text x="48" y="333" class="d">Syscom Computers</text>',
        '<rect x="25" y="348" width="12" height="12" fill="none" '
        'stroke="#FF2D2D" stroke-width="1.8"/>',
        '<text x="48" y="359" class="d">Data Science &amp; AI</text>',
        "</g>",
        "</g></svg>",
    ]
    svg = "".join(p)
    with open(os.path.join(OUT, "profile-card.svg"), "w", encoding="utf-8") as f:
        f.write(svg)
    return len(svg)


print("OK ->", OUT)
print(f"  matrix-rain.svg built ({matrix_rain()} bytes)")
print(f"  terminal.svg built ({typewriter()} bytes)")
print(f"  profile-card.svg built ({profile_card()} bytes)")
mangekyo()
for f in sorted(os.listdir(OUT)):
    print(f"  {f:26} {os.path.getsize(os.path.join(OUT, f)):>7} bytes")
