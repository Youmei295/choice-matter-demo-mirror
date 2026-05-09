import gradio as gr

# Story graph - each node has text and choices leading to other nodes
story_graph = {
    "start": {
        "text": """# The Enchanted Forest

You wake up at the edge of a mysterious forest. The trees tower above you, their leaves shimmering with an otherworldly glow. 

A worn path leads deeper into the woods, while to your right, you notice smoke rising from what might be a village.

What do you do?""",
        "choices": [
            ("Follow the path into the forest", "forest_path"),
            ("Head towards the village", "village"),
            ("Search the area for clues", "search_area")
        ]
    },
    "forest_path": {
        "text": """# Deep in the Woods

You venture down the forest path. The air grows cooler and the light dims as the canopy thickens above you.

Suddenly, you hear a rustling in the bushes. A small, glowing creature emerges - it looks like a fairy!

The fairy gestures for you to follow, then points at a glowing mushroom circle nearby.

What do you do?""",
        "choices": [
            ("Follow the fairy", "fairy_realm"),
            ("Step into the mushroom circle", "mushroom_portal"),
            ("Continue down the path alone", "deep_forest")
        ]
    },
    "village": {
        "text": """# The Village

You arrive at a small village. The inhabitants eye you with curiosity. An old woman approaches you.

"Traveler," she says, "we've been expecting you. The forest has been acting strange. Will you help us?"

What do you do?""",
        "choices": [
            ("Agree to help the village", "help_village"),
            ("Ask for more information first", "ask_info"),
            ("Politely decline and leave", "forest_path")
        ]
    },
    "search_area": {
        "text": """# The Discovery

You search the area carefully and find an old, weathered journal half-buried in the dirt.

Inside, you read: "The forest holds ancient magic. Those who seek with pure intent shall find the Crystal of Light."

You also find a small silver compass that seems to point toward the forest.

What do you do?""",
        "choices": [
            ("Follow the compass into the forest", "forest_path"),
            ("Take the journal to the village for answers", "village"),
            ("Keep searching for more clues", "hidden_cave")
        ]
    },
    "fairy_realm": {
        "text": """# The Fairy Realm

The fairy leads you through a shimmering veil between the trees. You find yourself in a magical realm filled with floating lights and crystalline structures.

The Fairy Queen appears before you. "You have a pure heart," she says. "I grant you the gift of forest speech. Use it wisely."

**You have gained the ability to communicate with all forest creatures!**

This is a good ending - you've been blessed by the fairies!""",
        "choices": [
            ("Start a new adventure", "start")
        ]
    },
    "mushroom_portal": {
        "text": """# The Portal

You step into the mushroom circle. The world spins around you!

When your vision clears, you find yourself back at the edge of the forest, but something feels different. You notice you're glowing faintly.

**You've been touched by forest magic, but you're not sure what it means...**

This is a mysterious ending - your adventure continues!""",
        "choices": [
            ("Start a new adventure", "start")
        ]
    },
    "deep_forest": {
        "text": """# Lost in the Woods

You continue alone, but the path becomes increasingly difficult to follow. The forest grows darker and more confusing.

After hours of wandering, you realize you're completely lost. As night falls, you hear howling in the distance...

**You got lost in the enchanted forest. Perhaps you should have accepted help?**

This is a bad ending - try making different choices!""",
        "choices": [
            ("Start a new adventure", "start")
        ]
    },
    "help_village": {
        "text": """# The Hero's Path

You agree to help. The old woman leads you to the village elder, who tells you about a dark presence corrupting the forest's heart.

She gives you a blessed amulet and a map to the Crystal of Light, which can purify the corruption.

Armed with knowledge and tools, you set off on your quest!

**You've become the village's champion! Your heroic journey begins!**

This is a good ending - you've found your purpose!""",
        "choices": [
            ("Start a new adventure", "start")
        ]
    },
    "ask_info": {
        "text": """# Knowledge is Power

The old woman explains that the forest's magic has been growing unstable. Strange creatures have appeared, and the ancient trees are withering.

She mentions that a Crystal of Light, hidden deep in the forest, might be the key to restoring balance.

She offers you supplies and a map if you'll help.

What do you do?""",
        "choices": [
            ("Accept the quest with the supplies", "help_village"),
            ("Venture into the forest alone", "forest_path"),
            ("Decline and explore elsewhere", "search_area")
        ]
    },
    "hidden_cave": {
        "text": """# The Hidden Cave

Your thorough search reveals a hidden cave entrance behind some vines. Inside, you find ancient carvings and a pedestal with a glowing crystal.

As you approach, the crystal pulses with light. A voice echoes: "Seeker of truth, you have found the Crystal of Light through your own determination."

**You've discovered the legendary Crystal of Light on your own! You are a true explorer!**

This is the best ending - you've achieved greatness through your own efforts!""",
        "choices": [
            ("Start a new adventure", "start")
        ]
    }
}

def get_story_content(node_id):
    """Get the story text and choices for a given node."""
    node = story_graph.get(node_id, story_graph["start"])
    return node["text"], node["choices"]

def make_choice(node_id, choice_idx):
    """Process a choice and return updated UI state."""
    node = story_graph.get(node_id, story_graph["start"])
    
    if choice_idx < len(node["choices"]):
        next_node_id = node["choices"][choice_idx][1]
    else:
        next_node_id = "start"
    
    text, choices = get_story_content(next_node_id)
    
    # Prepare button updates (text and visibility)
    button_updates = []
    for i in range(4):  # We have 4 buttons
        if i < len(choices):
            button_updates.append(gr.update(value=choices[i][0], visible=True))
        else:
            button_updates.append(gr.update(visible=False))
    
    return [text, next_node_id] + button_updates

def restart_game():
    """Restart the game from the beginning."""
    text, choices = get_story_content("start")
    
    button_updates = []
    for i in range(4):
        if i < len(choices):
            button_updates.append(gr.update(value=choices[i][0], visible=True))
        else:
            button_updates.append(gr.update(visible=False))
    
    return [text, "start"] + button_updates

# Create the Gradio interface
with gr.Blocks(title="Choice Matter - Interactive Story Game", theme=gr.themes.Soft()) as demo:
    # State to track current node
    current_node = gr.State("start")
    
    # Header
    gr.Markdown("# 🎮 Choice Matter: The Enchanted Forest")
    gr.Markdown("*An interactive story where your choices shape your destiny*")
    
    # Story display
    story_text = gr.Markdown(story_graph["start"]["text"])
    
    # Choice buttons (create 4 buttons, hide unused ones)
    with gr.Row():
        choice_btn_1 = gr.Button(story_graph["start"]["choices"][0][0], variant="primary", size="lg")
        choice_btn_2 = gr.Button(story_graph["start"]["choices"][1][0], variant="primary", size="lg")
    
    with gr.Row():
        choice_btn_3 = gr.Button(story_graph["start"]["choices"][2][0], variant="primary", size="lg")
        choice_btn_4 = gr.Button("", visible=False, variant="primary", size="lg")
    
    # Restart button
    with gr.Row():
        restart_btn = gr.Button("🔄 Restart Game", variant="secondary")
    
    # Wire up the buttons
    choice_btn_1.click(
        fn=lambda node: make_choice(node, 0),
        inputs=[current_node],
        outputs=[story_text, current_node, choice_btn_1, choice_btn_2, choice_btn_3, choice_btn_4]
    )
    
    choice_btn_2.click(
        fn=lambda node: make_choice(node, 1),
        inputs=[current_node],
        outputs=[story_text, current_node, choice_btn_1, choice_btn_2, choice_btn_3, choice_btn_4]
    )
    
    choice_btn_3.click(
        fn=lambda node: make_choice(node, 2),
        inputs=[current_node],
        outputs=[story_text, current_node, choice_btn_1, choice_btn_2, choice_btn_3, choice_btn_4]
    )
    
    choice_btn_4.click(
        fn=lambda node: make_choice(node, 3),
        inputs=[current_node],
        outputs=[story_text, current_node, choice_btn_1, choice_btn_2, choice_btn_3, choice_btn_4]
    )
    
    restart_btn.click(
        fn=restart_game,
        inputs=[],
        outputs=[story_text, current_node, choice_btn_1, choice_btn_2, choice_btn_3, choice_btn_4]
    )

if __name__ == "__main__":
    demo.launch()