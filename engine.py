import gradio as gr
from scenes import SCENES
from ui import build_status_panel

def initialize_state():
    """Create a fresh game state"""
    return {
        "scene_id": "001",
        "Player_Health": 100,
        "Has_Scanner": True,
        "Has_Artifact": False
    }

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
