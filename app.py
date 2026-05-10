import gradio as gr
import json
import os

# ============================================================================
# PHASE 1: STATE MANAGEMENT & SCENE ARCHITECTURE
# ============================================================================

# Scene database - The Kepler Artifact story nodes
SCENES = {
    "001": {
        "text": """You have just landed on the surface of Kepler-186f. The atmosphere is breathable, but a thick purple fog covers the ground. A few meters ahead, a strange, metallic artifact pulses with a faint blue light.""",
        "image": "assets/kepler_landing.png",
        "choices": [
            ("Reach out and touch the artifact.", "002", "damage_20"),
            ("Use your scanner to analyze it from a distance.", "003", "check_scanner"),
        ],
        "isTerminal": False
    },
    
    "002": {
        "text": """Your hand touches the cold metal. A sudden jolt of electricity courses through your suit! You take 20 damage. However, a map downloads directly into your visor's HUD, showing a cave nearby.""",
        "image": "assets/kepler_artifact.png",
        "choices": [
            ("Follow the map to the cave.", "004", None),
            ("This is too dangerous. Return to the ship.", "005", None),
        ],
        "isTerminal": False
    },
    
    "003": {
        "text": """The scanner beeps wildly. The artifact is emitting high levels of unstable energy. It is safe to handle only if contained properly. You happen to have a lead-lined containment box.""",
        "image": "assets/kepler_scan.png",
        "choices": [
            ("Carefully place the artifact in the containment box.", "006", "add_artifact"),
            ("Leave it alone and search the perimeter.", "004", None),
        ],
        "isTerminal": False
    },
    
    "004": {
        "text": """You arrive at a dark, echoing cave. Inside, coiled around a pedestal, is a massive, biomechanical alien entity. It appears to be dormant.""",
        "image": "assets/kepler_cave.png",
        "choices": [
            ("Sneak past it to see what is on the pedestal.", "007", None),
            ("Activate your suit's translation speaker to attempt communication.", "008", None),
        ],
        "isTerminal": False
    },
    
    "005": {
        "text": """You decide your life is more important than discovery. You board your ship and leave the planet. You are safe, but humanity learns nothing.

**[GAME OVER - THE COWARD'S RETREAT]**""",
        "image": "assets/kepler_ship.png",
        "choices": [
            ("Start over", "001", "reset"),
        ],
        "isTerminal": True
    },
    
    "006": {
        "text": """You successfully contain the artifact. You return to Earth a hero, ushering in a new era of clean energy based on your discovery.

**[VICTORY - THE SCIENTIST]**""",
        "image": "assets/kepler_victory.png",
        "choices": [
            ("Start over", "001", "reset"),
        ],
        "isTerminal": True
    },
    
    "007": {
        "text": """As you tiptoe past the creature, your boot kicks a loose rock. The entity awakens instantly, its glowing red eyes locking onto you. You are vaporized before you can scream.

**[GAME OVER - THE THIEF'S DEMISE]**""",
        "image": "assets/kepler_death.png",
        "choices": [
            ("Try again", "001", "reset"),
        ],
        "isTerminal": True
    },
    
    "008": {
        "text": """The entity stirs and listens to your greeting. It nods slowly. 'You are the first to speak instead of steal,' it says. It grants you the blueprints for faster-than-light travel.

**[TRUE VICTORY - THE DIPLOMAT]**""",
        "image": "assets/kepler_diplomat.png",
        "choices": [
            ("Begin a new journey", "001", "reset"),
        ],
        "isTerminal": True
    },
}

def initialize_state():
    """Create a fresh game state"""
    return {
        "scene_id": "001",
        "Player_Health": 100,
        "Has_Scanner": True,
        "Has_Artifact": False
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
    
    current_scene = SCENES.get(game_state["scene_id"], SCENES["001"])
    
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
    
    # Execute action (modify health/inventory)
    if action == "damage_20":
        game_state["Player_Health"] -= 20
    elif action == "check_scanner":
        if not game_state["Has_Scanner"]:
            # Player doesn't have scanner, this choice shouldn't be available
            # But if somehow triggered, stay in current scene
            next_scene_id = game_state["scene_id"]
    elif action == "add_artifact":
        game_state["Has_Artifact"] = True
    elif action == "reset":
        game_state = initialize_state()
        next_scene_id = "001"
    
    # Update scene
    game_state["scene_id"] = next_scene_id
    next_scene = SCENES.get(next_scene_id, SCENES["001"])
    
    # Prepare UI updates
    story_text = next_scene["text"]
    image_path = next_scene["image"]
    
    # Build status panel HTML
    status_html = build_status_panel(game_state)
    
    # Update buttons - filter choices based on conditions
    available_choices = []
    for choice_label, scene_id, choice_action in next_scene["choices"]:
        # Check if choice requires scanner
        if choice_action == "check_scanner" and not game_state["Has_Scanner"]:
            continue  # Skip this choice
        available_choices.append(choice_label)
    
    # Update buttons
    button_updates = []
    for i in range(3):
        if i < len(available_choices):
            button_updates.append(gr.update(value=available_choices[i], visible=True))
        else:
            button_updates.append(gr.update(visible=False))
    
    return story_text, image_path, status_html, *button_updates, game_state

def build_status_panel(game_state):
    """Generate HTML for the status panel"""
    health = game_state["Player_Health"]
    
    # Calculate health bar color based on health level
    if health > 70:
        health_color = "#00ff88"
    elif health > 40:
        health_color = "#ffaa00"
    else:
        health_color = "#ff4444"
    
    # Calculate health bar width percentage
    health_percent = max(0, min(100, health))
    
    # Build inventory display
    inventory_items = []
    if game_state["Has_Scanner"]:
        inventory_items.append("Scanner")
    if game_state["Has_Artifact"]:
        inventory_items.append("Artifact")
    
    inventory_display = ", ".join(inventory_items) if inventory_items else "Empty"
    
    html = f"""
    <div class='status-panel'>
        <div style='margin-bottom: 15px;'>
            <span style='color: #00d4ff; font-family: "Orbitron", sans-serif; font-weight: 600; font-size: 13px; text-transform: uppercase; letter-spacing: 2px;'>⚡ HEALTH</span>
            <div style='margin-top: 8px; background: rgba(0, 0, 0, 0.5); border: 1px solid rgba(0, 212, 255, 0.3); border-radius: 4px; height: 20px; overflow: hidden;'>
                <div style='background: linear-gradient(90deg, {health_color}, {health_color}88); height: 100%; width: {health_percent}%; transition: width 0.3s ease;'></div>
            </div>
            <div style='color: #e0e0e0; margin-top: 4px; font-size: 12px; text-align: right;'>{health} / 100</div>
        </div>
        <div style='margin-top: 15px; padding-top: 12px; border-top: 1px solid rgba(0, 212, 255, 0.2);'>
            <span style='color: #00d4ff; font-family: "Orbitron", sans-serif; font-weight: 600; font-size: 13px; text-transform: uppercase; letter-spacing: 2px;'>📡 INVENTORY</span>
            <div style='color: #e0e0e0; margin-top: 6px; font-size: 13px;'>{inventory_display}</div>
        </div>
    </div>
    """
    return html

def restart_game():
    """Reset the game to initial state"""
    game_state = initialize_state()
    scene = SCENES["001"]
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

# Custom CSS for premium sci-fi UI/UX
custom_css = """
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;700&family=Fira+Code:wght@400;500&display=swap');

/* Global styles with sci-fi gradient background */
body, .gradio-container {
    background: linear-gradient(135deg, #0a0a1a 0%, #1a1a3e 50%, #0a0a1a 100%) !important;
    color: #e0e0e0 !important;
    font-family: 'Fira Code', 'Courier New', monospace !important;
    min-height: 100vh !important;
}

.contain {
    background: transparent !important;
}

/* Main container - glassmorphism effect */
.main {
    background: rgba(10, 10, 26, 0.85) !important;
    backdrop-filter: blur(10px) !important;
    border: 1px solid rgba(0, 212, 255, 0.15) !important;
    border-radius: 12px !important;
    margin: 20px !important;
    padding: 25px !important;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.8), 0 0 60px rgba(0, 212, 255, 0.05) !important;
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
    color: #00d4ff !important;
    font-style: italic !important;
}

.prose strong {
    color: #00ff88 !important;
    font-weight: 600 !important;
    text-shadow: 0 0 10px rgba(0, 255, 136, 0.3) !important;
}

/* Premium button styling with sci-fi gradients */
button.primary, button.lg {
    background: linear-gradient(145deg, #1a1a2e 0%, #2a2a4e 100%) !important;
    border: 1px solid #3a3a6e !important;
    border-radius: 8px !important;
    color: #e0e0e0 !important;
    font-family: 'Orbitron', sans-serif !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    padding: 14px 28px !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4), inset 0 1px 0 rgba(0, 212, 255, 0.05) !important;
    position: relative !important;
    overflow: hidden !important;
}

button.primary:hover, button.lg:hover {
    background: linear-gradient(145deg, #2a2a4e 0%, #3a3a6e 100%) !important;
    border-color: #00d4ff !important;
    color: #00d4ff !important;
    box-shadow: 0 6px 25px rgba(0, 212, 255, 0.3), inset 0 1px 0 rgba(0, 212, 255, 0.1) !important;
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
    font-family: 'Orbitron', sans-serif !important;
    font-size: 12px !important;
    font-weight: 400 !important;
    padding: 10px 20px !important;
    transition: all 0.3s ease !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
}

button.secondary:hover {
    background: linear-gradient(145deg, #252525 0%, #333 100%) !important;
    border-color: #00d4ff !important;
    color: #00d4ff !important;
}

/* Image container with premium border */
.image-container {
    border-radius: 10px !important;
    overflow: hidden !important;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.6), 0 0 40px rgba(0, 212, 255, 0.1) !important;
    border: 1px solid rgba(0, 212, 255, 0.2) !important;
}

.image-container img {
    border-radius: 10px !important;
    display: block !important;
}

/* Headers with sci-fi styling */
h1 {
    color: #00d4ff !important;
    font-family: 'Orbitron', sans-serif !important;
    text-transform: uppercase !important;
    letter-spacing: 4px !important;
    font-size: 28px !important;
    text-shadow: 0 0 20px rgba(0, 212, 255, 0.4), 0 2px 4px rgba(0, 0, 0, 0.8) !important;
    margin-bottom: 5px !important;
}

h2, h3 {
    color: #00ff88 !important;
    font-family: 'Orbitron', sans-serif !important;
    text-transform: uppercase !important;
    letter-spacing: 2px !important;
    text-shadow: 0 0 15px rgba(0, 255, 136, 0.3) !important;
}

/* Status panel glassmorphism */
.status-panel {
    background: rgba(20, 20, 40, 0.7) !important;
    backdrop-filter: blur(8px) !important;
    border: 1px solid rgba(0, 212, 255, 0.2) !important;
    border-radius: 10px !important;
    padding: 15px !important;
    box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.3) !important;
}

/* Divider styling */
hr {
    border: none !important;
    height: 1px !important;
    background: linear-gradient(90deg, transparent, rgba(0, 212, 255, 0.3), transparent) !important;
    margin: 20px 0 !important;
}

/* Scrollbar styling */
::-webkit-scrollbar {
    width: 8px !important;
}

::-webkit-scrollbar-track {
    background: #0a0a1a !important;
}

::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, #3a3a6e, #2a2a4e) !important;
    border-radius: 4px !important;
}

::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(180deg, #4a4a7e, #3a3a6e) !important;
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
    0%, 100% { box-shadow: 0 0 20px rgba(0, 212, 255, 0.2); }
    50% { box-shadow: 0 0 30px rgba(0, 212, 255, 0.4); }
}

.pulse {
    animation: pulse-glow 3s ease-in-out infinite !important;
}
"""

# Build the Gradio interface
with gr.Blocks(css=custom_css, title="The Kepler Artifact - Sci-Fi Mystery", theme=gr.themes.Base()) as demo:
    # Game state
    game_state = gr.State(initialize_state())
    
    # Header with enhanced styling
    gr.HTML("""
    <div style='text-align: center; padding: 20px 0 10px 0;'>
        <h1 style='color: #00d4ff; font-family: "Orbitron", sans-serif; text-transform: uppercase; letter-spacing: 6px; font-size: 32px; margin: 0; text-shadow: 0 0 30px rgba(0, 212, 255, 0.5), 0 3px 6px rgba(0, 0, 0, 0.9);'>
            ◆ THE KEPLER ARTIFACT ◆
        </h1>
        <p style='color: #00ff88; font-family: "Orbitron", sans-serif; font-style: italic; font-size: 14px; letter-spacing: 3px; margin-top: 8px; text-shadow: 0 0 15px rgba(0, 255, 136, 0.4);'>
            A sci-fi mystery where survival depends on your choices
        </p>
    </div>
    """)
    
    with gr.Row():
        # Left column - Visual stage and status
        with gr.Column(scale=1):
            scene_image = gr.Image(
                value=SCENES["001"]["image"],
                label="",
                show_label=False,
                container=False,
                height=400
            )
            status_panel = gr.HTML(build_status_panel(initialize_state()))
        
        # Right column - Narrative and controls
        with gr.Column(scale=1):
            story_text = gr.Markdown(
                SCENES["001"]["text"],
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
                    SCENES["001"]["choices"][0][0],
                    variant="primary",
                    size="lg"
                )
                choice_btn_2 = gr.Button(
                    SCENES["001"]["choices"][1][0],
                    variant="primary",
                    size="lg"
                )
                choice_btn_3 = gr.Button(
                    "",
                    variant="primary",
                    size="lg",
                    visible=False
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