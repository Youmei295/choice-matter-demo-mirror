import gradio as gr
import json
import os

# ============================================================================
# PHASE 1: STATE MANAGEMENT & SCENE ARCHITECTURE
# ============================================================================

# Scene database - each scene contains narrative text, image, and available choices
SCENES = {
    "start": {
        "text": """*You awaken in a dimly lit chamber. Stone walls press close around you, and the air tastes of ancient dust.*

The only light comes from a faint glow emanating from a doorway to the north. To your left, you notice something glinting in the shadows.""",
        "image": "assets/crystal_chamber.png",
        "choices": [
            ("Investigate the glinting object", "examine_object", None),
            ("Head through the northern doorway", "village_entrance", None),
            ("Search the chamber thoroughly", "search_chamber", None),
        ]
    },
    
    "examine_object": {
        "text": """*You approach the shadows carefully. Your fingers close around cold metal—an ancient key, its surface etched with strange runes.*

**[Key added to inventory]**

The key pulses with a faint warmth. Something tells you it will be important.""",
        "image": "assets/crystal_chamber.png",
        "choices": [
            ("Take the key and head north", "village_entrance", "add_key"),
            ("Examine the runes more closely", "study_runes", "add_key"),
            ("Return to the center of the chamber", "start", "add_key"),
        ]
    },
    
    "search_chamber": {
        "text": """*You methodically search every corner of the chamber. Behind a loose stone, you discover a small vial containing a luminescent liquid.*

**[Potion added to inventory]**

The liquid swirls with its own inner light. It might restore your strength when needed.""",
        "image": "assets/crystal_chamber.png",
        "choices": [
            ("Pocket the potion and continue north", "village_entrance", "add_potion"),
            ("Drink the potion immediately", "drink_potion", "add_potion"),
            ("Leave the potion and head north", "village_entrance", None),
        ]
    },
    
    "study_runes": {
        "text": """*You trace the runes with your fingertips. Ancient knowledge floods your mind—these symbols speak of a great seal, and a darkness that was bound long ago.*

**[You have gained forbidden knowledge]**

The key grows warmer in your hand. You sense it's connected to something powerful.""",
        "image": "assets/crystal_chamber.png",
        "choices": [
            ("Proceed north with newfound understanding", "village_entrance", "learn_runes"),
            ("Meditate on the vision", "meditate", "learn_runes"),
        ]
    },
    
    "village_entrance": {
        "text": """*You emerge into the cool night air. Before you lies a village shrouded in mist, its windows glowing with warm candlelight.*

An old woman stands at the village gate, her eyes sharp despite her age. She seems to have been waiting for you.""",
        "image": "assets/village_twilight.png",
        "choices": [
            ("Approach the old woman", "meet_elder", None),
            ("Sneak around the village perimeter", "sneak_path", None),
            ("Call out to announce your presence", "announce_self", None),
        ]
    },

    "tavern": {
        "text": """*The tavern is warm and bustling. Patrons share tales over mugs of frothy ale. The innkeeper eyes you curiously.*\n\n\"What can I do for you, traveler?\"""",
        "image": "assets/tavern_interior.png",
        "choices": [
            ("Ask about rumors", "tavern_rumors", None),
            ("Accept a quest to find the lost amulet", "accept_amulet_quest", "start_quest"),
            ("Leave the tavern", "village_entrance", None),
        ]
    },
    "tavern_rumors": {
        "text": """*The innkeeper leans in.*\n\n\"There's talk of an ancient amulet hidden in a forgotten cave beyond the forest. Few have returned...\"""",
        "image": "assets/tavern_interior.png",
        "choices": [
            ("Leave the tavern", "village_entrance", None),
        ]
    },
    "accept_amulet_quest": {
        "text": """*The innkeeper smiles and hands you a rough map.*\n\n\"Find the amulet and bring it back, and I'll reward you handsomely.\"""",
        "image": "assets/tavern_interior.png",
        "choices": [
            ("Head into the forest", "forest_entrance", "start_quest"),
        ]
    },
    
    "tavern": {
        "text": """*The tavern is warm and bustling. Patrons share tales over mugs of frothy ale. The innkeeper eyes you curiously.*\n\n\"What can I do for you, traveler?\"""",
        "image": "assets/tavern_interior.png",
        "choices": [
            ("Ask about rumors", "tavern_rumors", None),
            ("Accept a quest to find the lost amulet", "accept_amulet_quest", "start_quest"),
            ("Leave the tavern", "village_entrance", None),
        ]
    },
    "tavern_rumors": {
        "text": """*The innkeeper leans in.*\n\n\"There's talk of an ancient amulet hidden in a forgotten cave beyond the forest. Few have returned...\"""",
        "image": "assets/tavern_interior.png",
        "choices": [
            ("Leave the tavern", "village_entrance", None),
        ]
    },
    "accept_amulet_quest": {
        "text": """*The innkeeper smiles and hands you a rough map.*\n\n\"Find the amulet and bring it back, and I'll reward you handsomely.\"""",
        "image": "assets/tavern_interior.png",
        "choices": [
            ("Head into the forest", "forest_entrance", "start_quest"),
        ]
    },
    "meet_elder": {
        "text": """*The old woman's eyes widen as she sees you.*

"So, the chamber has released another seeker," she whispers. "The forest grows restless. Dark things stir in the deep woods. Will you help us, traveler?"

*Her gaze lingers on your hands, as if she can sense what you carry.*""",
        "image": "assets/village_twilight.png",
        "choices": [
            ("Agree to help the village", "accept_quest", None),
            ("Ask what threatens the village", "learn_threat", None),
            ("Politely decline and move on", "refuse_quest", None),
        ]
    },
    
    "accept_quest": {
        "text": """*The elder's face softens with relief.*

"Thank you, brave soul. The darkness emanates from the heart of the forest. Take this—it will light your way."

**[Lantern added to inventory]**

*She hands you an ornate lantern that burns with cold, blue flame.*

"Follow the old path. And beware—the forest remembers everything.""",
        "image": "assets/village_twilight.png",
        "choices": [
            ("Enter the forest immediately", "forest_entrance", "add_lantern"),
            ("Rest in the village first", "rest_village", "add_lantern"),
            ("Ask for more information", "learn_threat", "add_lantern"),
        ]
    },
    
    "forest_entrance": {
        "text": """*The forest looms before you, ancient and watchful. Bioluminescent mushrooms cast an eerie glow along the path.*

The trees seem to whisper secrets in a language you almost understand. Your lantern flickers, responding to some unseen presence.""",
        "image": "assets/forest_entrance.png",
        "choices": [
            ("Follow the mushroom-lit path", "mushroom_path", None),
            ("Use your lantern to find another way", "lantern_path", None),
            ("Listen to the whispers", "forest_whispers", None),
        ]
    },
    
    "mushroom_path": {
        "text": """*You follow the glowing fungi deeper into the woods. The path spirals inward, and you realize too late that you're walking in circles.*

*The mushrooms' glow intensifies, and strange visions fill your mind...*

**[You have become lost in the enchanted forest]**

*Perhaps you should have been more cautious.*""",
        "image": "assets/forest_entrance.png",
        "choices": [
            ("Start over", "start", "reset"),
        ]
    },
    
    "lantern_path": {
        "text": """*You raise your lantern high. Its blue flame burns brighter, revealing a hidden trail that cuts through the undergrowth.*

*As you walk, the lantern's light seems to push back the darkness itself. You feel you're getting closer to the source of the corruption.*

**[You have found the true path]**""",
        "image": "assets/forest_entrance.png",
        "choices": [
            ("Continue deeper into the forest", "forest_heart", None),
            ("Mark the path and return to the village", "return_village", None),
        ]
    },
    
    "forest_heart": {
        "text": """*You reach a clearing where an ancient stone altar stands. Dark energy pulses from a crack in its surface.*

*If you have the key, you could seal this corruption. If you have the knowledge, you could understand it. If you have neither... you may not survive.*""",
        "image": "assets/crystal_chamber.png",
        "choices": [
            ("Use the ancient key (if you have it)", "seal_darkness", "check_key"),
            ("Apply your runic knowledge (if you learned it)", "understand_darkness", "check_runes"),
            ("Attempt to destroy the altar by force", "force_solution", None),
        ]
    },
    
    "seal_darkness": {
        "text": """*You insert the ancient key into the altar. The runes on the key blaze with golden light, and the crack begins to seal.*

*The darkness screams as it's forced back into its prison. The forest sighs with relief, and new growth springs up around you.*

**[VICTORY: You have sealed the darkness and saved the village]**

*The elder's faith in you was well-placed. You are a true hero.*""",
        "image": "assets/crystal_chamber.png",
        "choices": [
            ("Begin a new journey", "start", "reset"),
        ]
    },
    
    "understand_darkness": {
        "text": """*You speak the ancient words you learned from the runes. The darkness responds, and you realize—it was never evil, only imprisoned and afraid.*

*You negotiate a pact: the darkness will sleep peacefully if the village remembers to honor it with offerings. Balance is restored.*

**[WISDOM ENDING: You have brought understanding and peace]**

*Sometimes the greatest victories come not from force, but from compassion.*""",
        "image": "assets/forest_entrance.png",
        "choices": [
            ("Begin a new journey", "start", "reset"),
        ]
    },
    
    "force_solution": {
        "text": """*You strike the altar with all your might. The stone cracks—but so does the seal.*

*Darkness explodes outward, consuming everything. You hear the village's screams in the distance as shadows swallow the world.*

**[FAILURE: Your recklessness has doomed everyone]**

*Some problems cannot be solved with brute force.*""",
        "image": "assets/crystal_chamber.png",
        "choices": [
            ("Try again", "start", "reset"),
        ]
    },
    
    "drink_potion": {
        "text": """*You uncork the vial and drink deeply. Power surges through your veins!*

**[You feel invincible... but at what cost?]**

*The chamber begins to spin. Perhaps drinking unknown potions wasn't wise.*""",
        "image": "assets/crystal_chamber.png",
        "choices": [
            ("Try to stay conscious", "potion_effect", None),
            ("Embrace the darkness", "start", "reset"),
        ]
    },
}

def initialize_state():
    """Create a fresh game state"""
    return {
        "scene_id": "start",
        "inventory": [],
        "flags": {},
        "quests": []
    }

# ============================================================================
# PHASE 3: THE LOGIC BRIDGE - Core game engine
# ============================================================================

def handle_action(choice_text, game_state):
    """
    Process player choice and return updated UI components.
    Returns: (story_text, image, status_html, btn1_update, btn2_update, btn3_update, new_state)
    """
    if game_state is None:
        game_state = initialize_state()
    
    current_scene = SCENES.get(game_state["scene_id"], SCENES["start"])
    
    # Find which choice was selected
    next_scene_id = None
    action = None
    
    for choice_label, scene_id, choice_action in current_scene["choices"]:
        if choice_label == choice_text:
            next_scene_id = scene_id
            action = choice_action
            break
    
    # If no match found (shouldn't happen), stay in current scene
    if next_scene_id is None:
        next_scene_id = game_state["scene_id"]
    
    # Execute action (modify inventory/flags)
    if action == "add_key":
        if "key" not in game_state["inventory"]:
            game_state["inventory"].append("key")
    elif action == "add_potion":
        if "potion" not in game_state["inventory"]:
            game_state["inventory"].append("potion")
    elif action == "add_lantern":
        if "lantern" not in game_state["inventory"]:
            game_state["inventory"].append("lantern")
    elif action == "learn_runes":
        game_state["flags"]["knows_runes"] = True
    elif action == "check_key":
        if "key" not in game_state["inventory"]:
            # Player doesn't have key, redirect to failure
            next_scene_id = "force_solution"
    elif action == "check_runes":
        if not game_state["flags"].get("knows_runes", False):
            # Player doesn't have knowledge, redirect to failure
            next_scene_id = "force_solution"
    elif action == "reset":
        game_state = initialize_state()
        next_scene_id = "start"
    
    # Update scene
    game_state["scene_id"] = next_scene_id
    next_scene = SCENES.get(next_scene_id, SCENES["start"])
    
    # Prepare UI updates
    story_text = next_scene["text"]
    image_path = next_scene["image"]
    
    # Build status panel HTML
    status_html = build_status_panel(game_state)
    
    # Update buttons
    button_updates = []
    for i in range(3):
        if i < len(next_scene["choices"]):
            choice_label = next_scene["choices"][i][0]
            button_updates.append(gr.update(value=choice_label, visible=True))
        else:
            button_updates.append(gr.update(visible=False))
    
    return story_text, image_path, status_html, *button_updates, game_state

def build_status_panel(game_state):
    """Generate HTML for the status panel"""
    inventory_items = ", ".join(game_state["inventory"]) if game_state["inventory"] else "Empty"
    
    flags_display = ""
    if game_state["flags"].get("knows_runes"):
        flags_display += "<span style='color: #9d4edd;'>◆ Ancient Knowledge</span><br>"
    
    html = f"""
    <div class='status-panel'>
        <div style='margin-bottom: 12px;'>
            <span style='color: #ff6b6b; font-family: "Cinzel", serif; font-weight: 600; font-size: 13px; text-transform: uppercase; letter-spacing: 2px;'>⚔ INVENTORY</span>
            <div style='color: #e0e0e0; margin-top: 6px; font-size: 13px;'>{inventory_items}</div>
        </div>
        <div style='margin-top: 12px; padding-top: 10px; border-top: 1px solid rgba(157, 78, 221, 0.2);'>
            {flags_display}
        </div>
    </div>
    """
    return html

def restart_game():
    """Reset the game to initial state"""
    game_state = initialize_state()
    scene = SCENES["start"]
    status_html = build_status_panel(game_state)
    
    button_updates = []
    for i in range(3):
        if i < len(scene["choices"]):
            button_updates.append(gr.update(value=scene["choices"][i][0], visible=True))
        else:
            button_updates.append(gr.update(visible=False))
    
    return scene["text"], scene["image"], status_html, *button_updates, game_state

# ============================================================================
# PHASE 2 & 4: GRADIO UI WITH ATMOSPHERIC POLISH
# ============================================================================

# Custom CSS for premium dark fantasy UI/UX
custom_css = """
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600&family=Fira+Code:wght@400;500&display=swap');

/* Global styles with gradient background */
body, .gradio-container {
    background: linear-gradient(135deg, #0d0d0d 0%, #1a1a2e 50%, #0d0d0d 100%) !important;
    color: #e0e0e0 !important;
    font-family: 'Fira Code', 'Courier New', monospace !important;
    min-height: 100vh !important;
}

.contain {
    background: transparent !important;
}

/* Main container - glassmorphism effect */
.main {
    background: rgba(13, 13, 13, 0.85) !important;
    backdrop-filter: blur(10px) !important;
    border: 1px solid rgba(255, 107, 107, 0.15) !important;
    border-radius: 12px !important;
    margin: 20px !important;
    padding: 25px !important;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.8), 0 0 60px rgba(255, 107, 107, 0.05) !important;
}

/* Story text styling with improved readability */
.prose {
    color: #e0e0e0 !important;
    font-family: 'Fira Code', monospace !important;
    line-height: 1.9 !important;
    font-size: 15px !important;
    text-shadow: 0 1px 2px rgba(0, 0, 0, 0.5) !important;
}

.prose em {
    color: #9d4edd !important;
    font-style: italic !important;
}

.prose strong {
    color: #ff6b6b !important;
    font-weight: 600 !important;
    text-shadow: 0 0 10px rgba(255, 107, 107, 0.3) !important;
}

/* Premium button styling with gradients */
button.primary, button.lg {
    background: linear-gradient(145deg, #1f1f2e 0%, #2a2a3e 100%) !important;
    border: 1px solid #3a3a4e !important;
    border-radius: 8px !important;
    color: #e0e0e0 !important;
    font-family: 'Cinzel', serif !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    padding: 14px 28px !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.05) !important;
    position: relative !important;
    overflow: hidden !important;
}

button.primary:hover, button.lg:hover {
    background: linear-gradient(145deg, #2a2a3e 0%, #3a3a4e 100%) !important;
    border-color: #ff6b6b !important;
    color: #ff6b6b !important;
    box-shadow: 0 6px 25px rgba(255, 107, 107, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.1) !important;
    transform: translateY(-2px) !important;
}

button.primary:active, button.lg:active {
    transform: translateY(0) !important;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.4) !important;
}

button.secondary {
    background: linear-gradient(145deg, #1a1a1a 0%, #252525 100%) !important;
    border: 1px solid #333 !important;
    border-radius: 8px !important;
    color: #888 !important;
    font-family: 'Cinzel', serif !important;
    font-size: 12px !important;
    font-weight: 400 !important;
    padding: 10px 20px !important;
    transition: all 0.3s ease !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
}

button.secondary:hover {
    background: linear-gradient(145deg, #252525 0%, #333 100%) !important;
    border-color: #ff6b6b !important;
    color: #ff6b6b !important;
}

/* Image container with premium border */
.image-container {
    border-radius: 10px !important;
    overflow: hidden !important;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.6), 0 0 40px rgba(157, 78, 221, 0.1) !important;
    border: 1px solid rgba(157, 78, 221, 0.2) !important;
}

.image-container img {
    border-radius: 10px !important;
    display: block !important;
}

/* Headers with cinematic styling */
h1 {
    color: #ff6b6b !important;
    font-family: 'Cinzel', serif !important;
    text-transform: uppercase !important;
    letter-spacing: 4px !important;
    font-size: 28px !important;
    text-shadow: 0 0 20px rgba(255, 107, 107, 0.4), 0 2px 4px rgba(0, 0, 0, 0.8) !important;
    margin-bottom: 5px !important;
}

h2, h3 {
    color: #9d4edd !important;
    font-family: 'Cinzel', serif !important;
    text-transform: uppercase !important;
    letter-spacing: 2px !important;
    text-shadow: 0 0 15px rgba(157, 78, 221, 0.3) !important;
}

/* Status panel glassmorphism */
.status-panel {
    background: rgba(20, 20, 30, 0.7) !important;
    backdrop-filter: blur(8px) !important;
    border: 1px solid rgba(157, 78, 221, 0.2) !important;
    border-radius: 10px !important;
    padding: 15px !important;
    box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.3) !important;
}

/* Divider styling */
hr {
    border: none !important;
    height: 1px !important;
    background: linear-gradient(90deg, transparent, rgba(255, 107, 107, 0.3), transparent) !important;
    margin: 20px 0 !important;
}

/* Scrollbar styling */
::-webkit-scrollbar {
    width: 8px !important;
}

::-webkit-scrollbar-track {
    background: #0d0d0d !important;
}

::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, #3a3a4e, #2a2a3e) !important;
    border-radius: 4px !important;
}

::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(180deg, #4a4a5e, #3a3a4e) !important;
}

/* Animation for text fade-in */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

.fade-in {
    animation: fadeIn 0.5s ease-out !important;
}

/* Subtle pulse animation for important elements */
@keyframes pulse-glow {
    0%, 100% { box-shadow: 0 0 20px rgba(255, 107, 107, 0.2); }
    50% { box-shadow: 0 0 30px rgba(255, 107, 107, 0.4); }
}

.pulse {
    animation: pulse-glow 3s ease-in-out infinite !important;
}
"""

# Build the Gradio interface
with gr.Blocks(css=custom_css, title="Choice Matter - Dark Fantasy", theme=gr.themes.Base()) as demo:
    # Game state
    game_state = gr.State(initialize_state())
    
    # Header with enhanced styling
    gr.HTML("""
    <div style='text-align: center; padding: 20px 0 10px 0;'>
        <h1 style='color: #ff6b6b; font-family: "Cinzel", serif; text-transform: uppercase; letter-spacing: 6px; font-size: 32px; margin: 0; text-shadow: 0 0 30px rgba(255, 107, 107, 0.5), 0 3px 6px rgba(0, 0, 0, 0.9);'>
            ⬛ CHOICE MATTER ⬛
        </h1>
        <p style='color: #9d4edd; font-family: "Cinzel", serif; font-style: italic; font-size: 14px; letter-spacing: 3px; margin-top: 8px; text-shadow: 0 0 15px rgba(157, 78, 221, 0.4);'>
            A dark fantasy where every decision shapes your fate
        </p>
    </div>
    """)
    
    with gr.Row():
        # Left column - Visual stage and status
        with gr.Column(scale=1):
            scene_image = gr.Image(
                value=SCENES["start"]["image"],
                label="",
                show_label=False,
                container=False,
                height=400
            )
            status_panel = gr.HTML(build_status_panel(initialize_state()))
        
        # Right column - Narrative and controls
        with gr.Column(scale=1):
            story_text = gr.Markdown(
                SCENES["start"]["text"],
                container=True
            )
            
            gr.HTML("<div style='height: 15px;'></div>")
            
            # Choice buttons section with enhanced styling
            gr.HTML("""
            <div style='margin-bottom: 15px;'>
                <span style='color: #9d4edd; font-family: "Cinzel", serif; font-size: 11px; text-transform: uppercase; letter-spacing: 3px; opacity: 0.7;'>CHOOSE YOUR PATH</span>
            </div>
            """)
            
            with gr.Column():
                choice_btn_1 = gr.Button(
                    SCENES["start"]["choices"][0][0],
                    variant="primary",
                    size="lg"
                )
                choice_btn_2 = gr.Button(
                    SCENES["start"]["choices"][1][0],
                    variant="primary",
                    size="lg"
                )
                choice_btn_3 = gr.Button(
                    SCENES["start"]["choices"][2][0],
                    variant="primary",
                    size="lg"
                )
            
            gr.HTML("<div style='height: 20px;'></div>")
            
            # Restart button with icon
            restart_btn = gr.Button("↻ NEW GAME", variant="secondary")
    
    # Wire up event handlers
    outputs = [story_text, scene_image, status_panel, choice_btn_1, choice_btn_2, choice_btn_3, game_state]
    
    choice_btn_1.click(
        fn=lambda state: handle_action(choice_btn_1.value, state),
        inputs=[game_state],
        outputs=outputs
    )
    
    choice_btn_2.click(
        fn=lambda state: handle_action(choice_btn_2.value, state),
        inputs=[game_state],
        outputs=outputs
    )
    
    choice_btn_3.click(
        fn=lambda state: handle_action(choice_btn_3.value, state),
        inputs=[game_state],
        outputs=outputs
    )
    
    restart_btn.click(
        fn=restart_game,
        inputs=[],
        outputs=outputs
    )

# ============================================================================
# PHASE 5: DEPLOYMENT
# ============================================================================

if __name__ == "__main__":
    demo.launch()