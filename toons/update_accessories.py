#!/usr/bin/env python3
"""Update SVG accessories for ToonTone Cats."""

import os

WORKDIR = "/root/.hermes/workspace/toontone-clone/toons"

def update_file(filename, old_text, new_text):
    path = os.path.join(WORKDIR, filename)
    with open(path, 'r') as f:
        content = f.read()
    if old_text not in content:
        print(f"ERROR: Could not find old text in {filename}")
        print(f"Looking for: {repr(old_text[:80])}")
        return False
    content = content.replace(old_text, new_text)
    with open(path, 'w') as f:
        f.write(content)
    # Verify
    with open(path, 'r') as f:
        verified = f.read()
    if len(verified) < 200:
        print(f"ERROR: {filename} too short after update ({len(verified)} bytes)")
        return False
    print(f"OK: {filename} updated ({len(verified)} bytes)")
    return True

# =====================================================
# 1. whiskers.svg - Tabby Cat: red collar -> blue striped tie
# =====================================================
old_whiskers = '<!-- collar (target) --><rect x="75" y="105" width="50" height="12" rx="6" fill="#e94560"/><circle cx="100" cy="111" r="5" fill="#ffd700"/>'
new_whiskers = '<!-- blue striped tie (target) --><polygon points="85,105 100,130 115,105" fill="#2980b9"/><polygon points="88,105 100,125 112,105" fill="#3498db"/><line x1="100" y1="130" x2="100" y2="145" stroke="#2980b9" stroke-width="4" stroke-linecap="round"/><line x1="96" y1="138" x2="104" y2="138" stroke="#3498db" stroke-width="2"/>'
update_file("whiskers.svg", old_whiskers, new_whiskers)

# =====================================================
# 2. luna.svg - Black Cat: red bow tie -> silver crescent necklace
# =====================================================
old_luna = '<!-- bow tie (target) --><polygon points="85,108 100,115 115,108 115,122 100,115 85,122" fill="#ff6b6b"/><circle cx="100" cy="115" r="4" fill="#ff4444"/>'
new_luna = '<!-- silver crescent necklace (target) --><path d="M90,108 Q75,115 85,130 Q95,118 100,115 Q105,118 115,130 Q125,115 110,108" fill="none" stroke="#c0c0c0" stroke-width="2.5"/><path d="M88,110 A12,12 0 1,0 112,110 A10,10 0 1,1 88,110" fill="#c0c0c0"/>'
update_file("luna.svg", old_luna, new_luna)

# =====================================================
# 3. mochi.svg - Scottish Fold: purple sweater -> yellow scarf
# =====================================================
old_mochi = '<!-- sweater (target) --><rect x="60" y="100" width="80" height="30" rx="10" fill="#9b59b6"/><rect x="60" y="100" width="80" height="8" rx="4" fill="#8e44ad"/><line x1="70" y1="110" x2="70" y2="128" stroke="#8e44ad" stroke-width="2"/><line x1="130" y1="110" x2="130" y2="128" stroke="#8e44ad" stroke-width="2"/>'
new_mochi = '<!-- yellow scarf (target) --><path d="M65,100 Q100,112 135,100 L135,108 Q100,120 65,108 Z" fill="#f1c40f"/><path d="M120,105 L130,145 L115,140 Z" fill="#f1c40f"/><line x1="125" y1="110" x2="128" y2="140" stroke="#d4ac0d" stroke-width="1.5"/><line x1="115" y1="105" x2="113" y2="115" stroke="#d4ac0d" stroke-width="2"/>'
update_file("mochi.svg", old_mochi, new_mochi)

# =====================================================
# 4. ginger.svg - Orange Tabby: green bandana -> cyan bow tie
# =====================================================
old_ginger = '<!-- bandana (target) --><polygon points="85,105 100,128 115,105 100,112" fill="#2ecc71"/><circle cx="100" cy="115" r="3" fill="#27ae60"/>'
new_ginger = '<!-- cyan bow tie (target) --><polygon points="84,105 100,113 116,105 116,122 100,114 84,122" fill="#00bcd4"/><circle cx="100" cy="113.5" r="4" fill="#0097a7"/>'
update_file("ginger.svg", old_ginger, new_ginger)

# =====================================================
# 5. snowpaw.svg - Persian: pink ribbon -> sky blue bow hair clip
# =====================================================
old_snowpaw = '<!-- ribbon (target) --><polygon points="82,118 100,130 118,118 100,124" fill="#ff69b4"/><path d="M90,125 L95,145" stroke="#ff69b4" stroke-width="3" stroke-linecap="round"/><path d="M110,125 L105,145" stroke="#ff69b4" stroke-width="3" stroke-linecap="round"/>'
new_snowpaw = '<!-- sky blue bow hair clip (target) --><polygon points="82,118 100,132 118,118 100,125" fill="#87ceeb"/><circle cx="100" cy="123" r="4" fill="#5dade2"/><path d="M90,126 L86,142" stroke="#87ceeb" stroke-width="3" stroke-linecap="round"/><path d="M110,126 L114,142" stroke="#87ceeb" stroke-width="3" stroke-linecap="round"/>'
update_file("snowpaw.svg", old_snowpaw, new_snowpaw)

# =====================================================
# 6. sushi.svg - Siamese: golden collar red -> jade green collar
# =====================================================
old_sushi = '<!-- collar (target) --><rect x="72" y="107" width="56" height="10" rx="5" fill="#e74c3c"/><circle cx="100" cy="112" r="4" fill="#ffd700"/>'
new_sushi = '<!-- jade collar (target) --><rect x="72" y="107" width="56" height="10" rx="5" fill="#2ecc71"/><circle cx="100" cy="112" r="4" fill="#1abc9c"/>'
update_file("sushi.svg", old_sushi, new_sushi)

# =====================================================
# 7. patch.svg - Calico: purple harness -> orange cape
# =====================================================
old_patch = '<!-- harness (target) --><path d="M75,105 L125,105" stroke="#8e44ad" stroke-width="4" stroke-linecap="round"/><path d="M75,105 L70,140" stroke="#8e44ad" stroke-width="3" stroke-linecap="round"/><path d="M125,105 L130,140" stroke="#8e44ad" stroke-width="3" stroke-linecap="round"/><circle cx="100" cy="105" r="6" fill="#9b59b6"/><circle cx="100" cy="105" r="3" fill="#ffd700"/>'
new_patch = '<!-- orange cape (target) --><path d="M65,100 Q100,115 135,100 L130,140 Q100,148 70,140 Z" fill="#e67e22"/><circle cx="100" cy="102" r="8" fill="#d35400"/><circle cx="100" cy="102" r="4" fill="#f39c12"/>'
update_file("patch.svg", old_patch, new_patch)

# =====================================================
# 8. misty.svg - Russian Blue: orange scarf -> rose pink collar
# =====================================================
old_misty = '<!-- scarf (target) --><path d="M72,105 Q100,118 128,105" fill="none" stroke="#f39c12" stroke-width="6" stroke-linecap="round"/><path d="M120,108 L126,140 L116,138" fill="#f39c12"/><line x1="118" y1="110" x2="122" y2="135" stroke="#d4a020" stroke-width="1.5"/>'
new_misty = '<!-- rose pink collar (target) --><rect x="68" y="105" width="64" height="10" rx="5" fill="#ff69b4"/><circle cx="100" cy="110" r="5" fill="#ff1493"/>'
update_file("misty.svg", old_misty, new_misty)

# =====================================================
# 9. yoda.svg - Sphynx: red party hat -> gold chain necklace
# =====================================================
old_yoda = '<!-- hat (target) --><polygon points="65,52 100,35 135,52" fill="#e74c3c"/><rect x="70" y="48" width="60" height="8" rx="3" fill="#c0392b"/><circle cx="100" cy="42" r="4" fill="#ffd700"/>'
new_yoda = '<!-- gold chain necklace (target) --><path d="M72,105 Q86,118 100,112 Q114,118 128,105" fill="none" stroke="#ffd700" stroke-width="3"/><circle cx="100" cy="112" r="5" fill="#ffd700" stroke="#daa520" stroke-width="1"/><circle cx="100" cy="112" r="2" fill="#daa520"/>'
update_file("yoda.svg", old_yoda, new_yoda)

# =====================================================
# 10. rusty.svg - Maine Coon: unchanged (blue bell collar stays)
# =====================================================
print("OK: rusty.svg unchanged (blue bell collar kept)")

# =====================================================
# 11. mittens.svg - Tuxedo: red bow tie -> mint green bow tie
# =====================================================
old_mittens = '<!-- bow tie (target) --><polygon points="84,105 100,112 116,105 116,122 100,115 84,122" fill="#e74c3c"/><circle cx="100" cy="113.5" r="4" fill="#c0392b"/>'
new_mittens = '<!-- mint bow tie (target) --><polygon points="84,105 100,112 116,105 116,122 100,115 84,122" fill="#66d9b7"/><circle cx="100" cy="113.5" r="4" fill="#2ecc71"/>'
update_file("mittens.svg", old_mittens, new_mittens)

# =====================================================
# 12. bluebell.svg - Ragdoll: pink sweater -> lavender flower clip
# =====================================================
old_bluebell = '<!-- sweater/vest (target) --><rect x="65" y="100" width="70" height="28" rx="8" fill="#ff6b9d"/><rect x="65" y="100" width="70" height="6" rx="3" fill="#e85a8a"/><circle cx="100" cy="114" r="4" fill="#ffd700"/>'
new_bluebell = '<!-- lavender flower clip (target) --><circle cx="100" cy="112" r="8" fill="#b39ddb"/><circle cx="92" cy="108" r="5" fill="#ce93d8"/><circle cx="108" cy="108" r="5" fill="#ce93d8"/><circle cx="96" cy="118" r="5" fill="#ce93d8"/><circle cx="104" cy="118" r="5" fill="#ce93d8"/><circle cx="100" cy="112" r="4" fill="#e1bee7"/>'
update_file("bluebell.svg", old_bluebell, new_bluebell)

print("\n=== All existing SVGs updated successfully ===")
