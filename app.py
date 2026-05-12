import gradio as gr
from scenes import SCENES
from engine import initialize_state, handle_action, restart_game
from ui import custom_css, build_status_panel

# ============================================================================
# MAIN APPLICATION / ENTRY POINT
# ============================================================================

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
                    SCENES["001"]["choices"][2][0],
                    variant="primary",
                    size="lg",
                    visible=True
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

if __name__ == "__main__":
    demo.launch()